#Regula Delta
import numpy
import numpy as np

#functia de activare
def f(x):
    e = 2.71828
    return (2/1+pow(e, (-x)))-1


c=0.1
Emax=0.001
E=0
y=np.array([[45,85,-1],[50,43,-1],[40,80,-1],[55,42,-1],[200,43,-1],[48,40,-1],[195,41,-1],[43,87,-1],[190,40,-1]])
print("--------------Intrari---------------:")
print(y)
print("--------------Iesiri-----------------:")
d=np.array([[1,-1,-1],[-1,1,-1],[1,-1,-1],[-1,1,-1],[-1,-1,1],[-1,1,-1],[-1,-1,1],[1,-1,-1],[-1,-1,1]])
print(d)



#Aflarea minimului de pe fiecare coloana
min_col = []
for j in range(0, y.shape[1]):
        min = np.min(y[:,j])
        min_col.append(min)
min_col=np.array(min_col)
print("---------Minimul de pe fiecare coloana------------:", min_col)

#Aflarea maximului de pe fiecare coloana
max_col = []
for j in range(0, y.shape[1]):
        max = np.max(y[:,j])
        max_col.append(max)
max_col=np.array(max_col)
print("-----------Maximul de pe fiecare coloana:------------", max_col)

y_norm = []



#Normalizarea valorilor
for i in range(0, y.shape[0]):
    for j in range(0, y.shape[1]):
        val_norm = (y[i][j]-min_col[j])/(max_col[j]-min_col[j])
        y_norm.append(val_norm)

y_norm = np.array(y_norm)
y_norm = np.reshape(y_norm, (y.shape[0], y.shape[1]))


print("-------------Valorile normalizate:-----------------")
print(y_norm)

#Populam ponderile cu valori random
w1 = np.random.randint(-1, 1)
w2 = np.random.randint(-1, 1)
w3 = np.random.randint(-1, 1)
print("-------------Ponderile:---------------- ")
w = []
w.append(w1)
w.append(w2)
w.append(w3)
w = np.array(w)
print(w)


#Se calculeaza iesirile fiecarui perceptron
o = []
for i in range(len(y)):
    net = np.dot(w, y[i])
    o.append(f(net))
o=np.array(o)
print("-------------Iesirile:---------------- ")
print(o)











