#!/usr/bin/env python3
"""
Instructabot Headless Code Syntax & Execution Test Harness
---------------------------------------------------------
Extracts, parses, and validates all Python code blocks across curriculum markdown files:
1. Syntax Validation: Uses Python AST parser to catch syntax errors or invalid indentation.
2. Import Dependency Analysis: Identifies required packages (numpy, cv2, rclpy, webots).
3. Sandboxed Execution: Runs standalone mathematical/kinematic/simulation blocks in an
   isolated subprocess with execution timeout limits to verify output and stability.
"""

import os
import ast
import re
import sys
import time
import subprocess
from pathlib import Path
from typing import Dict, List, Any, Tuple

# Ensure UTF-8 output on Windows consoles
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"

class CodeExecutionHarness:
    def __init__(self, curriculum_dir: Path = CURRICULUM_DIR):
        self.curriculum_dir = curriculum_dir

    def extract_python_blocks(self, filepath: Path) -> List[str]:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return re.findall(r"```python(.*?)```", content, re.DOTALL)

    def validate_syntax(self, code_str: str) -> Tuple[bool, str]:
        """Parses code with ast to detect syntax/indentation errors."""
        try:
            ast.parse(code_str)
            return True, ""
        except SyntaxError as e:
            return False, f"Line {e.lineno}: {e.msg}"

    def can_run_standalone(self, code_str: str) -> bool:
        """Determines if a code block can be executed standalone in desktop CPython."""
        # 1. MicroPython dependencies (Pico / ESP32 hardware specific)
        micropython_keywords = ["import machine", "from machine", "time.ticks_ms", "time.sleep_ms", "ticks_diff"]
        if any(m in code_str for m in micropython_keywords):
            return False

        # 2. Hardware and robotics simulator middleware
        hardware_sim = [
            "from controller import", "import rclpy", "from rclpy", 
            "from nav2_simple_commander", "from setuptools", "from launch",
            "import tf2_ros", "cv2.VideoCapture", "cap.read()", "input(",
            "cv2.imshow"
        ]
        if any(h in code_str for h in hardware_sim):
            return False

        # 3. Exclude incomplete illustrative snippets (e.g. single while loops without helper defs)
        lines = [l.strip() for l in code_str.split("\n") if l.strip() and not l.strip().startswith("#")]
        if len(lines) < 6:
            return False

        # If it calls undefined placeholder functions like drive_forward() without defining them
        placeholders = ["drive_forward(", "read_distance_sensors(", "motor_left.", "motor.forward("]
        if any(p in code_str for p in placeholders):
            return False

        return True

    def test_file(self, filepath: Path) -> Dict[str, Any]:
        rel_path = filepath.relative_to(REPO_ROOT)
        blocks = self.extract_python_blocks(filepath)
        
        file_report = {
            "file": str(rel_path),
            "total_blocks": len(blocks),
            "syntax_passed": 0,
            "syntax_failed": 0,
            "executed_passed": 0,
            "executed_failed": 0,
            "errors": []
        }

        # Subprocess execution environment with UTF-8 encoding
        sub_env = {**os.environ, "PYTHONIOENCODING": "utf-8"}

        for idx, block in enumerate(blocks, 1):
            code = block.strip()
            if not code:
                continue

            # 1. Syntax Check
            valid, err = self.validate_syntax(code)
            if not valid:
                file_report["syntax_failed"] += 1
                file_report["errors"].append(f"Block #{idx} Syntax Error: {err}")
                continue
            else:
                file_report["syntax_passed"] += 1

            # 2. Execution Check (for standalone simulation/math blocks)
            if self.can_run_standalone(code):
                try:
                    res = subprocess.run(
                        [sys.executable, "-c", code],
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                        timeout=5.0,
                        env=sub_env
                    )
                    if res.returncode == 0:
                        file_report["executed_passed"] += 1
                    else:
                        err_line = res.stderr.strip().split("\n")[-1] if res.stderr else "Non-zero exit"
                        file_report["executed_failed"] += 1
                        file_report["errors"].append(f"Block #{idx} Runtime Failure: {err_line}")
                except subprocess.TimeoutExpired:
                    file_report["executed_failed"] += 1
                    file_report["errors"].append(f"Block #{idx} Timeout (>5s)")
                except Exception as ex:
                    file_report["executed_failed"] += 1
                    file_report["errors"].append(f"Block #{idx} Subprocess Error: {str(ex)}")
        return file_report

    def run_all(self) -> Dict[str, Any]:
        md_files = sorted(self.curriculum_dir.rglob("*.md"))
        md_files = [f for f in md_files if f.name not in ["LESSON_TEMPLATE.md", "SYLLABUS.md"]]

        total_files = len(md_files)
        total_blocks = 0
        total_syntax_pass = 0
        total_syntax_fail = 0
        total_exec_pass = 0
        total_exec_fail = 0
        all_reports = []

        for f in md_files:
            rep = self.test_file(f)
            total_blocks += rep["total_blocks"]
            total_syntax_pass += rep["syntax_passed"]
            total_syntax_fail += rep["syntax_failed"]
            total_exec_pass += rep["executed_passed"]
            total_exec_fail += rep["executed_failed"]
            if rep["errors"]:
                all_reports.append(rep)

        return {
            "total_files": total_files,
            "total_blocks": total_blocks,
            "syntax_passed": total_syntax_pass,
            "syntax_failed": total_syntax_fail,
            "executed_passed": total_exec_pass,
            "executed_failed": total_exec_fail,
            "failures": all_reports
        }

def main():
    print("=" * 65)
    print("💻 Instructabot Code Syntax & Headless Execution Test Harness")
    print("=" * 65)
    harness = CodeExecutionHarness()
    start_t = time.time()
    results = harness.run_all()
    elapsed = time.time() - start_t

    print(f"Scanned {results['total_files']} markdown files in {elapsed:.2f} seconds.")
    print(f"Total Python Code Blocks Discovered: {results['total_blocks']}")
    print(f"  ✅ Syntax Validated: {results['syntax_passed']} / {results['total_blocks']}")
    if results['syntax_failed'] > 0:
        print(f"  ❌ Syntax Failures:  {results['syntax_failed']}")
    print(f"  🚀 Standalone Subprocess Executions Passed: {results['executed_passed']}")
    if results['executed_failed'] > 0:
        print(f"  ⚠️ Standalone Execution Failures: {results['executed_failed']}")

    if results["failures"]:
        print("\n⚠️ Detailed Failures Log:")
        for rep in results["failures"]:
            print(f"\n📄 {rep['file']}:")
            for err in rep["errors"]:
                print(f"   ❌ {err}")
    else:
        print("\n🎉 ALL CODE BLOCKS PASSED SYNTAX & HEADLESS EXECUTION CHECKS!")

if __name__ == "__main__":
    main()
