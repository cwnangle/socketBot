import cv2
import numpy as np

img = cv2.imread('SocketTest.jpg')
img = cv2.resize(img,(0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,5,100,apertureSize = 3)
print("will this print?")
lines = cv2.HoughLines(edges,2,np.pi/180,230)
print(lines)
print(type(lines))
print(len(lines))
count =0



#for rho,theta in lines[2]:
while(count<len(lines)):
    rho = lines.item(count*2)
    theta = lines.item(count*2+1)
    
    print("count: "+str(count))
    print("rho: "+str(rho))
    print("theta: "+str(theta))
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    count = count+1

cv2.imshow('dst',img)    

print("wait for a zero keypress")
cv2.waitKey(0)

#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()