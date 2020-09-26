import numpy
import random
import time


def generarArreglos(n): 
    matriz= ([[0 for j in range(n)] for i in range(n)])
    res= ([0 for i in range(n)])
    return matriz,res

def generarMatrices():
    for i in range (n):
        for j in range (n):
            matriz[i][j]=round(random.randint(1,10),4)
        res[i]=round(random.randint(1,10),4)

def metodoGauss(n):
    for z in range(n - 1):
        for x in range(1, n - z):
            if (matriz[z][z] != 0):
                p = matriz[x + z][z] / matriz[z][z]
                for y in range(n):
                    matriz[x + z][y] = matriz[x + z][y] - (matriz[z][y] * p)
                res[x + z] = res[x + z] - (res[z] * p)

def metodoGaussJordan(n):
        for z in range(n - 1, 0, -1):
            for x in range(z):
                if (matriz[z][z] != 0):
                    p = matriz[x][z] / matriz[z][z]
                    matriz[x][z] = matriz[x][z] - (matriz[z][z] * p)
                    res[x] = res[x] - (res[z] * p)

def sol(n):
    print("\n")
    for i in range(n):
        if (matriz[i][i] != 0):
            ms = True
        else:
            ms = False
            break
    if (ms == True):
        print("El vector solucion X es: ")
        for i in range(n):
            print(str(res[i] / matriz[i][i]))
    else:
        print('Sin solucion :C')

def calDeterminante(n):
    deter = 1
    for x in range(n):
        deter *= matriz[x][x] 
    print('\nEl determinante es = ', deter)


#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#

#Prueba
#matrizA1 = ([[2,-1],
#                    [1,3]])
#matrizB1 = ([1,2])

#Ejercicio 1
#matrizA2 = np.array([[1,1],
#                    [(1/10000),1]])
#matrizB2 = np.array([2,1])


#Ejercicio 3
matrizA3 = ([[4,-1,-1],
                    [-1,4,-1],
                    [-1,-1,4]])
matrizB3 = ([1,2,3])

#Ejercicio 4
#matrizA4 = np.array([[2.6,0.3,2.4,6.2],
#                    [7.7,0.4,4.7,1.4],
#                    [5.1,9.9,9.5,1.5],
#                    [6.0,7.0,8.5,4.8]])
#matrizB4 = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-b
#matrizA4b = np.array([[2.6,0.3,2.4,6.2],
#                    [7.7,0.4,4.7,1.4],
#                    [5.1,9.9,9.5,1.5],
#                    [6.1,7.0,8.5,4.8]])
#matrizB4b = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-c
#matrizA4c = np.array([[2.6,0.3,2.4,6.2],
#                    [7.7,0.4,4.8,1.4],
#                    [5.1,9.9,9.5,1.5],
#                    [6.1,7.0,8.5,4.8]])
#matrizB4c = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-d
#matrizA4d = np.array([[2.6,0.3,2.4,6.2],
#                    [7.7,0.4,4.6,1.4],
#                    [5.1,9.9,9.5,1.5],
#                    [6.1,7.0,8.5,4.8]])
#matrizB4d = np.array([50.78,47.36,91.48,98.17])

#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#


#matriz,res = generarArreglos(n)
#generarMatrices()

matriz,res = matrizA3, matrizB3
n=len(res)


print("Resolviendo matriz por definicion: A*x = B")
print("A = ",numpy.array(matriz))
print("B = ", res)

metodoGauss(n)
metodoGaussJordan(n)
calDeterminante(n)
sol(n)
