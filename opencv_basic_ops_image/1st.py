import cv2
import numpy as np
from cv2 import cv2

img = cv2.imread('soccer_ball.jpg', 0)#specifying image ('filename', 1 for colored or 0 for grayscale, -1 inverted clr)
cv2.imshow('output', img) #(window name, variable want to display in the window)
cv2.imwrite('copied_output.jpg', img)#copying img with specified filename and writing it somewhere
'''
px = img[100,100] #idont know what this is
print(px) 
blue = img[100,100,0] #idk
print(blue)
img[100,100] = [255,255,255] #idk
print (img[100,100])

#accessing RED value
red = img.item(10,10,2)
print(red)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()