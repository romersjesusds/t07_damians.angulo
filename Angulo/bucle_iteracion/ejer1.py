# Sumar los x primeros numeros naturales
import os
#input
x=int(os.sys.argv[1])
#validacion de datos
x_invalido=(x<0)
while(x_invalido):
  x=int(input("ingrese valor correcto de x:"))
  x_invalido = (x < 0)
#processing
i=0
suma=0
#bucle_while
while(i<=x):
    suma += i
    i += 1
#fin_while
print("La suma de los ",x ,"primeros numeros es:", suma)
