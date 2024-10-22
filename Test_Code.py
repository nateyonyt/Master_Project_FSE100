Code we intend to test will be put into here
#imports:
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

#variables:
buzzTime = 0.5
beepTime = 0.5


turnoverTime = 1 #time between loops

#setups:
	vibratorPin = (number) #whatever number pin it is in
	PIRSensorPin = #
	passiveBuzzerPin = #
	tempSensorPin = #


	def buzzSetup(pin):
		GPIO.setmode(GPIO.BOARD)   	# Numbers GPIOs by physical location
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)

	def beepSetup(pin):
		GPIO.setmode(GPIO.BOARD)   	# Numbers GPIOs by physical location
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)

	def motionSetup(pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.IN)

	def tempSetup(pin):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.IN)
	


#vibrate code:
	buzzOn() #vibrates
		GPIO.output(BuzzerPin, GPIO.LOW)

	buzzOff() #stops vibrations
		GPIO.output(BuzzerPin, GPIO.HIGH)

	buzzRun() #buzzes once for x amount of time
		on()
		time.sleep(buzzTime)
		off()

#beep code:
	beepOn() #beeps
		GPIO.output(BuzzerPin, GPIO.LOW)

	beepOff() #stops beeping
		GPIO.output(BuzzerPin, GPIO.HIGH)

	beepRun()
		on()
		time.sleep(beepTime)
		off()

#sensors run code:
	while true:
		motion = GPIO.input(PIRSensorPin)
		if motion <= distThreshold:
			buzzRun()
		
		temp = GPIO.input(tempSensorPin)
		if temp >= tempThreshold:
			beepRun()
		
		time.sleep(turnoverTime)
