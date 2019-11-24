# Mostrar error "x" veces.
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
#bucle_while
while(i<=x):
    print("Error")
    i +=1

#fin_while
