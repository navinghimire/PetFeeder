#!/usr/bin/env python
print 'Content-type: text/html\n\n'
print '<h1>Running Python Script</h1>'
import RPi.GPIO as GPIO
import time
OUTPUT_PIN = 11
START = 2.0
END = 11.5
MID = 3.5
NUMBER_OF_SHAKE = 10 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
pwm = GPIO.PWM(OUTPUT_PIN, 50)
pwm.start(MID)
try:
	while True:
		pwm.ChangeDutyCycle(START)
		time.sleep(1)
		
		#shake
		c = 0	
		while c < NUMBER_OF_SHAKE: 	
			pwm.ChangeDutyCycle(MID)
			time.sleep(.2)
			pwm.ChangeDutyCycle(START)
			time.sleep(.2)
			c = c + 1

		pwm.ChangeDutyCycle(END)
		time.sleep(1)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
