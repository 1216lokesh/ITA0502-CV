import cv2
import time
import os

# Get the folder containing this Python file
folder = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(folder, "video.mp4")

print("Video path:", video_path)
print("File exists:", os.path.exists(video_path))

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Cannot open video. Check the file location.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
