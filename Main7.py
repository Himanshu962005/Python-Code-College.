# Q6.Write a Program that Takes a Positive Integer N and then Produces N Lines of Output Shown as Follows :
# For Example, Enter a Size : 5.
# *
# **
# ***
# ****
# *****
n = int(input("Enter Size : "))
for i in range(1, n + 1):
    print("*" * i)