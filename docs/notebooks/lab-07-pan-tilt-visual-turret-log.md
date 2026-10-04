# 📓 Engineering Log: Lab 7 — Real-Time Visual Pan-Tilt Tracking Turret

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 7: Vision: Giving Robots Sight with OpenCV  
**Target Platform**: [Webcam + OpenCV Python + 2-DOF Pan-Tilt Servo Gimbal]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Build a real-time computer vision pipeline that isolates target objects using color segmentation (HSV) or fiducial markers (ArUco), computes centroid pixel coordinates, and drives a 2-DOF pan-tilt gimbal to center the target in the video frame.

### Sense-Think-Act Hypothesis
- **SENSE**: Optical camera captures RGB video frames (640x480 resolution at 30 FPS).
- **THINK**: OpenCV converts frame to HSV color space, applies inRange thresholding, extracts largest contour centroid $(c_x, c_y)$, and calculates error $(e_x = c_x - 320, e_y = c_y - 240)$.
- **ACT**: Pan and tilt servos update angular positions proportionally to steer the camera toward optical center.
- **Hypothesis**: Operating in HSV color space rather than RGB will maintain target lock under varying ambient lighting conditions (200 Lux to 1200 Lux), preventing target loss caused by room shadows.

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
| **Optical Camera** | Standard USB Webcam or Raspberry Pi Camera | 1 | USB 2.0 / CSI Ribbon | 5.0V USB Bus |
| **Pan-Tilt Mechanism** | 2-DOF Mini Pan-Tilt Kit with 2x SG90 Servos | 1 | Pan (GP14), Tilt (GP15) | 5.0V 2A Power Rail |
| **Vision Processor** | Host Laptop / Raspberry Pi 4 / SBC | 1 | Python 3.10 + OpenCV (cv2) | Host Machine |
| **Calibration Target** | High-contrast Bright Colored Ball or ArUco Marker | 1 | Optical Target | Target Object |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Test Scenario | Ambient Lighting (Lux) | Processing Latency (ms) | Effective FPS | Centering Error (pixels) | Target Lock Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Bright Studio Light | 850 Lux | 18.2 ms | 30 FPS | 4 pixels | Locked (Stable) |
| Dim Incandescent Lamp | 120 Lux | 19.5 ms | 30 FPS | 8 pixels | Locked (Stable) |
| Sudden Shadow Cast | 350 -> 80 Lux | 21.0 ms | 28 FPS | 12 pixels | Brief jitter, regained lock |
| Rapid Target Motion (>1 m/s) | 500 Lux | 22.4 ms | 28 FPS | 25 pixels | Tracking without loss |

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

1. **Why is the HSV (Hue, Saturation, Value) color space far superior to standard RGB for computer vision color segmentation?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **What causes visual tracking hunting/oscillation when target error approaches zero, and how does a deadband zone solve it?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **What advantages do fiducial markers (like ArUco or AprilTags) offer over raw color thresholding for autonomous robotic docking?**
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
