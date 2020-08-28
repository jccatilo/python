#https://www.youtube.com/watch?v=-9MXhM_HmxE
import cv2
import numpy as np
from cv2 import cv2

dim=(528,720)
left = cv2.imread('left1.jpg', cv2.IMREAD_COLOR)
left = cv2.resize(left,dim, interpolation = cv2.INTER_AREA)
right = cv2.imread('right2.jpg', cv2.IMREAD_COLOR)
right = cv2.resize(right,dim, interpolation = cv2.INTER_AREA)

images= []
images.append(left)
images.append(right)

stitcher = cv2.createStitcher() #this is for openCV below 4.0
#stitcher = cv2.Stitcher.create() #this is for openCV 4.0 and above
'''
to check openCV version
import cv2
from cv2 import cv2
print(cv2.__version__)
'''

ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_OK:
    cv2.imshow('Panorama', pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("error duting stitching. :p ")