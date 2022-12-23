import numpy as np
import cv2 as cv

img=cv.imread('cars.jpeg')
carplate_img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

haar_cascade=cv.CascadeClassifier('haarcascade_russian_plate_number.xml')
carplate_rects = haar_cascade.detectMultiScale(carplate_img_rgb,scaleFactor=1.1, minNeighbors=6)
for x,y,w,h in carplate_rects: 
    cv.rectangle(carplate_img_rgb, (x,y), (x+w,y+h), (255,0,0), 2) 

cv.imshow('img',carplate_img_rgb)
cv.waitKey(0)