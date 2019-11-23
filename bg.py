import cv2
import numpy as np
m =  cv2.imread("Image01.jpg")
h,w,bpp = np.shape(m)
for py in range(0,h):
    for px in range(0,w):
        if(m[py][px][0] > 50):            
            m[py][px][0]=247
            m[py][px][1]=187
            m[py][px][2]=87
cv2.imshow('Modified Image', m)
cv2.waitKey(0)
cv2.imwrite('yourNewImage.jpg',m)