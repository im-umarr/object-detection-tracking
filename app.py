
import cv2
from ultralytics import YOLO
from pathlib import Path

# 1. Video file ka naam
VIDEO_PATH = "input.mp4"

# 2. Output video ka naam
OUTPUT_PATH = "tracked_output.mp4"


def main():
    # Check whether the input video exists
    if not Path(VIDEO_PATH).exists():
        print(f"Error: {VIDEO_PATH} not found!")
        print("Place your video in the same folder as app.py.")
        return

    print("Loading YOLO model...")
    model = YOLO("yolo11n.pt")

    # Open the input video
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("Error: Could not open the video.")
        return

    # Read video information
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25.0

    # Prepare the output video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        OUTPUT_PATH, fourcc, fps, (width, height)
    )

    if not out.isOpened():
        print("Error: Could not create the output video.")
        cap.release()
        return

    frame_count = 0
    print("Detecting and tracking objects...")
    print("Press Q in the preview window to stop early.")

    try:
        while True:
            success, frame = cap.read()

            if not success:
                break

            # Detect objects and track them across frames
            results = model.track(
                frame,
                persist=True,
                tracker="bytetrack.yaml",
                conf=0.30,
                verbose=False
            )

            # Draw boxes, labels and tracking IDs
            annotated_frame = results[0].plot()

            # Save the processed frame
            out.write(annotated_frame)
            frame_count += 1

            # Display the processed frame
            cv2.imshow("Object Detection and Tracking", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("Processing stopped by user.")
                break

            if frame_count % 30 == 0:
                print(f"Processed {frame_count} frames...")

    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    print(f"Done! Processed {frame_count} frames.")
    print(f"Output saved as: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
