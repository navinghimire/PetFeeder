#!/usr/bin/env python
print "Location:http://10.0.0.71\r\n"
#print 'Content-type: text/html\n\n'

import RPi.GPIO as GPIO
import time





LED_PIN=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN,GPIO.OUT)
try:
	while True:
		GPIO.output(LED_PIN,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

