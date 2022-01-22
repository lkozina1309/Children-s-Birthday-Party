# This script will use stream function one hundred times
# Function will start the stream and takes a photo when face is detected 
# Useful for automatic photographing


# import the libraries
import numpy as np
import cv2
import time

# Define type of stream and load haarcascade classifier
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')
face_cascade = cv2.CascadeClassifier('haar_cascades.xml')

# Fuction for stream and capturing photos automatically when face is detected
def stream(i):
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                   # convert to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 10)

        if len(faces) > 0:
            cv2.imwrite('image%s.jpg' % i, frame)  
            time.sleep(3)
            break

# Calling a function (change the parameter if you want more photos) 		
for x in range(100):
    stream(x)

cap.release()
cv2.destroyAllWindows()
