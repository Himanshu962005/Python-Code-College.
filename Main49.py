# E6.Raising Custom Errors in Python.
a = int(input("Enter Any Value Between 5 and 9 : "))
if a < 5 or a > 9:
    raise ValueError("Value should be Between 5 and 9")