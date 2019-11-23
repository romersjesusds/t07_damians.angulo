import os
#imprimir los 20 primeros numeros naturales elevados al cubo

#input
n=int(os.sys.argv[1])
i=0

#validador de datos
n_invalido=(n!=20)

while(n_invalido):
    n=int(input("ingrese el valor correcto:"))
    n_invalidon_invalido=(n!=20)

#processing
for i in range(n):
    print(i**3)

#fin_iterador_en_rango

print("Fin del bucle")

#output
print("el valor de n es:", n)
