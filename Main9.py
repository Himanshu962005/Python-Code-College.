# Q8.Write a Function that Takes an Interger Input and Calculates the Factorial of that Number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter Number : "))
print("Factorial =", factorial(n))