# This script will use stream function one hundred times
# Function will start the stream, take a photo and break after 3 seconds
# Useful for automatic photographing


# import the libraries
import numpy as np
import cv2
import time

def stream(i):
	
	while cap.isOpened():
		
		ret, frame1 = cap.read()           # we need 2 frames to compare the difference
		ret, frame2 = cap.read()

		diff = cv2.absdiff(frame1, frame2)
		gray = cv2.cvtColor (diff, cv2.COLOR_BGR2GRAY)                   # convert to grayscale
		blur = cv2.GaussianBlur(gray, (5,5), 0)                          # convert to blur  
		_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)                                 #determine the thresholds
		dilated = cv2.dilate(thresh, None, iterations=3)                                            # removing the noise
		contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)             #find contours

		for contour in contours:
			time.sleep(2)        
			array = []
			# set boundary for no_motion
			if cv2.contourArea(contour) < 100:
				no_motion= True
			else:
				no_motion=False
			array.append(no_motion)
			
			if (all(array)==True):
				cv2.imwrite('image%s.jpg' % i, frame1)              # capture a photo when no motion
				cap.release()

for x in range(100):
	cap = cv2.VideoCapture(0)
	#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')
	stream(x)
		
cv2.destroyAllWindows()
