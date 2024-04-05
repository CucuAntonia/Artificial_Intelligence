#Castigatorul ia tot
import numpy as np
x = np.array([[45,85],[50,43],[40,80],[55,42],[200,43],[48,40],[195,41],[43,87],[190,40]])
w = [[np.random.randint(40,200),np.random.randint(40,90)],
     [np.random.randint(40,200),np.random.randint(40,90)],
     [np.random.randint(40,200),np.random.randint(40,90)]]

c = 0.1
nr_epoci = 250
print("w =", w)
prototip=[]
for e in range(nr_epoci):
    for i in range(0, len(x)):
        for j in range(0, len(w)):
            r=abs(x[i][0]-w[j][0])+abs(x[i][1]-w[j][1])
            prototip.append(r)
        poz_min=np.argmin(prototip)
        w[poz_min]=w[poz_min]+c*(x[i]-w[poz_min])
        prototip.clear()
print("w =",w, "\n")

for i in range(0, len(x)):
    for j in range(0,len(w)):
        r=abs(x[i][0]-w[j][0])+abs(x[i][1]-w[j][1])
        prototip.append(r)
    poz_min=np.argmin(prototip)
    prototip.clear()
    print(x[i],"este asociat lui",w[poz_min])
    print("\n")

