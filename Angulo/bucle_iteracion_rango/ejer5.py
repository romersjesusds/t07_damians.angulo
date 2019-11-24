# sumar los numeros comprendidos en cierto intervalo
import os
#input
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
#validando valores
x_invalido=(x<0 or x>=y)
y_invalido=(y<0 or y<=x)
while(x_invalido):
  x=int(input("ingrese el valor de x:"))
  x_invalido=(x<0 or x>=y)
while(y_invalido):
  y=int(input("ingrese el valor de y:"))
  y_invalido=(y<0 or y<=x)
#processing
i=0
suma=0
#iterador
for i in range(x+1,y):
  print(i)
  suma+=i
print("la suma de todos lo numeros dentro del rango",x,",",y," es:",suma)
#fin_iterador_en_rango
print("Fin del bucle")

