import cv2
import numpy as np

img = cv2.imread('SocketTest.jpg')
img = cv2.resize(img,(0,0), fx=0.3, fy=0.3)
cv2.imshow("img",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray img", gray)

edges = cv2.Canny(gray,25,300,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('pictureWithLines',img)
cv2.imwrite('houghlines3.jpg',img)