import cv2

# Read the image
img = cv2.imread("download.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny
edges = cv2.Canny(gray, 100, 200)

# Display original and outline images
cv2.imshow("Original Image", img)
cv2.imshow("Image Outline", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
