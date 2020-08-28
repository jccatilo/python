'''
https://towardsdatascience.com/style-transfer-styling-images-with-convolutional-neural-networks-7d215b58f461
How does it work?
1.) We take input image and style images and resize them to equal shapes.
2.) We load a pre-trained Convolutional Neural Network (VGG16).
3.) Knowing that we can distinguish layers that are responsible for the style (basic shapes, colors etc.) and the ones responsible for the content (image-specific features), we can separate the layers to independently work on the content and style.

4.)Then we set our task as an optimization problem where we are going to minimize:
    -content loss (distance between the input and output images - we strive to preserve the content)
    -style loss (distance between the style and output images - we strive to apply a new style)
    -total variation loss (regularization - spatial smoothness to denoise the output image)
5. Finally, we set our gradients and optimize with the L-BFGS algorithm.
'''

import numpy as npy 
import matplotlib.image as Image

#1 Take input image and stile images and resize them to equal shapes
img_path = "images/autumn.jpg"
img_path = Image.imread("images/autumn.jpg")

# determining the length of original image 
w, h = img_path.shape[:2]

# xNew and yNew are new width and 
# height of image required  after scaling 
xNew = int(w * 1 / 2)
yNew = int(h * 1 / 2)
# calculating the scaling factor  
# work for more than 2 pixel  
xScale = xNew/(w-1)
yScale = yNew/(h-1)

# using numpy taking a matrix of xNew 
# width and yNew height with  
# 4 attribute [alpha, B, G, B] values 
newImage = npy.zeros([xNew, yNew, 4])
  
for i in range(xNew-1): 
   for j in range(yNew-1): 
       newImage[i + 1, j + 1]= img_path[1 + int(i / xScale), 
                                 1 + int(j / yScale)] 
  
# Save the image after scaling  
Image.imsave('scaled.png', newImage)