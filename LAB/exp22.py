import cv2
import numpy as np

# Read input image
img = cv2.imread('download.jpg')

if img is None:
    print("Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply closing
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    # Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Binary Image', binary)
    cv2.imshow('Closing Image', closing)

    # Save output
    cv2.imwrite('closing_image.jpg', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
