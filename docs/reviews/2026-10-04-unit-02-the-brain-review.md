# Daily Review Packet: Unit 2 — The Brain (Computational Thinking & Microcontrollers)
**Date**: October 4, 2026  
**Branch**: `curriculum/unit-02-the-brain`  
**Status**: Ready for Human Review — Unit 2 Complete!  

---

## 📋 Executive Summary
The authoring agent has fully drafted, cited, and audited **Unit 2: The Brain: Computational Thinking & Microcontrollers**:
- **[Module 2.1: Algorithmic Logic, Flowcharts, & State Machines](../curriculum/unit-02-the-brain/01-algorithmic-logic-and-flowcharts.md)**: Literalism of computers ("peanut butter sandwich" thought experiment), standard ANSI flowchart symbols, Finite State Machine (FSM) theory, Roomba case study, and eliminating deadlock/race conditions.
- **[Module 2.2: Python for Robotics Foundations](../curriculum/unit-02-the-brain/02-python-for-robotics.md)**: Python variables, lists for sensor streams, conditionals (`if/elif/else`), the infinite control loop heartbeat (`while True:`), why `time.sleep()` causes robot collisions, and non-blocking millisecond timing (`time.ticks_ms()`).
- **[Module 2.3: Microcontrollers vs. Single-Board Computers & GPIO](../curriculum/unit-02-the-brain/03-microcontrollers-vs-sbcs.md)**: Biological reflex arc vs. cortex analogy, bare-metal MCU (RP2040 Pico) vs. Linux SBC (Raspberry Pi 5), 3.3V logic boundaries, MicroPython `machine.Pin`, active-LOW logic with software internal pull-ups (`Pin.PULL_UP`), and switch debouncing.
- **[Lab 2: The Pedestrian-Responsive Intersection Controller](../curriculum/unit-02-the-brain/lab-02-intersection-controller.md)**: Complete hands-on simulation in Wokwi wiring a Raspberry Pi Pico to 4 LEDs and a pushbutton, programming a non-blocking multi-state traffic and crosswalk FSM in MicroPython.

---

## 🔍 Ground-Truth Citations Audit (Zero Hallucinations)
| Source ID | Title & Source Record | Institution / Standard | Verified URL |
| :--- | :--- | :--- | :--- |
| `micropython-docs` | MicroPython Language Reference & machine.Pin | George Robotics Ltd. | [docs.micropython.org](https://docs.micropython.org/en/latest/) |
| `raspberry-pi-pico-guide` | Raspberry Pi Pico Python SDK (RP2040) | Raspberry Pi Ltd. | [datasheets.raspberrypi.com](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) |
| `sipser-theory-of-computation` | Introduction to Theory of Computation (Finite Automata) | MIT OpenCourseWare (18.404J) | [ocw.mit.edu 18.404J](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) |
| `wokwi-simulator-docs` | Wokwi Embedded Systems Simulator Documentation | Wokwi | [docs.wokwi.com](https://docs.wokwi.com/) |
| `mit-ocw-601sc` | Introduction to EECS I (State Machines & Control Loops) | MIT OpenCourseWare | [ocw.mit.edu 6.01SC](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/) |

---

## 🖼️ Media & Open Licensing Manifest
All media referenced adheres to open licenses registered in `media/media_manifest.json`:
- `fsm-traffic-light.svg` — CC BY-SA 4.0 (Instructabot Team)
- `mcu-vs-sbc.svg` — CC BY-SA 4.0 (Instructabot Team)
- `pico-pinout.svg` — CC BY-SA 4.0 (Raspberry Pi Ltd. / Instructabot)
- `wokwi-traffic-system.png` — CC BY 4.0 (Wokwi / Instructabot)
- `five-subsystems-flow.svg` — CC BY-SA 4.0 (Instructabot Team)

---

## 🏁 Curriculum Progress Map
- ✅ **Unit 0: The Robotic Mindset & Anatomy of Systems** (4/4 Completed)
- ✅ **Unit 1: The Spark: Electricity & Electronics from Scratch** (4/4 Completed)
- ✅ **Unit 2: The Brain: Computational Thinking & Microcontrollers** (4/4 Completed)
- ⏳ **Unit 3: The Senses: Sensors, Signals, & Perception** (Next)
