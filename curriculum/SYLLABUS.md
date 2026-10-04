# Instructabot: Master Robotics Curriculum Syllabus
## *From Zero Knowledge to State-of-the-Art Autonomous Systems*

---

### Curriculum Overview & Mission
**Instructabot** is an open-access, rigorous robotics curriculum engineered for high school and undergraduate students who possess **zero prior experience** in computer programming, mechanical engineering, or electrical engineering. 

Rather than treating robotics as an isolated academic specialty, this curriculum treats robotics as an integrated discipline uniting the physical world with computational intelligence. Every unit is designed with a **low floor** (accessible, intuitive, simulation-first) and a **high ceiling** (culminating in modern industry-standard technologies like ROS 2, computer vision, SLAM, and AI-driven control).

---

### Core Pedagogical Principles

1. **Physical Intuition Before Mathematical Abstraction**
   - New concepts begin with physical analogs and visual simulations before introducing equations or formal theory.
2. **Simulation-First & Zero Financial Barrier**
   - Every lab can be completed in free, open-source, or browser-based simulators (Wokwi, Tinkercad, Webots, ROS 2 Docker environments) before requiring physical hardware.
3. **Strict Source Grounding & Verifiable Citations**
   - Every factual claim, scientific principle, and engineering standard is cited using reputable open sources (MIT OpenCourseWare, IEEE, NASA RAP, ROS 2 documentation, Creative Commons engineering texts).
4. **Scaffolded "Sense-Think-Act" Architecture**
   - The entire curriculum maps to the foundational robotics loop: how robots sense their environment, how they think and make decisions, and how they actuate physical mechanisms.

---

### Master Unit Map

| Unit | Title | Level | Hands-On Platform | Capstone Milestone |
| :--- | :--- | :--- | :--- | :--- |
| **Unit 0** | **The Robotic Mindset & Anatomy of Systems** | Beginner | Interactive Systems Viewer | Systems decomposition of real-world robots |
| **Unit 1** | **The Spark: Electricity & Electronics from Scratch** | Beginner | Tinkercad Circuits / PhET | Autonomously triggered sensor circuit |
| **Unit 2** | **The Brain: Computational Thinking & Microcontrollers** | Beginner | Wokwi (ESP32 / Pico) & Python | Multi-state smart traffic & crosswalk system |
| **Unit 3** | **The Senses: Sensors, Signals, & Perception** | Intermediate | Wokwi & Python | Ultrasonic radar scanner with noise filtering |
| **Unit 4** | **The Muscles: Motors, Actuation, & Power Electronics** | Intermediate | Wokwi (PWM & H-Bridges) | Bi-directional motor controller with soft start |
| **Unit 5** | **The Bones: Mechanics, Kinematics, & CAD Modeling** | Intermediate | Onshape CAD / Web Visualizer | 3D-modeled 2-DOF robotic arm with torque sizing |
| **Unit 6** | **Movement & Mobile Robotics: Driving the Physical World** | Advanced | Webots Robotics Simulator | Maze-navigating differential-drive mobile robot |
| **Unit 7** | **Vision: Giving Robots Sight with OpenCV** | Advanced | Python, OpenCV, Webots | Color-tracking & fiducial-marker targeting turret |
| **Unit 8** | **ROS 2: The Industry Standard Robot Operating System** | Professional | ROS 2 (Humble/Iron) & RViz | Distributed multi-node robotic control pipeline |
| **Unit 9** | **Autonomous Navigation: SLAM & Path Planning** | Professional | ROS 2 Nav2 & Webots / Gazebo | Autonomous warehouse mapping and waypoint navigation |
| **Unit 10** | **State of the Art: Modern AI, Foundation Models, & S2R** | SOTA | PyTorch, YOLO, Sim2Real | Visual object-sorting robot with deep learning |

---

## Detailed Unit Breakdown

---

### Unit 0: The Robotic Mindset & Anatomy of Systems
*Focus: Demystifying robotics, establishing systemic thinking, and safety.*

- **Module 0.1: What Makes a Robot a Robot?**
  - Defining the robot: Difference between automation, an appliance, a remote-controlled vehicle, and an autonomous robot.
  - The fundamental paradigm: **Sense $\rightarrow$ Think $\rightarrow$ Act**.
  - Historical context & modern landscape: Industrial arms, rovers (Mars Perseverance), warehouse logistics (Kiva/Amazon), surgical robotics (da Vinci), and humanoid systems.
