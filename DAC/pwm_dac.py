import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        GPIO.setmode(GPIO.BCM)
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0.0)

    def deinit(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        coeff = voltage / self.dynamic_range * 100
        print(f"Коэффициент заполнения: {coeff}")
        self.pwm.start(coeff)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

