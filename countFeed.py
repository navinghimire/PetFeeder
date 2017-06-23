import cv2
import numpy as np

cap = cv2.VideoCapture(3)

while(1):

	# Take each frame
	#frame=cv2.imread('testimage1.jpg')
	_, frame = cap.read()
	frame = frame[90:380,0:480]
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of blue color in HSV
	lower_blue = np.array([0,136,48])
	upper_blue = np.array([81,234,243])

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
