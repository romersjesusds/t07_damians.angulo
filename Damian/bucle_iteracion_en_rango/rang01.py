import os
#imprimir los numeros positivos menores o iguales a 100

#input
n=int(os.sys.argv[1])
i=0

#validaor de las variables
n_invalido=(n!=100)

while(n_invalido):
    n=int(input("ingresar el numero de rango correcto:"))
    n_invalido=(n!=100)

#processing
for i in range(n):
    print(i+1)

#fin_iterador_en_rango

print("Fin del bucle")

#output
print("el valor de n es:", n)
