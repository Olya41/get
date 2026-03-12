import time
import matplotlib.pyplot as plt
from r2r_adc import R2R_ADC


def plot_voltage_vs_time(time_arr, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time_arr, voltage)
    plt.xlabel("time, s")
    plt.ylabel("voltage, V")
    plt.title("U(t)")
    plt.grid(True)
    plt.show()


def plot_sampling_period_hist(time_arr):
    plt.figure(figsize=(10, 6))
    sampling_periods = []
    for i in range(1, len(time_arr)):
        sampling_periods.append(time_arr[i] - time_arr[i - 1])
    plt.hist(sampling_periods)
    plt.show()


def plot_voltage_and_hist(time_arr, voltage, max_voltage):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6)) 

    sampling_periods = []
    for i in range(1, len(time_arr)):
        sampling_periods.append(time_arr[i] - time_arr[i - 1])

    ax1.plot(time_arr, voltage)
    ax1.set_xlabel("time, s")
    ax1.set_ylabel("voltage, V")
    ax1.set_title("U(t)")
    ax1.grid(True)

    ax2.hist(sampling_periods)
    ax2.set_xlabel("sampling period, s")
    ax2.set_ylabel("count")
    ax2.set_title("Sampling period distribution")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    dynamic_range = 3.2
    adc = R2R_ADC(dynamic_range, compare_time=0.0001)
    voltage_values = []
    time_values = []
    duration = 3.0

    try:
        start = time.time()
        while time.time() - start < duration:
            time_values.append(time.time() - start)
            voltage_values.append(adc.get_sc_voltage())
        plot_voltage_vs_time(time_values, voltage_values, dynamic_range)
    finally:
        adc.deinit()

