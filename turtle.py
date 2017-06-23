#!/usr/bin/env python
print "Location:http://ghimire.xyz/petfeeder\r\n"
#print 'Content-type: text/html\n\n'
import datetime
import RPi.GPIO as GPIO
import time
import countFeed_edgeDetection
from subprocess import call

print "Setting up environment\n"
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
		print "Clearing feed\n"
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
		print "Turning on LED\n"
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.LOW)
		print "Taking snapshot\n"
		mydate = time.time()
		path = '/var/www/html/wp-content/images/'
		file = 	'image_'+ str(mydate) + '_' + str(i)+'.jpg'
		call(['fswebcam','-r','1280x720',path+file])
#		call(['scp','-i','/home/pi/.ssh/mykey',path+file,'ghimirenavin@35.184.166.128:/home/ghimirenavin/turtlefeeder_images'])			
		#call(['vipscripts.sh'])




		time.sleep(2)

		print "Turing off LED\n"
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.HIGH)
		
		print "Feeding\n"
		pwm.ChangeDutyCycle(END)
		time.sleep(1)
		print "Resetting feed\n"
		pwm.ChangeDutyCycle(START)
		time.sleep(1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

