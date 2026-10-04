# Daily Review Packet: Unit 4 — The Muscles (Motors, Actuation, & Power Electronics)
**Date**: October 4, 2026  
**Branch**: `curriculum/unit-04-the-muscles`  
**Status**: Ready for Human Review — Unit 4 Complete!  

---

## 📋 Executive Summary
The authoring agent has fully drafted, cited, and audited **Unit 4: The Muscles: Motors, Actuation, & Power Electronics**:
- **[Module 4.1: Electric Motors Compared](../curriculum/unit-04-the-muscles/01-electric-motors-compared.md)**: Four motor families (Brushed DC, RC Servos, Steppers, Brushless DC / BLDC), Back-EMF physics ($V_{\text{bemf}} = K_e \cdot \omega$), the stall current trap ($I_{\text{stall}} \gg I_{\text{free}}$), mechanical power ($P = \tau \cdot \omega$), and motor sizing for mobile robots.
- **[Module 4.2: Motor Driving & Power Isolation (The H-Bridge)](../curriculum/unit-04-the-muscles/02-h-bridge-motor-driving.md)**: Why microcontrollers cannot drive motors directly, H-Bridge 4-transistor topology (Forward, Reverse, Active Brake, Coast), shoot-through dead short protection, flyback diode kickback clamping ($-L \frac{di}{dt}$), legacy L298N vs. modern MOSFET TB6612FNG, and MicroPython driver code.
- **[Module 4.3: Speed & Direction Control: Soft-Start Acceleration Ramping](../curriculum/unit-04-the-muscles/03-speed-direction-soft-start.md)**: The "lead foot" problem (inrush current spikes, wheel slip, gear stripping), linear acceleration rate limiting algorithm, Jerk ($j = \frac{da}{dt}$), S-curve acceleration profiling, and Python rate limiter implementation.
- **[Lab 4: Precision Bi-Directional Motor Drive with Soft Acceleration](../curriculum/unit-04-the-muscles/lab-04-motor-drive-acceleration.md)**: Hands-on virtual lab in Wokwi wiring a Raspberry Pi Pico to a TB6612FNG driver and DC motor, programming 20 kHz PWM speed control, rate-limited smooth forward/reverse transitions, and instant dynamic braking with live console telemetry.

---

## 🔍 Ground-Truth Citations Audit (Zero Hallucinations)
| Source ID | Title & Source Record | Institution / Standard | Verified URL |
| :--- | :--- | :--- | :--- |
| `chapman-electric-machinery` | Electric Machinery Fundamentals (5th Edition) | McGraw-Hill Education | [mheducation.com](https://www.mheducation.com/highered/product/electric-machinery-fundamentals-chapman/M9780073529547.html) |
| `toshiba-tb6612fng` | TB6612FNG Driver IC for Dual DC Motors | Toshiba Semiconductor | [toshiba.semicon-storage.com](https://toshiba.semicon-storage.com/info/TB6612FNG_datasheet_en_20141001.pdf) |
| `ti-motor-driver-primer` | Motor Driver Current Ratings & Thermal Dissipation (SLVA714) | Texas Instruments | [ti.com/lit/an/slva714/slva714.pdf](https://www.ti.com/lit/an/slva714/slva714.pdf) |
| `lynch-park-modern-robotics` | Modern Robotics (Actuation & Dynamics) | Cambridge University Press | [modernrobotics.northwestern.edu](https://modernrobotics.northwestern.edu/) |
| `wokwi-simulator-docs` | Wokwi Simulator Documentation (Motors & PWM) | Wokwi | [docs.wokwi.com](https://docs.wokwi.com/) |

---

## 🖼️ Media & Open Licensing Manifest
All media referenced adheres to open licenses registered in `media/media_manifest.json`:
- `motor-types.svg` — CC BY-SA 4.0 (Instructabot Team)
- `h-bridge-circuit.svg` — CC BY-SA 4.0 (Instructabot Team)
- `motor-soft-start.svg` — CC BY-SA 4.0 (Instructabot Team)
- `tb6612-wiring.png` — CC BY-SA 4.0 (SparkFun Electronics / Instructabot)
- `five-subsystems-flow.svg` — CC BY-SA 4.0 (Instructabot Team)

---

## 🏁 Curriculum Progress Map
- ✅ **Unit 0: The Robotic Mindset & Anatomy of Systems** (4/4 Completed)
- ✅ **Unit 1: The Spark: Electricity & Electronics from Scratch** (4/4 Completed)
- ✅ **Unit 2: The Brain: Computational Thinking & Microcontrollers** (4/4 Completed)
- ✅ **Unit 3: The Senses: Sensors, Signals, & Perception** (5/5 Completed)
- ✅ **Unit 4: The Muscles: Motors, Actuation, & Power Electronics** (4/4 Completed)
- ⏳ **Unit 5: The Bones: Mechanics, Kinematics, & CAD Modeling** (Next)
