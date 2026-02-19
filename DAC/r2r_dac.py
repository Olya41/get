import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in bin(int(value))[2:].zfill(8)]

    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение выходит за динамический диапазон ЦАП")
            print("Устанавливаем 0 В")
            return 0
        return int(voltage / self.dynamic_range * 255)

    def set_number(self, number):
        GPIO.output(self.gpio_bits, self.dec2bin(number))

    def set_voltage(self, voltage):
        self.set_number(self.voltage_to_number(voltage))
        print(f"Число на вход ЦАП: {self.voltage_to_number(voltage)}")
        print(f"Биты: {self.dec2bin(self.voltage_to_number(voltage))}")


if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()