- **Module 0.2: The Five Subsystems of Any Robot**
  - Structure (the skeleton), Actuators (the muscles), Power (the circulatory system), Sensors (the senses), and Controller (the brain).
  - How energy and information flow through a robotic system.
- **Module 0.3: Engineering Notebooks, Safety, and Ethics**
  - Keeping a version-controlled engineering log.
  - Physical safety: High currents, battery chemistries (LiPo vs. NiMH vs. USB), pinch points, and emergency stops (E-Stops).
  - Ethical considerations: Automation, labor impacts, and algorithmic accountability.
- **Lab 0: Reverse-Engineering Systems Decomposition**
  - *Objective*: Given teardown schematics and videos of a Mars rover and an autonomous vacuum, map every component to its corresponding subsystem and trace the Sense-Think-Act loop.

---

### Unit 1: The Spark: Electricity & Electronics from Scratch
*Focus: Electrical intuition without math anxiety; circuits, components, and safety.*

- **Module 1.1: Intuitive Electrical Physics**
  - The fluid analogy: Voltage (pressure), Current (flow rate), and Resistance (pipe constriction).
  - Ohm’s Law ($V = I \cdot R$) explained through interactive visual sliders.
  - Alternating Current (AC) vs. Direct Current (DC); why robots run on DC.
- **Module 1.2: Essential Circuit Components**
  - How breadboards work internally (tie points, power rails).
  - Resistors (color codes, limiting current), Light Emitting Diodes (polarity, forward voltage drop).
  - Switches and pushbuttons: Normally Open (NO), Normally Closed (NC), pull-up/pull-down resistors.
- **Module 1.3: Power Delivery & Battery Management**
  - Voltage drop, regulators (linear vs. buck/boost switching regulators).
  - Why robots fail when motors start: Current draw spikes, brownouts, and common ground discipline.
- **Lab 1: The Zero-Code Light-Sensitive Nightlight**
  - *Simulation*: Tinkercad Circuits.
  - *Objective*: Construct a functional circuit using a breadboard, photoresistor (LDR), NPN transistor, resistor, and LED that automatically turns on in darkness without writing a single line of software.

---

### Unit 2: The Brain: Computational Thinking & Microcontrollers
*Focus: Transitioning from zero coding to algorithmic control of hardware using Python/MicroPython.*

- **Module 2.1: Algorithmic Logic & Flowcharts**
  - Deconstructing tasks into discrete computational steps.
  - Flowcharts: Decisions (if/else), Loops (while/for), and State Machines.
- **Module 2.2: Python for Robotics Foundations**
  - Variables, numbers, booleans, lists, and functions.
  - The infinite control loop (`while True:`): The heartbeat of a robotic controller.
  - Timing and delays: Blocking delays (`time.sleep`) vs. Non-blocking state timers (mills / timestamp comparison).
- **Module 2.3: Microcontrollers vs. Single-Board Computers**
  - Comparison: Microcontroller Units (ESP32, Raspberry Pi Pico, Arduino) vs. Single-Board Computers (Raspberry Pi 4/5, Jetson).
  - Understanding General Purpose Input/Output (GPIO) pins.
  - Digital Input (reading 1s and 0s) and Digital Output (writing HIGH/LOW).
- **Lab 2: The Pedestrian-Responsive Intersection Controller**
  - *Simulation*: Wokwi Simulator with Raspberry Pi Pico (MicroPython).
  - *Objective*: Build a finite-state machine (FSM) controlling red/yellow/green traffic LEDs with an interactive pedestrian crosswalk button and non-blocking yellow flashing warning state.

---

### Unit 3: The Senses: Sensors, Signals, & Perception
*Focus: Converting physical phenomena into digital data; dealing with noise in real-world measurements.*

- **Module 3.1: Analog vs. Digital Signals**
  - How the continuous real world becomes discrete numbers.
  - Analog-to-Digital Converters (ADC): Resolution (bits), reference voltages, and quantization.
  - Pulse Width Modulation (PWM) as an analog-like output.
