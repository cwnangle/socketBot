#As of Sunday March 22 This script needs to be ran in with the
#Python 3 interpreter because linux is hard
#


import cv2

import numpy as np
import picamera
import time


camera = picamera.PiCamera()

camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True 
camera.start_preview()
time.sleep(2)
camera.capture('camPhoto.jpg')
camera.close()

img = cv2.imread('camPhoto.jpg')


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
print(lines)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines5.jpg',img)

cv2.imshow('dst',img)
cv2.imwrite('featureTrack.png',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()