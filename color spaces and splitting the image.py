import cv2 as cv
import numpy as np 
img=cv.imread('1.jpg')
cv.imshow('Edinburgh',img)


b,g,r=cv.split(img)
blank =np.zeros(img.shape[0:2],dtype='uint8')

blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)
print(b.shape)
cv.waitKey(0)