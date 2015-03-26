import cv2
import numpy as np
import sys

filename = "SocketTest.jpg"
img = cv2.imread(filename)
img = cv2.resize(img,(0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, gray = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)
cv2.imshow('binary',gray)
#gray = np.float32(gray)
lines = np.empty([1,4])

print(len(lines))
print(type(lines))
print(lines)

rho = 10.0
theta =1.0
minLineLength = 30.0
maxLineGap = 10.0
threshold = 300

cv2.HoughLinesP(gray,rho,theta,threshold,lines,minLineLength,maxLineGap)
print("the Hough thing ran")

dst =0;
print(len(lines))
print(type(lines))
print(lines)


i=0
while(i<1):
	x1 = np.int(np.round(lines.item((i,0))))
	#print(lines.item((i,0)))
	print("x1: "+ str(x1))
	#print(sys.getsizeof(x1))
	        	
	y1=  np.int(np.round(lines.item((i,1))))
	print("y1: "+ str(y1))
	
	x2=  np.int(np.round(lines.item((i,2))))
	print("x2: "+ str(x2))
	
	y2 = np.int(np.round(lines.item((i,3))))
	print("y2: "+ str(y2))
	
	cv2.line(gray,(x1,y1),(x2,y2),(140,0,255),5)
	#cv2.line(gray,(0,0),(500,500),(0,0,255),5)
        i = i+1
    
#result is dilated for marking the corners, not important
#dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
#img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',gray)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()