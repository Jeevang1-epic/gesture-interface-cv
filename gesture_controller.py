import cv2
import mediapipe as mp
import math
import pydirectinput

# OPTIMIZATION SETTINGS 

pydirectinput.PAUSE = 0.0
pydirectinput.FAILSAFE = True

# 2. i am going to Setup MediaPipe bellow
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 3. Open Webcam with Lower Resolution (Faster processing)
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Width
cap.set(4, 480) # Height

# Logic Tracking to prevent key spamming
current_action = "IDLE" 

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5, max_num_hands=1) as hands:
    
    print("---------------------------------------")
    print("TURBO MODE ACTIVE - NO LAG")
    print("---------------------------------------")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                thumb = hand_landmarks.landmark[4]
                index = hand_landmarks.landmark[8]
                
                h, w, c = image.shape
                x1, y1 = int(thumb.x * w), int(thumb.y * h)
                x2, y2 = int(index.x * w), int(index.y * h)
                
                dist = math.hypot(x2 - x1, y2 - y1)

                # OPTIMIZED CONTROLS 
                # We check if action CHANGED to avoid spamming the console
                if dist > 50: 
                    cv2.putText(image, "GAS", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    pydirectinput.keyDown('right')
                    pydirectinput.keyUp('left')
                else:
                    cv2.putText(image, "BRAKE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    pydirectinput.keyDown('left')
                    pydirectinput.keyUp('right')

        cv2.imshow('Controller', image)
        cv2.setWindowProperty('Controller', cv2.WND_PROP_TOPMOST, 1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
