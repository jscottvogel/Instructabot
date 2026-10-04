# 🚀 Getting Started with Instructabot

> **Welcome to Robotics!**  
> If you have never written a single line of code, never held a soldering iron, and never taken physics—**you are in the right place.**

---

## 🌟 The First-Day Guarantee
You will make a virtual electronic circuit work in your web browser **within 5 minutes of opening this page**, with **zero software to install**.

### ⚡ Live In-Browser Nightlight Simulator
Try it right now below—drag the slider to shine a flashlight on the sensor and watch the circuit react autonomously:

<div style="background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 18px; max-width: 580px; margin: 16px 0; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 10px; margin-bottom: 12px;">
    <div>
      <strong style="font-size: 15px; color: #f8fafc;">⚡ Autonomous Transistor Nightlight</strong>
      <div style="font-size: 12px; color: #94a3b8;">Sense &rarr; Think &rarr; Act Circuit Loop</div>
    </div>
    <span id="nl-badge" style="padding: 4px 10px; border-radius: 9999px; font-size: 12px; font-weight: bold; background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3);">
      🌙 Dark: LED ON
    </span>
  </div>

  <!-- SVG Circuit Diagram -->
  <div style="background: #020617; border-radius: 8px; padding: 12px; border: 1px solid #1e293b; text-align: center;">
    <svg viewBox="0 0 460 200" style="width: 100%; max-height: 190px;">
      <!-- Power Rails -->
      <line x1="30" y1="20" x2="430" y2="20" stroke="#ef4444" stroke-width="2.5"/>
      <text x="35" y="15" fill="#ef4444" font-size="11" font-weight="bold">+9V Rail</text>
      <line x1="30" y1="180" x2="430" y2="180" stroke="#3b82f6" stroke-width="2.5"/>
      <text x="35" y="195" fill="#60a5fa" font-size="11" font-weight="bold">Ground (0V)</text>

      <!-- Battery -->
      <rect x="35" y="65" width="22" height="42" rx="3" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
      <text x="46" y="89" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">9V</text>
      <line x1="46" y1="65" x2="46" y2="20" stroke="#ef4444" stroke-width="2"/>
      <line x1="46" y1="107" x2="46" y2="180" stroke="#3b82f6" stroke-width="2"/>

      <!-- LDR Photoresistor -->
      <circle cx="150" cy="55" r="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
      <path d="M142 55 L146 51 L150 59 L154 51 L158 55" fill="none" stroke="#f59e0b" stroke-width="2"/>
      <text x="150" y="28" fill="#fbbf24" font-size="10" text-anchor="middle" font-weight="bold">LDR Sensor</text>
      <line x1="150" y1="39" x2="150" y2="20" stroke="#ef4444" stroke-width="2"/>
      <line x1="150" y1="71" x2="150" y2="100" stroke="#cbd5e1" stroke-width="2"/>

      <!-- 10k Resistor -->
      <rect x="142" y="125" width="16" height="26" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="150" y="142" fill="#f8fafc" font-size="9" text-anchor="middle">10kΩ</text>
      <line x1="150" y1="100" x2="150" y2="125" stroke="#cbd5e1" stroke-width="2"/>
      <line x1="150" y1="151" x2="150" y2="180" stroke="#3b82f6" stroke-width="2"/>

      <!-- Junction to Base -->
      <circle cx="150" cy="100" r="4" fill="#fbbf24"/>
      <line x1="150" y1="100" x2="250" y2="100" stroke="#fbbf24" stroke-width="2"/>
      <text id="nl-vb-text" x="195" y="93" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">V_b = 0.72V</text>

      <!-- 2N2222 Transistor -->
      <line x1="250" y1="85" x2="250" y2="115" stroke="#f8fafc" stroke-width="3"/>
      <line x1="250" y1="92" x2="265" y2="78" stroke="#f8fafc" stroke-width="2"/>
      <line x1="265" y1="78" x2="265" y2="50" stroke="#f8fafc" stroke-width="2"/>
      <line x1="265" y1="50" x2="360" y2="50" stroke="#f8fafc" stroke-width="2"/>
      
      <line x1="250" y1="108" x2="265" y2="122" stroke="#f8fafc" stroke-width="2"/>
      <polygon points="262,118 266,122 267,117" fill="#f8fafc"/>
      <line x1="265" y1="122" x2="265" y2="180" stroke="#3b82f6" stroke-width="2"/>
      <text x="250" y="138" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle">2N2222 NPN</text>

      <!-- 330 Ohm Resistor -->
      <rect x="352" y="45" width="16" height="24" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="360" y="61" fill="#f8fafc" font-size="9" text-anchor="middle">330Ω</text>
      <line x1="360" y1="20" x2="360" y2="45" stroke="#ef4444" stroke-width="2"/>
      <line x1="360" y1="69" x2="360" y2="90" stroke="#f8fafc" stroke-width="2"/>

      <!-- LED Symbol & Radiant Glow -->
      <circle id="nl-glow" cx="360" cy="100" r="32" fill="#facc15" opacity="0.45"/>
      <polygon id="nl-led" points="348,90 372,90 360,110" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
      <line x1="348" y1="110" x2="372" y2="110" stroke="#eab308" stroke-width="2"/>
      <text x="360" y="128" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">LED</text>
      <line x1="360" y1="110" x2="360" y2="140" stroke="#f8fafc" stroke-width="2"/>
      <line x1="360" y1="140" x2="265" y2="140" stroke="#f8fafc" stroke-width="2"/>
      <line x1="265" y1="140" x2="265" y2="78" stroke="#f8fafc" stroke-width="2"/>
    </svg>
  </div>

  <!-- Multimeter Readouts -->
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin: 12px 0; text-align: center; background: #020617; padding: 10px; border-radius: 8px; border: 1px solid #1e293b;">
    <div>
      <div style="font-size: 10px; color: #94a3b8; text-transform: uppercase;">Ambient Light</div>
      <div id="nl-lux-val" style="font-size: 13px; font-weight: bold; color: #f59e0b;">20 Lux (Dark)</div>
    </div>
    <div>
      <div style="font-size: 10px; color: #94a3b8; text-transform: uppercase;">Base Voltage</div>
      <div id="nl-vb-val" style="font-size: 13px; font-weight: bold; color: #34d399;">0.72V (&ge;0.7V)</div>
    </div>
    <div>
      <div style="font-size: 10px; color: #94a3b8; text-transform: uppercase;">Transistor State</div>
      <div id="nl-state-val" style="font-size: 13px; font-weight: bold; color: #34d399;">CLOSED (ON)</div>
    </div>
  </div>

  <!-- Flashlight Slider Control -->
  <div style="margin: 12px 0;">
    <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
      <span>🌙 Midnight Darkness</span>
      <span style="color: #94a3b8;">&larr; Drag to shine flashlight &rarr;</span>
      <span>☀️ Direct Sunlight</span>
    </div>
    <input id="nl-slider" type="range" min="0" max="100" value="15" style="width: 100%; accent-color: #f59e0b; cursor: pointer;">
  </div>

  <!-- Pedagogical Explanation -->
  <div id="nl-explanation" style="font-size: 12px; line-height: 1.5; color: #cbd5e1; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25); padding: 10px; border-radius: 8px;">
    <strong>🌙 How Autonomy Works Here:</strong> In the dark, the photoresistor's resistance rises, raising the transistor Base voltage above <strong>0.7V</strong>. The transistor switch snaps shut, allowing power to flood into the nightlight LED!
  </div>
