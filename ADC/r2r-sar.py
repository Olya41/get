import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_and_hist


dynamic_range = 3.2
adc = R2R_ADC(dynamic_range, compare_time=0.001)
voltage_values = []
time_values = []
duration = 3.0


try:
    start = time.time()
    while time.time() - start < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - start)
    plot_voltage_and_hist(time_values, voltage_values, dynamic_range)
finally:
    adc.deinit()
