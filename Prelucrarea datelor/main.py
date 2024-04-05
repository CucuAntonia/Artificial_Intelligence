import numpy as np
import csv

myList = []
with open('C:\\Users\\Antonia\\Desktop\\iris.data') as csvfile:
    readCSV = csv.reader(csvfile, delimiter =',')
    for row in readCSV:
        if len(row) == 5:
            myList.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])

npArray = np.array(myList)

#Pentru fiecare coloană cu valori numerice calculați valoarea minima#
col0_min = np.min(npArray[:,0])
col1_min = np.min(npArray[:,1])
col2_min = np.min(npArray[:,2])
col3_min = np.min(npArray[:,3])
print("Valoarea minima de pe coloana 0: " )
print(col0_min)
print("Valoarea minima de pe coloana 1: " )
print(col1_min)
print("Valoarea minima de pe coloana 2: " )
print(col2_min)
print("Valoarea minima de pe coloana 3: " )
print(col3_min)

#Pentru fiecare coloană cu valori numerice calculați valoarea maxima#
col0_max = np.max(npArray[:,0])
col1_max = np.max(npArray[:,1])
col2_max = np.max(npArray[:,2])
col3_max = np.max(npArray[:,3])
print("Valoarea maxima de pe coloana 0: " )
print(col0_max)
print("Valoarea maxima de pe coloana 1: " )
print(col1_max)
print("Valoarea maxima de pe coloana 2: " )
print(col2_max)
print("Valoarea maxima de pe coloana 3: " )
print(col3_max)

#Pentru fiecare coloană cu valori numerice calculați valoarea mediana#
col0_med = np.median(npArray[:,0])
col1_med = np.median(npArray[:,1])
col2_med = np.median(npArray[:,2])
col3_med = np.median(npArray[:,3])
print("Valoarea mediana de pe coloana 0: " )
print(col0_med)
print("Valoarea mediana de pe coloana 1: " )
print(col1_med)
print("Valoarea mediana de pe coloana 2: " )
print(col2_med)
print("Valoarea mediana de pe coloana 3: " )
print(col3_med)

# Normalizați valorile de pe fiecare coloană #
col0_norm = (npArray[:,0]-min(npArray[:,0])) / (max(npArray[:,0])- min(npArray[:,0]))
col1_norm = (npArray[:,1]-min(npArray[:,1])) / (max(npArray[:,1])- min(npArray[:,1]))
col2_norm = (npArray[:,2]-min(npArray[:,2])) / (max(npArray[:,2])- min(npArray[:,2]))
col3_norm = (npArray[:,3]-min(npArray[:,3])) / (max(npArray[:,3])- min(npArray[:,3]))
print("Valorile normalizate de pe coloana 0: " )
print(col0_norm)
print("Valorile normalizate de pe coloana 1: " )
print(col1_norm)
print("Valorile normalizate de pe coloana 2: " )
print(col2_norm)
print("Valorile normalizate de pe coloana 3: " )
print(col3_norm)

# Calculați suma ponderată a valorilor numerice de pe fiecare linie #
# Ponderi:  [0.2, 1.1, -0.9, 1]
ponderi=[]
for row in npArray:
    ponderi.append(0.2*row[0]+1.1*row[1]+(-0.9)*row[2]+1*row[3])
#print(ponderi)
#Stack arrays in sequence vertically (row wise).
npPonderi = np.vstack(ponderi)
#print(npPonderi)
#axis=1 -> horizontally, axis=0 -> vertically
npArray = np.concatenate([npArray, npPonderi], axis=1)
print(npArray)









