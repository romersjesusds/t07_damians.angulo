# factorial de un numero x
import os
#input
x=int(os.sys.argv[1])
#validacion de datos
x_invalido=(x<0)
while(x_invalido):
  x=int(input("ingrese valor correcto de x:"))
  x_invalido = (x < 0)
#processing
i=1
producto=1
#bucle_while
while(i<=x):
    producto *= i
    i += 1
#fin_while
print("el factorial de ",x ,"es:",producto)
