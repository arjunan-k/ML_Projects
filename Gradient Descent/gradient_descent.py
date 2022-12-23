# Gradient Descent for Linear Regression
# yhat = wx + b
# loss = (y - yhat)**2 / N
import numpy as np

# Setting both x and y
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = 5
y = 100*x + b
print(f"x: {x}\n"
      f"y: {y}\n"
      f"Parameters we are trying to predict is, w = 100 and b = 5")

# Parameters
w = 0.0
b = 0.0
# Hyperparameter
learning_rate = 0.01

# Create Gradient Descent Function
def gradient_descent(x, y, w, b, learning_rate):
    dldw = 0.0
    dldb = 0.0
    N = x.shape[0]
    # loss = (y - (wx + b))**2
    for xi, yi in zip(x, y):
        dldw += -2 * xi * (yi-(w * xi + b)) * (1 / N)
        dldb += -2 * (yi-(w * xi + b)) * (1 / N)
    w = w - learning_rate * dldw
    b = b - learning_rate * dldb
    return w, b

# Iteratively Make Updates
for epoch in range(2000):
    w, b = gradient_descent(x, y, w, b, learning_rate)
    yhat = w * x + b
    loss = np.divide(np.sum((y - yhat)**2, axis=0), x.shape[0])
    print(f"{epoch} loss is {loss}, parameters w: {w}, b: {b}")

for i, j in zip(yhat, y):
    print(j, round(i, 3))
print(f"Original w: 100 and Gradient Descent w: {round(w, 3)}\n"
      f"Original b: 5   and Gradient Descent b: {round(b, 3)}")
