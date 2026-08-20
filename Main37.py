# M6.Generate Different Subplots from a Given Plot and Color Plot Data.
import numpy as np;
import matplotlib.pyplot as plt;
x = np.linspace(0, 10, 100)
plt.subplot(2, 2, 1)
plt.plot(x, x)
plt.title("Linear")
plt.subplot(2, 2, 2)
plt.plot(x, x**2)
plt.title("Square")
plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x))
plt.title("Sine")
plt.subplot(2, 2, 4)
plt.scatter(x, np.cos(x))
plt.title("Cosine")
plt.tight_layout()
plt.show()