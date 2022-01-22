import numpy as np
import cv2
import time

def stream(i):

	while cap.isOpened():
		
		ret, frame1 = cap.read()
		ret, frame2 = cap.read()

		diff = cv2.absdiff(frame1, frame2)
		gray = cv2.cvtColor (diff, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray, (5,5), 0)
		_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
		dilated = cv2.dilate(thresh, None, iterations=3)
		contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		for contour in contours:
			time.sleep(2)
			array = []
		
			if cv2.contourArea(contour) < 100:
				no_motion= True
			else:
				no_motion=False
			array.append(no_motion)
			print(all(array))
			if (all(array)==True):
				cv2.imwrite('image%s.jpg' % i, frame1)
				cap.release()

for x in range(3):
	cap = cv2.VideoCapture(0)
	#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')
	stream(x)
		
cv2.destroyAllWindows()
