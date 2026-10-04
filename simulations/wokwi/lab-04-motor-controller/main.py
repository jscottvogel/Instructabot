"""
Instructabot Lab 04: H-Bridge Motor Driving with Soft-Start S-Curve Acceleration
Firmware: MicroPython / Desktop simulation
"""

import sys
import time
import math

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

class MotorController:
    def __init__(self):
        self.current_duty = 0.0 # 0.0 to 1.0 (0% to 100%)
        self.direction = "STOP"

    def set_hardware(self, in1, in2, pwm_val):
        pass # In physical hardware: IN1.value(in1), IN2.value(in2), PWM.duty_u16(int(pwm_val * 65535))

    def ramp_speed(self, target_duty, duration_sec=1.5, steps=30):
        start_duty = self.current_duty
        step_dt = duration_sec / steps
        print(f"🔄 Ramping speed: {start_duty*100:.0f}% -> {target_duty*100:.0f}% over {duration_sec}s")
        
        for step in range(1, steps + 1):
            t = step / steps # 0.0 to 1.0
            # S-curve smoothstep formula: 3*t^2 - 2*t^3
            s_curve_factor = 3 * (t ** 2) - 2 * (t ** 3)
            current_pwm = start_duty + s_curve_factor * (target_duty - start_duty)
            self.current_duty = current_pwm
            
            bar = "▓" * int(current_pwm * 25)
            print(f"   [t={step*step_dt:4.2f}s] PWM: {current_pwm*100:5.1f}% | {bar:<25}| Direction: {self.direction}")
            time.sleep(0.02)

    def drive_forward(self, target_speed=1.0):
        self.direction = "FORWARD"
        self.ramp_speed(target_speed)

    def brake_to_stop(self):
        self.direction = "BRAKING"
        self.ramp_speed(0.0, duration_sec=0.8)
        self.direction = "STOPPED"

def main():
    print("⚙️ Instructabot H-Bridge Motor Controller Initialized...")
    motor = MotorController()
    
    print("\n1. Accelerating Forward Smoothly (Prevents gear stripping & high inrush current):")
    motor.drive_forward(target_speed=0.85)
    
    print("\n2. Cruising at steady speed:")
    time.sleep(0.5)
    
    print("\n3. Soft Deceleration to Stop:")
    motor.brake_to_stop()
    print("✅ Motor sequence safely concluded.")

if __name__ == "__main__":
    main()
