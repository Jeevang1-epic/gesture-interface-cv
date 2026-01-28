import cv2
import mediapipe as mp
import math
import pydirectinput

# --- CONFIGURATION SETTINGS ---
CAM_WIDTH = 640
CAM_HEIGHT = 480
CONFIDENCE_THRESHOLD = 0.7
ACTION_THRESHOLD = 50  # Distance between fingers to trigger action

# Optimization for PyDirectInput
pydirectinput.PAUSE = 0.0
pydirectinput.FAILSAFE = True

def main():
    """
    Main loop for Hand Gesture Controller.
    Captures video, detects hand landmarks, and simulates keyboard inputs.
    """
    
    # 1. Initialize MediaPipe Hand Tracking
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # 2. Initialize Webcam with Optimized Resolution
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

    print("---------------------------------------")
    print("    GESTURE CONTROLLER ACTIVE    ")
    print("   Press 'q' to quit application     ")
    print("---------------------------------------")

    # 3. Start Detection Loop
    # strict context manager ensures resources are freed
    try:
        with mp_hands.Hands(
            min_detection_confidence=CONFIDENCE_THRESHOLD,
            min_tracking_confidence=0.5,
            max_num_hands=1
        ) as hands:

            while cap.isOpened():
                success, frame = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    continue

                # Flip frame horizontally for natural user interaction (mirror effect)
                image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
                
                # Performance Optimization: Mark image as not writeable to pass by reference
                image.flags.writeable = False
                results = hands.process(image)
                
                # Re-enable drawing
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # 4. Gesture Logic
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        # Draw hand connections for visual feedback
                        mp_drawing.draw_landmarks(
                            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                        # Extract Key Landmarks (Thumb Tip & Index Tip)
                        thumb_tip = hand_landmarks.landmark[4]
                        index_tip = hand_landmarks.landmark[8]

                        # Convert normalized coordinates to pixel coordinates
                        h, w, _ = image.shape
                        x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
                        x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

                        # Calculate Euclidean Distance
                        distance = math.hypot(x2 - x1, y2 - y1)

                        # Control Logic: Threshold Check
                        if distance > ACTION_THRESHOLD:
                            # State: ACCELERATE
                            cv2.putText(image, "GAS (Accelerating)", (30, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            pydirectinput.keyDown('right')
                            pydirectinput.keyUp('left')  # Ensure opposite key is released
                        else:
                            # State: BRAKE
                            cv2.putText(image, "BRAKE (Stopping)", (30, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            pydirectinput.keyDown('left')
                            pydirectinput.keyUp('right') # Ensure opposite key is released

                # Display the feed
                cv2.imshow('Gesture Controller', image)
                
                # Keep window on top (Optional, good for single-screen users)
                cv2.setWindowProperty('Gesture Controller', cv2.WND_PROP_TOPMOST, 1)

                # Exit condition
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    finally:
        # Cleanup Resources
        cap.release()
        cv2.destroyAllWindows()
        print("System shutdown safely.")

if __name__ == "__main__":
    main()
