import math

import numpy as np
def F(x):
    return (1 - np.exp(-net)) / (1 + np.exp(-net))


W = np.array([1, -1, 0, 0.5])
W2 = W
c = 1
x = np.array([[1, -2, 1.5, 0], [1, -0.5, -2, -1.5], [0, 1, -1, 1.5]])
i = 0
j = 0
x_length = len(x)

while(i<x_length):
    net = np.dot(x[i], W)
    W = W + np.sign(net)+x[i]
    print("W = ", W)
    i = i + 1


while(j<x_length):
    net = np.dot(x[j], W2)
    W2 = W2 + F(net) * x[j]
    print("F(net) = ", F(net))
    print("W2 = ", W2)
    j = j + 1
