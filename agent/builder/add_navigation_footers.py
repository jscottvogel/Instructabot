#!/usr/bin/env python3
"""
Instructabot Navigation Footer Generator & Auditor
--------------------------------------------------
Iterates through all 51 curriculum modules across Units 0 through 10,
extracts concise titles, calculates clean relative links (with forward slashes),
and adds standardized "Lesson Navigation" footers + Capstone Celebration banners.
"""

import sys
import os
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
CURRICULUM_DIR = REPO_ROOT / "curriculum"

CAPSTONE_MILESTONES = {
    0: {
        "title": "Unit 0 Foundations Capstone Complete!",
        "desc": "You have deconstructed real autonomous robots and established NASA/JPL-standard engineering logs and safety protocols.",
        "next_preview": "In **Unit 1: The Spark**, you will wire your first circuits and build autonomous solid-state hardware from scratch!"
    },
    1: {
        "title": "Unit 1 Electronics Capstone Complete!",
        "desc": "You designed and verified an autonomous Sense-Think-Act nightlight circuit operating entirely on analog semiconductor physics without code.",
        "next_preview": "In **Unit 2: The Brain**, you will connect microcontrollers and write real-time Python state machines to control physical hardware!"
    },
    2: {
        "title": "Unit 2 Computational Thinking Capstone Complete!",
        "desc": "You engineered an autonomous pedestrian intersection controller with non-blocking state machines and interrupt handling in MicroPython.",
        "next_preview": "In **Unit 3: The Senses**, you will connect distance sensors and IMUs to give your robot spatial awareness and sensory perception!"
    },
    3: {
        "title": "Unit 3 Sensory Perception Capstone Complete!",
        "desc": "You built an active ultrasonic polar radar and implemented digital filtering to reject acoustic multipath noise.",
        "next_preview": "In **Unit 4: The Muscles**, you will drive high-power DC motors, servos, and steppers using H-Bridges and PWM velocity curves!"
    },
    4: {
        "title": "Unit 4 Actuation & Power Capstone Complete!",
        "desc": "You constructed high-current H-bridge drivers with S-curve soft acceleration, preventing battery brownouts and gear lash.",
        "next_preview": "In **Unit 5: The Bones**, you will step into 3D CAD modeling, mechanics, gear ratios, and torque sizing for robotic arms!"
    },
    5: {
        "title": "Unit 5 Mechanics & CAD Capstone Complete!",
        "desc": "You modeled structural robotic limbs in parametric CAD and verified structural safety margins under gravitational payloads.",
        "next_preview": "In **Unit 6: Movement & Mobile Robotics**, you will deploy mobile wheeled robots into the Webots 3D physics simulator!"
    },
    6: {
        "title": "Unit 6 Mobile Robotics Capstone Complete!",
        "desc": "You tuned closed-loop PID wall-following controllers and odometry dead-reckoning to solve complex 3D mazes autonomously.",
        "next_preview": "In **Unit 7: Robot Vision**, you will give your robot sight using OpenCV, computer vision color segmentation, and visual tracking!"
    },
    7: {
        "title": "Unit 7 Computer Vision Capstone Complete!",
        "desc": "You engineered a real-time 2-DOF pan-tilt tracking gimbal capable of centering optical targets dynamically at 30 FPS.",
        "next_preview": "In **Unit 8: ROS 2 Middleware**, you will enter the industry standard robot operating system with multi-node pub/sub graphs!"
    },
    8: {
        "title": "Unit 8 ROS 2 Middleware Capstone Complete!",
        "desc": "You architected modular ROS 2 publisher, subscriber, and service nodes with live RViz2 coordinate transform telemetry.",
        "next_preview": "In **Unit 9: Autonomous Navigation**, you will solve the fundamental problem of SLAM with 2D LiDAR and Nav2 costmaps!"
    },
    9: {
        "title": "Unit 9 SLAM & Navigation Capstone Complete!",
        "desc": "You mapped an unfamiliar warehouse with 2D LiDAR SLAM and commanded obstacle-aware waypoint navigation via Nav2.",
        "next_preview": "In **Unit 10: Modern AI & Sim2Real**, you will complete the grand capstone: YOLO object detection, 3D point clouds, and mobile manipulation!"
    },
    10: {
        "title": "🎓 Master Capstone Complete: You Are a Full-Stack Autonomous Roboticist!",
        "desc": "You integrated end-to-end deep learning perception, 3D point-cloud coordinate projection, MoveIt 2 arm trajectory planning, and autonomous mobile navigation.",
        "next_preview": "You have mastered the entire spectrum of autonomous robotics from discrete transistor electronics to state-of-the-art AI foundation models!"
    }
}


