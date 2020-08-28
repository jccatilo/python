import cv2
import numpy as np
from cv2 import cv2

#playing a video
cap = cv2.VideoCapture('maroon.mp4')
while(True):
    ret, frame=cap.read()
    cv2.imshow('output', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

#activate webcam
cap = cv2.VideoCapture(0)
while(cap.isOpened):
    ret, frame=cap.read()
    cv2.imshow('output', frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

