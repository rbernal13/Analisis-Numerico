import math
import numpy as np
import pylab

e = math.e
pi = math.pi

nIteraciones=[]
valoresX=[]

def newton_raphson(f, df, x, TOL):
    error = 1
    ite = 0
    while error > TOL:
        nIteraciones.append(ite)
        new_x = x - f(x)/df(x)
        error = abs(new_x - x)
        x = new_x
        valoresX.append(x)
        ite += 1
        print(f'x{ite}: {x:.15f}')
    print(f"Estimacion de Newton = {x:.15f}\nIteraciones: {ite}")

def modificado_newton(f, df, ddf, x, TOL):
    error = 1
    ite = 0
    while error > TOL:
        f_x = f(x)
        d_x = df(x)
        new_x = x - (f_x*d_x)/(d_x*d_x - f_x*ddf(x))
        error = abs(new_x - x)
        x = new_x
        ite += 1
        print(f'x{ite}: {x}')
    print(f"Estimacion de Newton Modificado = {abs(x):.15f}\nIteraciones: {ite}")


'''----------MAIN---------------'''
#f = lambda x: x**4 - 2*x**3 - 12*x*x + 16*x - 40
f = lambda x: ((math.exp(x)) - x - 1)
#df = lambda x: 4*x**3 - 6*x*x - 24*x + 16
df = lambda x: ((math.exp(x)) - 1)
#ddf = lambda x: 12*x*x - 12*x - 24
ddf = lambda x: (math.exp(x))
newton_raphson(f, df, 1, 1e-16)
modificado_newton(f, df, ddf, 1, 1e-16)

pylab.title("Iteraciones vs Raiz")
pylab.plot(nIteraciones,valoresX)
pylab.xlabel('(x) Iteraciones')
pylab.ylabel('(y) X (Valor aproximado de la Raiz)') 
pylab.show()