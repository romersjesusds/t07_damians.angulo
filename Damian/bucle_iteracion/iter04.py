import os
#iterar la cadena nombre del curso

#input
nombre_curso=os.sys.argv[1]

#validador de los datos
nombre_curso_invalido=(nombre_curso!="Programacion I")

while(nombre_curso_invalido):
    nombre_curso=input("ingresar el nombre del curso correcto:")
    nombre_curso_invalido=(nombre_curso!="Programacion I")

#processing
for letra in nombre_curso:
    print(letra)

#fin_iterar
print("fin del bucle")

#output
print("el nombre del curso es:", nombre_curso)
