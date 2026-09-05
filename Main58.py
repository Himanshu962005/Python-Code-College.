# E15.Read(), Readlines() and Other Methods.
# f = open('MyFile2.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of Student {i} in Maths is : {m1*2}")
#     print(f"Marks of Student {i} in English is : {m2*2}")
#     print(f"Marks of Student {i} in SST is : {m3*2}")
#     print(line)
f = open('MyFile3.txt', 'w')
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
f.writelines(lines)
f.close()