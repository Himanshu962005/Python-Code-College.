# Q20.Python Program to Remove the "i"th Occurrence of the Given Word in a List Where Words Repeat.
words = ["Apple", "Banana", "Apple", "Mango", "Apple"]
word = "Apple"
n = 2
count = 0
result = []
for i in words:
    if i == word:
        count += 1
        if count == n:
            continue
    result.append(i)
print(result)