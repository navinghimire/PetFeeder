import cv2
import numpy as np

camera_port = 1
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)

def get_images():
	retval, im = camera.read()
	return im

for i in xrange(ramp_frames):
	temp = get_images()
aimg = get_images()
file = "capture.jpg"
cv2.imwrite(file,aimg)
del(camera)
img = cv2.imread('capture.jpg',0)
img = cv2.medianBlur(img,25)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,20,
                            param1=50,param2=30,minRadius=50,maxRadius=100)
print circles.size

circles = np.uint16(np.around(circles))
feeds = 0
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    feeds = feeds + 1

cv2.imshow('detected circles ' + str(feeds),cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()