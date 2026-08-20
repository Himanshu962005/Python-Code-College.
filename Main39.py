# M8.Perform Vectorized Implementation of Simple Matrix Operation Like Finding the Transpose of a Matrix, Adding, Subtracting or Multiplying Two Matrices.
import numpy as np;
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Transpose.
print("Transpose of A :")
print(A.T)
# Matrix Addition.
print("\nAddition :")
print(A + B)
# Matrix Subtraction.
print("\nSubtraction :")
print(A - B)
# Matrix Multiplication.
print("\nMultiplication :")
print(np.dot(A, B))