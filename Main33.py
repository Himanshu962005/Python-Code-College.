# M2.Perform Basic Operations on Matrices (Like Addition, Subtraction, Multiplication).
import numpy as np;
# Create Two Matrices.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A :")
print(A)
print("\nMatrix B :")
print(B)
# Addition.
print("\nAddition :")
print(A + B)
# Subtraction.
print("\nSubtraction :")
print(A - B)
# Matrix Multiplication.
print("\nMultiplication :")
print(A @ B)