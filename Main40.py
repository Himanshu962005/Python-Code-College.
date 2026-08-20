# M9.Implement Linear Regression Problem. For Example, Based on a Dataset Comprising of Existing Set of Prices and Area/Size of the Houses, Predict the Estimated Price of a Given House.
import numpy as np;
import matplotlib.pyplot as plt;
from sklearn.linear_model import LinearRegression;
# Area of Houses.
X = np.array([[1000], [1200], [1500], [1800], [2000]])
# Price of Houses.
y = np.array([30, 36, 45, 54, 60])
# Create Model.
model = LinearRegression()
# Train Model.
model.fit(X, y)
# Predict Price.
area = np.array([[1600]])
prediction = model.predict(area)
print("Predicted Price :", prediction[0])
# Plot.
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("Linear Regression")
plt.show()