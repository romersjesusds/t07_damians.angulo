import os
#imprimir la suma de los cubos de los numeros del intervalo [0,100]

#input
n=int(os.sys.argv[1])
i=0

#validador de dato
n_invalido=(n<0 or n>100)

while(n_invalido):
    n=int(input("digite el valor correcto de n:"))
    n_invalido=(n<0 or n>100)

#processing
suma_cubos=0

while(i<=n):
    suma_cubos +=i*i*i
    i +=1

#fin_while
print("la suma de los cubos es igual a:", suma_cubos)

#output
print("el valor de n es:", n)
