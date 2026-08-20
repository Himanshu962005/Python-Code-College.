# M12.Use Some Function for Neural Networks, Like Stochastic Gradient Descent or Back Propagation - Algorithm to Predict the Value of a Variable Based on the Dataset of Problem.
import numpy as np;
from sklearn.neural_network import MLPClassifier;
# =====================================================
# Q12 - NEURAL NETWORK / BACKPROPAGATION.
# =====================================================
# Input Data.
# AND Operation.
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Output.
# 0 = False.
# 1 = True.
y = np.array([0, 0, 0, 1])
# Create Neural Network.
model = MLPClassifier(
    hidden_layer_sizes=(5,), solver="lbfgs", max_iter=10000, random_state=1
)
# Train the Model.
model.fit(X, y)
# Test Data.
test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Prediction.
prediction = model.predict(test)
print("===== NEURAL NETWORK =====")
print("Predictions :")
print(prediction)
# Test New Data.
new_data = np.array([[1, 1]])
new_prediction = model.predict(new_data)
print("\nPrediction for [1, 1] :", new_prediction[0])