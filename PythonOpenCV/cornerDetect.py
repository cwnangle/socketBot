import cv2
import numpy as np

filename = 'chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

lines = np.empty([1,4])
rho = 10.0
theta =1.0
minLineLength = 30.0
maxLineGap = 10.0
threshold = 30


dst = cv2.HoughLinesP(gray,rho,theta,threshold,lines,minLineLength,maxLineGap)
print("houghLines ran!!!!")

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()