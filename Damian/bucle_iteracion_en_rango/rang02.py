import os
#imprimir los 10 primeros numeros naturales elevados al cuadrado

#input
n=int(os.sys.argv[1])
i=0

#validador de datos
n_invalido=(n!=10)

while(n_invalido):
    n=int(input("ingresar el numero correcto:"))
    n_invalido=(n!=10)

#processing
for i in range(n):
    print(i**2)

#fin_iterador_en_rango

print("Fin del bucle")

#output
print("el velor de n es:", n)
