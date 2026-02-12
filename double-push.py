
import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 9
down = 10
ind_up = 0
ind_down = 0
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0
sleep_time = 0.2

while True:
    ind_up = GPIO.input(up)
    ind_down = GPIO.input(down)
    if ind_up and ind_down:
        num = 255
        print(num, dec2bin(num))
    else:
        if ind_up:
            num += 1
            if num > 255:
                num = 0
            print(num, dec2bin(num))
        else:
            if ind_down:
                num -= 1
                if num < 0:
                    num = 0
                print(num, dec2bin(num))
    GPIO.output(leds, dec2bin(num))
    time.sleep(sleep_time)


