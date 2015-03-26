#As of Sunday March 22 This script needs to be ran in with the
#Python 3 interpreter because linux is hard
#

import io
import cv2
import numpy as np
import picamera
import time
import picamera.array

camera = picamera.PiCamera()

camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True 
camera.start_preview()
time.sleep(2)
camera.stop_preview()
#camera.capture('camPhoto.jpg')

stream = io.BytesIO()


while(True):
	print('capturing frame')
	camera.capture(stream, format='jpeg')
	print('frame Captured')
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	print('data from stream converted')
	img = cv2.imdecode(data, 1)
	print('image formatted')
	#ret, img = cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,16,3,0.04)
	print('corners detected')
	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)
	
	# Threshold for an optimal value, it may vary depending on the image.
	img[dst>0.01*dst.max()]=[0,0,255]
	
	cv2.imshow('dst',img)
	time.sleep(2)
	print('image shown')
	if cv2.waitKey(0) & 0xff == 27:
		cv2.destroyAllWindows()
		break