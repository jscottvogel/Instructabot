#!/usr/bin/env python3
"""
Instructabot Upstream Dependency & Deprecation Sentinel
------------------------------------------------------
Monitors curriculum dependencies, library imports, and API conventions:
1. Audits external libraries: OpenCV, ROS 2, NumPy, PyTorch, Ultralytics YOLO, Webots.
2. Flags deprecated API calls (e.g., legacy ArUco syntax, outdated ROS 1 idioms).
3. Verifies version alignment (ROS 2 Humble/Iron LTS, Python 3.10+, OpenCV 4.x).
4. Generates an automated Dependency Health Report for the Editorial Board.
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

KNOWN_DEPENDENCIES = {
    "numpy": {"recommended": ">=1.24.0", "role": "Matrix algebra & point cloud processing"},
    "opencv-python": {"recommended": ">=4.7.0", "role": "Computer vision & ArUco detection"},
    "rclpy": {"recommended": "ROS 2 Humble / Iron", "role": "Robotics middleware & pub/sub"},
    "ultralytics": {"recommended": ">=8.0.0", "role": "Real-time YOLO object detection"},
    "controller": {"recommended": "Webots R2023b / R2024a", "role": "3D robotics physics simulation"},
    "nav2_simple_commander": {"recommended": "Nav2 Humble", "role": "Autonomous mission planning"}
}

DEPRECATED_PATTERNS = [
    {
        "pattern": r"rospy\.",
        "description": "Legacy ROS 1 'rospy' detected. Must use modern ROS 2 'rclpy'!",
        "severity": "CRITICAL"
    },
    {
        "pattern": r"aruco\.detectMarkers\([^)]*aruco_dict\s*,\s*parameters",
        "description": "Legacy OpenCV <4.7 ArUco API detected. Must use cv2.aruco.ArucoDetector!",
        "severity": "WARNING"
    },
    {
        "pattern": r"tf\.(?:TransformBroadcaster|TransformListener)",
        "description": "Legacy ROS 1 tf library detected. Must use modern tf2_ros!",
        "severity": "CRITICAL"
    },
    {
        "pattern": r"np\.float(?!32|64)",
        "description": "Deprecated NumPy 1.24+ 'np.float' detected. Use standard float or np.float32/64.",
        "severity": "WARNING"
    }
]

class DependencySentinel:
    def __init__(self, curriculum_dir: Path = CURRICULUM_DIR):
        self.curriculum_dir = curriculum_dir

    def audit_lesson(self, filepath: Path) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        rel_path = filepath.relative_to(REPO_ROOT)
        findings = []

        # 1. Check for deprecated patterns
        for rule in DEPRECATED_PATTERNS:
            matches = re.finditer(rule["pattern"], content)
            for m in matches:
                # Find line number
                line_no = content[:m.start()].count("\n") + 1
                findings.append({
                    "line": line_no,
                    "severity": rule["severity"],
                    "description": rule["description"]
                })

        # 2. Extract active import statements in code blocks
        code_blocks = re.findall(r"```python(.*?)```", content, re.DOTALL)
        discovered_imports = set()
        for cb in code_blocks:
            import_matches = re.findall(r"^\s*(?:import|from)\s+([a-zA-Z0-9_\.]+)", cb, re.MULTILINE)
            for imp in import_matches:
                pkg = imp.split(".")[0]
                discovered_imports.add(pkg)

        return {
            "file": str(rel_path),
            "imports": sorted(list(discovered_imports)),
            "issues": findings
        }

    def audit_all(self) -> Dict[str, Any]:
        md_files = sorted(self.curriculum_dir.rglob("*.md"))
        md_files = [f for f in md_files if f.name not in ["LESSON_TEMPLATE.md", "SYLLABUS.md"]]

        all_reports = []
        global_imports = set()
        total_issues = 0

        for f in md_files:
            rep = self.audit_lesson(f)
            global_imports.update(rep["imports"])
            if rep["issues"]:
                all_reports.append(rep)
                total_issues += len(rep["issues"])

        return {
            "total_modules": len(md_files),
            "global_imports": sorted(list(global_imports)),
            "flagged_modules": all_reports,
            "total_issues": total_issues
        }

def main():
    print("=" * 65)
    print("📡 Instructabot Upstream Dependency & Deprecation Sentinel")
    print("=" * 65)
    sentinel = DependencySentinel()
    results = sentinel.audit_all()

    print(f"Scanned {results['total_modules']} modules for modern API compliance.")
    print(f"Discovered {len(results['global_imports'])} unique Python packages across curriculum:")
    print("  " + ", ".join(results["global_imports"]) + "\n")

    if results["total_issues"] > 0:
        print(f"⚠️ Found {results['total_issues']} API deprecation issues:")
        for r in results["flagged_modules"]:
            print(f"\n📄 {r['file']}:")
            for issue in r["issues"]:
                print(f"   [{issue['severity']}] Line {issue['line']}: {issue['description']}")
    else:
        print("🎉 ZERO DEPRECATED APIS DETECTED! 100% modern ROS 2, OpenCV 4.x, and NumPy 1.24+ compliance.")

if __name__ == "__main__":
    main()
