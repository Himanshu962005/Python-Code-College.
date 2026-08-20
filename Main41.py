# M10.Based on Multiple Features/Variables Perform Linear Regression. For Example, Based on a Number of Additional Features Like Number of Bedrooms, Servant Room, Number of Balconies, Number of Houses of Years a House has Been Built - Predict the Price of a House.
import numpy as np;
from sklearn.linear_model import LinearRegression;
# Features :
# Area, Bedrooms, Servant Rooms, Balconies, Age of House.
X = np.array(
    [
        [1000, 2, 1, 1, 5],
        [1200, 2, 1, 2, 4],
        [1500, 3, 1, 2, 3],
        [1800, 3, 2, 3, 2],
        [2000, 4, 2, 3, 1],
    ]
)
# House Prices.
y = np.array([30, 38, 50, 65, 75])
# Create Model.
model = LinearRegression()
# Train Model.
model.fit(X, y)
# New House :
# Area = 1600.
# Bedrooms = 3.
# Servant Rooms = 1.
# Balconies = 2.
# Age = 3 years.
new_house = np.array([[1600, 3, 1, 2, 3]])
prediction = model.predict(new_house)
print("Predicted House Price :", prediction[0])