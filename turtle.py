#!/usr/bin/env python
print "Location:http://10.0.0.239\r\n"
#print 'Content-type: text/html\n\n'

import RPi.GPIO as GPIO
import time
from subprocess import call
print "Setting up environment..."
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

		call(['fswebcam','image.jpg'])

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

