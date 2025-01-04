# Live Camera Edge Detection

This project uses Python and OpenCV to perform edge detection on a live camera feed. The program captures video from the default webcam, applies an edge detection algorithm, and displays both the original video and the processed edge-detected output in real-time.

## Features
- Captures video from the default webcam.
- Performs edge detection using OpenCV.
- Displays both the original feed and edge-detected output side by side.
- Allows the user to exit the program by pressing the `q` key.

## Requirements
- Python 3.6 or higher
- OpenCV library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/edge-detection.git
   
The left side is the live camera feed, while the right side shows the edges detected in real-time.

---

## Controls

- **Start Program**: Run the Python script to start capturing and processing the video feed.
- **Exit Program**: Press `q` to stop the program and close all windows.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the license terms.

---

## Troubleshooting

### Common Issues:
- **`cv2` not found**:
  Make sure OpenCV is installed via:
  ```bash
  pip install opencv-python
  ```
- **Webcam not accessible**:
  Check your webcam settings, and ensure it's not being used by another application.

---

Happy coding!