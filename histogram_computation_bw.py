import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
img=cv.imread('1.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank=np.ones(img.shape[:2],dtype='uint8')
circl=cv.circle(blank,(img.shape[0]//2,img.shape[1]//2),100,255,-1)
mask=cv.bitwise_and(gray,blank,mask=circl)
hist=cv.calcHist([gray],[0],mask,[256],[0,256])
cv.imshow('g',mask)
cv.waitKey(0)
plt.figure()
plt.xlabel('bins')
plt.ylabel('number of pixels')
plt.xlabel([0,256])
plt.plot(hist)
plt.show()
cv.waitKey(0)