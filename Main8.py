# Q7.Write a Function that Takes an Integer _N' as Input and Calculates the Value of 1 + 1/1! + 1/2! + 1/3! + ... + 1/N.
import math;
def series(n):
    sum = 1
    for i in range(1, n + 1):
        sum += 1 / math.factorial(i)
    return sum
n = int(input("Enter Value of N : "))
print("Sum of Series =", series(n))