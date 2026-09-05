# E18.Map, Filter and Reduce in Python.
# Map in Python.
# def cube(x):
#     return x * x * x
# print(cube(2))
# l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))
# newl = list(map(lambda x: x * x * x, l))
# print(newl)

# Filter in Python.
# def filter_function(a):
#     return a > 2
# newnewl = list(filter(filter_function, l))
# print(newnewl)

# Reduce in Python.
from functools import reduce
# List of Numbers.
numbers = [1, 2, 3, 4, 5]
# Calculate the Sum of the Numbers using the Reduce Function.
def mysum(x, y):
    return x + y
sum = reduce(mysum, numbers)
# Print the Sum.
print(sum)