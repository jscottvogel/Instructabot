# 📓 Engineering Log: Lab 2 — Autonomous Traffic Intersection Controller

**Author**: [Your Full Name]  
**Date**: [YYYY-MM-DD]  
**Collaborators**: [Solo / Partner Name]  
**Milestone**: Unit 2: The Brain: Computational Thinking & Microcontrollers  
**Target Platform**: [Raspberry Pi Pico (RP2040) / Wokwi MicroPython Simulation]  

---

## 1. Executive Objective & Sense-Think-Act Hypothesis

### Objective
Design and program a deterministic, non-blocking finite state machine (FSM) in MicroPython that manages traffic flow, services pedestrian crossing requests via button interrupts, and guarantees fail-safe timing.

### Sense-Think-Act Hypothesis
- **SENSE**: Digital momentary pushbuttons sense pedestrian crosswalk requests with software debouncing.
- **THINK**: MicroPython state machine evaluates state timers (`time.ticks_ms()`) and triggers transitions: GREEN -> YELLOW -> RED -> PED_WALK -> PED_FLASH.
- **ACT**: High-efficiency Red, Yellow, Green, and Walk LEDs indicate real-time intersection priority.
- **Hypothesis**: When the pedestrian button is pressed, the system will not instantly drop vehicular green (which causes collisions), but will gracefully schedule a state transition to Yellow after a mandatory minimum vehicular green window (>= 5000ms).

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
| **Microcontroller** | Raspberry Pi Pico (RP2040) | 1 | GPIO 10-15 | 5V USB / 3.3V Regulated |
| **Traffic LED Array** | Red, Yellow, Green 5mm LEDs | 3 | GP10 (R), GP11 (Y), GP12 (G) | 3.3V Logic via 330Ω |
| **Pedestrian Walk LED** | Blue or White 5mm LED | 1 | GP13 | 3.3V Logic via 330Ω |
| **Crosswalk Pushbutton** | Momentary Tactile Button | 1 | GP14 (Internal Pull-Up) | Active-Low Ground |

---

## 4. Empirical Data & Test Results

Record your actual bench or simulator readings below:

| FSM State Name | Vehicular Lights | Pedestrian Walk Light | State Duration / Timeout | Next State Trigger |
| :--- | :--- | :--- | :--- | :--- |
| STATE_VEHICLE_GREEN | Green ON (Red/Yellow OFF) | Walk OFF | Min 5000ms / Max 15000ms | Timer expired & Pedestrian requested |
| STATE_VEHICLE_YELLOW | Yellow ON (Green/Red OFF) | Walk OFF | 3000ms fixed | Timer expired |
| STATE_ALL_RED_CLEAR | Red ON (Yellow/Green OFF) | Walk OFF | 1500ms safety buffer | Timer expired |
| STATE_PED_WALK | Red ON | Walk ON steady | 5000ms fixed | Timer expired |
| STATE_PED_FLASH | Red ON | Walk FLASHING (2Hz) | 3000ms (6 toggles) | Timer expired -> Return to GREEN |

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

1. **Why is using `time.sleep()` disastrous in real-time robotics compared to non-blocking `time.ticks_ms()`?**
   [Answer in 2-4 sentences based on your experimental observations.]

2. **What causes physical switch contact 'bounce' and how did your software state machine filter it?**
   [Answer in 2-4 sentences based on your experimental observations.]

3. **How does an embedded watchdog timer protect this intersection controller from an infinite freeze?**
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
