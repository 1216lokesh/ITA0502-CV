import cv2
import numpy as np

# Read input image
img = cv2.imread('download.jpg')

if img is None:
    print("Image not found")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Black Hat operation
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', gray)
    cv2.imshow('Black Hat Image', blackhat)

    # Save output
    cv2.imwrite('blackhat_image.jpg', blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
