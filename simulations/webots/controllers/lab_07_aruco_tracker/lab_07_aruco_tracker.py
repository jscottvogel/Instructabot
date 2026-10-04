"""
Instructabot Webots Controller: Pan-Tilt ArUco Marker Tracker
Computer Vision: OpenCV 4.7+ cv2.aruco.ArucoDetector
"""

import sys
import numpy as np
import cv2

# Windows console encoding safety
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

class MockCamera:
    def __init__(self): pass
    def enable(self, ts): pass
    def getImage(self): return None
    def getWidth(self): return 640
    def getHeight(self): return 480

class MockMotor:
    def __init__(self, name): self.name = name; self.pos = 0.0
    def setPosition(self, p): self.pos = p

def main():
    print("👁️ Instructabot Visual ArUco Tracking Subsystem...")
    
    # Initialize modern OpenCV 4.7+ ArUco detector
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Generate synthetic synthetic test image with marker 42
    test_frame = np.ones((480, 640, 3), dtype=np.uint8) * 240
    marker_img = cv2.aruco.generateImageMarker(aruco_dict, 42, 120)
    marker_bgr = cv2.cvtColor(marker_img, cv2.COLOR_GRAY2BGR)
    
    # Place marker off-center at (x=380, y=180) to test tracking error
    test_frame[180:180+120, 380:380+120] = marker_bgr

    # Detect markers
    corners, ids, rejected = detector.detectMarkers(test_frame)

    if ids is not None and len(ids) > 0:
        flat_ids = ids.flatten()
        print(f"✅ Successfully detected ArUco Marker ID: {flat_ids[0]}")
        
        # Calculate marker centroid
        marker_corners = corners[0][0]
        centroid_x = np.mean(marker_corners[:, 0])
        centroid_y = np.mean(marker_corners[:, 1])
        
        frame_center_x = 640 / 2
        frame_center_y = 480 / 2
        
        error_x = centroid_x - frame_center_x
        error_y = centroid_y - frame_center_y
        
        print(f"   Centroid: ({centroid_x:.1f}, {centroid_y:.1f})")
        print(f"   Tracking Error: ΔX = {error_x:+.1f} px, ΔY = {error_y:+.1f} px")
        
        # Proportional pan-tilt angle correction
        kp = 0.0015
        pan_correction = -kp * error_x
        tilt_correction = kp * error_y
        print(f"   Servo Commands: Pan = {pan_correction:+.4f} rad, Tilt = {tilt_correction:+.4f} rad")
    else:
        print("⚠️ No marker detected in frame.")

if __name__ == "__main__":
    main()
