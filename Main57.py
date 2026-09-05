# E14.File IO in Python.
# text = f.read().
# print(text).
# f.close().
# Writing a File.
f = open("MyFile.txt", "a")
f.write("Hello, World!")
f.close()
with open("MyFile.txt", "a") as f:
    f.write(" Hey, I am Inside with.")