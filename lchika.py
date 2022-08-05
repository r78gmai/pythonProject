import RPi.GPIO as GPIO
import time

GREEN_LED = 20
RED_LED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup( GREEN_LED , GPIO.OUT)       # green
GPIO.setup( RED_LED , GPIO.OUT)         # red

#beat
for x in range (3):
    GPIO.output(GREEN_LED, 1)  # green on
    time.sleep(0.2)  # 0.2s
    GPIO.output(GREEN_LED, 0)  # green off
    time.sleep(0.2)
    GPIO.output(GREEN_LED, 1)
    time.sleep(0.2)
    GPIO.output(GREEN_LED, 0)
    time.sleep(0.2)
    GPIO.output(22, 1)  # red on
    time.sleep(0.5)     # 0.5
    GPIO.output(22, 0)  # red off
    time.sleep(0.5)

LED_ON_OFF_FLAG = 0
# for x in range(5):
#     #led_flag = 0
#     if ( LED_ON_OFF_FLAG ):
#         #RED
#         GPIO.output(22, 1)  # red on
#         #time.sleep(0.4)  # ↑ time (red 2s light)
#         LED_ON_OFF_FLAG = 0
#         #GREEN
#         GPIO.output(GREEN_LED, 1)  # green on
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 0)  # green off
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 1)  # green on
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 0)  # green off
#         time.sleep(0.2)  # ↑ time (red 2s light)
#     else:
#         #RED
#         GPIO.output(22, 0)  # red on
#         #time.sleep(0.4)  # ↑ time (red 2s light)
#         LED_ON_OFF_FLAG = 1
#         #GREEN
#         GPIO.output(GREEN_LED, 1)  # green on
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 0)  # green off
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 1)  # green on
#         time.sleep(0.2)  # ↑ time (red 2s light)
#         GPIO.output(GREEN_LED, 0)  # green off
#         time.sleep(0.2)  # ↑ time (red 2s light)


# for x in range(5):   #5 roop
#     GPIO.output(GREEN_LED, 0)  # green off
#     GPIO.output(22, 1)  # red on
#     time.sleep(0.5)  # ↑ time (red 2s light)
#
#     GPIO.output( GREEN_LED ,1) #green on
#     GPIO.output(22,0) #red off
#     time.sleep(0.5)  #↑ time (green 0.5s light)

GPIO.cleanup()