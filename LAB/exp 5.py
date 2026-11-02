import cv2
import matplotlib.pyplot as plt

# Read the color image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Define colors and channel names
    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    # Calculate and display histogram for each color
    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=names[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.show()
