# 📓 Engineering Log: Lab 3 — Ultrasonic Sonar Radar Scanner

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 3: The Senses: Sensors, Signals, & Perception  
**Target Platform**: [Raspberry Pi Pico + HC-SR04 + SG90 Servo / Wokwi Simulation]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Build an active scanning ultrasonic radar that sweeps a 180° field of view, measures distance via high-precision time-of-flight acoustic pulses, and filters out multipath noise using a rolling moving-average window.

### Sense-Think-Act Hypothesis
- **SENSE**: HC-SR04 transducer emits 40kHz ultrasound bursts and measures echo return time $\Delta t$.
- **THINK**: Microcontroller computes distance $d = \frac{v \cdot \Delta t}{2}$ where $v = 343\,\text{m/s}$ and applies a 5-sample median/moving-average noise filter.
- **ACT**: SG90 micro-servo positions the acoustic sensor between 0° and 180° in 5° increments.
- **Hypothesis**: The moving-average filter will suppress spurious echo dropouts (0cm or 400cm spikes) caused by angled surfaces, reducing measurement noise standard deviation by at least 60% compared to raw telemetry.

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
| **Microcontroller** | Raspberry Pi Pico (RP2040) | 1 | GPIO 16, 17, 18 | 5V USB / 3.3V Logic |
| **Ultrasonic Sensor** | HC-SR04 (40kHz Transceiver) | 1 | GP16 (Trig), GP17 (Echo) | 5.0V VCC / 3.3V Resistor Divider |
| **Micro Servo Motor** | SG90 9g 180° Servo | 1 | GP18 (PWM 50Hz) | 5.0V VBUS |
| **Voltage Divider** | 1kΩ and 2kΩ Resistors | 2 | Echo Pin Level Shifter | Steps 5.0V Echo down to 3.3V safe |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| Scanning Angle (°) | True Object Distance (cm) | Raw Echo Reading (cm) | Filtered Reading (cm) | Noise Error (%) |
| :--- | :--- | :--- | :--- | :--- |
| 30° | 25.0 cm | 25.2 cm | 25.0 cm | 0.0% |
| 60° | 40.0 cm | 48.5 cm (glance error) | 41.2 cm | 3.0% |
| 90° (Boresight) | 15.0 cm | 15.1 cm | 15.0 cm | 0.0% |
| 120° | 30.0 cm | 0.0 cm (missed ping) | 29.8 cm (rejected) | 0.6% |
| 150° | 50.0 cm | 51.4 cm | 50.3 cm | 0.6% |

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

1. **Why is a voltage divider or level shifter mandatory on the HC-SR04 Echo pin when connecting to a 3.3V microcontroller?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **What environmental factors change the speed of sound in air, and how would you calibrate for temperature variations?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **Compare ultrasonic distance sensing to optical LiDAR: under what conditions does sound outperform light?**
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
