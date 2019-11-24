#impresion de la edad de 4 personas
import os
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])
q=int(os.sys.argv[4])
x_invalido=(x<0 or x>100)
y_invalido=(y<0 or y>100)
z_invalido=(z<0 or z>100)
q_invalido=(q<0 or q>100)
while(x_invalido==True):
    x=int(input("ingrese edad1 correcta:"))
    x_invalido = (x < 0 or x > 100)
while(y_invalido==True):
    y=int(input("ingrese edad2 correcta:"))
    y_invalido = (y < 0 or y > 100)
while(z_invalido==True):
    z=int(input("ingrese edad3 correcta:"))
    z_invalido = (z < 0 or z > 100)
while(q_invalido==True):
    q=int(input("ingrese edad4 correcta:"))
    q_invalido = (q < 0 or q > 100)

coleccion={"Juan":x,"Maria":y,"Carlos":z,"Pablo":q}
print("Nombre"     ,    "    Edad")
for i in coleccion:
   print(i,"->",coleccion[i])
