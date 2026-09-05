# E16.Seek(), Tell() and Other Functions.
# with open('File.txt', 'r') as f:
#     print(type(f)) # Move to the 10th Byte in the File.
#     f.seek(10)
#     # Read the Next 5 Bytes.
#     print(f.tell())
#     data = f.read(5)
#     print(data)
with open("Sample.txt", "w") as f:
    f.write("Hello, World!")
    f.truncate(3)
with open("Sample.txt", "r") as f:
    print(f.read())