# 🚀 Getting Started with Instructabot

> **Welcome to Robotics!**  
> If you have never written a single line of code, never held a soldering iron, and never taken physics—**you are in the right place.**

---

## 🌟 The First-Day Guarantee
You will make a virtual electronic circuit work in your web browser **within 5 minutes of opening this page**, with **zero software to install**.

### ⚡ Step 1: Open Your First Circuit (Zero Installs)

> [!TIP] **Launch the Interactive Web Simulator**  
> We host a standalone interactive circuit simulator that runs directly in your browser with zero logins or software installations:  
> 🚀 **[Click Here to Launch the Live Interactive Nightlight Simulator](https://jscottvogel.github.io/Instructabot/simulator.html)**

#### How the Autonomous Sense-Think-Act Loop Operates:

```mermaid
flowchart LR
    Sensor["👁️ 1. SENSE<br/>Photoresistor (LDR)<br/>Measures Ambient Light"] --> Brain["🧠 2. THINK<br/>2N2222 Transistor<br/>Compares V_base to 0.7V"]
    Brain --> Actuator["💡 3. ACT<br/>Nightlight LED<br/>Emits Light in Darkness"]
```

| Environmental State | Sensor Resistance ($R_{\text{LDR}}$) | Transistor Base Voltage ($V_b$) | Transistor Switch State | Nightlight LED |
| :--- | :--- | :--- | :--- | :--- |
| **☀️ Bright Daylight / Flashlight ON** | Very Low ($\approx 500\,\Omega$) | Drops to **$< 0.7\,\text{V}$** | **OPEN** (Cutoff — No Current) | **OFF (Dark)** |
| **🌙 Midnight Darkness / Flashlight OFF** | Very High ($> 200\,\text{k}\Omega$) | Rises to **$\ge 0.7\,\text{V}$** | **CLOSED** (Saturation — Conducting) | **ON (Glowing!)** |

#### Step-by-Step Instructions:
1. **Launch the Simulation**:
   - Open the **[Live In-Browser Nightlight Simulator](https://jscottvogel.github.io/Instructabot/simulator.html)**.
   - Or open [Autodesk Tinkercad Circuits](https://www.tinkercad.com/circuits) for the hands-on virtual breadboard wiring lab.
2. **Interact with the Sensor**:
   - Drag the ambient light / flashlight slider back and forth.
   - **Shine light on the sensor** $\to$ Watch Base Voltage drop below $0.7\,\text{V}$ $\to$ The LED automatically turns **OFF**.
   - **Pull the light into darkness** $\to$ Watch Base Voltage exceed $0.7\,\text{V}$ $\to$ The LED instantly illuminates **ON**.
3. 🎉 **Congratulations! You just analyzed your first autonomous sensor-actuator robotic circuit!**

---

### 🛠️ Next: Build the Full Physical Circuit on a Breadboard
Ready to wire the components together yourself?
- Follow the full step-by-step breadboard assembly guide in [Lab 1: The Zero-Code Light-Sensitive Nightlight](curriculum/unit-01-electronics/lab-01-zero-code-nightlight.md).
- In Unit 2, we introduce programmable microcontrollers using Wokwi with pre-configured project files in [`simulations/wokwi/`](https://github.com/jscottvogel/Instructabot/tree/main/simulations/wokwi).

🎉 **Congratulations! You just analyzed your first autonomous sensor-actuator robotic circuit!**

---

## 🗺️ Choose Your Learning Track

Not everyone learns at the same pace or has the same goals. Choose the track that fits your schedule:

| Track | Who It's For | Weekly Commitment | Path Highlights |
| :--- | :--- | :--- | :--- |
| **🎒 High School / Explorer Track** | High school students, curious beginners, after-school robotics clubs. | 2–3 hours / week | Units 0 through 4 (Electronics, MicroPython, Sensors, Motors). Focus on hands-on Wokwi circuits and intuitive mechanical analogies. |
| **🎓 College / Engineering Track** | Undergraduate CS/ME/EE students, STEM majors, career transitioners. | 5–8 hours / week | Units 0 through 10 (Full Curriculum). Deep dive into C++/Python, kinematics, ROS 2 middleware, SLAM, and YOLO computer vision. |
| **🛠️ Weekend Maker Track** | Adults and hobbyists building practical physical projects. | 3–4 hours / week | Units 1, 2, 4, 6, 7. Focus on physical motor control, 3D printing/CAD, and OpenCV pan-tilt turrets. |

---

## 🖥️ Software Environment: Zero-Friction Progression

Instructabot is designed so you only install software **when you genuinely need it**:

```mermaid
flowchart TD
    Phase1["Stage 1: Units 0 – 4<br/>100% In-Browser (Zero Installs)<br/>Wokwi Browser Simulator + Online Python"] --> Phase2["Stage 2: Units 5 – 7<br/>Lightweight Free Desktop Tools<br/>Webots 3D Simulator + VS Code + Python 3.10"]
    Phase2 --> Phase3["Stage 3: Units 8 – 10<br/>Professional Robotics Tools<br/>ROS 2 Humble / Jazzy + Ubuntu Linux (or WSL2 on Windows)"]
```

1. **Units 0 – 4 (Foundations, Electronics, Brain, Senses, Motors)**:
   - Requires only a modern web browser (Chrome, Edge, Firefox, Safari).
   - All labs run in **Wokwi** and web Python. Works seamlessly on Chromebooks, MacBooks, and Windows laptops!
2. **Units 5 – 7 (Mechanics, Mobile Robotics, Computer Vision)**:
   - Install **[Webots Robot Simulator](https://cyberbotics.com)** (Free, open-source 3D physics simulator for Windows, Mac, and Linux).
   - Install **[Python 3.10+](https://www.python.org)** and **VS Code**.
3. **Units 8 – 10 (ROS 2, Autonomous SLAM, SOTA AI Foundation Models)**:
   - Run **ROS 2 Humble / Jazzy** natively on Ubuntu Linux, or inside **Windows Subsystem for Linux (WSL2)**, or using our pre-configured Docker container.

---

## 🛑 How to Get Unstuck: The "Three-Step Rule"

Whenever code throws an error or a circuit doesn't respond:
1. **Check the Common Pitfalls Section**: Every lesson includes a dedicated `[!WARNING]` troubleshooting guide addressing the most frequent beginner mistakes.
2. **Check the Plain-English Glossary**: If a technical term feels confusing, look it up in the [Robotics Glossary](glossary.md) for an everyday mechanical analogy.
3. **Consult the AI Editorial Board**: Run `python agent/reviewers/persona_tester.py` to evaluate your lab code against student friction metrics.
