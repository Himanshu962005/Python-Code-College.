# Q19.Write a Program to Sort a List Using Insertion Sort and Bubble Sort.
arr = [5, 2, 9, 1, 3]
insertion = arr.copy()
for i in range(1, len(insertion)):
    key = insertion[i]
    j = i - 1
    while j >= 0 and insertion[j] > key:
        insertion[j + 1] = insertion[j]
        j -= 1
    insertion[j + 1] = key
print("Insertion Sort :", insertion)
bubble = arr.copy()
for i in range(len(bubble)):
    for j in range(0, len(bubble) - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print("Bubble Sort :", bubble)