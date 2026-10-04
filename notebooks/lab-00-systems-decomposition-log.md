# 📓 Engineering Log: Lab 0 — Reverse-Engineering Systems Decomposition

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 0 Foundations: The Robotic Mindset & Anatomy of Systems  
**Target Platform**: [Physical Teardown / System Block Diagram / Case Study]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Deconstruct a real-world autonomous robot (e.g., robotic vacuum or automated warehouse AMR) into its five fundamental engineering subsystems and trace the complete Sense-Think-Act control loop.

### Sense-Think-Act Hypothesis
- **SENSE**: Contact bumper switches, optical cliff sensors, and infrared wall sensors measure physical proximity and obstacles.
- **THINK**: An embedded microcontroller analyzes sensor triggers against threshold logic and prioritizes safety interlocks (e.g. cliff detection overrides forward motion).
- **ACT**: Differential drive motors alter heading, main brush motor sweeps debris, and piezoelectric buzzer alerts the user.
- **Hypothesis**: When the robot encounters an obstacle or negative drop (cliff), the low-level safety loop will interrupt forward motion within 50ms and initiate a turn-away recovery sequence without human intervention.

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
| **Robotic System / Case Model** | Autonomous Vacuum or Warehouse AMR | 1 | Internal Bus | 14.4V Li-ion |
| **Sensory Network** | IR Cliff Sensors, Bumper Microswitches, Wheel Encoders | 6+ | GPIO / ADC | 3.3V / 5.0V Logic |
| **Actuation Subsystem** | Dual DC Gearmotors + Cleaning Brush Motors | 3 | H-Bridge Drivers | 14.4V Motor Rail |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Subsystem Pillar | Physical Component / Model | Measured Voltage / Signal | Functional Role in Autonomy | Fail-Safe Behavior |
| :--- | :--- | :--- | :--- | :--- |
| 1. Structure | Molded Chassis & Suspension Bumper | N/A (Mechanical) | Protects internals and absorbs kinetic impacts | Mechanical spring return |
| 2. Energy & Power | 4S 18650 Li-ion Pack (14.8V Nominal) | 14.8V - 16.4V | Supplies high current to drive motors and logic | BMS cuts power if V < 12.0V |
| 3. Actuators | Brushed DC Drive Motors with 50:1 Gearbox | 0V to 14.8V PWM | Differential steering and forward locomotion | H-Bridge dynamic braking |
| 4. Senses | Infrared Phototransistor Cliff Sensor Array | 0.4V (Reflecting) / 3.1V (Cliff) | Detects stairs and floor boundary drops | Emergency reverse & stop |
| 5. Computation | 32-bit ARM Cortex-M Microcontroller | 3.3V Logic Rail | Runs Sense-Think-Act navigation and obstacle avoidance | Watchdog reset if loop hangs |

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

1. **Why is software unable to guarantee safety if a physical mechanical interlock (like an E-Stop) is missing?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **How does the Sense-Think-Act loop change between a teleoperated RC vehicle and this autonomous robot?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **What potential single point of failure (SPOF) exists in this robot's power distribution system?**
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
