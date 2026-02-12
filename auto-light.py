import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
photo = 6

GPIO.setup(photo, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

while True:
    state = GPIO.input(photo)
    GPIO.output(led, state)
    time.sleep(0.05)


