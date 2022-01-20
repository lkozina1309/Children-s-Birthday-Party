import cv2
import time

face = cv2.CascadeClassifier('/home/marija/OpenCV/haar_cascades.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 4)
    cv2.imshow('frame', frame)

    for i in faces:
        time.sleep(3)
        cv2.imwrite('image%s.jpg' % i, frame)
        time.sleep(3)
		
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
		
cap.release()
cv2.destroyAllWindows()