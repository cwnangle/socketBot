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

gray = np.float32(gray)
#dst = cv2.cornerHarris(gray,16,3,0.04)
src_gray = gray
corners =0
maxCorners =30
qualityLevel =.001
minDistance =.01
Mat =0
blockSize =3
useHarris = 0
k =.4

dst =  cv2.GoodFeaturesToTrack( src_gray,corners,maxCorners,qualityLevel,minDistance,Mat(),blockSize,useHarrisDetector,k );

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
cv2.imwrite('featureTrack.png',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()