#!/usr/bin/env python
print "Location: http://10.0.0.239/index.php/sample-page/\n"
#print 'Content-type: text/html\n\n'
import datetime
import RPi.GPIO as GPIO
import time
from time import localtime, strftime
from subprocess import call
from subprocess import Popen, PIPE

f = open('/home/pi/PetFeeder/database','a')
LED_PIN=12


OUTPUT_PIN = 11
START = 2.0
END = 11.5
MID = 3.5
NUMBER_OF_SHAKE = 2 
feed = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.setup(LED_PIN,GPIO.OUT)

pwm = GPIO.PWM(OUTPUT_PIN, 50)
pwm.start(MID)
i = 0
feedCalorie = 10
totalCalorieCount = 0
try:

	while (True):
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
		
		
		pwm.ChangeDutyCycle(7.5)
		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.LOW)

		mydate = time.time()
		path = '/var/www/html/wp-content/uploads/images/'
		file = 	'image_'+ str(mydate) + '_' + str(i)+'.jpg'
#		call(['modprobe','uvcvideo'])
		call(['fswebcam','-d','/dev/video0','-q',path+file,'--no-banner'])
		time.sleep(4)
		call(['chmod','+x',path+file])
		call(['scp','-i','/home/pi/wordpress.pem',path+file,'ubuntu@ec2-34-227-200-184.compute-1.amazonaws.com:/home/ubuntu/images/image'+str(i)+'.jpg'])			
		#call(['vipscripts.sh'])
		p = Popen(['ssh','-i','/home/pi/wordpress.pem','ubuntu@ec2-34-227-200-184.compute-1.amazonaws.com', 'python', '/home/ubuntu/PetFeeder/countFeed_edgeDetection.py', '/home/ubuntu/images/image'+str(i)+'.jpg'],stdin=PIPE,stdout=PIPE,stderr=PIPE)
		output,err = p.communicate() 
		#print int(output) 

		currenttime = strftime("%Y-%m-%d %H:%M:%S",localtime())
		f.write(currenttime+' '+str(output)) 
		totalCalorieCount = totalCalorieCount + int(output)

		time.sleep(1)
		GPIO.output(LED_PIN,GPIO.HIGH)
		pwm.ChangeDutyCycle(END)
		time.sleep(1)
		pwm.ChangeDutyCycle(START)
		time.sleep(1)

		#if enough is feed, break

		if totalCalorieCount >= feedCalorie:
			break
		i = i + 1
	f.close()
	pwm.stop()
	GPIO.cleanup(12)
	GPIO.cleanup(11)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup(12)
	GPIO.cleanup(11)
