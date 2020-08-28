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
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.Canny(img,100,200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]
for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray') #plt.subplot (row, column, i+1)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()