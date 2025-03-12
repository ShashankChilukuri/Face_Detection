# Face Detection with MTCNN and OpenCV

This project performs real-time face detection using MTCNN (Multi-Task Cascaded Convolutional Networks) and OpenCV.

## Features
- Real-time face detection using your webcam
- Draws bounding boxes around detected faces
- Press 'x' to exit the webcam window

## Prerequisites
- Python 3.x
- OpenCV
- MTCNN

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/face-detection.git
cd face-detection
```

2. Install dependencies:
```bash
pip install opencv-python mtcnn
```

## Usage
Run the script with:
```bash
python face_detection.py
```

## Expected Output
- Webcam window opens with real-time face detection.
- Green rectangles appear around detected faces.

## Troubleshooting
- If the webcam does not open, try changing the camera index:
```python
video = cv2.VideoCapture(1, cv2.CAP_DSHOW)
```



