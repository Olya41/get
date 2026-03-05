import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.xlabel("time, s")
    plt.ylabel("voltage, V")
    plt.title("U(t)")
    plt.grid(True)
    plt.show()


dynamic_range = 3.2
adc = R2R_ADC(dynamic_range, compare_time=0.0001)
voltage_values = []
time_values = []
duration = 3.0


try:
    start = time.time()
    while time.time() - start < duration:
        time_values.append(time.time() - duration)
        voltage_values.append(adc.get_sc_voltage())
    plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
finally:
    adc.deinit()

