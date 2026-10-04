# Daily Review Packet: Unit 0, Lab 0
**Date**: October 4, 2026  
**Branch**: `curriculum/unit-00-lab-00`  
**Status**: Ready for Human Review — Unit 0 Foundations Complete!  

---

## 📋 Executive Summary
The authoring agent has drafted the capstone lab completing **Unit 0: The Robotic Mindset & Anatomy of Systems**:
- **Lab File**: [`curriculum/unit-00-foundations/lab-00-systems-decomposition.md`](../curriculum/unit-00-foundations/lab-00-systems-decomposition.md)
- **Title**: *Reverse-Engineering Systems Decomposition*
- **Target Audience**: High School & College Students with Zero Prior Engineering or Coding Experience.

---

## 🎯 Pedagogical Architecture & Core Milestones
1. **Real-World Engineering Teardown**:
   - Compares the **NASA Mars Perseverance Rover** with an **Industrial Warehouse Autonomous Mobile Robot (AMR)**.
2. **Subsystems Breakdown**:
   - Details real engineering decisions: Rocker-bogie suspension (why springs are avoided on Mars), nuclear MMRTG vs. LiFePO4 batteries, LiDAR vs. Navcams, safety relays vs. autonomous watchdogs.
3. **Dual Flows (Energy vs. Information)**:
   - Maps high-power motor paths versus low-voltage sensor communication buses.
4. **Git-Backed Engineering Notebook**:
   - Walks students through creating and committing their first formal engineering log entry.

---

## 🔍 Ground-Truth Citations Audit (Zero Hallucinations)
| Footnote | Source Record | Institution / Standard | Verified URL |
| :--- | :--- | :--- | :--- |
| `[^1]` | Robotics Subsystems & Notebook Standards | NASA Robotics Alliance Project | [robotics.nasa.gov](https://robotics.nasa.gov/educational-resources/) |
| `[^2]` | Mars 2020 Architecture & 3D Explorer | NASA Jet Propulsion Laboratory | [photojournal.jpl.nasa.gov](https://photojournal.jpl.nasa.gov/) |
| `[^3]` | ANSI/RIA R15.06-2012 Safety Requirements | Association for Advancing Automation (A3) | [automate.org](https://www.automate.org/a3-content/ansi-ria-r15-06-2012-robot-safety-standard) |
| `[^4]` | AutoNav Planetary Rover Navigation | NASA JPL / IEEE Aerospace | [trs.jpl.nasa.gov/handle/2014/37656](https://trs.jpl.nasa.gov/handle/2014/37656) |

---

## 🖼️ Media & Open Licensing Manifest
All media referenced adheres to open licenses in `media/media_manifest.json`:
- `curiosity-rover-annotated.jpg` — Public Domain (NASA/JPL-Caltech)
- `estop-circuit.svg` — Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- `five-subsystems-flow.svg` — Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)

---

## 🏁 Unit 0 Completion Status
With Lab 0 complete, **Unit 0: The Robotic Mindset & Anatomy of Systems** is fully drafted and audited:
- ✅ [Module 0.1: What Makes a Robot a Robot?](../curriculum/unit-00-foundations/01-what-is-a-robot.md)
- ✅ [Module 0.2: The Five Subsystems of Any Robot](../curriculum/unit-00-foundations/02-the-five-subsystems.md)
- ✅ [Module 0.3: Engineering Notebooks, Safety, and Ethics](../curriculum/unit-00-foundations/03-safety-ethics-notebook.md)
- ✅ [Lab 0: Reverse-Engineering Systems Decomposition](../curriculum/unit-00-foundations/lab-00-systems-decomposition.md)
- ✅ Automated Verification Tool: [`agent/verifier/check_citations.py`](https://github.com/jscottvogel/Instructabot/blob/main/agent/verifier/check_citations.py)

---

## ✅ Human Review Checklist (For You)
When reviewing the drafted lab, please check:
- [ ] Is the comparison between space robotics and warehouse robotics engaging for students?
- [ ] Approve merge into `main` branch: `git merge curriculum/unit-00-lab-00`
