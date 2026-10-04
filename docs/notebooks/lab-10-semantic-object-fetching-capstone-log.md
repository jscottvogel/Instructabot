# 📓 Engineering Log: Lab 10 — Capstone: Semantic Object Fetching & Sorting Pipeline

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 10: State of the Art: Modern AI, Foundation Models, & Sim2Real  
**Target Platform**: [Mobile Manipulator + RGB-D Camera + YOLOv8 + ROS 2 MoveIt 2]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Integrate all 10 units into an end-to-end autonomous perception-to-action robotics pipeline: detect target objects semantically using YOLOv8, project 2D bounding boxes into 3D camera coordinates via RGB-D depth point clouds, plan collision-free arm trajectories via MoveIt 2, and complete autonomous pick-and-sort cycles.

### Sense-Think-Act Hypothesis
- **SENSE**: RGB-D camera captures synchronized color image and 3D depth point cloud ($X, Y, Z$).
- **THINK**: YOLOv8 detects object class label and 2D bounding box; coordinate projection calculates 3D grasp pose; MoveIt 2 generates inverse kinematics (IK) trajectory.
- **ACT**: Mobile base maneuvers to table, robotic arm executes pick trajectory, gripper closes, and arm sorts item into appropriate bin.
- **Hypothesis**: Domain randomization in simulation (varying lighting, table textures, object colors) will bridge the Sim2Real gap, achieving $>85\%$ zero-shot object grasp success rate on real physical hardware.

---

## 2. System Architecture & Schematic

```mermaid
flowchart LR
    Sensor["👁️ SENSE<br/>Input Transducers"] --> Logic["🧠 THINK<br/>Control Logic / Microcontroller / AI"]
    Logic --> Actuator["⚙️ ACT<br/>Actuators / Motors / End-Effector"]
```

> Attach an ASCII schematic, pinout diagram, or photograph/screenshot of your build or simulation below:
> *(Optional: Save images in `notebooks/media/` and reference them here)*

---

## 3. Bill of Materials & Subsystem Verification

| Component / Subsystem | Part Number / Specs | Quantity | Interface / GPIO Pin | Power Supply Rail |
| :--- | :--- | :--- | :--- | :--- |
| **Mobile Base** | Omnidirectional or Differential Mobile AMR | 1 | Nav2 Waypoint Navigation | 24V Battery Subsystem |
| **Manipulator Arm** | 4-DOF or 6-DOF Robotic Arm with Parallel Gripper | 1 | MoveIt 2 Trajectory Execution | 12V Actuator Rail |
| **Perception Sensor** | Intel RealSense D435 / OAK-D Lite RGB-D Camera | 1 | USB 3.0 High-Speed | 5.0V USB Bus |
| **AI Inference Engine** | Ultralytics YOLOv8 (PyTorch / TensorRT) | 1 | Host GPU / Jetson Orin Nano | Deep Learning Inference |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Object Class | Detection Confidence (YOLO) | 3D Depth Estimate (m) | IK Trajectory Plan Time (ms) | Grasp & Sort Result |
| :--- | :--- | :--- | :--- | :--- |
| Target 1: Red Soda Can | 0.94 | 0.62 m | 42 ms | Success (Sorted to Recycling) |
| Target 2: Blue Screwdriver | 0.89 | 0.58 m | 55 ms | Success (Sorted to Tool Tray) |
| Target 3: Green Apple | 0.92 | 0.64 m | 38 ms | Success (Sorted to Food Bin) |
| Target 4: Shiny Metallic Cylinder | 0.78 | 0.60 m (Depth noise) | 82 ms | Success after 1 retry |

---

## 5. Troubleshooting & Root Cause Analysis

> Record at least one wiring, logic, or algorithmic challenge encountered during this lab and how you resolved it.

- **Symptom Observed**: [e.g., Target behavior failed, motor jittered, sensor returned NaN, communication timed out]
- **Diagnostic Step**: [e.g., Checked oscilloscope trace, printed debug telemetry, verified voltage levels with multimeter]
- **Root Cause**: [e.g., Timing latency in control loop, loose jumper wire, noisy ground plane, misconfigured baud rate]
- **Resolution**: [e.g., Added decoupling capacitor, modified PID derivative filter, corrected pin mapping in firmware]

---

## 6. Code & Firmware Implementation

```python
# Insert your primary control loop, state machine, or firmware snippet here:
def run_autonomous_loop():
    pass
```
- **Firmware Commit Hash**: `[Optional: git rev-parse --short HEAD]`

---

## 7. Engineering Reflection & Future Iterations

1. **What is the 'Sim2Real Domain Gap', and why do deep learning models trained exclusively in clean simulators often fail on real physical robots?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **How do Vision-Language-Action (VLA) foundation models represent a paradigm shift from traditional modular pipelines (YOLO -> Planner -> IK)?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **Reflecting across all 10 units: how did the simple analog transistor nightlight from Lab 1 foreshadow the autonomous closed-loop behavior of this AI capstone?**
   [Answer in 2-4 sentences based on your experimental observations.]

---

## 8. Self-Assessment Rubric Checklist

- [ ] **Objective & Hypothesis**: Clearly formulated with measurable success criteria.
- [ ] **System Architecture**: Complete schematic and pinout documented.
- [ ] **Empirical Data Recorded**: Real test measurements entered in Section 4 data table.
- [ ] **Root Cause Analysis**: At least one diagnostic failure and fix explained in Section 5.
- [ ] **Code Implementation**: Functional firmware snippet included in Section 6.
- [ ] **Reflection Questions Answered**: All 3 reflection prompts thoroughly analyzed.
- [ ] **Version Control**: Log committed to Git repository with a descriptive message.
