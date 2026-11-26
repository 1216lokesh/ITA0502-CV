import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread('download.jpg')

# Check whether image is loaded
if img is None:
    print("Image not found")
else:
    # Convert image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel operator in X direction
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel operator in Y direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Convert results to absolute values
    abs_x = cv2.convertScaleAbs(sobel_x)
    abs_y = cv2.convertScaleAbs(sobel_y)

    # Combine X and Y gradients
    sobel = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

    # Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Sobel X', abs_x)
    cv2.imshow('Sobel Y', abs_y)
    cv2.imshow('Sobel Edge Detection', sobel)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
