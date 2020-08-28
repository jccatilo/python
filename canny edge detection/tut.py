'''
Canny edge detection algorithm 5 steps (https://www.youtube.com/watch?v=CGfXCkHNemo)
1.) Noise Reduction (use gaussian filter to remove noice)
2.) Gradient Calculation (find intensity gradients)
3.) Non-maximum suppression (to get rid spurrios response to edge supression)
4.) Double threshold (to determine potential edges)
5.) Edge tracking by hysteresis (to set low and high values. basta gets mo na yon diga. haha)
'''

import cv2
import numpy as np 
from matplotlib import pyplot as plt 
from cv2 import cv2

img = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



