# 📓 Engineering Log: Lab 9 — Autonomous Warehouse Delivery Challenge (SLAM & Nav2)

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 9: Autonomous Navigation: SLAM & Path Planning  
**Target Platform**: [ROS 2 Nav2 Stack + 2D LiDAR + TurtleBot3 in Simulation/Physical]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Execute a complete autonomous mobile robotics delivery mission: map an unfamiliar warehouse facility using Cartographer/SLAM Toolbox, configure static and dynamic costmaps, and command waypoint missions via Nav2 with obstacle avoidance.

### Sense-Think-Act Hypothesis
- **SENSE**: 360° 2D LiDAR and wheel encoders provide point clouds and odometric velocity frames.
- **THINK**: Nav2 global planner computes Dijkstra/A* path, local controller (DWB/MPPI) generates collision-free velocity arcs around sudden obstacles.
- **ACT**: Robot drives autonomously between pick-and-place waypoints without collisions.
- **Hypothesis**: Configuring a dynamic inflation radius buffer of $0.25\,\text{m}$ around obstacles will allow the Nav2 local controller to navigate tight warehouse aisles without scraping walls while maintaining travel speeds $\ge 0.3\,\text{m/s}$.

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
| **Robotic Platform** | TurtleBot3 Burger / Custom Warehouse AMR | 1 | Differential Drive | Simulation / Physical |
| **Primary Sensor** | 360° 2D Laser Distance Sensor (LiDAR) | 1 | `/scan` Topic | 5.0V Power Bus |
| **SLAM Framework** | SLAM Toolbox (Lifelong / Async Mapping) | 1 | ROS 2 Package | Occupancy Grid Generation |
| **Navigation Stack** | ROS 2 Nav2 (Navigation 2) | 1 | ROS 2 Stack | Path Planning & Recovery Behaviors |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Delivery Waypoint | Nominal Distance (m) | Obstacle Condition | Path Re-plan Triggered? | Navigation Time (s) | Arrival Accuracy (cm) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Waypoint A (Loading Dock) | 8.5 m | Clear hallway | No | 18.2 s | 1.8 cm |
| Waypoint B (Storage Bay 3) | 14.2 m | Dynamic pedestrian blocked corridor | Yes (Local avoidance detour) | 34.5 s | 2.4 cm |
| Waypoint C (Packing Station) | 6.1 m | Narrow aisle with pallets | No (Smooth navigation) | 14.0 s | 1.5 cm |
| Waypoint D (Charging Dock) | 11.0 m | Unknown box placed in center | Yes (Costmap inflation updated) | 26.1 s | 0.9 cm (Dock aligned) |

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

1. **What is the 'Kidnapped Robot Problem' in mobile robotics, and how does the AMCL particle filter recover localization when a robot is picked up and moved?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **Explain the difference between a Global Costmap (static floor plan) and a Local Costmap (rolling sensor window) in Nav2.**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **What are Nav2 Recovery Behaviors, and how does clear-costmap / backup / spin prevent a robot from getting permanently stuck in a deadlock?**
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
