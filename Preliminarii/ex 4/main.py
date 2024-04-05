import numpy as np


o1_anterior = 1
o2_anterior = 1
o3_anterior = 1
ok = 1
while ok == 1:
    o1=np.sign(o2_anterior-o3_anterior)
    o2=np.sign(o1_anterior-o3_anterior)
    o3=np.sign(-o1_anterior-o2_anterior)
    if o1==o1_anterior and o2==o2_anterior and o3==o3_anterior:
        ok = 0
    o1_anterior=o1
    o2_anterior=o2
    o3_anterior=o3

print(o1, end=" ")
print(o2, end=" ")
print(o3, end=" ")

