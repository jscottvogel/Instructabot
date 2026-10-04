#!/usr/bin/env python3
"""
Instructabot Simulated Learner Persona Stress-Tester
---------------------------------------------------
Evaluates curriculum lessons against three distinct learner personas:
1. Maya (10th Grader, Novice): Zero coding, zero advanced physics/EE background.
2. Jordan (College ME Sophomore): Strong calculus/physics, zero Linux/Python.
3. Sam (Vocational Hardware Technician): Pragmatic, safety-focused, hates fluff.

Outputs a structured "Student Friction Report" with actionable author feedback.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any

# Ensure UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"

class PersonaTester:
    def __init__(self, curriculum_dir: Path = CURRICULUM_DIR):
        self.curriculum_dir = curriculum_dir

    def evaluate_lesson(self, filepath: Path) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        rel_path = filepath.relative_to(REPO_ROOT)
        is_lab = "lab" in filepath.name.lower()

        report = {
            "file": str(rel_path),
            "is_lab": is_lab,
            "overall_friction_index": 0,  # 0 (smooth) to 100 (extreme friction)
            "persona_feedback": {}
        }

        # -------------------------------------------------------------
        # Persona 1: Maya (10th Grader, Novice)
        # -------------------------------------------------------------
        maya_friction = 0
        maya_notes = []

        # Check for intimidating advanced math symbols without plain English translation
        unexplained_math = re.findall(r"\$\$(.*?)\$\$", content, re.DOTALL)
        for eq in unexplained_math:
            # Check for calculus integrals or partial derivatives
            if ("\\int" in eq or "\\partial" in eq or "\\sum" in eq) and ("intuition" not in content.lower() and "analogy" not in content.lower()):
                maya_friction += 15
                maya_notes.append("Found dense mathematical formula ($$\\int$$ or $$\\sum$$) without immediate intuitive plain-English analogy.")
                break

        # Check for code blocks without inline comments (#)
        code_blocks = re.findall(r"```python(.*?)```", content, re.DOTALL)
        for cb in code_blocks:
            lines = [l.strip() for l in cb.strip().split("\n") if l.strip()]
            comment_lines = [l for l in lines if l.startswith("#")]
            if len(lines) > 25 and len(comment_lines) / len(lines) < 0.15:
                maya_friction += 12
                maya_notes.append("Code block has >25 lines with fewer than 15% explanatory comments. Maya feels intimidated.")
                break

        # Check for visual diagram support
        if "```mermaid" not in content and not is_lab:
            maya_friction += 15
            maya_notes.append("Missing visual diagram (flowchart or diagram). Maya struggles to visualize abstract concepts.")

        # Check for real-world metaphor
        metaphors = ["imagine", "like a", "analogy", "think of", "just as", "metaphor"]
        if not any(m in content.lower() for m in metaphors):
            maya_friction += 10
            maya_notes.append("No intuitive real-world analogy detected ('Imagine...', 'Like a...').")

        # -------------------------------------------------------------
        # Persona 2: Jordan (College ME Sophomore, Zero Linux/Python)
        # -------------------------------------------------------------
        jordan_friction = 0
        jordan_notes = []

        # Check for unexplained terminal commands or imports
        unexplained_terminal = re.findall(r"```(?:bash|sh)(.*?)```", content, re.DOTALL)
        for tb in unexplained_terminal:
            if ("export" in tb or "source" in tb or "colcon" in tb) and "why" not in tb.lower():
                jordan_friction += 10
                jordan_notes.append("Unexplained shell configuration commands (`source`, `export`, `colcon`). Jordan doesn't know what sourcing means.")
                break

        # Check for physical units of measurement
        units = ["m/s", "rad/s", "nm", "mm", "meters", "degrees", "v", "a", "hz", "kg", "seconds", "ms"]
        unit_mentions = sum(1 for u in units if f" {u}" in content.lower() or f"{u} " in content.lower())
        if unit_mentions < 3 and not is_lab:
            jordan_friction += 8
            jordan_notes.append("Few explicit physical units detected. Jordan wants to know exact torque, velocity, and mass dimensions.")

        # -------------------------------------------------------------
        # Persona 3: Sam (Vocational Hardware Technician)
        # -------------------------------------------------------------
        sam_friction = 0
        sam_notes = []

        # Safety & Hardware Warnings Check
        has_safety = (
            "> [!WARNING]" in content or
            "> [!CAUTION]" in content or
            "short circuit" in content.lower() or
            "current limit" in content.lower() or
            "stall current" in content.lower()
        )
        if not has_safety and not is_lab:
            sam_friction += 12
            sam_notes.append("Missing practical hardware safety callout ([!WARNING] or [!CAUTION]). Sam asks: 'What blows up if I wire this wrong?'")

        # Hands-On / Simulation Link
        if "```python" not in content and "step 1" not in content.lower():
            sam_friction += 15
            sam_notes.append("Too theoretical with zero runnable code or concrete assembly steps. Sam gets bored.")

        # Compute aggregate friction
        avg_friction = int((maya_friction * 0.45) + (jordan_friction * 0.30) + (sam_friction * 0.25))
        report["overall_friction_index"] = avg_friction
        report["persona_feedback"] = {
            "maya_10th_grader": {"friction": maya_friction, "notes": maya_notes},
            "jordan_college_me": {"friction": jordan_friction, "notes": jordan_notes},
            "sam_technician": {"friction": sam_friction, "notes": sam_notes}
        }
        return report

    def evaluate_curriculum(self) -> Dict[str, Any]:
        all_files = sorted(self.curriculum_dir.rglob("*.md"))
        excluded = {"LESSON_TEMPLATE.md", "SYLLABUS.md", "README.md", "GETTING_STARTED.md", "GLOSSARY.md"}
        md_files = [f for f in all_files if f.name not in excluded]

        all_reports = []
        total_friction = 0
        for f in md_files:
            rep = self.evaluate_lesson(f)
            all_reports.append(rep)
            total_friction += rep["overall_friction_index"]

        avg_friction = int(total_friction / len(all_reports)) if all_reports else 0
        return {
            "average_friction_index": avg_friction,
            "modules_evaluated": len(all_reports),
            "reports": all_reports
        }

def main():
    print("=" * 65)
    print("🧒 Instructabot Simulated Learner Persona Stress-Test")
    print("=" * 65)
    tester = PersonaTester()
    summary = tester.evaluate_curriculum()

    print(f"Evaluated {summary['modules_evaluated']} modules across Maya, Jordan, and Sam.")
    print(f"Overall Curriculum Friction Index: {summary['average_friction_index']}/100 (Lower is smoother)\n")

    high_friction = [r for r in summary["reports"] if r["overall_friction_index"] > 15]
    if high_friction:
        print(f"⚠️ {len(high_friction)} modules with notable student friction points (>15):")
        for r in high_friction:
            print(f"\n📄 {r['file']} (Friction Index: {r['overall_friction_index']}/100)")
            for persona, pdata in r["persona_feedback"].items():
                if pdata["notes"]:
                    print(f"   👤 {persona} (Friction: {pdata['friction']}):")
                    for n in pdata["notes"]:
                        print(f"      - {n}")
    else:
        print("🎉 EXCELLENT! Friction Index is exceptionally low across all student personas.")

if __name__ == "__main__":
    main()
