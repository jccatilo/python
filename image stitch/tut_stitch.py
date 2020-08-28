# https://www.youtube.com/watch?v=ToldvnUtBh0
import cv2
import numpy as np
from cv2 import cv2

img_ = cv2.imread('left.jpg')
#img_ = cv2.resize(img_, (0,0), fx = 1, fy=2) #just to resize image
img1 = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)

img = cv2.imread('right.jpg')
#img = cv2.resize(img, (0,0), fx = 1, fy=2) #just to resize image
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
#find keypoints
kp1, des1 = sift.detectAndCompute(img1, None)
kp1, des2 = sift.detectAndCompute(img2, None)
print("here na")
cv2.imshow('left', cv2.drawKeypoints(img_,kp1,None))