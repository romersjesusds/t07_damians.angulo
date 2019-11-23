import os
#imprimir la suma de los pares de los numeros del intervalo [0,100]

#input
y=int(os.sys.argv[1])
i=0

#validador del dato
y_invalido=(y<0 or y>100)

while(y_invalido):
    y=int(input("digite correctamente el valor de y:"))
    y_invalido=(y<0 or y>100)

#processing
suma_pares=0

while(i<=y):
    suma_pares +=i
    i +=2

#fin_while
print("la suma de los pares es es igual a:", suma_pares)

#output
print("el valor de y es:", y)
