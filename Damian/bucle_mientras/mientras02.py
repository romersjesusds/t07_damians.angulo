import os
#declarar las variables
velocidad_1,velocidad_2,distancia=0.0,0.0,0.0


#input
velocidad_1=int(os.sys.argv[1])
velocidad_2=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

#validador de datos
velocidad_1_invalida=(velocidad_1 < 0)
velocidad_2_invalida=(velocidad_2 < 0)
distancia_invalida=(distancia < 0)

#mientras los datos sean invalidos ingresar nuevamente
while(velocidad_1_invalida):
    velocidad_1=int(input("ingrese un valor correcto para velocidad 1:"))
    velocidad_1_invalida=(velocidad_1 < 0)

while(velocidad_2_invalida):
    velocidad_2=int(input("ingrese un valor correcto para velocidad 2:"))
    velocidad_2_invalida=(velocidad_2 < 0)

while(distancia_invalida):
    distancia=int(input("ingrese un valor correcto para distancia:"))
    distancia_invalida=(distancia < 0)
#fin_while

#processing
tiempo_encuentro=(distancia)/(velocidad_1+velocidad_2)

#output
print("####################################################")
print("#    CALCULO DEL TIEMPO DE ENCUENTRO     #")
print("####################################################")
print("#")
print("#velocidad primer movil:", velocidad_1, "m/s")
print("#velocidad segundo movil:", velocidad_2, "m/s")
print("#distancia de separacion:", distancia, "metros")
print("#tiempo de encuentro:", tiempo_encuentro)
print("#")
print("#####################################################")