</div>

<script>
(function() {
  var slider = document.getElementById('nl-slider');
  var badge = document.getElementById('nl-badge');
  var luxVal = document.getElementById('nl-lux-val');
  var vbVal = document.getElementById('nl-vb-val');
  var stateVal = document.getElementById('nl-state-val');
  var vbText = document.getElementById('nl-vb-text');
  var glow = document.getElementById('nl-glow');
  var led = document.getElementById('nl-led');
  var exp = document.getElementById('nl-explanation');

  function update(val) {
    var isDark = val < 45;
    var lux = Math.round(Math.pow(val / 10, 2) * 15 + 5);
    var vb = (0.76 - (val / 100) * 0.58).toFixed(2);
    if (vb > 0.75) vb = "0.75";
    if (vb < 0.20) vb = "0.20";

    luxVal.textContent = lux + " Lux (" + (isDark ? "Darkness" : "Bright") + ")";
    vbVal.textContent = vb + "V (" + (isDark ? "≥0.7V" : "<0.7V") + ")";
    vbText.textContent = "V_b = " + vb + "V";

    if (isDark) {
      badge.textContent = "🌙 Dark: LED ON";
      badge.style.background = "rgba(16, 185, 129, 0.2)";
      badge.style.color = "#34d399";
      stateVal.textContent = "CLOSED (ON)";
      stateVal.style.color = "#34d399";
      vbVal.style.color = "#34d399";
      vbText.setAttribute('fill', '#4ade80');
      glow.setAttribute('opacity', '0.5');
      led.setAttribute('fill', '#facc15');
      exp.style.background = "rgba(16, 185, 129, 0.1)";
      exp.style.borderColor = "rgba(16, 185, 129, 0.25)";
      exp.innerHTML = "<strong>🌙 How Autonomy Works Here:</strong> In the dark, the sensor resistance rises, raising Base voltage above <strong>0.7V</strong>. The transistor switch snaps shut, illuminating your LED nightlight!";
    } else {
      badge.textContent = "☀️ Light: LED OFF";
      badge.style.background = "rgba(245, 158, 11, 0.2)";
      badge.style.color = "#fbbf24";
      stateVal.textContent = "OPEN (OFF)";
      stateVal.style.color = "#f59e0b";
      vbVal.style.color = "#f59e0b";
      vbText.setAttribute('fill', '#94a3b8');
      glow.setAttribute('opacity', '0');
      led.setAttribute('fill', '#475569');
      exp.style.background = "rgba(245, 158, 11, 0.1)";
      exp.style.borderColor = "rgba(245, 158, 11, 0.25)";
      exp.innerHTML = "<strong>☀️ Closed-Loop Feedback:</strong> The flashlight floods the sensor, dropping resistance and pulling Base voltage down to <strong>" + vb + "V</strong> (below 0.7V). The transistor snaps open, shutting off the LED!";
    }
  }

  if (slider) {
    slider.addEventListener('input', function(e) {
      update(Number(e.target.value));
    });
    update(15);
  }
})();
</script>

### 🛠️ Next: Build the Full Physical Circuit in Simulation
Once you've explored the live simulation above, you can build the complete breadboard circuit with your own hands:
- **Zero-Code Breadboard Lab**: Follow the full step-by-step assembly guide in [Lab 1: The Zero-Code Light-Sensitive Nightlight](curriculum/unit-01-electronics/lab-01-zero-code-nightlight.md).
- **Interactive Simulator Options**:
  1. **Autodesk Tinkercad**: Build on a virtual breadboard using [Autodesk Tinkercad Circuits](https://www.tinkercad.com/circuits) (free, browser-based, recommended for analog circuits).
  2. **Wokwi**: In Unit 2, we introduce microcontrollers using Wokwi with pre-configured project files in [`simulations/wokwi/`](https://github.com/jscottvogel/Instructabot/tree/main/simulations/wokwi).

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
