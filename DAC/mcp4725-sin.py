import mcp4725_driver as mcp
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 1
sampling_frequency = 100


start = time.time()
dac = mcp.MCP_4725(dynamic_range=5.0)



while True:
    delta_t = time.time() - start
    voltage = sg.get_sin_wave_amplitude(signal_frequency, delta_t) * amplitude
    dac.set_voltage(voltage)
    sg.wait_for_sampling_period(sampling_frequency)
    print(f"Напряжение: {voltage} В")

dac.deinit()



