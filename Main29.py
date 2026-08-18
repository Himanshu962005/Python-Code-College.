# Q28.Python Program to Read the Contents of a File in Reverse Order.
file = open("Test.txt", "r")
text = file.read()
file.close()
print(text[::-1])