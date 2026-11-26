import cv2

# Read the input image
img = cv2.imread('download.jpg')

if img is None:
    print("Image not found")
else:
    # Display original image
    original = img.copy()

    # Get image dimensions
    h, w = img.shape[:2]

    # Select Region of Interest (ROI)
    roi = img[50:150, 50:250]

    # Copy the selected region
    copied_roi = roi.copy()

    # Get ROI dimensions
    rh, rw = copied_roi.shape[:2]

    # Crop the image
    cropped = copied_roi.copy()

    # Select paste position (top-right corner)
    x = w - rw
    y = 0

    # Paste copied region
    img[y:y+rh, x:x+rw] = copied_roi

    # Display images
    cv2.imshow('Original Image', original)
    cv2.imshow('Cropped Image', cropped)
    cv2.imshow('Copied and Pasted Image', img)

    # Save output
    cv2.imwrite('cropped_image.jpg', cropped)
    cv2.imwrite('pasted_image.jpg', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
