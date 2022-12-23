import cv2 as cv
import numpy as np 
img=cv.imread('1.jpg')

#average
avg=cv.blur(img,(7,7))


#gaussian
g=cv.GaussianBlur(img,(7,7),0)


#median- advanced and used in opencv  projects also reduces noises
m=cv.medianBlur(img,7)


#bilateral blur-advanced cv- blur retains edges in the image-beech ka clear baaki blurred based on radius
l=cv.bilateralFilter(img,200,35,25)
cv.imshow('Edinburgh',l)
cv.waitKey(0)