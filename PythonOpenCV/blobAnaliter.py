import cv2
#import cv2.cv as cv
import numpy as np;

threshDelta =.05 
count =0
threshMin =.1
threshMax =.9
minSize =2
maxSize =20000

# Read image
img = cv2.imread("SocketTest.jpg")
img = cv2.resize(img,(0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

while(count<10):
	cv2.destroyAllWindows()
	params = cv2.SimpleBlobDetector_Params()
	print(count)
	# Change thresholds
	
	ret, im = cv2.threshold(gray, np.round(255*threshMin),np.round(255*threshMax),cv2.THRESH_BINARY)
	#cv2.imshow("Thresholded Image", im)
	currentMin =.1 #threshMin+threshDelta*count*0+.15
	currentMax =.9 #threshMax-threshDelta*count*0-.15
	
	
	print("currentMin: "+str(currentMin))
	print("currentMax: "+str(currentMax))	

	params.minThreshold = np.round(255*currentMin);
	params.maxThreshold = np.round(255*currentMax);
	#params.thresholdStep = .05	

	# Filter by Area.
	params.filterByArea = True
	params.minArea = 2+count*2
	params.maxArea = 70000-count*2
	 
	print("minimum Blob size: " +str(params.minArea))
	print("maximum Blob size: " +str(params.maxArea))	

	# Filter by Circularity
	#params.filterByCircularity = True
	#params.minCircularity = 0
	#params.maxCircularity = 1
	 
	# Filter by Convexity
	#params.filterByConvexity = True
	#params.minConvexity = 0
	#params.maxConvexity = 1 
	 
	# Filter by Inertia
	#params.filterByInertia = True
	#params.minInertiaRatio = 0
	#params.maxInertiaRatio = 1
	
	# Set up the detector with default parameters.
	detector = cv2.SimpleBlobDetector_create(params)
	
	
	 
	# Detect blobs.
	keypoints = detector.detect(gray)
	print(str(len(keypoints))+ " blobs found") 
	
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	 
	# Show keypoints
	cv2.imshow("Keypoints", im_with_keypoints)
	count = count+1
	cv2.waitKey(0)