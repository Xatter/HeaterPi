import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

off_button = 3
on_button = 5

GPIO.setup(off_button, GPIO.OUT)
GPIO.output(off_button, 1)

time.sleep(1)
GPIO.output(off_button, 0)
