# Object Detection and Tracking using YOLO

## Overview
This project detects and tracks objects in a video using Python, the Ultralytics YOLO model, and OpenCV. It processes video frames, identifies objects, draws bounding boxes and labels, and uses the ByteTrack tracker to track objects across consecutive frames.

## Features
- Object detection using a pretrained YOLO11n model.
- Multi-object tracking using ByteTrack.
- Bounding boxes and object labels displayed on video frames.
- Video preview while processing.
- Saves the processed video as `tracked_output.mp4`.
- Displays progress in the terminal.
- Allows the user to stop processing early by pressing `Q` in the preview window.

## Technologies Used
- **Python** — main programming language.
- **Ultralytics YOLO** — object detection.
- **OpenCV** — video reading, displaying, and saving.
- **ByteTrack** — object tracking across video frames.

## Project Structure
```text
object-detection-tracking/
├── app.py
├── input.mp4
├── tracked_output.mp4
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/object-detection-tracking.git
cd object-detection-tracking
```

### 2. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Add a video
Place an MP4 video named `input.mp4` in the same folder as `app.py`.

### 4. Run the project
```bash
python app.py
```

The pretrained YOLO model may download automatically the first time the program runs.

## Output
The program displays the processed video with detection boxes and labels. It saves the annotated video to:

`tracked_output.mp4`

The program also prints the number of processed frames in the terminal.

## How It Works
1. Loads the pretrained YOLO model.
2. Opens the input video using OpenCV.
3. Reads the video frame by frame.
4. Detects objects and tracks them using ByteTrack.
5. Draws detection results on each frame.
6. Displays and saves the processed frames.
7. Releases the video resources when processing finishes.

## Limitations
- Detection performance depends on video quality, lighting, object size, and the pretrained model.
- Processing speed depends on the computer hardware and video resolution.
- Tracking IDs may change or become inconsistent when objects overlap or disappear from view.
- The project currently processes a local video file rather than a live camera feed.

## Future Improvements
- Add live webcam detection and tracking.
- Count unique objects passing through a selected area.
- Display FPS and detection statistics.
- Add a user interface for selecting video files.
- Export object counts and tracking data to CSV.

## Learning Outcomes
Through this project, I practised working with pretrained computer vision models, processing video frames, using object tracking, and saving annotated video output.

## Author
Created as part of my AI learning and project development journey.

## Acknowledgements
- [Ultralytics YOLO Documentation](https://docs.ultralytics.com/modes/track/)
- [OpenCV Documentation](https://docs.opencv.org/)
