import cv2

import numpy as np;
 
# Read image
img = cv2.imread("SocketTest.jpg")
img = cv2.resize(img,(0,0), fx=0.3, fy=0.3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

params = cv2.SimpleBlobDetector_Params()

# Change thresholds
threshMin =.18
threshMax =.6
ret, im = cv2.threshold(gray, np.round(255*threshMin),np.round(255*threshMax),cv2.THRESH_BINARY)
cv2.imshow("Thresholded Image", im)

params.minThreshold = np.round(255*threshMin);
params.maxThreshold = np.round(255*threshMax);

# Filter by Area.
params.filterByArea = True
params.minArea = 10
params.maxArea = 70000
 
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
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)

cv2.waitKey(0)