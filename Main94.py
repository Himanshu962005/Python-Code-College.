# E51.Generators in Python.
def my_generator():
    for i in range(50000000):
        # Complex Computations.
        yield i
        my_generator()
gen = my_generator()
# print(next(gen)).
# print(next(gen)).
# print(next(gen)).
for j in gen:
    print(j)