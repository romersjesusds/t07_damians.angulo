import os
#imprimir la resta de los numeros positivos [0,2]

#input
y=float(os.sys.argv[1])
i=0

#validador del dato
y_invalido=(y<0 or y>2)

while(y_invalido):
    y=int(input("digite el valor correcto de y:"))
    y_invalido=(y<0 or y>2)

#processing
resta=0

while(i<=y):
    resta -=i
    i +=0.1

#fin_while
print("la resta es igual a:", resta)

#output
print("el valor de y es:", y)
