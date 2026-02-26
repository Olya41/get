import pwm_dac as pwm
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 1
sampling_frequency = 100


dynamic_range = amplitude
start = time.time()
dac = pwm.PWM_DAC(12, 500, dynamic_range, True)



while True:
    delta_t = time.time() - start
    voltage = sg.get_sin_wave_amplitude(signal_frequency, delta_t) * dynamic_range
    dac.set_voltage(voltage)
    sg.wait_for_sampling_period(sampling_frequency)
    print(f"Напряжение: {voltage} В")

dac.deinit()