import cv2

# Read images
img = cv2.imread(r'C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\image.jpg')
template = cv2.imread(r'C:\Users\jana lokesh\OneDrive\Desktop\ComputerVision\watch.jpg')

if img is None or template is None:
    print("Image not found")

else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    temp = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    best_score = -1
    best_location = None
    best_size = None

    # Check different template sizes
    for scale in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:

        new_w = int(temp.shape[1] * scale)
        new_h = int(temp.shape[0] * scale)

        if new_w >= gray.shape[1] or new_h >= gray.shape[0]:
            continue

        resized = cv2.resize(temp, (new_w, new_h))

        result = cv2.matchTemplate(
            gray, resized, cv2.TM_CCOEFF_NORMED
        )

        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > best_score:
            best_score = max_val
            best_location = max_loc
            best_size = (new_w, new_h)

    print("Matching score:", best_score)

    # Display best matching result
    if best_score > 0.5:
        x, y = best_location
        w, h = best_size

        cv2.rectangle(
            img, (x, y), (x+w, y+h), (0,255,0), 2
        )

        cv2.putText(
            img, "Watch Detected",
            (x, max(20, y-10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0,255,0), 2
        )

        print("Watch detected successfully!")
    else:
        print("Watch not detected. Try another template image.")

    cv2.imshow("Watch Recognition", img)
    cv2.imwrite("watch_output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
