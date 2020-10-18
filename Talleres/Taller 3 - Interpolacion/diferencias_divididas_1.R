f<-function(x) log(1)+((log(1)-log(2))/(1-2))

p<-function(x) log(1)+((log(1)-log(2))/(1-2))*(x-1)

#[1,2]

#cat("f(x0)", log(1))
#cat("f(x1)", ((log(1)-log(2))/(1-2)))

x <- c(seq(1,2,0.1))

fx <- c()
for (j in 1:length(x)) {
  fx[j] = log(x[j])
}
print("Funcion fx",fx)

px <- c()
for (j in 1:length(x)) {
  px[j] = p(x[j])
}
print("Diferencia divida",px)

plot(x,px,main="X vs Px",xlab="x",ylab="px",col="blue")

plot(fx,px,main="Fx vs Px",xlab="fx",ylab="px",col="blue")

#print("Error Relativo", abs(log(1.5)-f(1.5)))








#dat <- data.frame(cbind(x, fx))


#ggplot(dat, aes(x=x, y=fx)) + 
#  geom_point(size=5, col='blue') + 
#  stat_function(fun = p3x, size=1.25, alpha=0.4)