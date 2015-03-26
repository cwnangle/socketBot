import numpy as np
import cv2

#Number of frames to capture
numFrames = 150;

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (2*320,2*240))
count =0;
while(cap.isOpened()):
    if (count>numFrames):
	break
    print(count)
    print('cap openend')
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
	
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,12,1,0.03)
	
	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)
	
	# Threshold for an optimal value, it may vary depending on the image.
	frame[dst>0.01*dst.max()]=[0,0,255]
	
	#cv2.imshow('dst',frame)
        
	# write the flipped frame
        out.write(frame)
	count = count+1
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
print('capture relseased')
out.release()
print('out released')
cv2.destroyAllWindows()
print(str(count) + " frames successfully captured")
print('everything closed peacefully')