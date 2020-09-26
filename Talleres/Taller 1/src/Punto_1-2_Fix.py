import math
import numpy as np 

# Conversion de numeros decimales (con float) a binario

def float_binario(numero):
    
    nEntero, nDecimal = str(numero).split(".")
    
    entero = decimal_a_binario(int(nEntero))
    decimal = decimal_a_binario(int(nDecimal))

    resultado = str(entero) + "." + str(decimal)

    return resultado

def decimal_a_binario(num): 
      
    bin_number = 0
    contador = 0
    while (num != 0): 
        residuo = num % 2
        c = pow(10, contador)  
        bin_number += residuo * c  
        num //= 2
          
        # Count used to store exponent value  
        contador += 1
      
    return bin_number  
  
# Conversion de binario a decimal (con float)

def binario_float(numero):

    nEntero, nDecimal = str(numero).split(".")
    
    entero = binario_a_decimal(int(nEntero))
    decimal = binario_a_decimal(int(nDecimal))

    resultado = str(entero) + "." + str(decimal)

    return resultado

def binario_a_decimal(bin):
    
    decimal, i, n = 0, 0, 0
    while(bin != 0): 
        dec = bin % 10
        decimal = decimal + dec * pow(2, i) 
        bin = bin//10
        i += 1
    return decimal



# MAIN

# a)
print("a) Encuentre los primeros 15 bits en la representacion binaria de π")

n1 = np.round(np.pi, 15)
print("Primeros 15 digitos de π: ", n1)
res = float_binario(n1)
print("Primeros 15 digitos de π en binario: ", res)

# b)
print("b) Convertir los siguientes numeros binarios a base 10: 1010101; 1011.101; 10111.010101...; 111.1111")
n1, n2, n3, n4 = 1010101, 1011.101, 10111.010101, 111.1111

print(binario_a_decimal(n1))
print(binario_float(n2))
print(binario_float(n3))
print(binario_float(n4))

# c)
print("c) Convierta los siguientes numeros de base 10 a binaria: 11.25;2/3; 30.6; 99.9")
n1, n2, n3, n4 = 11.25, (2/3), 30.6, 99.9

print(float_binario(n1))
print(float_binario(n2))
print(float_binario(n3))
print(float_binario(n4))

print(float_binario(0.4))