- **Module 3.2: Distance & Proximity Sensing**
  - Ultrasonic Time-of-Flight (HC-SR04): Physics of sound waves, speed of sound calculation, blind spots, and specular reflections.
  - Infrared (IR) distance sensors & Time-of-Flight (ToF) laser sensors (VL53L0X).
- **Module 3.3: Motion & Orientation Sensing (IMUs)**
  - Accelerometers (measuring gravity and linear acceleration).
  - Gyroscopes (measuring angular velocity / rotation).
  - The drift problem and introduction to complementary/sensor fusion filtering.
- **Module 3.4: Real-World Noise & Signal Conditioning**
  - Sensor jitter and false triggers.
  - Software filters: Moving average filters, median filters, and threshold debouncing.
- **Lab 3: Ultrasonic Sonar Radar Scanner**
  - *Simulation*: Wokwi with MicroPython + Web Serial Plotter.
  - *Objective*: Interface an ultrasonic sensor mounted to a sweeping servo motor; implement a moving-average filter to clean jitter and plot detected obstacles in a 180-degree field of view.

---

### Unit 4: The Muscles: Motors, Actuation, & Power Electronics
*Focus: How software commands translate into physical force, speed, and positioning.*

- **Module 4.1: Electric Motors Compared**
  - Direct Current (DC) Brushed Motors: Simple rotation, back-EMF, torque curves.
  - Servo Motors (RC Servos): Closed-loop internal potentiometer, PWM position command ($0^\circ$ to $180^\circ$).
  - Stepper Motors: Precise angular steps, holding torque, open-loop positioning.
  - Brushless DC (BLDC) Motors: High efficiency, ESC controllers (drones, modern mobile robots).
- **Module 4.2: Motor Driving & Power Isolation**
  - Why microcontrollers cannot power motors directly (current limits, inductive flyback spikes).
  - The H-Bridge circuit topology (forward, reverse, brake, coast).
  - Motor driver ICs (L298N, TB6612FNG, TMC2209 silent steppers).
  - Optical isolation, flyback diodes, and shared grounds.
- **Module 4.3: Speed & Direction Control**
  - Duty cycle and PWM frequency.
  - Soft-start algorithms to prevent current spikes and mechanical gear stripping.
- **Lab 4: Precision Bi-Directional Motor Drive with Soft Acceleration**
  - *Simulation*: Wokwi / Tinkercad.
  - *Objective*: Write code to control a motor via an H-Bridge using PWM; implement an S-curve or linear acceleration ramp to move forward, reverse, and dynamically brake safely.

---

### Unit 5: The Bones: Mechanics, Kinematics, & CAD Modeling
*Focus: Mechanical integrity, gear trains, 3D design, and spatial geometry.*

- **Module 5.1: Structural Fundamentals & Materials**
  - Centers of gravity, tip-over thresholds, and structural rigidity.
  - Materials comparison: 3D printed PLA/PETG, acrylic, aluminum extrusion (2020), fasteners (M3/M4 hardware).
- **Module 5.2: Mechanical Power Transmission**
  - Gears: Spur gears, planetary gears, worm gears.
  - Gear ratios: Trade-off between speed ($\omega$) and torque ($\tau$) ($\text{Ratio} = \frac{N_{\text{driven}}}{N_{\text{driving}}}$).
  - Pulleys, belts, lead screws, and rack-and-pinion mechanisms.
- **Module 5.3: Spatial Geometry & Coordinate Frames**
  - 3D Cartesian coordinates ($X, Y, Z$).
  - Rotation: Roll, Pitch, Yaw.
  - Degrees of Freedom (DOF) of robotic manipulators.
- **Module 5.4: Computer-Aided Design (CAD) for Robotics**
  - Parametric 3D modeling using cloud-native CAD (Onshape / Tinkercad 3D).
  - Designing for 3D printing (tolerances, overhangs, print orientation).
- **Lab 5: Designing and Sizing a 2-DOF Robotic Arm Link**
  - *Tool*: Onshape (Free Educational License) & mechanical calculation sheet.
  - *Objective*: Model a 2-link robotic arm with servo mount brackets; calculate the stall torque required at the shoulder joint based on arm weight and payload.

---

### Unit 6: Movement & Mobile Robotics: Driving the Physical World
*Focus: Wheeled kinematics, odometry, closed-loop feedback, and physics simulation.*

