# Q27.Python Program to Read a File and Capitalize the First Letter of Every Word in the File.
file = open("Test.txt", "r")
text = file.read()
file.close()
print(text.title())