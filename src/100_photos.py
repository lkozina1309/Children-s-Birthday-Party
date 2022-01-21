# This script will use stream function one hundred times
# Function will start the stream, take a photo after 2 seconds and break after 3 seconds
# Useful for automatic photographing

# import the libraries
import cv2
import time

# Define type of stream
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')

def stream(i):
    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        time.sleep(2)
        cv2.imwrite('image%s.jpg' % i, frame)  
        time.sleep(3)
        break
        
# change the parameter if you want more photos 
for x in range(100):
    stream(x)

cap.release()
cv2.destroyAllWindows()
