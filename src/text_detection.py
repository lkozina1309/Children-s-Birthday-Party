import cv2 
from PIL import Image
import pytesseract
import time

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')

def stream(i):
    while cap.isOpened():
        ret, frame = cap.read()
        text = pytesseract.image_to_string(frame)
        if (text=="M"):
            cv2.imwrite('image%s.jpg' % i, frame)  
            break
        
for x in range(3):
    time.sleep(2)
    stream(x)

cap.release()
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()