# 🎮 Instructabot Turn-Key Simulation Asset Pack

This directory contains standalone, ready-to-run simulation environments and hardware models for the entire Instructabot curriculum.

---

## 📁 Directory Structure

```text
simulations/
├── wokwi/                         # Zero-cost browser electronic circuits (Wokwi / MicroPython)
│   ├── lab-01-nightlight/         # Unit 1: Autonomous Transistor Nightlight Circuit
│   │   └── diagram.json
│   ├── lab-02-intersection/       # Unit 2: Smart Pedestrian Traffic Light State Machine
│   │   ├── diagram.json
│   │   ├── main.py
│   │   └── wokwi.toml
│   ├── lab-03-sonar-radar/        # Unit 3: Ultrasonic Sonar Sweep with Median Filter
│   │   ├── diagram.json
│   │   ├── main.py
│   │   └── wokwi.toml
│   └── lab-04-motor-controller/   # Unit 4: H-Bridge S-Curve Soft-Start Motor Controller
│       ├── diagram.json
│       ├── main.py
│       └── wokwi.toml
│
├── cad_urdf/                      # Kinematic CAD & Robot Description Format (URDF)
│   ├── instructabot_arm.urdf      # Unit 5: 3-DOF Spatial Robotic Arm with Joint Limits
│   └── instructabot_diffdrive.urdf# Unit 8/9: Mobile Robot (Wheels, Caster, LiDAR, Camera)
│
└── webots/                        # 3D Physics Simulation Worlds & Robot Controllers
    ├── worlds/
    │   └── lab_06_differential_drive_maze.wbt # Enclosed maze environment with obstacles
    └── controllers/
        ├── lab_06_maze_solver/    # Differential drive obstacle avoidance
        │   └── lab_06_maze_solver.py
        └── lab_07_aruco_tracker/  # OpenCV 4.7+ ArUco pan-tilt vision tracker
            └── lab_07_aruco_tracker.py
```

---

## 🚀 How to Run Simulations

### 1. Wokwi Browser Circuits (Labs 1 – 4)
- **Web Browser**: Open [wokwi.com](https://wokwi.com) and upload the corresponding `diagram.json` and `main.py` files.
- **VS Code Extension**: Install the **Wokwi Simulator** extension in VS Code. Open any `diagram.json` file and press `F1` $\to$ `Wokwi: Start Simulator`.

### 2. Robot URDF Visualizer (Unit 5, 8, 9)
- Open [`instructabot_arm.urdf`](cad_urdf/instructabot_arm.urdf) or [`instructabot_diffdrive.urdf`](cad_urdf/instructabot_diffdrive.urdf) in any online URDF viewer (e.g. [gkjohnson.github.io/urdf-loaders](https://gkjohnson.github.io/urdf-loaders/)) or in RViz2:
```bash
ros2 launch urdf_tutorial display.launch.py model:=simulations/cad_urdf/instructabot_diffdrive.urdf
```

### 3. Webots 3D Physics Simulator (Labs 6 – 10)
- Launch Webots (R2023b or later).
- File $\to$ Open World $\to$ select [`simulations/webots/worlds/lab_06_differential_drive_maze.wbt`](webots/worlds/lab_06_differential_drive_maze.wbt).
- Click the **Play** button in the Webots toolbar to watch the differential drive robot navigate the maze using real-time obstacle avoidance.
