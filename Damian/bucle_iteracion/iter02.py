import os
#iterar la cadena nombre de mi universidad

#input
nombre_mi_universidad=os.sys.argv[1]
#validador de datos
nombre_invalido=(nombre_mi_universidad!="Universidad Nacional Pedro Ruiz Gallo")

while(nombre_invalido):
    nombre_mi_universidad=input("ingresar el verdadero nombre de mi universidad:")
    nombre_invalido=(nombre_mi_universidad!="Universidad Nacional Pedro Ruiz Gallo")

#processing
for letra in nombre_mi_universidad:
    print(letra)

#fin_iterar
print("fin del bucle")

#output
print("mi universidad se llama:", nombre_mi_universidad)
