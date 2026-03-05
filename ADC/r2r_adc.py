import RPi.GPIO as GPIO
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec2bin(self, value):
        return [int(element) for element in bin(value)[2:].zfill(8)]

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, self.dec2bin(number))
        if self.verbose:
            print(f"На выход подано {number}")

    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                if self.verbose:
                    print(f"Compare with {i}, result 1")
                return i
            else:
                if self.verbose:
                    print(f"Compare with {i}, result 0")
        return 255

    def get_sc_voltage(self):
        return (self.sequential_counting_adc() / 256) * dynamic_range


if __name__ == "__main__":
    dynamic_range = 3.2
    adc = R2R_ADC(dynamic_range, compare_time=0.01, verbose=True)
    try:
        while True:
            voltage = adc.get_sc_voltage()
            print(f"{voltage} V")
    finally:
        adc.deinit()


