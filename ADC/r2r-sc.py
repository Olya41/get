import time
import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC

def plot_sampling_period_hist(time_arr):
    plt.figure(figsize=(10, 6))
    sampling_periods = []
    for i in range(1, len(time_arr)):
        sampling_periods.append(time_arr[i] - time_arr[i - 1])
    plt.hist(sampling_periods)
    plt.show()


dynamic_range = 3.2
adc = R2R_ADC(dynamic_range, compare_time=0.001)
voltage_values = []
time_values = []
duration = 3.0


try:
    start = time.time()
    while time.time() - start < duration:
        time_values.append(time.time() - start)
        voltage_values.append(adc.get_sc_voltage())
    plot_sampling_period_hist(time_values)
finally:
    adc.deinit()