- **Module 6.1: Mobile Robot Drive Architectures**
  - Differential Drive: Turning via wheel speed differential; Instantaneous Center of Curvature (ICC).
  - Ackermann Steering (car-like), Mecanum / Holonomic omni-wheels.
- **Module 6.2: Odometry & Encoders**
  - Quadrature optical and magnetic encoders: Counting ticks and measuring phase difference.
  - Calculating dead-reckoning position $(x, y, \theta)$ from wheel revolutions.
  - Wheel slip, drift, and accumulated positional error.
- **Module 6.3: Closed-Loop Control (The PID Controller)**
  - Why open-loop control fails in the real world.
  - Proportional (P), Integral (I), and Derivative (D) control explained visually without calculus.
  - Tuning a PID controller to drive straight and maintain target velocity.
- **Module 6.4: Open-Source Physics Simulators (Webots)**
  - Introduction to Webots / Gazebo.
  - Simulating gravity, mass, collision friction, and sensor rays.
- **Lab 6: Autonomous Maze-Navigating Mobile Robot in Webots**
  - *Simulation*: Webots open-source robotics simulator.
  - *Objective*: Program a two-wheeled differential robot (e-puck or custom robot) in Python to navigate an unknown maze using wall-following and bumper/distance sensor reactive obstacle avoidance.

---

### Unit 7: Vision: Giving Robots Sight with OpenCV
*Focus: Computer vision fundamentals, camera geometry, and real-time visual tracking.*

- **Module 7.1: Digital Images as Numeric Matrices**
  - Pixels, channels, and image coordinates (why $(0,0)$ is top-left).
  - Color spaces: RGB vs. Grayscale vs. HSV (Hue, Saturation, Value) for robust lighting invariance.
- **Module 7.2: OpenCV Foundations in Python**
  - Loading camera feeds, frame rate constraints.
  - Blurring (Gaussian blur), edge detection (Canny), thresholding, and contour extraction.
- **Module 7.3: Object Tracking & Fiducial Markers**
  - Color mask segmentation: Isolating and tracking a colored object.
  - Centroid calculation and pixel error offsets.
  - ArUco / AprilTags: Precision visual fiducials for 3D position estimation and docking.
- **Module 7.4: 3D Depth Sensing Technologies**
  - Stereo vision (parallax), Structured Light, and LiDAR (Time of Flight).
  - Point clouds and depth maps.
- **Lab 7: Real-Time Visual Pan-Tilt Tracking Turret**
  - *Platform*: Python + OpenCV + Webots camera simulation.
  - *Objective*: Write a vision loop that detects a bright tennis ball in a simulated camera frame, computes horizontal and vertical error offsets from frame center, and drives pan-tilt motors to continuously center the target.

---

### Unit 8: ROS 2: The Industry Standard Robot Operating System
*Focus: Transitioning to professional robotics middleware, distributed computing, and pub/sub architecture.*

- **Module 8.1: Why Middleware? The Monolith Problem**
  - Limitations of single-script robot code.
  - How ROS 2 solves modularity, multi-process architecture, and multi-language support.
- **Module 8.2: The Core ROS 2 Computational Graph**
  - **Nodes**: Single-responsibility software processes.
  - **Topics & Messages**: Asynchronous publisher/subscriber data pipelines.
  - **Services**: Synchronous request/response communications.
  - **Actions**: Long-running goal-oriented tasks with feedback and preemption.
  - **Parameters**: Dynamic runtime configuration.
- **Module 8.3: Introspection & Visualization Tools**
  - Command line tools: `ros2 node list`, `ros2 topic echo`, `ros2 topic hz`.
  - RViz2: Visualizing sensor streams, coordinate transforms, and laser scans.
  - Rqt graph: Visualizing the live computational topology.
- **Module 8.4: Spatial Relationships with TF2 (Transform Library)**
  - Coordinate frames: `base_link`, `odom`, `map`, `camera_link`.
  - Why math breaks without frame trees: Transforming camera pixel vectors into robot gripper coordinates.
- **Lab 8: Building a Modular ROS 2 Robot Control Package**
  - *Platform*: ROS 2 (Humble/Iron) in Docker / local install.
  - *Objective*: Create a ROS 2 package containing an Odometry Publisher node, an Obstacle Detector node, and a Teleoperation/Supervisor node communicating over custom and standard `geometry_msgs` topics.

