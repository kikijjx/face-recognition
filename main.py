import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('pic.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) > 0:
    print(f"Found {len(faces)} faces:")
    for i, (x, y, w, h) in enumerate(faces):
        print(f"Face {i + 1}: x={x}, y={y}, w={w}, h={h}")
else:
    print("No faces found.")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imwrite('outpic.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
