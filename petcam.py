import time
import Jetson.GPIO as GPIO
buz = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buz, GPIO.OUT,initial=GPIO.LOW)
i = input()
while True:
	if i == '1':
		GPIO.output(buz,GPIO.HIGH)
	else:
		GPIO.output(buz,GPIO.LOW)
	i = input()
# GPIO.output(buz, GPIO.HIGH)
GPIO.cleanup()
