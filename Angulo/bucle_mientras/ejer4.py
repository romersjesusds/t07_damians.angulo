# Mostrar "Acceso denegado" mientras la clave ingresada no sea 12345
import os
clave=int(os.sys.argv[1])
clave_invalida=(clave != "12345")
while(clave_invalida==True):
    clave=input("Ingrese la clave:")
    clave_invalida=(clave != "12345")
#fin_while
print("clave:*****")
