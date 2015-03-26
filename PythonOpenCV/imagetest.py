import cv2
import numpy as np

filename = 'SocketTest.jpg'
img = cv2.imread(filename)

resized_img = cv2.resize(img,(0,0), fx=0.3, fy=0.3) 

gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

resized_img[gray>100]=[0,0,255]

cv2.imshow('gray',resized_img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()