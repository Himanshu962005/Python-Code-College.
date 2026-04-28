# Q5.Write a Program that Reads an Integer Value and Prints — Leap Year or — Not a Leap Year.
year = int(input("Enter Year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year.")
else:
    print("Not a Leap Year.")