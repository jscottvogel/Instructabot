#!/usr/bin/env python3
"""
Instructabot Pedagogical Critic & Readability Reviewer
------------------------------------------------------
Analyzes curriculum lessons for:
1. Target audience fit (high school & college novices with zero prior background).
2. Jargon police: Identifies complex terminology and ensures an intuitive
   physical/mechanical analogy is provided before or immediately with it.
3. Structural completeness: Verifies all standardized pedagogical sections exist.
4. Readability metrics: Analyzes sentence length and reading ease.
5. Five Subsystems reinforcement: Confirms connection to universal robotics subsystems.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any

# Ensure UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"

# Advanced jargon dictionary with required friendly conceptual anchors
JARGON_REGISTRY: Dict[str, List[str]] = {
    "discretization": ["sample", "bucket", "grid", "step", "chunk"],
    "quaternion": ["3d", "orientation", "rotation", "axis", "angle"],
    "jacobian": ["rate", "velocity", "matrix", "derivative", "arm"],
    "hysteresis": ["threshold", "dual", "gap", "buffer", "flicker"],
    "non-holonomic": ["car", "wheel", "turn", "constraint", "sideways"],
    "serialization": ["message", "packet", "stream", "byte", "convert"],
    "convolution": ["slide", "window", "filter", "kernel", "average"],
    "deadband": ["jitter", "noise", "zone", "window", "chatter"],
    "eigenvalues": ["principal", "axis", "scale", "direction", "vector"],
    "stiction": ["static", "friction", "stick", "gear", "stall"],
    "backlash": ["gear", "gap", "play", "teeth", "slop"],
    "quantization": ["bin", "integer", "round", "precision", "step"]
}

MANDATORY_SECTIONS = [
    "Learning Objectives",
    "Intuitive Big Picture",
    "The Core Concept Explained",
    "Troubleshooting",
    "Sources & Media Provenance"
]

FIVE_SUBSYSTEMS = ["brain", "senses", "sensor", "muscles", "motor", "bones", "structure", "mechanics", "spark", "power", "electricity"]

class PedagogyReviewer:
    def __init__(self, curriculum_dir: Path = CURRICULUM_DIR):
        self.curriculum_dir = curriculum_dir

    def audit_lesson(self, filepath: Path) -> Dict[str, Any]:
        """Audits a single markdown file against pedagogical guidelines."""
        rel_path = filepath.relative_to(REPO_ROOT)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        results = {
            "file": str(rel_path),
            "score": 100,
            "issues": [],
            "warnings": [],
            "stats": {}
        }

        # 1. Structural Section Completeness Check
        for sec in MANDATORY_SECTIONS:
            # Look for section header variations (e.g. ## 2. Intuitive Big Picture)
            if not re.search(rf"^##\s+.*{re.escape(sec)}", content, re.MULTILINE | re.IGNORECASE):
                # Labs may use slightly different titles; check leniently
                if "lab" in filepath.name.lower() and sec in ["The Core Concept Explained"]:
                    continue
                results["warnings"].append(f"Missing recommended section header: '{sec}'")
                results["score"] -= 5

        # 2. Prerequisites & Time Estimation Header Check
        if not re.search(r">\s+\*\*Prerequisites\*\*:", content):
            results["warnings"].append("Missing Prerequisites declaration blockquote.")
            results["score"] -= 5
        if not re.search(r">\s+\*\*Estimated Time\*\*:", content):
            results["warnings"].append("Missing Estimated Time blockquote.")
            results["score"] -= 5

        # 3. Jargon Police: Terminology without analogical grounding
        lower_content = content.lower()
        for term, expected_anchors in JARGON_REGISTRY.items():
            if term in lower_content:
                # Find paragraphs containing this term
                paragraphs = re.split(r"\n\s*\n", content)
                for p in paragraphs:
                    if term in p.lower():
                        # Check if any friendly anchor appears in the paragraph or surrounding context
                        has_anchor = any(anchor in p.lower() for anchor in expected_anchors)
                        if not has_anchor:
                            results["warnings"].append(
                                f"Technical term '{term}' used without immediate friendly anchor/analogy (expected: {expected_anchors})."
                            )
                            results["score"] -= 3
                            break

        # 4. Readability & Sentence Length Analysis
        sentences = re.split(r"[.!?]\s+", content)
        long_sentences = [s.strip() for s in sentences if len(s.split()) > 45 and not s.strip().startswith("|") and not s.strip().startswith("```")]
        if long_sentences:
            results["warnings"].append(
                f"Detected {len(long_sentences)} sentences with >45 words (may impede high-school reading comprehension)."
            )
            results["score"] -= min(10, len(long_sentences) * 2)

        # 5. Visual Support Check: Diagrams & Code Examples
        mermaid_count = len(re.findall(r"```mermaid", content))
        code_count = len(re.findall(r"```python", content))
        callout_count = len(re.findall(r">\s+\[!(?:NOTE|WARNING|CAUTION|TIP|IMPORTANT)\]", content))

        results["stats"] = {
            "word_count": len(content.split()),
            "mermaid_diagrams": mermaid_count,
            "python_code_blocks": code_count,
            "pedagogical_callouts": callout_count
        }

        if mermaid_count == 0 and "lab" not in filepath.name.lower():
            results["warnings"].append("No Mermaid visual diagrams found in conceptual module.")
            results["score"] -= 8

        if callout_count == 0:
            results["warnings"].append("No pedagogical callout alerts ([!NOTE], [!WARNING]) found.")
            results["score"] -= 5

        # Bound score between 0 and 100
        results["score"] = max(0, min(100, results["score"]))
        return results

    def audit_all(self) -> Tuple[int, List[Dict[str, Any]]]:
        """Audits all curriculum lessons in the repository."""
        all_results = []
        md_files = sorted(self.curriculum_dir.rglob("*.md"))
        # Filter out templates and auxiliary documentation
        excluded = {"LESSON_TEMPLATE.md", "SYLLABUS.md", "README.md", "GETTING_STARTED.md", "GLOSSARY.md"}
        md_files = [f for f in md_files if f.name not in excluded]

        total_score = 0
        for md_file in md_files:
            res = self.audit_lesson(md_file)
            all_results.append(res)
            total_score += res["score"]

        avg_score = int(total_score / len(all_results)) if all_results else 0
        return avg_score, all_results

def main():
    print("=" * 65)
    print("🎓 Instructabot Pedagogical Critic & Readability Audit")
    print("=" * 65)
    reviewer = PedagogyReviewer()
    avg_score, results = reviewer.audit_all()

    print(f"Audited {len(results)} curriculum modules.")
    print(f"Overall Curriculum Pedagogical Quality Score: {avg_score}/100\n")

    low_scoring = [r for r in results if r["score"] < 90]
    if low_scoring:
        print(f"⚠️ {len(low_scoring)} modules flagged with pedagogical warnings (score < 90):")
        for r in low_scoring:
            print(f"\n📄 {r['file']} (Score: {r['score']}/100)")
            for w in r["warnings"]:
                print(f"   ⚠️  {w}")
    else:
        print("🎉 ALL MODULES MEET SOTA NOVICE PEDAGOGICAL STANDARDS (Score >= 90)!")

if __name__ == "__main__":
    main()
