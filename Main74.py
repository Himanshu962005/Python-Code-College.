# E31.Clear the Clutter in Python.
import os;
files = os.listdir("Cluttered_Folder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Cluttered_Folder/{file}", f"Cluttered_Folder/{i}.png")
        i = i + 1