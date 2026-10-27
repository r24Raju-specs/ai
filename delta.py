import numpy as np

X = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
y = np.array([1, 1, 1, 0])

w = np.zeros(2)
b = 0
lr = 0.1

for epoch in range(100):
    for i in range(len(X)):
        output = np.dot(X[i], w) + b
        error = y[i] - output
        w += lr * error * X[i]
        b += lr * error

print("Weights:", w)
print("Bias:", b)
print("Predictions:", np.round(X @ w + b))
