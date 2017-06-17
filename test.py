#!/usr/bin/env python
print "Location:http://10.0.0.71\r\n"
#print 'Content-type: text/html\n\n'

import RPi.GPIO as GPIO
import time
#from cv2 import *

#cap = cv2.VideoCapture(0)




LED_PIN=12

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
pwm.start(START)
try:
	pwm.ChangeDutyCycle(START)
	time.sleep(1)
	pwm.ChangeDutyCycle(MID)
	time.sleep(2)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

