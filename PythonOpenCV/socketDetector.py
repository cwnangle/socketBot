import numpy as np
import numbers
import cv2
import operator
import serial


	

###############################
"""
all imports

initialise serial



main()
	keep listening
	if listened ==m
		flag = m
		while flag ==m
			look for socket
				videocapture
				if socket == found
					serialSend stop
					break	
		
end main

##############################

def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]

#############################
"""
def look_for_socket(frame,show):
	frame = cv2.flip(frame,0)
   	socketDetected = False
   	sampleArray = np.empty((1,1))
	biggest = sampleArray
	max_area =0
	xmin =0
	xmax =0
	ymax =0
	ymin =0	    
	
###########PARAMS
	params = cv2.SimpleBlobDetector_Params()
	
	# Change thresholds
	threshMin =.18
	threshMax =.6
	
	
	params.minThreshold = np.round(255*threshMin);
	params.maxThreshold = np.round(255*threshMax);
	
	# Filter by Area.
	params.filterByArea = True
	params.minArea = 10
	params.maxArea = 7000
	 
	# Filter by Circularity
	#params.filterByCircularity = True
	#params.minCircularity = 0
	#params.maxCircularity = 1
	 
	# Filter by Convexity
	#params.filterByConvexity = True
	#params.minConvexity = 0
	#params.maxConvexity = 0.2
	 
	# Filter by Inertia
	#params.filterByInertia = True
	#params.minInertiaRatio = 0
	#params.maxInertiaRatio = 0.2
	
	# Set up the detector with default parameters.
	detector = cv2.SimpleBlobDetector_create(params)
###########
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray,(0,0), fx=0.5, fy=0.5)

	gray = cv2.GaussianBlur(gray,(3,3),0)
	th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)
	_,contours,_ = cv2.findContours(th2.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area>100 and area < 40000:
			peri = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			if area>max_area and len(approx)==4:
				biggest = approx
				biggest_cnt = cnt
				max_area = area
				
	gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)

	if((type(biggest)==type(sampleArray))and(biggest.shape != sampleArray.shape)):	
		xmin =0
		xmax =0
		ymax =0
		ymin =0		

		
		cv2.drawContours(gray,biggest,-1,(0,255,0),3)
		
		max_area = 0		
		font = cv2.FONT_HERSHEY_SIMPLEX
		myCentroidx = biggest.item((0,0,0))+biggest.item((1,0,0))+biggest.item((2,0,0))+biggest.item((3,0,0))
		myCentroidy = biggest.item((0,0,1))+biggest.item((1,0,1))+biggest.item((2,0,1))+biggest.item((3,0,1))
		
		x1 = biggest.item((0,0,0))
		x2 = biggest.item((1,0,0))
		x3 = biggest.item((2,0,0))
		x4 = biggest.item((3,0,0))
		xmax = max(x1,x2,x3,x4)
		xmin = min(x1,x2,x3,x4)

		y1 = biggest.item((0,0,1))
		y2 = biggest.item((1,0,1))
		y3 = biggest.item((2,0,1))
		y4 = biggest.item((3,0,1))

		ymax = max(y1,y2,y3,y4)
		ymin = min(y1,y2,y3,y4)
		
		
	
	
	keypoints = detector.detect(gray)
		
	confirmedBlobs =0
	
	for keyp in keypoints:
		
		keyX = keyp.pt[0]
		keyY = keyp.pt[1]
		
		if( keyX<=xmax and keyX>= xmin and keyY<=ymax and keyY>=ymin ):
			confirmedBlobs = confirmedBlobs+1

		
	
	im_with_keypoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 	
	
	
	if(confirmedBlobs==6):
		socketDetected = True
		cv2.putText(im_with_keypoints,'S',(myCentroidx/4,myCentroidy/4),font,1,(255,0,0),2,cv2.LINE_AA)

	if(show):
		cv2.imshow("image with keypoints",im_with_keypoints)	

	return socketDetected;
	


if __name__ == '__main__':
	#ser = serial.Serial('/dev/ttyACM1', 19200, timeout = 1)
	cap = cv2.VideoCapture(0)
	mouseMode = True
	socketFound = False
	
	#while(mouseMode ==False):
	#	serIn = ser.read()
	#	if(serIn == "M"):
	#		mouseMode = True

	while(mouseMode and (socketFound==False)):
		ret, frame = cap.read()
		
		socketFound = look_for_socket(frame,True)
		if cv2.waitKey(1) & 0xFF == ord('q'):
            		break
	#serial.write("D")
	print("Socket Found!! press 0 to close")
	cv2.waitKey(0)		
	cap.release()
	print('capture released')
	cv2.destroyAllWindows()
	print('everything closed peacefully')		
	






	