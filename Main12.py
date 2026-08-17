# Q11.Write a Program to Generate Fibonacci Series.
n = int(input("Enter Number of Terms : "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b