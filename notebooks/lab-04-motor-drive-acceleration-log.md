# 📓 Engineering Log: Lab 4 — Precision Bi-Directional Motor Drive with Soft Acceleration

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 4: The Muscles: Motors, Actuation, & Power Electronics  
**Target Platform**: [Raspberry Pi Pico + L298N / TB6612FNG H-Bridge + Geared DC Motor]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Construct and tune a high-current H-bridge motor driving system with variable Pulse Width Modulation (PWM) and an S-curve acceleration profile that suppresses inrush current and eliminates gear lash.

### Sense-Think-Act Hypothesis
- **SENSE**: Optical or Hall-effect quadrature encoders track motor shaft position and angular velocity.
- **THINK**: MicroPython firmware modulates PWM duty cycle following an S-curve ramp algorithm ($a(t) = a_{\max} \sin^2$) rather than an instantaneous step jump.
- **ACT**: H-Bridge MOSFETs switch motor power rail, driving bidirectional rotation with smooth acceleration.
- **Hypothesis**: Implementing an S-curve soft acceleration profile over 800ms will prevent the motor power rail from dipping below 4.5V (preventing logic brownouts) and reduce peak stall current by >50% compared to bang-bang step full throttle.

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
| **Motor Driver** | TB6612FNG or L298N Dual H-Bridge | 1 | GP2-GP5 (IN1, IN2, PWM) | External 7.4V - 12V Battery |
| **DC Geared Motor** | TT Motor or Metal Gearmotor (6V-12V) | 1 | Driver Motor A Outputs | Direct from H-Bridge |
| **Flyback Diodes** | 1N4007 or Internal Driver Diodes | 4 | Inductive Kick Protection | Motor Terminals |
| **Decoupling Capacitors** | 100uF Electrolytic + 0.1uF Ceramic | 2 | Power Rail Buffers | Between VM and GND |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Throttle Profile Mode | Target RPM | Ramp Time (ms) | Peak Inrush Current (A) | Supply Rail Voltage Dip (V) |
| :--- | :--- | :--- | :--- | :--- |
| Instantaneous Step (0 -> 100%) | 200 RPM | 0 ms | 1.85 A (Stall surge) | Dips from 9.0V to 6.2V (Severe!) |
| Linear Ramp (0 -> 100%) | 200 RPM | 500 ms | 0.95 A | Dips to 8.2V |
| S-Curve Soft Acceleration | 200 RPM | 800 ms | 0.62 A (Smooth) | Dips to 8.7V (Minimal brownout risk) |
| Instantaneous Direction Reversal | -200 to +200 | 0 ms | 2.40 A (Destructive spike) | Dips to 4.8V (Microcontroller Brownout!) |
| Controlled Decel-Stop-Accel | -200 to +200 | 1200 ms | 0.65 A (Safe) | Dips to 8.6V (Clean) |

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

1. **What causes inductive 'kickback' (Back-EMF) when a motor suddenly shuts off, and how do flyback diodes protect switching transistors?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **What is 'shoot-through' in an H-bridge circuit, and how does dead-time generation in firmware prevent physical short circuits?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **Why is an external battery mandatory for motors rather than powering them directly from a microcontroller's 5V or 3.3V pin?**
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
