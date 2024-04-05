
import math
import numpy as np

x = np.array([2,1,2])
y = np.array([1,-1,4])
print(x)
print(y)
norma_x = 0
norma_y = 0
for i in range (0, len(x)):
    norma_x = norma_x + x[i] ** 2

for j in range (0, len(y)):
    norma_y = norma_y + y[j] ** 2

print("Norma lui x: ")
print(math.sqrt(norma_x))
print("Norma lui y: ")
print(math.sqrt(norma_y))

prod_scalar = np.dot(x, y)
print("Produsul scalar: ")
print(prod_scalar)

cos  = prod_scalar / (math.sqrt(norma_x) * math.sqrt(norma_y))
print("Cosinusul: " )
print(cos)
print("Cosinului folosind metoda degrees: ")
print(math.degrees(cos))