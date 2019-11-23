import os
#imprimir el producto de los numeros positivos <=y

#input
y=int(os.sys.argv[1])
i=1

#validador del dato
y_invalido=(y<0 or y>50)

while(y_invalido):
    y=int(input("digite correctamente el valor y:"))
    y_invalido=(y<0 or y>50)

#processing
producto=1

while(i<=y):
    producto *=i
    i +=1

#fin_while
print("el producto es igual a:", producto)

#output
print("el valor de y es:", y)
