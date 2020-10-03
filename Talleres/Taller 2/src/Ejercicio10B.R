#Ejercicio 10 - Parte B

#NOTA: Se debe instalar lib BB

library("BB")
require(BB)

trigexp = function(x) {
  n = length(x)
  F = rep(NA, n)
  F[1] = 3*x[1]^2 + 2*x[2] - 5 + sin(x[1] - x[2]) * sin(x[1] + x[2])
  tn1 = 2:(n-1) # Esto actua como un for in range(2,n-1)
  F[tn1] = -x[tn1-1] * exp(x[tn1-1] - x[tn1]) + x[tn1] *
    ( 4 + 3*x[tn1]^2) + 2 * x[tn1 + 1] + sin(x[tn1] -
                                               x[tn1 + 1]) * sin(x[tn1] + x[tn1 + 1]) - 8
  F[n] = -x[n-1] * exp(x[n-1] - x[n]) + 4*x[n] - 3
  F
}

n = 10000 # Cantidad de numeros aleatorios
p0 = runif(n) # Genera 'n' numeros aleatorios para los "starting guesses"
sol = BBsolve(par=p0, fn=trigexp)
sol$par