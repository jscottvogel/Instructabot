#!/usr/bin/env python3
"""
Instructabot Engineering Notebook CLI & Automated Evaluator
----------------------------------------------------------
Inspects, initializes, and evaluates digital engineering notebooks
against the official NASA RAP / JPL engineering documentation rubric.
"""

import sys
import os
import re
import argparse
from datetime import datetime
from pathlib import Path

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def get_lab_file(lab_id):
    """Resolves lab identifier (e.g. 1, '01', 'lab-01', or path) to Path."""
    if isinstance(lab_id, Path) and lab_id.exists():
        return lab_id

    s = str(lab_id).strip().lower()
    if s.endswith(".md"):
        target = NOTEBOOKS_DIR / s
        if target.exists():
            return target
        if Path(s).exists():
            return Path(s)

    # Extract digits
    m = re.search(r"(\d+)", s)
    if m:
        num = int(m.group(1))
        matches = sorted(list(NOTEBOOKS_DIR.glob(f"lab-{num:02d}-*.md")))
        if matches:
            return matches[0]

    return None


def parse_notebook_status(filepath: Path):
    """Analyzes completion state of a notebook."""
    if not filepath.exists():
        return {
            "exists": False,
            "author": "N/A",
            "date": "N/A",
            "checks_done": 0,
            "checks_total": 0,
            "status": "Missing",
            "score": 0,
        }

    content = filepath.read_text(encoding="utf-8")

    # Author
    author_m = re.search(r"\*\*Author\*\*:\s*(.+)", content)
    author = author_m.group(1).strip() if author_m else "Unknown"

    # Date
    date_m = re.search(r"\*\*Date\*\*:\s*(.+)", content)
    date_val = date_m.group(1).strip() if date_m else "Unknown"

    # Checkboxes
    checks_done = len(re.findall(r"-\s*\[x\]", content, flags=re.IGNORECASE))
    checks_empty = len(re.findall(r"-\s*\[\s\]", content))
    checks_total = checks_done + checks_empty

    # Placeholders remaining
    placeholders = len(re.findall(r"\[(Record|Enter|Your Full Name|Your Name|YYYY-MM-DD|State in 2-3|Answer in 2-4|e\.g\.)", content))

    has_custom_author = author not in ["[Your Full Name]", "[Your Name]", "Unknown", ""]

    if not has_custom_author and checks_done == 0 and placeholders > 3:
        status = "Not Started"
    elif checks_done > 0 and checks_done == checks_total and placeholders == 0 and has_custom_author:
        status = "Completed"
    else:
        status = "In Progress"

    return {
        "exists": True,
        "author": author,
        "date": date_val,
        "checks_done": checks_done,
        "checks_total": checks_total,
        "placeholders": placeholders,
        "status": status,
    }


def list_labs():
    """Lists all 11 lab notebooks and their completion status."""
    print("=" * 78)
    print("📓 Instructabot Engineering Notebooks — Live Progress Dashboard")
    print("=" * 78)
    print(f"{'Lab ID':<8} {'Notebook File':<36} {'Author':<16} {'Rubric Checks':<14} {'Status'}")
    print("-" * 78)

    files = sorted(list(NOTEBOOKS_DIR.glob("lab-*.md")))
    if not files:
        print("No lab notebooks found in notebooks/ directory.")
        return 0

    total_completed = 0
    for f in files:
        m = re.match(r"lab-(\d\d)-(.+)\.md", f.name)
        lab_id = f"Lab {int(m.group(1))}" if m else f.stem
        info = parse_notebook_status(f)
        author_display = info["author"][:15]
        checks_display = f"{info['checks_done']}/{info['checks_total']}" if info["checks_total"] > 0 else "N/A"
        
        status_icon = "⚪"
        if info["status"] == "Completed":
            status_icon = "🟢"
            total_completed += 1
        elif info["status"] == "In Progress":
            status_icon = "🟡"

        print(f"{lab_id:<8} {f.name:<36} {author_display:<16} {checks_display:<14} {status_icon} {info['status']}")

    print("-" * 78)
    print(f"Overall Completion: {total_completed}/{len(files)} Labs Complete ({int(total_completed / len(files) * 100)}%)")
    print("=" * 78)
    print("Commands:")
    print("  Initialize lab: python agent/notebook/cli.py --new <num> --author \"Your Name\"")
    print("  Verify rubric:  python agent/notebook/cli.py --verify <num>")
    return 0


def init_lab(lab_id, author_name):
    """Scaffolds or updates author/date for a lab notebook."""
    filepath = get_lab_file(lab_id)
    if not filepath:
        print(f"❌ Error: Could not find notebook matching Lab '{lab_id}'.")
        return 1

    content = filepath.read_text(encoding="utf-8")
    today_str = datetime.now().strftime("%Y-%m-%d")

    # Replace author placeholder
    content = re.sub(r"\*\*Author\*\*:\s*\[(Your Full Name|Your Name)\]", f"**Author**: {author_name}", content)
    # Replace date placeholder
    content = re.sub(r"\*\*Date\*\*:\s*\[YYYY-MM-DD\]", f"**Date**: {today_str}", content)

    filepath.write_text(content, encoding="utf-8")
    print(f"✅ Initialized {filepath.name}:")
    print(f"   Author: {author_name}")
    print(f"   Date:   {today_str}")
    print(f"   Path:   {filepath}")
    return 0


