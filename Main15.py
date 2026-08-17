# Q14.Write a Program to Print Factors of a Given Number.
num = int(input("Enter Number : "))
print("Factors are :")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)