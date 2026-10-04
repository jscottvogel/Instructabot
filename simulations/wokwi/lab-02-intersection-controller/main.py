"""
Instructabot Lab 02: Smart Pedestrian Intersection Controller
Firmware: MicroPython for Raspberry Pi Pico / ESP32
Target Audience: Novices (Zero prior hardware coding)
"""

import sys
import time

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

try:
    from machine import Pin
except ImportError:
    # Desktop mock fallback
    class MockPin:
        OUT = 1
        IN = 0
        PULL_UP = 2
        def __init__(self, pin, mode=1, pull=-1):
            self.pin = pin
            self.val = 0
        def value(self, v=None):
            if v is not None:
                self.val = v
            return self.val
        def on(self): self.val = 1
        def off(self): self.val = 0
    Pin = MockPin
    import time

# Pin Definitions (Pico GPIOs)
LED_RED = Pin(15, Pin.OUT)
LED_YELLOW = Pin(14, Pin.OUT)
LED_GREEN = Pin(13, Pin.OUT)
LED_PED_WALK = Pin(12, Pin.OUT)
LED_PED_STOP = Pin(11, Pin.OUT)
BTN_PED_REQUEST = Pin(10, Pin.IN, Pin.PULL_UP)

STATE_CAR_GREEN = 0
STATE_CAR_YELLOW = 1
STATE_PED_WALK = 2
STATE_PED_CLEARING = 3

state = STATE_CAR_GREEN
pedestrian_requested = False

def set_signals(car_r, car_y, car_g, ped_walk, ped_stop):
    LED_RED.value(car_r)
    LED_YELLOW.value(car_y)
    LED_GREEN.value(car_g)
    LED_PED_WALK.value(ped_walk)
    LED_PED_STOP.value(ped_stop)

print("🚦 Instructabot Smart Intersection Controller Active...")

def run_controller():
    global state, pedestrian_requested
    set_signals(0, 0, 1, 0, 1) # Car Green, Ped Stop
    
    # Run test cycle
    for cycle in range(1, 4):
        print(f"\n--- Cycle {cycle}: Traffic Flowing Green ---")
        time.sleep(0.05)
        print("🚶 Pedestrian button pressed!")
        pedestrian_requested = True
        
        if pedestrian_requested:
            # Transition to yellow
            print("⚠️ Switching Car signals to Yellow...")
            set_signals(0, 1, 0, 0, 1)
            time.sleep(0.05)
            
            # Transition to Pedestrian Walk
            print("🚸 Car Red! Walk Signal ON for Pedestrians...")
            set_signals(1, 0, 0, 1, 0)
            time.sleep(0.05)
            
            # Pedestrian Clearing (Flashing Stop)
            print("⏳ Pedestrian Clearance: Flashing Don't Walk...")
            for _ in range(3):
                set_signals(1, 0, 0, 0, 1)
                time.sleep(0.02)
                set_signals(1, 0, 0, 0, 0)
                time.sleep(0.02)
                
            # Return to Green
            print("🟢 Traffic Flow Resumes.")
            set_signals(0, 0, 1, 0, 1)
            pedestrian_requested = False

if __name__ == "__main__":
    run_controller()
