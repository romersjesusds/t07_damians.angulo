# Imprimir los numeros naturales en forma descendente en cierto rango
import os
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
#validando valores
x_invalido=(x<0 or x<=y)
y_invalido=(y<0 or y>=x)
while(x_invalido):
  x=int(input("ingrese el valor de x:"))
  x_invalido=(x<0 or x<=y)
while(y_invalido):
  y=int(input("ingrese el valor de y:"))
  y_invalido=(y<0 or y>=x)
#processing
i=0
#iterador
for i in range(x,y-1,-1):
  print(i)

#fin_iterador_en_rango
print("Fin del bucle")
