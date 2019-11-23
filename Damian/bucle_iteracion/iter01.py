import  os
#input
abecedario=os.sys.argv[1]

#validador del dato
abecedario_invalido=(abecedario!="abcdefghijklmnopqrstuvwxyz")

while(abecedario_invalido):
    abecedario=input("ingrese el abecedario correcto:")
    abecedario_invalido=(abecedario!="abcdefghijklmnopqrstuvwxyz")

#processing
for letra in abecedario:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("abecedario: ", abecedario)
