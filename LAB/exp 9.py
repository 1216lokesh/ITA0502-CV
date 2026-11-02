import cv2

# Read the image
img = cv2.imread("download.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    # Resize to a bigger size
    bigger = cv2.resize(img, None, fx=2, fy=2)

    # Resize to a smaller size
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
