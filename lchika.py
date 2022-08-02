import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT) #green
GPIO.setup(22,GPIO.OUT) #red

for x in range(10):
    GPIO.output(20,0)
    GPIO.output(22,1)
    time.sleep(0.5)
    GPIO.output(20,1)
    GPIO.output(22,0)
    time.sleep(0.5)
GPIO.cleanup()