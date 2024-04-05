
def g(x, y) :
    return pow(x, 2) + 2 * pow(y, 2)

def g_dv_x(x):
    return 2*x
def g_dv_y(y):
    return 4*y
 #h = (1-x)^2+100(x-y^2)^2

def h(x, y):
    return (1-x)**2+100*((x-y**2)**2)
# h = -2 + 202x - 200y^2
def h_dv_x(x, y):
    return 202*x - 2 - 200*(y**2)
# h = 400y^3-400xy --> OVERFLOW ERROR
def h_dv_y(x,y):
    return int(400 * ((y ** 3) - x * y))



c = 0.01
x0 = 17
x_anterior = 0
y0 = 23
y_anterior = 0
print("PENTRU FUNCTIA G:")
while abs(x0-x_anterior) > 0.0001 and abs(y0 - y_anterior) > 0.0001:
    x_anterior = x0
    y_anterior = y0
    x0 = x_anterior - c * g_dv_x(x_anterior)
    y0 = y_anterior - c * g_dv_y(y_anterior)
    print("x: ")
    print(x0)
    print("y: ")
    print(y0)


x1 = 99
x1_anterior = 0
y1 = 98
y1_anterior = 0
print("PENTRU FUNCTIA H:")
while abs(x1-x1_anterior) > 0.0001 and abs(y1 - y1_anterior) > 0.0001:
    x1_anterior = x1
    y1_anterior = y1
    x1 = x1_anterior - c * h_dv_y(x1_anterior, y1_anterior)
    y1 = y1_anterior - c * h_dv_y(x1_anterior,y1_anterior)
    print("x: ")
    print(x1)
    print("y: ")
    print(y1)