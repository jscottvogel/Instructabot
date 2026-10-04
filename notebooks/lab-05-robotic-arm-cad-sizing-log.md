# 📓 Engineering Log: Lab 5 — Designing & Sizing a 2-DOF Robotic Arm Link

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 5: The Bones: Mechanics, Kinematics, & CAD Modeling  
**Target Platform**: [Onshape / Fusion 360 CAD + Physics Sizing Calculations]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Design a 3D-printable 2-Degree-of-Freedom (2-DOF) robotic arm link in parametric CAD, calculate maximum gravitational and dynamic torque requirements under full payload, and select servo actuators with a Factor of Safety $\ge 2.0$.

### Sense-Think-Act Hypothesis
- **SENSE**: CAD mass properties tools calculate center of mass ($L_{\text{cm}}$), link volume, and total assembly weight.
- **THINK**: Static equilibrium equations $\tau_{\text{joint}} = (m_{\text{link}} \cdot g \cdot L_{\text{cm}}) + (m_{\text{payload}} \cdot g \cdot L_{\text{total}})$ determine required torque.
- **ACT**: Export 3D printable STL mesh with optimized structural ribs and verify servo mounting tolerances.
- **Hypothesis**: A truss/ribbed structural link design will reduce link mass by 35% compared to a solid rectangular beam while maintaining deflection $< 1.0\,\text{mm}$ under a 200g end-effector payload.

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
| **Structural Material** | PLA or PETG 3D Printing Filament | ~120g | FDM 3D Printer (0.2mm layer) | Mechanical Structure |
| **Base Joint Actuator** | MG996R Metal Gear High-Torque Servo | 1 | 10 kg-cm rated torque | 5V - 6V Dedicated Rail |
| **Elbow Joint Actuator** | SG90 or MG90S Micro Metal Servo | 1 | 2.2 kg-cm rated torque | 5V Logic Rail |
| **Hardware Fasteners** | M3 Hex Machine Screws & Brass Heat-Set Inserts | 8 | Structural Joint Rigidity | Mechanical |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Design Iteration | Link Mass (g) | Payload Mass (g) | Total Torque Required (kg-cm) | Selected Servo Rating | Factor of Safety (FOS) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Iter 1: Solid Rectangular Beam | 185 g | 200 g | 7.8 kg-cm | MG996R (10 kg-cm) | 1.28 (Too Low!) |
| Iter 2: Lightweight I-Beam Profile | 115 g | 200 g | 5.4 kg-cm | MG996R (10 kg-cm) | 1.85 (Marginal) |
| Iter 3: Ribbed Truss with Heat-Sets | 88 g | 200 g | 4.6 kg-cm | MG996R (10 kg-cm) | 2.17 (Target Met: FOS >= 2.0) |

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

1. **Why is the Factor of Safety (FOS) in educational robotics typically specified between 2.0 and 3.0 rather than exactly 1.0?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **What is the difference between static holding torque and dynamic acceleration torque when an arm swings rapidly?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **How does 3D printing print orientation (layer line direction) affect the mechanical tensile strength of a robotic arm link?**
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
