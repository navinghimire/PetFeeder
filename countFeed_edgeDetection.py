#!/usr/bin/python
import cv2
import numpy as np;
import sys
print "Content-type: text/html\n\n"
src = sys.argv[1]

BLOB_SIZE_MIN = 2000
BLOB_SIZE_MAX = 4000

im = cv2.imread(src)
# Crop a Region 
im = im[90:380,0:480]
imw = im

# Blur image
blur = cv2.medianBlur(im,15)

# Convert color to hsv
im = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

# Upper and lower limits of color to be tracked. In this case brown
lower_values = np.array([0,0,59])
upper_values = np.array([107,141,239])

both = cv2.inRange(im,lower_values,upper_values)
#cv2.imshow('range',both)

# Erod the image
erode = cv2.erode(both,None,iterations = 2)
#cv2.imshow('eroded',erode)

# Dilate image
dilate = cv2.dilate(erode, None, iterations = 5)
#cv2.imshow('dilated',dilate)

# Get Contours
contours,im2 = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imw,contours,-1,(0,255,0),3)

total = 0
for cnt in contours:
	if cv2.contourArea(cnt) > BLOB_SIZE_MAX :
		# Area divided by the approximate size of the blob
		total = total + (int(cv2.contourArea(cnt))/BLOB_SIZE_MAX)
	elif cv2.contourArea(cnt) > BLOB_SIZE_MIN:
		total = total + 1	
	else:
		total = total
			
cv2.imshow('contours',imw)
print total
