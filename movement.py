import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

ain2 = 31
ain1 = 33
bin1 = 35
bin2 = 37

GPIO.setup(ain2, GPIO.OUT)
GPIO.setup(ain1, GPIO.OUT)
GPIO.setup(bin1, GPIO.OUT)
GPIO.setup(bin2, GPIO.OUT)

def moveForward():
	GPIO.output(ain1, 0)
	GPIO.output(ain2, 1)
	GPIO.output(bin1, 1)
	GPIO.output(bin2, 0)

def moveBackwards():
	GPIO.output(ain1, 1)
	GPIO.output(ain2, 0)
	GPIO.output(bin1, 0)
	GPIO.output(bin2, 1)

def turnLeft():
	GPIO.output(ain1, 0)
	GPIO.output(ain2, 1)
	GPIO.output(bin1, 0)
	GPIO.output(bin2, 1)

def turnRight():
	GPIO.output(ain1, 1)
	GPIO.output(ain2, 0)
	GPIO.output(bin1, 1)
	GPIO.output(bin2, 0)

def stop():
	GPIO.output(ain1, 0)
	GPIO.output(ain2, 0)
	GPIO.output(bin1, 0)
	GPIO.output(bin2, 0)

#try:
#	while True:
#		turnRight()

#except KeyboardInterrupt:
#	GPIO.cleanup()
