# Q26.Python Program to Find the Length of a List Using Recursion.
def list_length(lst):
    if not lst:
        return 0
    return 1 + list_length(lst[1:])
lst = [1, 2, 3, 4, 5]
print("Length =", list_length(lst))