"""
Instructabot Lab 03: Ultrasonic Radar Scanner with Running Median Noise Filter
Firmware: MicroPython for Raspberry Pi Pico / ESP32
"""

import sys
import time
import random

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

class UltrasonicScanner:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.buffer = []

    def read_raw_distance_simulated(self, angle):
        """Simulates raw distance readings with occasional electrical noise spikes."""
        # Simulated obstacle at 45 degrees, distance 28 cm
        if 35 <= angle <= 55:
            base_dist = 28.0 + random.uniform(-0.5, 0.5)
        else:
            base_dist = 120.0 + random.uniform(-2.0, 2.0)
            
        # 10% chance of random noise glitch spike
        if random.random() < 0.10:
            return 999.0 # Sensor timeout spike
        return base_dist

    def filter_reading(self, raw_val):
        self.buffer.append(raw_val)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)
        # Running median calculation
        sorted_window = sorted(self.buffer)
        median_val = sorted_window[len(sorted_window) // 2]
        return median_val

def main():
    print("📡 Instructabot Ultrasonic Sonar Radar Active...")
    scanner = UltrasonicScanner()
    
    print("\nStarting 180-Degree Radar Sweep:")
    print("Angle (deg) | Raw Distance (cm) | Filtered Distance (cm) | Radar Map")
    print("-" * 65)
    
    for angle in range(0, 181, 15):
        raw = scanner.read_raw_distance_simulated(angle)
        filtered = scanner.filter_reading(raw)
        
        # ASCII visualization
        bars = int(filtered // 5)
        display_bar = "█" * min(bars, 20)
        
        print(f"   {angle:3d}°     |    {raw:6.1f} cm   |     {filtered:6.1f} cm     | {display_bar}")
        time.sleep(0.05)

if __name__ == "__main__":
    main()
