import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
img=cv.imread('1.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8') #blank screen 
mask=cv.circle(blank,(img.shape[0]//2,img.shape[1]//2),100,255,-1) #white circle on blank screen
masked=cv.bitwise_and(img,img,mask=mask) # img ka khudke saath and in the circle as mask
cv.imshow('img',masked)
cv.waitKey(0)
colours=('b','g','r')
for i,col in enumerate(colours) :
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()