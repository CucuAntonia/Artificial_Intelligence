import numpy as np

def func_clasificare(x1, x2, x3):
    suma = x1 + x2 + x3 # suma ponderata, ponderile = 1
    if np.sign(suma) == 1:
        print("Clasa 1")
    elif np.sign(suma) == -1:
        print("Clasa 2")
    else:
        print("Eroare!")


P0 = [-1, -1, -1]
P1 = [-1, -1, 1]
P2 = [-1, 1, -1]
P3 = [-1, 1, 1]
P4 = [1, -1, -1]
P5 = [1, -1, 1]
P6 = [1, 1, -1]
P7 = [1, 1, 1]

print("Punctul P0:" , P0, " : ", end=" ")
func_clasificare(P0[0], P0[1], P0[2])
print("Punctul P1:" , P1, " : ", end=" ")
func_clasificare(P1[0], P1[1], P1[2])
print("Punctul P2:" , P2, " : ", end=" ")
func_clasificare(P2[0], P2[1], P2[2])
print("Punctul P3:" , P3, " : ", end=" ")
func_clasificare(P3[0], P3[1], P3[2])
print("Punctul P4:" , P4, " : ", end=" ")
func_clasificare(P4[0], P4[1], P4[2])
print("Punctul P5:" , P5, " : ", end=" ")
func_clasificare(P5[0], P5[1], P5[2])
print("Punctul P6:" , P6, " : ", end=" ")
func_clasificare(P6[0], P6[1], P6[2])
print("Punctul P7:" , P7, " : ", end=" ")
func_clasificare(P7[0], P7[1], P7[2])