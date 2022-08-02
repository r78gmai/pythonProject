import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT) #green
GPIO.setup(22,GPIO.OUT) #red

for x in range(10):
    GPIO.output(20,0) #green off
    GPIO.output(22,1) #red on
    time.sleep(2)   #↑ time (red 2s light)
    GPIO.output(20,1) #green on
    GPIO.output(22,0) #red off
    time.sleep(0.5)  #↑ time (green 0.5s light)

GPIO.cleanup()