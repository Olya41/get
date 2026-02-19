
import RPi.GPIO as GPIO

dynamic_range = 3.3

GPIO.setmode(GPIO.BCM)

dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]
GPIO.setup(dac_bits, GPIO.OUT)
GPIO.output(dac_bits, 0)

#num = 5
#GPIO.setup(num, GPIO.IN)


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)][::-1]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print("Напряжение выходит за динамический диапазон ЦАП")
        print("Устанавливаем 0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    print(f"Число на вход ЦАП: {number}")
    print(f"Биты: {dec2bin(number)}")
    GPIO.output(dac_bits, dec2bin(number))

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Не число")
    
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()



