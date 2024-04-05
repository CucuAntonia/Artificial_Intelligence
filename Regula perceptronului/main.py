
#Regula perceptronului

import numpy as np

w = [0, 1, 0]
x = np.array([[2,1,-1],[0,-1,-1]])
x1 = [2, 1, -1]
x2 = [0, -1, -1]

c = 0.1
d = np.array([-1, 1])
d1 = -1
d2 = 1

for j in range (0, len(x)):
    net = np.dot(w, x[j])
    print("net =", net)
    o = np.sign(net)
    print("o =", o)
    if o!=d[j]:
      for i in range(0, len(x[j])):
         r = d[j] - o
         w[i] = w[i] + c * r * x[j][i]
      print("Ponderile dupa corectie:", w)


