# E24.Decorators in Python.
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning.")
        fx(*args, **kwargs)
        print("Thanks for using this Function.")
    return mfx
@greet
def hello():
    print("Hello World.")
@greet
def add(a, b):
    print(a + b)
# greet(hello)().
hello()
# greet(add)(1, 2).
add(1, 2)