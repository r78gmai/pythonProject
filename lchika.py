import RPi.GPIO as GPIO
import time

GREEN_LED = 20
RED_LED = 22
LED_ON_OFF_FLAG = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup( GREEN_LED ,GPIO.OUT) #green
GPIO.setup(22,GPIO.OUT) #red

for x in range(5):
    #led_flag = 0

    if ( LED_ON_OFF_FLAG ):
        #RED
        GPIO.output(22, 1)  # red on
        #time.sleep(0.4)  # ↑ time (red 2s light)
        LED_ON_OFF_FLAG = 0
        #GREEN
        GPIO.output(GREEN_LED, 1)  # green on
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 0)  # green off
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 1)  # green on
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 0)  # green off
        time.sleep(0.2)  # ↑ time (red 2s light)
    else:
        #RED
        GPIO.output(22, 0)  # red on
        #time.sleep(0.4)  # ↑ time (red 2s light)
        LED_ON_OFF_FLAG = 1
        #GREEN
        GPIO.output(GREEN_LED, 1)  # green on
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 0)  # green off
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 1)  # green on
        time.sleep(0.2)  # ↑ time (red 2s light)
        GPIO.output(GREEN_LED, 0)  # green off
        time.sleep(0.2)  # ↑ time (red 2s light)


# for x in range(5):   #5 roop
#     GPIO.output(GREEN_LED, 0)  # green off
#     GPIO.output(22, 1)  # red on
#     time.sleep(0.5)  # ↑ time (red 2s light)
#
#     GPIO.output( GREEN_LED ,1) #green on
#     GPIO.output(22,0) #red off
#     time.sleep(0.5)  #↑ time (green 0.5s light)

GPIO.cleanup()