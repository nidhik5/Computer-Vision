import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
img=cv.imread('1.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
#cv.imshow('simple',thresh)
cv.waitKey(0)

# inverse simple thresholding
threshold,thresh_inverse=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
#cv.imshow('simple',thresh_inverse)
cv.waitKey(0)

#Adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,0)
cv.imshow('simple',adaptive_thresh)
cv.waitKey(0)
#mean is mean value of surrounding pixel
#kernel size is size of kernel considered for central pixel ka mean
#gaussian mein weight is assigned to every surrounding pixel then beech ka 
#last parameter c ka agar value badhaya toh jyada minus hoga hence max value is of white so more white space
#second last parameter is kernel size its more accurate so border n edge dikhega