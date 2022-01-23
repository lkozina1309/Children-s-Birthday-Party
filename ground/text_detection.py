# This script will use stream function one hundred times
# Function will start the stream, take a photo when certain text (letter M here) is detected and break
# Useful for automatic photographing


# import the libraries
import cv2 
from PIL import Image
import pytesseract
import time

# Define type of stream
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.5.16:8080/video')

def stream(i):
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                     # convert to grayscale
        text = pytesseract.image_to_string(gray)                           # extract text from an image   
        if (text=="M"):
            cv2.imwrite('image%s.jpg' % i, frame)                          # take a photo if letter M is detected
            break
        
for x in range(100):
    time.sleep(20)
    stream(x)

cap.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
