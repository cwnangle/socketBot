#As of Sunday March 22 This script needs to be ran in with the
#Python interpreter because linux is hard
#


import cv2
import numpy as np
import picamera
import time


camera = picamera.PiCamera()

camera.resolution = (1024, 768)
camera.vflip = True
camera.start_preview()
time.sleep(2)
camera.capture('camPhoto.jpg')
camera.close()


img = cv2.imread('chessboard.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000000, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

print('term Criteria max iter')
print(cv2.TERM_CRITERIA_MAX_ITER)

print('term Criteria EPS')
print(cv2.TERM_CRITERIA_EPS)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv2.imwrite('subpixel5.png',img)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()