def extract_clean_title(filepath: Path) -> str:
    """Extracts a clean, concise navigation title from Markdown file."""
    lines = filepath.read_text(encoding="utf-8").splitlines()
    unit_num = ""
    mod_num = ""
    title_text = ""

    for line in lines[:10]:
        line = line.strip()
        m_unit = re.match(r"# Unit\s*(\d+)", line, re.IGNORECASE)
        if m_unit:
            unit_num = m_unit.group(1)

        m_mod = re.match(r"# (?:Module|Lab)\s*([\d\.]+):\s*(.+)", line, re.IGNORECASE)
        if m_mod:
            mod_num = m_mod.group(1)
            title_text = m_mod.group(2).strip()
            break

    if not title_text:
        for line in lines[:10]:
            if line.startswith("# "):
                title_text = line[2:].strip()
                if ":" in title_text:
                    title_text = title_text.split(":")[-1].strip()
                break

    filename = filepath.stem
    if "lab-" in filename:
        m = re.match(r"lab-(\d\d)-(.*)", filename)
        lab_digits = int(m.group(1)) if m else 0
        name_clean = m.group(2).replace("-", " ").title() if m else "Lab Capstone"
        return f"Lab {lab_digits}: {title_text or name_clean}"
    elif filename.startswith("0") or filename[0].isdigit():
        num = filename[:2]
        return f"Module {unit_num}.{num.lstrip('0') or '0'}: {title_text}"

    return title_text or filepath.stem.replace("-", " ").title()


def get_curriculum_sequence():
    """Returns sorted list of all 51 curriculum module Paths."""
    unit_dirs = sorted([d for d in CURRICULUM_DIR.iterdir() if d.is_dir() and d.name.startswith("unit-")])
    sequence = []
    for u_dir in unit_dirs:
        md_files = sorted(u_dir.glob("*.md"))
        sequence.extend(md_files)
    return sequence


def add_navigation_to_file(filepath: Path, prev_info, next_info, capstone_info=None):
    """Formats and writes standard navigation block to the end of a lesson file."""
    content = filepath.read_text(encoding="utf-8")

    # Remove existing navigation section if present
    content = re.sub(r"\n---\s*\n\s*## 🧭 Lesson Navigation.*$", "", content, flags=re.DOTALL)
    content = re.sub(r"\n---\s*\n\s*## 🏆 Milestone Achieved.*$", "", content, flags=re.DOTALL)
    content = content.rstrip()

    nav_lines = ["", "", "---", ""]

    # Capstone celebratory banner if applicable
    if capstone_info:
        nav_lines.extend([
            f"## 🏆 Milestone Achieved: {capstone_info['title']}",
            "",
            f"🎉 {capstone_info['desc']}",
            "",
            f"> 💡 **What's Next?** {capstone_info['next_preview']}",
            "",
            "---",
            ""
        ])

    nav_lines.append("## 🧭 Lesson Navigation")
    nav_lines.append("")
    nav_lines.append("| ⬅️ Previous Lesson | 🗺️ Course Hub | ➡️ Next Lesson |")
    nav_lines.append("| :--- | :---: | ---: |")

    # Previous Link
    if prev_info:
        prev_title, prev_rel = prev_info
        prev_cell = f"[← {prev_title}]({prev_rel})"
    else:
        prev_cell = "[🚀 Getting Started Guide](../GETTING_STARTED.md)"

    # Hub Links
    hub_cell = "[**Master Syllabus**](../SYLLABUS.md) • [**Getting Started**](../GETTING_STARTED.md)"

    # Next Link
    if next_info:
        next_title, next_rel = next_info
        next_cell = f"[**{next_title} →**]({next_rel})"
    else:
        next_cell = "[🎓 **Autonomous Robotics Graduation & Community →**](../../README.md)"

    nav_lines.append(f"| {prev_cell} | {hub_cell} | {next_cell} |")
    nav_lines.append("")

    new_content = content + "\n".join(nav_lines)
    filepath.write_text(new_content, encoding="utf-8")


def main():
    print("=" * 70)
    print("🧭 Instructabot Standardized Lesson Navigation Injector")
    print("=" * 70)

    modules = get_curriculum_sequence()
    print(f"Discovered {len(modules)} curriculum modules across Units 0 through 10.")

    titles = [extract_clean_title(m) for m in modules]

    updated_count = 0
    for idx, mod_path in enumerate(modules):
        # Previous
        prev_info = None
        if idx > 0:
            prev_path = modules[idx - 1]
            rel_prev = os.path.relpath(prev_path, mod_path.parent).replace("\\", "/")
            prev_info = (titles[idx - 1], rel_prev)

        # Next
        next_info = None
        if idx < len(modules) - 1:
            next_path = modules[idx + 1]
            rel_next = os.path.relpath(next_path, mod_path.parent).replace("\\", "/")
            next_info = (titles[idx + 1], rel_next)

        # Capstone check
        capstone_info = None
        if "lab-" in mod_path.name:
            m = re.match(r"lab-(\d\d)", mod_path.name)
            if m:
                lab_num = int(m.group(1))
                capstone_info = CAPSTONE_MILESTONES.get(lab_num)

        add_navigation_to_file(mod_path, prev_info, next_info, capstone_info)
        updated_count += 1

    print(f"🎉 Successfully injected standardized navigation across all {updated_count} lessons!")
    print("=" * 70)


if __name__ == "__main__":
    main()
