#!/usr/bin/python
#Standard imports
import cv2
import numpy as np;


cam = cv2.VideoCapture(3)

_,im = cam.read()
im = im[90:380,0:480]
imw = im
#Blur image
blur = cv2.medianBlur(im,15)

#convert color to hsv
im = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

#upper and lower limits of color to be tracked. In this case brown
lower_values = np.array([0,0,59])
upper_values = np.array([107,141,239])

both = cv2.inRange(im,lower_values,upper_values)
#cv2.imshow('range',both)

# erod the image
erode = cv2.erode(both,None,iterations = 2)
#cv2.imshow('eroded',erode)
#dilate image
dilate = cv2.dilate(erode, None, iterations = 5)
#cv2.imshow('dilated',dilate)
contours,im2 = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
drawing = np.zeros([100,100],np.uint8)
cv2.drawContours(imw,contours,-1,(0,255,0),3)
cv2.imshow('contours',imw)
print cv2.contourArea(contours[0])
print cv2.contourArea(contours[1])
print str(len(contours))
total = 0
for cnt in contours:
	print cv2.contourArea(cnt)
	if cv2.contourArea(cnt) > 1000:
		total = total + 1	
print "Total blobs detected: " + str(total)
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200


# Filter by Area.
params.filterByArea = True
params.minArea = 1500

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
    
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
