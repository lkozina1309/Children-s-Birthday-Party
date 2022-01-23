import cv2 
import numpy as np
import time

def stream(i):
	while cap.isOpened():
		_, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		blur = cv2.medianBlur(gray, 5)
		circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=200, param2=60, minRadius=0, maxRadius=0)
		if circles is not None:
			cv2.imwrite('image%s.jpg' % i, frame)
			cap.release()

for x in range(3):
	time.sleep(5)
	cap = cv2.VideoCapture(0)
	#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')
	stream(x)

cap.release()