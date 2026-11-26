import cv2

# Read the original image
img = cv2.imread('download.jpg')

# Read the watermark image
watermark = cv2.imread('download.jpg')

# Check whether images are loaded
if img is None or watermark is None:
    print("Image not found")
else:
    # Resize watermark
    watermark = cv2.resize(watermark, (150, 80))

    # Get image dimensions
    h, w, _ = img.shape

    # Set watermark position (bottom right)
    x = w - 150
    y = h - 80

    # Insert watermark using weighted addition
    roi = img[y:y+80, x:x+150]

    result = cv2.addWeighted(roi, 0.6, watermark, 0.4, 0)

    # Place watermark into original image
    img[y:y+80, x:x+150] = result

    # Display original and watermarked images
    cv2.imshow('Watermarked Image', img)

    # Save output image
    cv2.imwrite('watermarked_image.jpg', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
