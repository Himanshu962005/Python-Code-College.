# E13.Local vs Global Variables in Python.
x = 10 # Global Variable.
def my_function():
    global x
    x = 5 # This will Change the Value of the Global Variable X.
    y = 5 # Local Variable.
my_function()
print(x) # Prints 5.
# print(y) # This will Cause an Error because Y is a Local Variable and is not Accessible Outside of the Function.