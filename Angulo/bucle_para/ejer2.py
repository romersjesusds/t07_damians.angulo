# Decodificar mensaje encriptado
# X= TE QUIERO
# C = MUCHO
# V = BEBE
# B = CUIDATE
import os
#input
MSG=os.sys.argv[1].upper()
#validacion de datos
MSG_invalido=( MSG!= "XCVB" and MSG != "BXCV" and
               MSG!= "VBXC" and MSG != "BVXC" and
               MSG != "VBXC" and MSG !="XCBV" and MSG !="VXBC"
               and MSG!="XVBC")
while(MSG_invalido):
    MSG=input("ingrese mensaje correcto:")
    MSG_invalido = (MSG != "XCVB" and MSG != "BXCV" and
                    MSG != "VBXC" and MSG != "BVXC" and
                    MSG != "VBXC" and MSG != "XCBV" and MSG != "VXBC"
                    and MSG != "XVBC")
#proccesing
letra=0
#bucle
for letra in MSG:
 if letra == "X":
    print("TE QUIERO")
 if letra == "C":
    print("MUCHO")
 if letra == "V":
    print("BEBE")
 if letra == "B":
    print("CUIDATE")
#fin_iterador
print("\n")
print("Fin del bucle")
