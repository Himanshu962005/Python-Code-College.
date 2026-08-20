# M5.Create Various Type of Plots/Charts Like Histogram, Plot Based on Sine/Cosine Function Based on Data from a Matrix. Further Label Different Axes in a Plot and Data in a Plot.
import numpy as np;
import matplotlib.pyplot as plt;
# Histogram.
data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 50]
plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()
# Sine and Cosine Plot.
x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), label="Sine")
plt.plot(x, np.cos(x), label="Cosine")
plt.title("Sine and Cosine")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
# Matrix Data Plot.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
plt.plot(matrix)
plt.title("Matrix Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()