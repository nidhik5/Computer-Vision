import cv2 as cv
import numpy as np
img=cv.imread('1.jpg')

#create black screen to show contours on it
blank=np.ones(img.shape,dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(img,125,175)

countours,hierarchies=cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(countours))
#retr list returns all contours
#retr external returns only external contours
#retrtree returns all hierarchial contours
#chain aprrox none return all coordinates
#chain approx simple returns start and end cordinates
#contours is a list containing start and end coordinates of contours

cv.drawContours(blank,countours,-1,(0,0,255),1)
#kispe draw karna hai, kya draw karna hai, kaha tak as in kitne whether saare or not, konsa colour and thickness of contour lines

thresh,ret=cv.threshold(gray,125,255,cv.THRESH_BINARY) #always takes in gray img cuz threshold value 155 given in terms of grey intensity
cv.imshow('contouring',blank)
cv.waitKey(0)