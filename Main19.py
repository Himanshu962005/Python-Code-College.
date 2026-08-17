# Q18.Write a Program to Implement Linear and Binary Search on Lists.
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [10, 20, 30, 40, 50]
x = 30
print("Linear Search :", linear_search(arr, x))
print("Binary Search :", binary_search(arr, x))