# Ejercicio 3
# Parte B


# Matriz A
A = matrix(c(4, -1, -1, -1, -1, 4,
             -1, -1, -1, -1, 4, -1,
             -1, -1, -1, 4), nrow=4, byrow=TRUE)
print(A)

# Matiz B
b = c(1.11111, 5, 1.5,-2.33)
print(b)

# Ahora vamos a evaluar la solucion con cada uno de los metodos iterativos y determinaremos cual es mas favorable
# Teniendo en cuenta que ambos son algoritmos lineales entonces tienen una complejidad de O(n)

tol=1e-8 # Tolerancia

# Por Gauss-Seidel

solGauss=itersolve(A,b,x0=NULL, nmax = 1000, tol, method = "Gauss-Seidel")
print(solGauss) # 32 Iteraciones

# Por Jacobi

solJacobi=itersolve(A, b, 1:4, nmax = 1000, tol, method = c("Jacobi"))
print(solJacobi) # 56 Iteraciones

# Por Richardson

solRichar=itersolve(A, b, x0 = NULL, nmax = 1000, toleracia, method = c("Richardson"))
print(solRichar) # 39 Iteraciones

