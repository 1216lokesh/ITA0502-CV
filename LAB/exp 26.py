
import cv2

# Input and output video paths
input_video = r"C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\video.mp4"
output_video = r"C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\reversed_video.mp4"

def reverse_video(input_video, output_video):

    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error: Video not found!")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []

    # Read video frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Create reversed video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(
        output_video, fourcc, fps, (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):
        out.write(frame)

    out.release()

    print("Video reversed successfully!")
    print("Saved as:", output_video)

# Call function
reverse_video(input_video, output_video)
