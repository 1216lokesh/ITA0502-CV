
import cv2

# Read input image
image_path = r"C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\face.jpg"

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")

else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Detect human faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display number of faces
    print("Number of faces detected:", len(faces))

    # Display output image
    cv2.imshow("Face Detection", img)

    # Save output image
    output_path = r"C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\download.jpg"

    cv2.imwrite(output_path, img)

    print("Face detection completed!")
    print("Output saved successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
