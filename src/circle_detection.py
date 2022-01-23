# This script will use stream function one hundred times
# Function will start the stream, take a photo when circle is detected and break 
# Useful for automatic photographing


# import the libraries
import cv2 
import numpy as np
import time

def stream(i):
	while cap.isOpened():
		_, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                  # convert to grayscale
		blur = cv2.medianBlur(gray, 5)                                  # convert to blur
		circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=200, param2=60, minRadius=0, maxRadius=0)    # detect circles
		
		if circles is not None:
			cv2.imwrite('image%s.jpg' % i, frame)                   # take a photo if circle is detected
			cap.release()                                           # break to start another stream

for x in range(100):
	time.sleep(20)
	cap = cv2.VideoCapture(0) 
	#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')                
	stream(x)

cv2.destroyAllWindows()
