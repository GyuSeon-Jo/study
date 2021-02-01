import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

src = cv2.imread('img/sample0.jpg')
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 1)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]

cv2.imshow('res', src)
cv2.waitKey(0)