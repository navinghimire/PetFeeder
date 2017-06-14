import RPi.GPIO as GPIO
import time

#initializes the datapin, setups up the PWM 
def initialize():
	OUTPUT_PIN = 11
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(OUTPUT_PIN, GPIO_OUT)
	pwm = GPIO.PWM(OUTPUT_PIN, 50)
	pwm.start(2.5)

def main():
	
	initialize()
	
	print "working"
	
	try:
		while True:
			pwm.ChangeDutyCycle(7.5)
			time.sleep(1)
	except KeyboardInterrupt:
		p.stop()
		GPIO.cleanup()

	
if __name__ == "__main__":
	main()
	
