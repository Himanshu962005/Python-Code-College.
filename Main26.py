# Q25.Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character.
words = ["Apple", "Banana", "Ball", "Cat"]
d = {}
for word in words:
    key = word[0]
    d.setdefault(key, []).append(word)
print(d)