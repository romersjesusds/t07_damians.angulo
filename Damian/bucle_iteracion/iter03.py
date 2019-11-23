import os
#iterar la cadena mi nombre

#input
Mi_nombre=os.sys.argv[1]

#validador del dato
Mi_nombre_incorrecto=(Mi_nombre!="Romers Jesus Damian Suclupe")
while(Mi_nombre_incorrecto):
    Mi_nombre=input("ingresar mi nombre correcto:")
    Mi_nombre_incorrecto=(Mi_nombre!="Romers Jesus Damian Suclupe")

#processing
for letra in Mi_nombre:
    print(letra)

#fin_iterar
print("fin del bucle")

#output
print("Mi nombre es: ", Mi_nombre)
