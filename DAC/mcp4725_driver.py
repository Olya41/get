import RPi.GPIO as GPIO
import smbus

class MCP_4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
    
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
    
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.set_number(0)
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        if not (0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0 - {self.dynamic_range}) В")
        else:
            number = int(voltage / self.dynamic_range * 4095)
            self.set_number(number)
    
if __name__ == "__main__":

    try:
        dac = MCP_4725(dynamic_range=5.0)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()














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