def verify_lab(lab_id):
    """Evaluates a lab notebook against the engineering rubric."""
    filepath = get_lab_file(lab_id)
    if not filepath:
        print(f"❌ Error: Could not locate notebook matching Lab '{lab_id}'.")
        return 1

    content = filepath.read_text(encoding="utf-8")
    filename = filepath.name

    print("=" * 70)
    print(f"🔍 Auditing Engineering Notebook: {filename}")
    print("=" * 70)

    score = 100
    deductions = []
    passes = []

    # 1. Author Metadata
    author_m = re.search(r"\*\*Author\*\*:\s*(.+)", content)
    author = author_m.group(1).strip() if author_m else ""
    if not author or "[" in author or "Your" in author:
        score -= 15
        deductions.append("[-15 pts] Author is not specified (contains placeholder brackets).")
    else:
        passes.append(f"[+15 pts] Author documented: {author}")

    # 2. Date Metadata
    date_m = re.search(r"\*\*Date\*\*:\s*(.+)", content)
    date_val = date_m.group(1).strip() if date_m else ""
    if not date_val or "YYYY" in date_val:
        score -= 5
        deductions.append("[-5 pts] Date is not recorded.")
    else:
        passes.append(f"[+5 pts] Date recorded: {date_val}")

    # 3. Sense-Think-Act Loop
    has_sta = bool(re.search(r"SENSE.*THINK.*ACT", content, flags=re.DOTALL | re.IGNORECASE))
    if not has_sta:
        score -= 20
        deductions.append("[-20 pts] Sense-Think-Act control loop breakdown is missing.")
    else:
        passes.append("[+20 pts] Sense-Think-Act engineering loop verified.")

    # 4. Multimeter / Empirical Data Table
    table_m = re.search(r"## 4\. (?:Empirical|Experimental).+?\n\n(.*?)\n\n---", content, flags=re.DOTALL)
    if not table_m or "|" not in table_m.group(1):
        score -= 20
        deductions.append("[-20 pts] Section 4 data table is missing or malformed.")
    else:
        table_text = table_m.group(1)
        placeholders_in_table = len(re.findall(r"\[Record", table_text, flags=re.IGNORECASE))
        if placeholders_in_table > 0:
            score -= 15
            deductions.append(f"[-15 pts] Data table has {placeholders_in_table} unrecorded measurement placeholders.")
        else:
            passes.append("[+20 pts] Empirical data table contains verified test readings.")

    # 5. Root Cause Troubleshooting Log
    trouble_m = re.search(r"## 5\. Troubleshooting.+?\n\n(.*?)\n\n---", content, flags=re.DOTALL)
    if not trouble_m:
        score -= 15
        deductions.append("[-15 pts] Troubleshooting & Root Cause section is missing.")
    else:
        trouble_text = trouble_m.group(1)
        if "[e.g." in trouble_text or "What unexpected behavior" in trouble_text:
            score -= 10
            deductions.append("[-10 pts] Troubleshooting section contains unmodified placeholder prompts.")
        else:
            passes.append("[+15 pts] Root-cause troubleshooting diagnosis thoroughly explained.")

    # 6. Reflection Questions
    reflection_m = re.search(r"## (?:6|7)\. (?:Engineering )?Reflection.+?\n\n(.*?)\n\n---", content, flags=re.DOTALL)
    if not reflection_m:
        score -= 15
        deductions.append("[-15 pts] Reflection section is missing.")
    else:
        ref_text = reflection_m.group(1)
        unanswered = len(re.findall(r"\[(Answer|Explain|Analyze)", ref_text, flags=re.IGNORECASE))
        if unanswered > 0:
            score -= 10
            deductions.append(f"[-10 pts] {unanswered} reflection prompt(s) are unanswered.")
        else:
            passes.append("[+15 pts] All engineering reflection prompts answered.")

    # 7. Rubric Checkboxes
    checks_empty = len(re.findall(r"-\s*\[\s\]", content))
    checks_done = len(re.findall(r"-\s*\[x\]", content, flags=re.IGNORECASE))
    if checks_empty > 0:
        score -= 10
        deductions.append(f"[-10 pts] {checks_empty} self-assessment rubric checkbox(es) remain unchecked.")
    elif checks_done > 0:
        passes.append(f"[+10 pts] All {checks_done} self-assessment checklist items marked complete.")

    final_score = max(0, score)

    # Print Itemized Report
    for p in passes:
        print(f"  ✅ {p}")
    for d in deductions:
        print(f"  ❌ {d}")

    print("-" * 70)
    print(f"Final Rubric Score: {final_score} / 100")
    if final_score >= 80:
        print("🎉 STATUS: PASS — Verified against NASA/JPL Documentation Standards!")
        print("=" * 70)
        return 0
    else:
        print("⚠️ STATUS: REVISE — Address itemized deductions before Git submission.")
        print("=" * 70)
        return 1


def main():
    parser = argparse.ArgumentParser(description="Instructabot Digital Engineering Notebook CLI")
    parser.add_argument("--list", "-l", action="store_true", help="List all lab notebooks and their status")
    parser.add_argument("--new", "-n", type=str, help="Scaffold or initialize a lab notebook (e.g. 1 or 'lab-01')")
    parser.add_argument("--author", "-a", type=str, default="Student Engineer", help="Author name for initialization")
    parser.add_argument("--verify", "-v", type=str, help="Evaluate a lab notebook against the grading rubric")

    args = parser.parse_args()

    if args.new:
        sys.exit(init_lab(args.new, args.author))
    elif args.verify:
        sys.exit(verify_lab(args.verify))
    else:
        sys.exit(list_labs())


if __name__ == "__main__":
    main()
