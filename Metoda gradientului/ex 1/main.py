

def f(x) :
    return 6 * pow(x, 2) - 12 * x + 1
def f_dv(x):
    return 12 * x - 12

c = 0.01
x0 = 60
x_anterior = 0

while abs(x0 - x_anterior) > 0.0001:
    x_anterior = x0
    x0 = x_anterior - c * f_dv(x_anterior)
    print(x0)








