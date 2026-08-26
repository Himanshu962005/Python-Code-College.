# E4.Recursion in Python.
# Factorial(9) = 9*8*7*6*5*4*3*2*1.
# Factorial(8) = 8*7*6*5*4*3*2*1.
# Factorial(7) = 7*6*5*4*3*2*1.
# Factorial(6) = 6*5*4*3*2*1.
# Factorial(5) = 5*4*3*2*1.
# Factorial(4) = 4*3*2*1.
# Factorial(3) = 3*2*1.
# Factorial(2) = 2*1.
# Factorial(1) = 1.
# Factorial(0) = 1.
# Factorial(n) = n * Factorial(n-1).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(9))
# 5 * Factorial(4).
# 5 * 4 * Factorial(3).
# 5 * 4 * 3 * Factorial(2).
# 5 * 4 * 3 * 2 * Factorial(1).
# 5 * 4 * 3 * 2 * 1.
# Quick Quiz : Write a Python to Print the Fibonacci Sequence.
# f(0) = 0.
# f(1) = 1.
# f(2) = f(1) + f(0).
# f(n) = f(n-1) + f(n-2).
# 0 1 1 2 3 5 8.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the Number of Terms : "))
for i in range(n):
    print(fibonacci(i), end=" ")