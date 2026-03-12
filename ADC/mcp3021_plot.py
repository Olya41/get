import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_and_hist


dynamic_range = 3.3
adc = MCP3021(dynamic_range)
voltage_values = []
time_values = []
duration = 3.0


try:
    start = time.time()
    while time.time() - start < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - start)
    plot_voltage_and_hist(time_values, voltage_values, dynamic_range)
finally:
    adc.deinit()
