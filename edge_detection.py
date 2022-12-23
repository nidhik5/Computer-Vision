import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
img=cv.imread('1.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#laplacian edge detection
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplace',lap)
cv.waitKey(0)

#sobel edge detection
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('sobel x',sobelx)
cv.waitKey(0)
cv.imshow('sobel y',sobely)
cv.waitKey(0)
cv.imshow('sobel ',combined_sobel)
cv.waitKey(0)

#canny edges
c=cv.Canny(gray,150,175)
cv.imshow('canny ',c)
cv.waitKey(0)