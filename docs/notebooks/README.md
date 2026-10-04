# 📓 Instructabot Digital Engineering Notebooks

> *"If it isn’t documented, it didn't happen."*  
> — **NASA Robotics Alliance Project (RAP)** & JPL Standard Protocol

Welcome to the **Instructabot Version-Controlled Engineering Notebook System**. In professional aerospace, automotive, and medical robotics, hardware and code are only as good as the experimental evidence and iteration logs that accompany them.

---

## 🚀 Quickstart: How to Use Your Engineering Notebook

You can manage your engineering logs either directly in your text editor (VS Code, GitHub, etc.) or using our turnkey CLI tool:

### 1. View All Labs & Completion Status
Run the automated notebook inspector from the project root:
```bash
python agent/notebook/cli.py --list
```
This displays a live dashboard of all 11 lab entries and your completion status.

### 2. Scaffold a New Lab Entry
To start a new lab log pre-filled with your name and today's date:
```bash
python agent/notebook/cli.py --new 1 --author "Ada Lovelace"
```
This creates or initializes `notebooks/lab-01-nightlight-log.md` with your metadata.

### 3. Record Your Findings
Open your lab notebook file (e.g., `notebooks/lab-01-nightlight-log.md`) in your editor. As you conduct the lab:
- Formulate your **Sense-Think-Act Hypothesis**.
- Record raw **Multimeter / Telemetry Readings** in the data table.
- Document at least one **Troubleshooting & Root Cause Analysis** entry (what failed, why, and how you fixed it).
- Complete the **Self-Assessment Rubric Checklist**.

### 4. Verify Your Notebook (Rubric Quality Check)
Before submitting or pushing to GitHub, evaluate your entry against the automated grading rubric:
```bash
python agent/notebook/cli.py --verify 1
```
The verifier checks that:
- [x] Placeholder brackets (`[Your Name]`, `[Insert...]`) are replaced with genuine data.
- [x] Numerical measurements are recorded in data tables.
- [x] The Sense-Think-Act loop is analyzed.
- [x] Root-cause troubleshooting details are explained.
- [x] All rubric checkboxes are marked complete.

### 5. Commit Your Progress to Git
Commit your log into version control:
```bash
git add notebooks/lab-01-nightlight-log.md
git commit -m "docs(notebook): complete Lab 1 autonomous nightlight log"
```

---

## 📂 Directory Index

| File | Associated Curriculum Lab | Core Milestone |
| :--- | :--- | :--- |
| [**MASTER_NOTEBOOK_TEMPLATE.md**](MASTER_NOTEBOOK_TEMPLATE.md) | Universal Standard | Master template for custom or independent robotics projects |
| [**lab-00-systems-decomposition-log.md**](lab-00-systems-decomposition-log.md) | Unit 0 Lab 0 | Reverse-Engineering & 5 Subsystems Decomposition |
| [**lab-01-nightlight-log.md**](lab-01-nightlight-log.md) | Unit 1 Lab 1 | Autonomous Zero-Code Transistor Nightlight |
| [**lab-02-intersection-controller-log.md**](lab-02-intersection-controller-log.md) | Unit 2 Lab 2 | MicroPython State Machine Traffic Controller |
| [**lab-03-sonar-radar-scanner-log.md**](lab-03-sonar-radar-scanner-log.md) | Unit 3 Lab 3 | Ultrasonic Polar Sonar & Moving-Average Filter |
| [**lab-04-motor-drive-acceleration-log.md**](lab-04-motor-drive-acceleration-log.md) | Unit 4 Lab 4 | H-Bridge PWM Motor Driving & S-Curve Profiling |
| [**lab-05-robotic-arm-cad-sizing-log.md**](lab-05-robotic-arm-cad-sizing-log.md) | Unit 5 Lab 5 | 3-DOF Robotic Arm CAD & Torque Sizing |
| [**lab-06-maze-navigation-webots-log.md**](lab-06-maze-navigation-webots-log.md) | Unit 6 Lab 6 | Closed-Loop PID Odometry Maze Navigation |
| [**lab-07-pan-tilt-visual-turret-log.md**](lab-07-pan-tilt-visual-turret-log.md) | Unit 7 Lab 7 | OpenCV ArUco / Color Visual Tracking Turret |
| [**lab-08-modular-ros2-package-log.md**](lab-08-modular-ros2-package-log.md) | Unit 8 Lab 8 | Modular ROS 2 Pub/Sub & RViz2 Telemetry Graph |
| [**lab-09-autonomous-warehouse-nav2-log.md**](lab-09-autonomous-warehouse-nav2-log.md) | Unit 9 Lab 9 | 2D LiDAR SLAM & Nav2 Costmap Waypoint Navigation |
| [**lab-10-semantic-object-fetching-capstone-log.md**](lab-10-semantic-object-fetching-capstone-log.md) | Unit 10 Lab 10 | Sim2Real Capstone: YOLO Object Detection & Mobile Manipulation |

---

## 📐 The Five Core Questions of Every Entry

Every professional engineering entry must provide definitive answers to these five questions:
1. **Goal**: What specific problem or hypothesis am I tackling today?
2. **Design / Approach**: What components, schematics, or algorithmic flowcharts am I testing?
3. **Observations & Data**: What actually happened? (Numerical measurements and logs, not just *"it worked"*).
4. **Root Cause Analysis**: Why did it fail or succeed?
5. **Next Steps**: What specific parameter or code change will be tested next based on this evidence?
