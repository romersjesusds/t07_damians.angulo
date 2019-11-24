# Decodificar mensaje encriptado
# A= Hola
# E = ¿como estas?
# I = Te extraño
# O = Cuidate
# U = Adios
import os
#input
MSG=os.sys.argv[1].upper()
#validacion de datos
MSG_invalido=( MSG!= "AEIOU" and MSG != "EAIOU" and
               MSG!= "IAEOU" and MSG != "OAEIU" and
               MSG != "UAEIO" )
while(MSG_invalido):
    MSG=input("ingrese mensaje correcto:")
    MSG_invalido = (MSG != "AEIOU" and MSG != "EAIOU" and
                    MSG != "IAEOU" and MSG != "OAEIU" and
                    MSG != "UAEIO")
#proccesing
letra=0
#bucle
for letra in MSG:
 if letra == "A":
    print("Hola")
 if letra == "E":
    print("¿Como estas?")
 if letra == "I":
    print("Te extraño")
 if letra == "O":
    print("Cuidate")
 if letra == "U":
    print("Adios")
#fin_iterador
print("\n")
print("Fin del bucle")
