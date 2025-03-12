from mtcnn import MTCNN
import cv2

detect = MTCNN()

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    faces = detect.detect_faces(frame)

    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

video.release()
cv2.destroyAllWindows()
