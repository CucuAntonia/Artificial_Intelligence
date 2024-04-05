#Tema 3 - regresia liniara

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datele de intrare
data = pd.read_csv('Salary_data.csv') #citire din fisier
X = data.iloc[:, 0] #numeroteaza si salveaza in X prima coloana din fisier
Y = data.iloc[:, 1] #numeroteaza si salveaza in Y a doua coloana din fisier
print(X)
print(Y)

# y = w1*x + w2 - dreapta de regresie
w1 = 0 #valoarea ponderii initial
w2 = 0 #valoarea ponderii initial
c=0.01 #rata de instruire
epochs = 5000
error = []

for i in range(epochs):
     y_hat = w1*X+w2
     E = (2/len(X)) * np.sum((Y-y_hat)**2) #calculam eroarea
     error.append(E) #adaugam eroarea in lista

     E_dv_w1 = (-1/len(X)) * np.sum(X*(Y-y_hat)) #derivata in raport cu w1
     E_dv_w2 = (-1/len(X)) * np.sum(Y-y_hat)     #derivata in raport cu w2

     w1 = w1 - c * E_dv_w1 #recalculam ponderile (metoda gradientului)
     w2 = w2 - c * E_dv_w2

print("w1 =",w1)
print("w2 =",w2)
print("Error list: ", error)

Y_Line = w1*X+w2 #calculam dreapta de regresie cu noile ponderi
plt.scatter(X, Y) #afisam punctele pe grafic
plt.plot(X, Y_Line, color='black') #afisam dreapta de regresie pe grafic
plt.xlabel('YearsExperience[X]')
plt.ylabel('Salary[Y]')
plt.show()



