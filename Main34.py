# M3.Display Specific Rows and Columns of the Matrix.
import numpy as np;
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Matrix :")
print(matrix)
# Display First Row.
print("\nFirst Row :")
print(matrix[0])
# Display Second Row.
print("\nSecond Row :")
print(matrix[1])
# Display First Column.
print("\nFirst Column :")
print(matrix[:, 0])
# Display Second Column.
print("\nSecond Column :")
print(matrix[:, 1])