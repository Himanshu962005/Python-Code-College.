# M4.Perform Other Matrix Operations Like Converting Matrix Data to Absolute Values, Taking the Negative of Matrix Values, Adding/Removing Rows/Columns from a Matrix, Finding the Maximum or Minimum Values in a Matrix or in a Row/Column, and Finding the Sum of Some/All Elements in a Matrix.
import numpy as np;
matrix = np.array([[10, -20, 30], [-40, 50, -60], [70, -80, 90]])
print("Original Matrix :")
print(matrix)
# 1. Absolute Values.
print("\nAbsolute Values :")
print(np.abs(matrix))
# 2. Negative of Matrix.
print("\nNegative of Matrix :")
print(-matrix)
# 3. Maximum Value.
print("\nMaximum Value :", np.max(matrix))
# 4. Minimum Value.
print("Minimum Value :", np.min(matrix))
# 5. Maximum Value in Each Row.
print("\nMaximum of Each Row :")
print(np.max(matrix, axis=1))
# 6. Minimum Value in Each Column.
print("\nMinimum of Each Column :")
print(np.min(matrix, axis=0))
# 7. Sum of All Elements.
print("\nSum of All Elements :", np.sum(matrix))
# 8. Add a Row.
new_row = np.array([[100, 110, 120]])
matrix_with_row = np.vstack((matrix, new_row))
print("\nAfter Adding a Row :")
print(matrix_with_row)
# 9. Add a Column.
new_column = np.array([[1], [2], [3]])
matrix_with_column = np.hstack((matrix, new_column))
print("\nAfter Adding a Column :")
print(matrix_with_column)
# 10. Remove Last Row.
removed_row = np.delete(matrix, -1, axis=0)
print("\nAfter Removing Last Row :")
print(removed_row)
# 11. Remove Last Column.
removed_column = np.delete(matrix, -1, axis=1)
print("\nAfter Removing Last Column :")
print(removed_column)