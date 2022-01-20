import cv2
import time

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')

while(True):
    ret, frame = cap.read()
    for i in range(100):
        time.sleep(3)
        cv2.imwrite('image%s.jpg' % i, frame)
        time.sleep(3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
		
cap.release()
cv2.destroyAllWindows()
