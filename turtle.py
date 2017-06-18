#!/usr/bin/env python
#print "Location:http://10.0.0.239\r\n"
print 'Content-type: text/html\n\n'
import datetime
import RPi.GPIO as GPIO
import time

from subprocess import call
import cv2

print "Setting up environment..."
LED_PIN=12

# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = camera.read()
	return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
	temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "/home/pi/test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
 
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)



OUTPUT_PIN = 11
START = 2.0
END = 11.5
MID = 3.5
NUMBER_OF_SHAKE = 2 
feed = 2
GPIO.setmode(GPIO.BOARD)

GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.setup(LED_PIN,GPIO.OUT)

pwm = GPIO.PWM(OUTPUT_PIN, 50)
pwm.start(MID)

try:

	for i in range(0,feed):
		pwm.ChangeDutyCycle(START)
		print "Clearing feed"
		time.sleep(1)
		
		#shake
		c = 0	
		while c < NUMBER_OF_SHAKE: 	
			pwm.ChangeDutyCycle(MID)
			time.sleep(.2)
			pwm.ChangeDutyCycle(START)
			time.sleep(.2)
			c = c + 1
		
		
		pwm.ChangeDutyCycle(7.5)
		print "Turning on LED"
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.LOW)
		print "Taking snapshot"
		
		
		mydate = time.time()
		call(['sudo','fswebcam','/var/www/html/image123.jpg'])
		
		#call(['vipscripts.sh'])




		time.sleep(2)

		print "Turing off LED"
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.HIGH)
		
		print "Feeding..."
		pwm.ChangeDutyCycle(END)
		time.sleep(1)
		print "Resetting feed..."
		pwm.ChangeDutyCycle(START)
		time.sleep(1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

