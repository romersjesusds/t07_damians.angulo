
#tabla de multiplicar de un numero
import os
#input
x=int(os.sys.argv[1])
#validacion de datos
x_invalido=(x<=0)
while(x_invalido):
    x=int(input("ingrese valor correcto de x:"))
    x_invalido = (x <= 0)
for tabla in range(x,x+1,1):
    print("tabla del",tabla)
    for num in range(13):
        print(tabla,"x",num,"=",tabla*num)
#fin_iterador_en_rango
print("Fin del bucle")
