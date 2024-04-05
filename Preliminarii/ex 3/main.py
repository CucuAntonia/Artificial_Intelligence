import numpy as np
import array as arr

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0



pattern = np.array([
    [1,1,1,1,0,1,1,1,1] ,
    [0,1,0,1,0,1,0,1,0] ,
    [0,1,0,0,1,0,0,1,0] ,
    [1,1,0,0,1,0,0,1,0]
])

weights = [-0.14, -0.06, -0.28, -0.93, -0.08, 0.28, -0.64, 0.47, -0.85]
nr_lin = pattern.shape[0]
nr_col = pattern.shape[1]
print("Ponderile: ")
print(weights)

for i in range (0, nr_lin):
    suma = np.dot(pattern[i], weights)
    o = step_function(suma)
    print("Raspunsul neuronului pentru linia" , i , "este:", o)





