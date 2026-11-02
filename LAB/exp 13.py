
import cv2
import numpy as np

# Read the image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    rows, cols = img.shape[:2]

    # Select three points from the original image
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

    # Define their new positions
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Calculate affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(img, matrix, (cols, rows))
#Apply affine transformation to an image to change its position, scale, or shape using OpenCV.
    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformed Image", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
