import cv2
import numpy as np
image =  cv2.imread("Image01.jpg")
cv2.imshow('Original Image', image)
h,w,bpp = np.shape(image)
for py in range(0,h):
    for px in range(0,w):
        if(image[py][px][0] < 250):
            if(image[py][px][1] < 150):
                if(image[py][px][2] < 250):
                    image[py][px][0]=200 # BLUE should not be more than 255
                    image[py][px][1]=250 # GREEN should not be more than 255
                    image[py][px][2]=0 # RED should not be more than 255
cv2.imshow('Modified Image', image)
cv2.waitKey(0)