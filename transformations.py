import cv2 as cv
import numpy as np

img=cv.imread('1.jpg')

#translation
def translation(img,x,y) :
    translation_matrix=np.float32([[1,0,x],[0,1,y]])
    dimensions=[img.shape[0],img.shape[1]]
    return cv.warpAffine(img,translation_matrix,dimensions) #method call kiya hai so this is the answer returned
translated_img=translation(img,100,200)
#cv.imshow('Edinburgh,Scotland',translated_img)
cv.waitKey(0)
#-x left
#-y up
#x right
#y down

#Rotation
height,width=img.shape[0:2]

def rotate (img, angle, rotpoint=None) :
    if (rotpoint== None) :
        rotpoint=height//2,width//2
    
    rotation_matrix=cv.getRotationMatrix2D(rotpoint,angle,1) #img nahi paas karni hai its a matrix that will have centre and angle
    #                                                        #scale chane karke zoom in ho raha
    dimensions= height,width
    return cv.warpAffine(img,rotation_matrix,dimensions)#multiplies rotation matrix with original dimensions

rotated_matrix=rotate(img,45)
double_rotation=rotate(rotated_matrix,45)
#cv.imshow('Edinburgh,Scotland',double_rotation)
cv.waitKey(0)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#cv.imshow('Edinburgh,Scotland',resized)
cv.waitKey(0)

#flip
flipped=cv.flip(img,1)#0 for about x axis, 1 for about y axis and -1 for about diagonal
cv.imshow('Edinburgh,Scotland',flipped)
cv.waitKey(0)
