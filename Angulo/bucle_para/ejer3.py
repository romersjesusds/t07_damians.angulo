#impresion de los promedios de cada alumno
import os
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])
x_invalido=(x<0 or x>20)
y_invalido=(y<0 or y>20)
z_invalido=(z<0 or z>20)
while(x_invalido==True):
    x=int(input("ingrese nota1 correcta:"))
    x_invalido = (x < 0 or x > 20)
while(y_invalido==True):
    y=int(input("ingrese nota2 correcta:"))
    y_invalido = (y < 0 or y > 20)
while(z_invalido==True):
    z=int(input("ingrese nota3 correcta:"))
    z_invalido = (z < 0 or z > 20)
coleccion={"alejandro":x,"Maria":y,"jose":z}
print("Nombre"     ,    "    Promedio")
for i in coleccion:
   print(i,"->",coleccion[i])
