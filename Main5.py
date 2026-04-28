# Q4.Using While Loop, Produce a Table of Sins, Cosines and Tangents. Make a Variable X in Range from 0 to 10 in Steps of 0.2. For Each Value of X, Print the Value of : Sin(X), Cos(X) and Tan(X).
import math

x = 0.0
end_value = 10.0
step = 0.2
print(f"{'X':<10} {'Sin(X)':<15} {'Cos(X)':<15} {'Tan(X)':<15}")
print("-" * 55)
while x <= end_value:
    s = math.sin(x)
    c = math.cos(x)
    t = math.tan(x)
    print(f"{x:<10.1f} {s:<15.4f} {c:<15.4f} {t:<15.4f}")
    x += step