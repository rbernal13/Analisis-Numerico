library(deSolve)
#tamaño poblacional
N = 1000
#estado inicial de los compartimentos
init <- c(S = 990,
          I = 5,
          R = 0,
          V= 0,
          E = 5)
#parámetros del modelo (coeficientes de las variables)
param <- c(
  L = 10,
  miu = 0.001,
  beta = 0.0003,
  alpha =  0.0004,
  gammaa=0.0025,
  epsilon=0.001,
  siggma = 0.0014,
  delta= 0.001,
  phi=9.41e-8)
#crear la función con las ODE
sir <- function(times, init, param) {
  with(as.list(c(init, param)), {
    #ecuaciones diferenciales   
    dS <- (miu*N) - (phi*S*I) - (miu*S) -(siggma*S) + (epsilon*V) + (delta*R)
    dE <- (phi*S*I) - (miu+alpha)*E
    dI <- (alpha*E) - (miu+gammaa)*I
    dR <- (gammaa*I) - (miu+delta)*R
    dV <- (siggma*S) - (miu+epsilon)*V
           
    #resultados de las tasas de cambio    
    return(list(c(dS, dE, dI, dR, dV)))
  })
}
#intervalo de tiempo y resolución
times <- seq(0, 10, by = 1)
#resolver el sistema de ecuaciones con función 'ode'
out1 <- ode(y = init, times = times, func = sir, parms = param, method="euler")
#cambiar out a un data.frame
out1 <- as.data.frame(out1*N) #aqui puede multiplicar 'out' por N
#eliminar la variable 'time' en out
out1$time <- NULL
#mostrar 10 primeros datos
head(out1, 10)

out2 <- ode(y = init, times = times, func = sir, parms = param, method="adams")
#cambiar out a un data.frame
out2 <- as.data.frame(out2*N) #aqui puede multiplicar 'out' por N
#eliminar la variable 'time' en out
out2$time <- NULL
#mostrar 10 primeros datos
head(out2, 10)









# matplot(x = times, y = out, type = "l",
#          xlab = "Tiempo", ylab = "S, I, R", main = "Modelo SIR básico",
#          lwd = 1, lty = 1, bty = "l", col = 2:4)
# #añadir leyenda de líneas
# legend(40, 0.7, c("Susceptibles", "Infectados", "Recuperados"), 
#         pch = 1, col = 2:4, bty = "n", cex = 1)library(deSolve)
#tamaño poblacional
N = 1
#estado inicial de los compartimentos
init <- c(S = 1-1e-6,
          I = 1e-6,
          R = 0)
#parámetros del modelo (coeficientes de las variables)
param <- c(beta = 0.085,
           gamma = 0.14286,
           alpha = 350)
#crear la función con las ODE
sir <- function(times, init, param) {
  with(as.list(c(init, param)), {
    #ecuaciones diferenciales   
    dS <- -beta * S * I
    dI <- beta * S * I - gamma * I
    dR <- gamma * I
    dV <- 
    dE <- 
    #resultados de las tasas de cambio    
    return(list(c(dS, dI, dR)))
  })
}
#intervalo de tiempo y resolución
times <- seq(0, 70, by = 1)
#resolver el sistema de ecuaciones con función 'ode'
out <- ode(y = init, times = times, func = sir, parms = param)
#cambiar out a un data.frame
out <- as.data.frame(out*N) #aqui puede multiplicar 'out' por N
#eliminar la variable 'time' en out
out$time <- NULL
#mostrar 10 primeros datos
head(out, 10)

matplot(x = times, y = out, type = "l",
        xlab = "Tiempo", ylab = "S, I, R", main = "Modelo SIR básico",
        lwd = 1, lty = 1, bty = "l", col = 2:4)
#añadir leyenda de líneas
legend(40, 0.7, c("Susceptibles", "Infectados", "Recuperados"), 
       pch = 1, col = 2:4, bty = "n", cex = 1)