import numpy as np

#Prueba
matrizA1 = np.array([[2,-1],
                    [1,3]])
matrizB1 = np.array([1,2])

#Ejercicio 1
matrizA2 = np.array([[1,1],
                    [(1/10000),1]])
matrizB2 = np.array([2,1])


#Ejercicio 3
matrizA3 = np.array([[4,-1,-1],
                    [-1,4,-1],
                    [-1,-1,4]])
matrizB3 = np.array([1,2,3])

#Ejercicio 4
matrizA4 = np.array([[2.6,0.3,2.4,6.2],
                    [7.7,0.4,4.7,1.4],
                    [5.1,9.9,9.5,1.5],
                    [6.0,7.0,8.5,4.8]])
matrizB4 = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-b
matrizA4b = np.array([[2.6,0.3,2.4,6.2],
                    [7.7,0.4,4.7,1.4],
                    [5.1,9.9,9.5,1.5],
                    [6.1,7.0,8.5,4.8]])
matrizB4b = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-c
matrizA4c = np.array([[2.6,0.3,2.4,6.2],
                    [7.7,0.4,4.8,1.4],
                    [5.1,9.9,9.5,1.5],
                    [6.1,7.0,8.5,4.8]])
matrizB4c = np.array([50.78,47.36,91.48,98.17])

#Ejercicio 4-d
matrizA4d = np.array([[2.6,0.3,2.4,6.2],
                    [7.7,0.4,4.6,1.4],
                    [5.1,9.9,9.5,1.5],
                    [6.1,7.0,8.5,4.8]])
matrizB4d = np.array([50.78,47.36,91.48,98.17])


def sol_cramer(A,B,R):
    
    matriz_aux = A.copy() 

    for i in range(0,len(B)):
        for j in range(0,len(B)):
            matriz_aux[j][i]=B[j]
            if i>0:
                matriz_aux[j][i-1]=A[j][i-1]
        D = np.linalg.det(matriz_aux)/np.linalg.det(A)
        R.append(round(D,8))
    
    return R

matriz,res = matrizA4,matrizB4

print("Matrices")
print("A = ",np.array(matriz))
print("B = ", res)


print("Solucion Directa Exacta")
X = np.linalg.solve(matriz,res)
print(X)


print("Solucion por Cramer")
R = []
resultado = sol_cramer(matriz,res,R)
print(resultado)




