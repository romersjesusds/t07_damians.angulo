import os
#imprimir el resultado de la division entre 3 de cada numero <20

#input
n=int(os.sys.argv[1])
i=0

#validador de dato
n_invalido=(n!=20)

while(n_invalido):
    n=int(input("ingrese el valor correcto de n:"))
    n_invalido=(n!=20)

#processing
for i in range(n):
    print(i/3)

#fin_iterador_en_rango

print("Fin del bucle")

#output
print("el valor de n es:", n)
