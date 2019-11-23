import os
#imprimir la suma de los cuadrados de los numeros del intervalo [0,10]

#input
numero=int(os.sys.argv[1])
i=0

#validador de los datos
interv_no_permitido=(numero<0 or numero>10)

while(interv_no_permitido):
        numero=int(input("ingresar un numero del intervalo permitido:"))
        interv_no_permitido=(numero<0 or numero>10)

#processing
suma_cuadrados=0

while(i<=numero):
        suma_cuadrados +=i*i
        i +=1

#fin_while
print("la suma de los cuadrados es igual a:", suma_cuadrados)

#output
print("el numero es: ", numero)
