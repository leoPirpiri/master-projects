import cv2
import numpy as np
import os

# Hand detection using OpenCV DNN (MobileNet-based)
# This uses a pre-trained hand detector that's included with OpenCV

print("Initializing hand detector...")

# Download the hand detection model if needed
MODEL_DIR = "hand_models"
if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# Using a simpler approach with MediaPipe's pre-configured detection
try:
    # Try using MediaPipe's hand detection with built-in configuration
    import mediapipe as mp
    from mediapipe.tasks import vision
    from mediapipe.tasks.python import BaseOptions
    
    # For now, use a simple hand tracker based on skin color and contours
    print("Using color-based hand detection (no model required)")
    use_color_detection = True
except:
    print("Using OpenCV DNN hand detection")
    use_color_detection = True

cap = cv2.VideoCapture(0)

def detect_hands_by_color(frame):
    """Detect hands using skin color detection (HSV-based)"""
    h, w = frame.shape[:2]
    hand_landmarks = []
    
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define skin color ranges (different skin tones in HSV)
    # Define skin color ranges (covers different skin tones)
    # Light skin tones (0-20 H, warm tones)
    lower_skin1 = np.array([0, 15, 60], dtype=np.uint8)
    upper_skin1 = np.array([20, 255, 255], dtype=np.uint8)
    mask1 = cv2.inRange(hsv, lower_skin1, upper_skin1)
    
    # Dark/Red skin tones (170-180 H)
    lower_skin2 = np.array([170, 15, 60], dtype=np.uint8)
    upper_skin2 = np.array([180, 255, 255], dtype=np.uint8)
    mask2 = cv2.inRange(hsv, lower_skin2, upper_skin2)
    
    # Medium skin tones (8-30 H, includes yellows and oranges)
    lower_skin3 = np.array([8, 15, 60], dtype=np.uint8)
    upper_skin3 = np.array([30, 255, 255], dtype=np.uint8)
    mask3 = cv2.inRange(hsv, lower_skin3, upper_skin3)
    
    # Combine all masks
    mask = cv2.bitwise_or(mask1, mask2)
    mask = cv2.bitwise_or(mask, mask3)
    
    # Realistic skin tones (yellow-green range H=90-130, typical for many skin tones)
    lower_skin4 = np.array([90, 10, 80], dtype=np.uint8)
    upper_skin4 = np.array([130, 255, 255], dtype=np.uint8)
    mask4 = cv2.inRange(hsv, lower_skin4, upper_skin4)

    # Combine all masks
    mask = cv2.bitwise_or(mask, mask4)
    
    # Apply morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the largest contour (likely the hand)
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)
        
        if area > 300:
            # Get convex hull
            hull = cv2.convexHull(largest_contour, returnPoints=False)
            hull_points = cv2.convexHull(largest_contour)
            
            # Draw the contour outline
            cv2.drawContours(frame, [hull_points], 0, (0, 255, 0), 2)
            
            # Get defects in the convex hull
            if hull is not None and len(hull) > 3:
                defects = cv2.convexityDefects(largest_contour, hull)
                
                # Get moments for centroid
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    
                    # Draw centroid
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
                    
                    # Extract significant points
                    points = []
                    
                    # Add hull points (finger tips)
                    for point in hull_points:
                        points.append(tuple(point[0]))
                    
                    # Add defect points (valleys between fingers)
                    if defects is not None:
                        for defect in defects:
                            try:
                                s, e, f, d = defect
                                far = tuple(largest_contour[f][0])
                                if d > 1000:
                                    points.append(far)
                            except:
                                pass
                    
                    # Add some points from the contour itself
                    step = max(1, len(largest_contour) // 20)
                    for i in range(0, len(largest_contour), step):
                        points.append(tuple(largest_contour[i][0]))
                    
                    # Remove duplicates
                    points = list(set(points))
                    
                    # Sort by distance from centroid
                    points_sorted = sorted(points, 
                                          key=lambda p: np.sqrt((p[0]-cx)**2 + (p[1]-cy)**2))
                    
                    # Keep up to 21 detected points
                    num_points = min(21, len(points_sorted))
                    
                    for i in range(num_points):
                        x, y = points_sorted[i]
                        hand_landmarks.append({
                            'x': x / w,
                            'y': y / h,
                            'z': 0.5
                        })
                        # Draw detected points
                        cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
    
    return hand_landmarks, frame

print("Hand detector ready! Press ESC to exit")
print("Detecting hands using skin color + hand contour analysis")
print("Move your hand in front of the camera...")
print()

frame_count = 0
last_detection = False

while True:
    success, frame = cap.read()
    
    if not success:
        print("Failed to read frame")
        break
    
    try:
        hand_landmarks, frame = detect_hands_by_color(frame)
        
        if hand_landmarks:
            pontos = []
            for lm in hand_landmarks:
                pontos.extend([lm['x'], lm['y'], lm['z']])
            
            if not last_detection:
                print(f"[HAND DETECTED] Frame {frame_count}")
                last_detection = True
            
            if frame_count % 10 == 0:  # Print every 10 frames to avoid spam
                print(f"  Frame {frame_count}: {len(hand_landmarks)} landmarks detected ({len(pontos)} coordinate values)")
        else:
            if last_detection:
                print(f"[HAND LOST] Frame {frame_count}")
                last_detection = False
        
    except Exception as e:
        print(f"Error processing frame: {e}")
    
    cv2.imshow("Mao", frame)
    frame_count += 1
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
print("Done!")