---

### Unit 9: Autonomous Navigation: SLAM & Path Planning
*Focus: State estimation, mapping unknown environments, and global/local path execution.*

- **Module 9.1: The Fundamental Problem of SLAM**
  - Simultaneous Localization and Mapping (the chicken-and-egg problem).
  - Occupancy Grid Maps: Cells as free, occupied, or unknown space ($P(\text{occupied})$).
- **Module 9.2: 2D LiDAR SLAM Algorithms**
  - Scan matching: Aligning consecutive laser range scans.
  - Particle filters (Monte Carlo Localization / AMCL).
  - Graph-based SLAM and loop closure (recognizing previously visited places).
- **Module 9.3: Path Planning & Obstacle Avoidance**
  - Global Planners: Grid search ($A^*$, Dijkstra), Rapidly-exploring Random Trees (RRT).
  - Costmaps: Inflation layers, lethal obstacles, footprint padding.
  - Local Planners: Dynamic Window Approach (DWA), Timed Elastic Band (TEB) for velocity obstacle avoidance.
- **Module 9.4: The ROS 2 Navigation Stack (Nav2)**
  - Nav2 architecture: Behavior trees, navigator, recoveries, and controllers.
- **Lab 9: Autonomous Warehouse Delivery Challenge**
  - *Platform*: ROS 2 Nav2 in Webots / Gazebo simulation.
  - *Objective*: Teleoperate a simulated mobile robot equipped with 2D LiDAR to create a high-resolution map of a simulated warehouse; configure Nav2 to autonomously navigate between designated loading docks while dynamically steering around moving obstacles.

---

### Unit 10: State of the Art: Modern AI, Foundation Models, & Sim2Real
*Focus: Deep learning, neural perception, reinforcement learning, and the future of robotics.*

- **Module 10.1: Classical Control vs. Machine Learning in Robotics**
  - Where classical control shines (kinematics, deterministic safety, PID).
  - Where deep learning is essential (unstructured perception, generalizable manipulation, semantic scene reasoning).
- **Module 10.2: Deep Learning Object Detection (YOLO) for Robots**
  - Real-time bounding box detection, class labels, and confidence thresholds.
  - Deploying neural nets on edge robotics hardware (NVIDIA Jetson, Coral TPU, ONNX runtime).
- **Module 10.3: Simulation-to-Real (Sim2Real) Transfer & Domain Randomization**
  - The reality gap: Why robots trained in simulation fail on real hardware.
  - Techniques: Domain randomization (varying friction, lighting, mass), system identification.
- **Module 10.4: Vision-Language-Action (VLA) & Foundation Models in Robotics**
  - Overview of state-of-the-art robotic models: Google RT-1/RT-2, Open X-Embodiment, diffusion policies for robotic manipulation.
  - How multimodal LLMs translate natural language instructions ("Pick up the red apple") into spatial robotic waypoints.
- **Lab 10 / Capstone: Semantic Object Fetching & Sorting Pipeline**
  - *Platform*: Python, YOLO / Pretrained Vision Model, ROS 2, Webots.
  - *Objective*: Integrate visual object classification with mobile manipulation: a simulated robot receives a semantic target ("Find the soda can"), plans a path across the room, detects the item using a neural vision detector, aligns its gripper, and completes the retrieval.

---

### Assessment, Verification, & Citation Standard

Every lesson authored within this curriculum follows strict criteria:
1. **Verifiable Footnote Standard**:
   - Every physical constant, formula, and technical specification contains an active reference link or citation from established repositories (IEEE, MIT OCW, NASA RAP, ROS 2 Documentation, etc.).
2. **Standardized Lesson Format**:
   - `01. Objectives & Prerequisites` (Written in plain English).
   - `02. Physical Intuition & The Big Picture` (Metaphors, visual diagrams, no jargon).
   - `03. Technical Core & Schematics` (Formulas explained step-by-step with interactive calculations).
   - `04. Hands-On Simulation Lab` (Reproducible, zero-cost code and breadboard/3D models).
   - `05. Common Troubleshooting Pitfalls` (Why it doesn't work, debugging checklist).
   - `06. Sources & Provenance` (Complete list of citations, licenses, and verified links).
