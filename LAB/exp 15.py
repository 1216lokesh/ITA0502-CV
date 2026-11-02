
import cv2
import numpy as np

# Read the image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner points for better visibility
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    result = img.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]
#Read an image and detect important corner points using
    #the Harris Corner Detection method in OpenCV.
    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Harris Corner Detection", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
