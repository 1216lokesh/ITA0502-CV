
import cv2

# Read the image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Rotate image 270 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image - 270 Degrees Clockwise", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
