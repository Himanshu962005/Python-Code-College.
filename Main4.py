# Q3.Using for Loop, Print a Table of Celsius/Fahrenheit Equivalences. Let C be the Celsius Temperatures Ranging from 0 to 100, for Each Value of C, Print the Corresponding Fahrenheit Temperature.
print(f"{'Celsius':>8} | {'Fahrenheit':>10}")
print("-" * 22)
for celsius in range(0, 101):
    Fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:8} | {Fahrenheit:10.1f}")