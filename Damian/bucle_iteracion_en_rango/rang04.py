import os
#imprimir  la lista del producto de consecutivos de a dos en el intervalo de [0,9]

#input
n=int(os.sys.argv[1])
i=0

#validador de dato
n_invalido=(n!=9)

while(n_invalido):
    n=int(input("ingrese el numero del intervalo correcto:"))
    n_invalido=(n!=9)

#processing
for i in range(n):
    print(i*(i+1))

#fin_iterador_en_rango

print("Fin del bucle")

#output
print("el valor del n es:", n)
