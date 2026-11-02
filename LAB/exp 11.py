
import cv2

# Read the image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Rotate image by 180 degrees
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image - 180 Degrees", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
