"""
Instructabot Webots Controller: Differential Drive Maze Solver
Algorithm: Closed-Loop Obstacle Avoidance & Wall Following
"""

try:
    from controller import Robot, DistanceSensor, Motor
except ImportError:
    # Standalone mock for testing
    class Robot:
        def __init__(self): pass
        def getBasicTimeStep(self): return 32
        def step(self, ts): return -1 # Exit test loop
        def getDevice(self, name): return MockDevice(name)
    class MockDevice:
        def __init__(self, name): self.name = name
        def enable(self, ts): pass
        def getValue(self): return 100.0
        def setPosition(self, p): pass
        def setVelocity(self, v): pass

def run_maze_solver():
    robot = Robot()
    time_step = int(robot.getBasicTimeStep())
    
    # Sensors
    ds_left = robot.getDevice("ds_left")
    ds_right = robot.getDevice("ds_right")
    ds_left.enable(time_step)
    ds_right.enable(time_step)
    
    # Motors
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    if hasattr(left_motor, "setPosition"):
        left_motor.setPosition(float('inf'))
        right_motor.setPosition(float('inf'))
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)

    max_speed = 6.28 # rad/s
    print("🤖 Instructabot Maze Navigation Controller initialized...")

    step_count = 0
    while robot.step(time_step) != -1 and step_count < 100:
        step_count += 1
        val_l = ds_left.getValue()
        val_r = ds_right.getValue()

        # Wall avoidance logic
        if val_l > 500: # Obstacle on left
            speed_l = max_speed * 0.5
            speed_r = -max_speed * 0.5
        elif val_r > 500: # Obstacle on right
            speed_l = -max_speed * 0.5
            speed_r = max_speed * 0.5
        else: # Clear forward path
            speed_l = max_speed * 0.8
            speed_r = max_speed * 0.8

        if hasattr(left_motor, "setVelocity"):
            left_motor.setVelocity(speed_l)
            right_motor.setVelocity(speed_r)

    print("🏁 Maze controller simulation step complete.")

if __name__ == "__main__":
    run_maze_solver()
