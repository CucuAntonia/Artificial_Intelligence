# IMPORTANT! Uneori, codul trebuie rulat de mai multe ori
# pentru a functiona corespunzator deoarece exista probabilitatea cs unul dintre cele K clustere sa fie nule (Division by zero)

import numpy as np


def distance(x1, x2):
    dist = (abs(x2[0]-x1[0])+abs(x2[1]-x1[1]))
    return dist

def centroide(cluster, myList, centroid):
    for i in range(0, len(myList)):
        dist1 = distance(myList[i], centroid[0])
        dist2 = distance(myList[i], centroid[1])
        dist3 = distance(myList[i], centroid[2])
        if min(dist1, dist2, dist3) == dist1:
            cluster.append(1)
        elif min(dist1, dist2, dist3) == dist2:
            cluster.append(2)
        elif min(dist1, dist2, dist3) == dist3:
            cluster.append(3)
    return cluster

def afisare_cluster(cluster):
    cluster1= []
    cluster2= []
    cluster3 =[]
    for i in range (0, len(cluster)):
        if cluster[i] == 1 :
            cluster1.append(myList[i])
        elif cluster[i] == 2:
            cluster2.append(myList[i])
        elif cluster[i] == 3:
            cluster3.append(myList[i])
    print("Punctele ce apartin primului cluster: ", cluster1)
    print("Punctele ce apartin celui de-al doilea cluster:", cluster2)
    print("Punctele ce apartin celui de-al treilea cluster:", cluster3)

def new_centroide(centroid, cluster):
    sx1 = 0
    sy1 = 0
    sx2 = 0
    sy2 = 0
    sx3 = 0
    sy3 = 0
    nr1 = 0
    nr2 = 0
    nr3 = 0
    for i in range (len(cluster)):
        if cluster[i] == 1:
            nr1 = nr1 + 1
            sx1 = sx1 + myList[i][0]
            sy1 = sy1 + myList[i][1]
        elif cluster[i] == 2:
            nr2 = nr2 + 1
            sx2 = sx2 + myList[i][0]
            sy2 = sy2 + myList[i][1]
        elif cluster[i] == 3:
            nr3 = nr3 + 1
            sx3 = sx3 + myList[i][0]
            sy3 = sy3 + myList[i][1]
    centru1 = [sx1 / nr1, sy1 / nr1]
    centru2 = [sx2 / nr2, sy2 / nr2]
    centru3 = [sx3 / nr3, sy3 / nr3]
    new_centroide = []
    new_centroide.append(centru1)
    new_centroide.append(centru2)
    new_centroide.append(centru3)
    return new_centroide

def k_mean_clustering(myList, centroid, K, cluster):
    cluster = centroide(cluster, myList, centroid)
    afisare_cluster(cluster)
    new_centroid = new_centroide(centroid, cluster)
    print("Noii centroizi: ", new_centroid)
    if centroid!=new_centroid:
        cluster=[]
        k_mean_clustering(myList, new_centroid, K, cluster)

K = 3
P1 = [45, 85]
P2 = [50, 43]
P3 = [40, 80]
P4 = [55, 42]
P5 = [200, 43]
P6 = [48, 40]
P7 = [195, 41]
P8 = [43, 87]
P9 = [190, 40]
myList = []
myList.append(P1)
myList.append(P2)
myList.append(P3)
myList.append(P4)
myList.append(P5)
myList.append(P6)
myList.append(P7)
myList.append(P8)
myList.append(P9)

#Calcularea celor 3 clustere random
K1_index = np.random.randint(1, 9)
K2_index = np.random.randint(1, 9)
K3_index = np.random.randint(1, 9)
K1 = myList[K1_index]
K2 = myList[K2_index]
K3 = myList[K3_index]
cluster = []
centroid = []
centroid.append(K1)
centroid.append(K2)
centroid.append(K3)

print("Primul centroid generat random: " , K1)
print("Al doilea centroid generat random: " , K2)
print("Al trailea centroid generat random", K3)

#Apelarea algoritmului
k_mean_clustering(myList,centroid, K, cluster)