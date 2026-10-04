#!/usr/bin/env python3
"""
Instructabot Mermaid Syntax Linter & Fixer
-----------------------------------------
Fixes unquoted Mermaid subgraph titles containing parentheses, colons,
brackets, or special characters that trigger GitHub Markdown render errors.
"""

import sys
import re
from pathlib import Path

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def fix_mermaid_in_file(filepath: Path) -> int:
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return 0

    modified = False
    new_lines = []
    changes = 0

    in_mermaid = False

    for line in content.splitlines():
        trimmed = line.strip()
        if trimmed.startswith("```mermaid"):
            in_mermaid = True
            new_lines.append(line)
            continue
        elif in_mermaid and trimmed.startswith("```"):
            in_mermaid = False
            new_lines.append(line)
            continue

        if in_mermaid:
            # Match subgraph definitions
            # Examples to fix:
            #   subgraph Energy Network (Power Rails)
            #   subgraph The High-Level Cortex: Single-Board Computer (SBC)
            m = re.match(r"^(\s*subgraph\s+)(.+)$", line)
            if m:
                prefix = m.group(1)
                title = m.group(2).strip()

                # If already enclosed in double quotes or bracketed id ["..."], skip
                if not (title.startswith('"') and title.endswith('"')) and not re.match(r'^\w+\s*\[".*"\]$', title):
                    # Wrap title in double quotes
                    # Remove any existing outer quotes if mismatched
                    clean_title = title.strip('"')
                    new_line = f'{prefix}"{clean_title}"'
                    new_lines.append(new_line)
                    modified = True
                    changes += 1
                    continue

        new_lines.append(line)

    if modified:
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"🔧 Fixed {changes} Mermaid subgraph(s) in: {filepath.relative_to(REPO_ROOT)}")

    return changes


def main():
    print("=" * 65)
    print("🔍 Scanning repository for Mermaid syntax issues...")
    print("=" * 65)

    total_fixed = 0
    search_dirs = [
        REPO_ROOT / "curriculum",
        REPO_ROOT / "hardware",
        REPO_ROOT / "simulations",
        REPO_ROOT / "docs",
        REPO_ROOT / "reviews",
        REPO_ROOT / "README.md"
    ]

    md_files = []
    for target in search_dirs:
        if target.is_file():
            md_files.append(target)
        elif target.is_dir():
            md_files.extend(list(target.rglob("*.md")))

    for f in sorted(set(md_files)):
        total_fixed += fix_mermaid_in_file(f)

    print("=" * 65)
    print(f"🎉 Complete! Fixed {total_fixed} Mermaid syntax instances across repository.")
    print("=" * 65)


if __name__ == "__main__":
    main()
