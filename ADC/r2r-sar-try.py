from r2r_adc import R2R_ADC

dynamic_range = 3.2
adc = R2R_ADC(dynamic_range, compare_time=0.1, verbose=True)
try:
    while True:
        voltage = adc.successive_approximation_adc()
        print(f"{voltage} V")
finally:
    adc.deinit()

