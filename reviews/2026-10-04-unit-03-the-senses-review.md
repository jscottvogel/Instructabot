# Daily Review Packet: Unit 3 — The Senses (Sensors, Signals, & Perception)
**Date**: October 4, 2026  
**Branch**: `curriculum/unit-03-the-senses`  
**Status**: Ready for Human Review — Unit 3 Complete!  

---

## 📋 Executive Summary
The authoring agent has fully drafted, cited, and audited **Unit 3: The Senses: Sensors, Signals, & Perception**:
- **[Module 3.1: Analog vs. Digital Signals & The ADC](../curriculum/unit-03-the-senses/01-analog-vs-digital-signals.md)**: Physical continuous phenomena vs. digital bits, sampling frequency (Nyquist-Shannon), ADC bit depth ($2^N$), quantization noise, Raspberry Pi Pico 12-bit hardware ADC / MicroPython 16-bit `read_u16()` normalization, and PWM duty cycle emulation.
- **[Module 3.2: Distance & Proximity Sensing](../curriculum/unit-03-the-senses/02-distance-and-proximity.md)**: Time-of-Flight (ToF) echolocation physics ($d = \frac{v \cdot t}{2}$), HC-SR04 ultrasonic sensor trigger/echo timing, failure modes (specular reflections, acoustic absorption, blind zones), and safe $5\text{V} \to 3.3\text{V}$ voltage divider level shifting.
- **[Module 3.3: Motion & Orientation Sensing (IMUs & Gyroscopes)](../curriculum/unit-03-the-senses/03-motion-and-orientation-imus.md)**: Biological inner ear analogy, 3D coordinate frames (Roll, Pitch, Yaw), MEMS accelerometer gravity vector tilt formulas, MEMS gyroscope angular velocity integration drift, and the Complementary Filter ($98\%$ gyro $+ 2\%$ accel fusion) in Python.
- **[Module 3.4: Real-World Sensor Noise & Digital Signal Filtering](../curriculum/unit-03-the-senses/04-noise-and-signal-conditioning.md)**: Gaussian white noise vs. impulsive outlier spikes, Moving Average Filter sliding window implementation, Median Filter for complete spike rejection, and the fundamental trade-off between smoothness and phase lag.
- **[Lab 3: The Ultrasonic Sonar Radar Scanner](../curriculum/unit-03-the-senses/lab-03-sonar-radar-scanner.md)**: Hands-on virtual lab in Wokwi wiring an HC-SR04 sensor and an SG90 servo motor to a Raspberry Pi Pico, programming a $180^\circ$ sweep with real-time median noise filtering and rendering an ASCII polar radar map in the console.

---

## 🔍 Ground-Truth Citations Audit (Zero Hallucinations)
| Source ID | Title & Source Record | Institution / Standard | Verified URL |
| :--- | :--- | :--- | :--- |
| `oppenheim-signals-and-systems` | Signals and Systems (6.007) | MIT OpenCourseWare | [ocw.mit.edu 6.007](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/) |
| `sparkfun-ultrasonic-guide` | HC-SR04 Distance Sensing Basics | SparkFun Electronics | [learn.sparkfun.com](https://learn.sparkfun.com/tutorials/distance-sensing-basics) |
| `invensense-mpu6050` | MPU-6050 MotionTracking Specification | TDK InvenSense | [invensense.tdk.com](https://invensense.tdk.com/products/motion-tracking/6-axis/mpu-6050/) |
| `smith-dsp-guide` | Digital Signal Processing (Chapter 15) | California Technical Publishing | [dspguide.com](https://www.dspguide.com/ch15.htm) |
| `wokwi-simulator-docs` | Wokwi Embedded Systems Simulator Documentation | Wokwi | [docs.wokwi.com](https://docs.wokwi.com/) |

---

## 🖼️ Media & Open Licensing Manifest
All media referenced adheres to open licenses registered in `media/media_manifest.json`:
- `adc-sampling.svg` — CC BY-SA 4.0 (Instructabot Team)
- `ultrasonic-tof.svg` — CC BY-SA 4.0 (Instructabot Team)
- `imu-coordinates.svg` — CC BY-SA 4.0 (Instructabot Team)
- `sensor-noise-filtering.svg` — CC BY-SA 4.0 (Instructabot Team)
- `wokwi-radar.png` — CC BY 4.0 (Wokwi / Instructabot)

---

## 🏁 Curriculum Progress Map
- ✅ **Unit 0: The Robotic Mindset & Anatomy of Systems** (4/4 Completed)
- ✅ **Unit 1: The Spark: Electricity & Electronics from Scratch** (4/4 Completed)
- ✅ **Unit 2: The Brain: Computational Thinking & Microcontrollers** (4/4 Completed)
- ✅ **Unit 3: The Senses: Sensors, Signals, & Perception** (5/5 Completed)
- ⏳ **Unit 4: The Muscles: Motors, Actuation, & Power Electronics** (Next)
