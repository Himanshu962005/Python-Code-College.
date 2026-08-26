# E5.Exception Handling in Python.
# a = input("Enter the Number : ")
# print(f"Multiplication Table of {a} is : ")
# try:
#     for i in range(1, 11):
#         print(f"{a} x {i} = {int(a) * i}")
# except:
#     print("Invalid Input!")
# print("Some IMP Lines of Code")
# print("End of Program")
try:
    num = int(input("Enter a Integer : "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number Entered is not an Integer.")
except IndexError:
    print("Index Error.")