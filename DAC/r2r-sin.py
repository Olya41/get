import r2r_dac as r2r
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 1
sampling_frequency = 100


dynamic_range = amplitude
start = time.time()
obj = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], dynamic_range, True)



while True:
    delta_t = time.time() - start
    voltage = sg.get_sin_wave_amplitude(signal_frequency, delta_t) * dynamic_range
    obj.set_voltage(voltage)
    sg.wait_for_sampling_period(sampling_frequency)
    print(f"Напряжение: {voltage} В")

obj.deinit()


try:
    dynamic_range = amplitude
    obj = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], dynamic_range, True)

    print("Here")

    while True:
        try:
            voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time())
            obj.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
            print("Напряжение: {voltage} В")
        except Exception:
            break
            print("finish")
except Exception:
    print() 
