import cv2 as cv
import numpy as np 

#bitwise operation

#blank=np.zeros((500,500),dtype='unit8')
#rect=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
#circle=cv.circle(blank.copy(),(250,250),250,255,-1)
#a=cv.bitwise_and(rect,circle)
#o=cv.bitwise_or(rect,circle)
#nr=cv.bitwise_not(rect)
#cr=cv.bitwise_not(circle)
#x=cv.bitwise_xor(rect,circle)

#Masking
img=cv.imread('1.jpg')
b=np.zeros(img.shape[:2], dtype='uint8')
mask=cv.circle(b,(img.shape[0]//2+45,img.shape[1]//2)+45,100,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask',masked)
cv.waitKey(0)


