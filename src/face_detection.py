import numpy as np
import cv2
import time



cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')
face_cascade = cv2.CascadeClassifier('/home/marija/OpenCV/haar_cascades.xml')

def stream(i):
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 10)
        #cv2.imshow("frame", frame)
        if len(faces) > 0:
            cv2.imwrite('image%s.jpg' % i, frame)  
            time.sleep(3)
            break
		
for x in range(3):
    stream(x)

cap.release()
cv2.destroyAllWindows()