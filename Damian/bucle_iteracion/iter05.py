import os
#decodificador del lel lenguaje xyzxyzxyz
#x = mi curso
#y = favorito
#z = es programacion

#input
frase_ciclo=os.sys.argv[1]

#validador del dato
frase_ciclo_invalido=(frase_ciclo!="xyzxyzxyz")

while(frase_ciclo_invalido):
    frase_ciclo=input("ingrese el valor de correcto del decodificador:")
    frase_ciclo_invalido=(frase_ciclo!="xyzxyzxyz")

#iterar frase_ciclo
#processing
for letra in frase_ciclo:
    if letra == "x":
        print("mi curso ")
    if letra == "y":
        print("favorito ")
    if letra == "z":
        print("es Programacion")

#fin_iterar
print("find del bucle")

#output
print("el valor de frace del ciclo es:", frase_ciclo)
