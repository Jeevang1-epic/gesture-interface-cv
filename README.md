# Real-Time Gesture Interface (Computer Vision)

A computer vision pipeline that translates human hand gestures into digital control signals in real-time. This project demonstrates **multimodal interaction** by mapping physical kinematics to software inputs with low latency.

## 🎯 Project Overview
Built as a study into **Human-Computer Interaction (HCI)**, this tool uses **MediaPipe** for hand landmark detection and **OpenCV** for frame processing. It calculates Euclidean distance between key skeletal points (Thumb tip & Index tip) to trigger discrete control events.

**Application:** Currently deployed as a controller for driving simulation (Hill Climb Racing), replacing keyboard latency with gesture inputs.

## 🛠️ Tech Stack
* **Python 3.10**
* **MediaPipe:** For robust hand-tracking and skeletal extraction.
* **OpenCV:** For image processing and visual feedback overlay.
* **PyDirectInput:** For DirectX-level keyboard simulation (0.0s latency).

## 🚀 How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the controller:
    ```bash
    python gesture_controller.py
    ```
3.  Active Control:
    * **Open Hand:** Gas (Right Arrow)
    * **Pinch (Thumb+Index):** Brake (Left Arrow)

## 🔮 Future Scope (Red Hen Lab Interests)
* Recording gesture datasets for automated analysis.
* Integrating speech commands for multimodal control.
* Analyzing gesture velocity as a feature for "intensity" control.
