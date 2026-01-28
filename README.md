# 🏎️ Gesture Interface for Hill Climb Racing (Computer Vision)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)

A real-time Computer Vision interface that replaces a physical keyboard with hand gestures to control the game *Hill Climb Racing*. This project utilizes **MediaPipe** for hand landmark detection and **OpenCV** for frame processing to map physical hand states to game inputs (Gas/Brake).

### 🎥 Demo: See it in Action

[![Watch the Demo Video](https://img.youtube.com/vi/FoCdLMe8Rw0/maxresdefault.jpg)](https://youtu.be/FoCdLMe8Rw0)
*(Click the image above to watch the full demo)*

---

## 🛠️ Tech Stack
* **Language:** Python
* **Vision Pipeline:** OpenCV (`cv2`), MediaPipe Hands
* **Input Simulation:** PyDirectInput / Keyboard
* **Math:** NumPy (for vector calculations)

## 🚀 Key Features
* **Real-time Hand Tracking:** Detects 21 hand landmarks with high precision.
* **Gesture Recognition Logic:**
    * **Open Palm / Fingers Up:** Triggers `GAS` (Accelerate).
    * **Closed Fist / Fingers Down:** Triggers `BRAKE` (Decelerate).
* **Low Latency:** Optimized frame processing for responsive gameplay control.

## ⚙️ How It Works
1.  **Capture:** The webcam feed is processed frame-by-frame using OpenCV.
2.  **Detection:** MediaPipe extracts hand landmarks (wrist, finger tips, joints).
3.  **Logic:** The algorithm calculates the distance between specific landmarks (e.g., Thumb tip vs. Index tip) to determine the hand state.
4.  **Actuation:** If the "Gas" state is detected, the script simulates a key press (e.g., Right Arrow) using `pydirectinput`.

## 📦 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Jeevang1-epic/gesture-interface-cv.git](https://github.com/Jeevang1-epic/gesture-interface-cv.git)
    cd gesture-interface-cv
    ```

2.  **Install Dependencies**
    ```bash
    pip install opencv-python mediapipe pydirectinput
    ```

3.  **Run the Controller**
    ```bash
    python main.py
    ```

4.  **Play:** Open *Hill Climb Racing* (or any racing game) and position your hand in front of the camera.

## 🔮 Future Improvements (Roadmap)
* [ ] Add **Steering Control** (Left/Right) using hand tilt angle.
* [ ] Implement **Adaptive Thresholding** to work better in low-light conditions.
* [ ] Create a calibration script to customize gesture sensitivity for different users.

---
*Built by [G1] - Open Source Contributor*
