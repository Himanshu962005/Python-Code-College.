# M1.Use Command to Compute the Size of a Matrix, Size/Length of a Particular Row/Column, Load Data from a Text File, Store Matrix Data to a Text File, Finding Out Variables and their Features in the Current Scope.
import numpy as np;
# Create a Matrix.
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Matrix :")
print(matrix)
# Size of Matrix.
print("Size of Matrix :", matrix.size)
# Shape of Matrix.
print("Shape of Matrix :", matrix.shape)
# Number of Rows.
print("Number of Rows :", len(matrix))
# Number of Columns.
print("Number of Columns :", len(matrix[0]))
# Length of First Row.
print("Length of First Row :", len(matrix[0]))
# Length of First Column.
print("Length of First Column :", len(matrix[:, 0]))