import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("download.jpg", 0)

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Apply histogram equalization
    equalized = cv2.equalizeHist(img)
#Histogram equalization improves the contrast of many grayscale images, making some details easier to observe.
    
    # Display original and equalized images
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap='gray')
    plt.title("Equalized Image")
    plt.axis("off")

    plt.show()
