import os
#declarar las variables
usuario,operadora,gigas_usadas,costo_giga="","",0.0,0.0

#input
usuario=os.sys.argv[1]
operadora=os.sys.argv[2]
gigas_usadas=int(os.sys.argv[3])
costo_giga=float(os.sys.argv[4])

#validador de datos
usuario_falso=(usuario!="juan")
operadora_incorrecta=(operadora!="bitel" and operadora!="claro" and operadora!="movistar" and operadora!="entel")
gigas_usadas_incorrectas=(gigas_usadas<0)
costo_giga_incorrecta=(costo_giga<0)

#mientras los valores usados sean incorrectos
while(usuario_falso):
    usuario=input("ingresar el usuario correcto:")
    usuario_falso=(usuario!="juan")

while(operadora_incorrecta):
    operadora=input("ingresar operadora correcta:")
    operadora_incorrecta=(operadora!="bitel" and operadora!="claro" and operadora!="movistar" and operadora!="entel")

while(gigas_usadas_incorrectas):
    gigas_usadas=int(input("ingresar gigas usadas correcta:"))
    gigas_usadas_incorrectas=(gigas_usadas<0)

while(costo_giga_incorrecta):
    costo_giga=float(input("ingresar el costo correcto:"))
    costo_giga_incorrecta=(costo_giga<0)

#fin_while
print("fin del bucle")

#processing
total=gigas_usadas*costo_giga
igv=total*0.18
total_pagar=total+igv
gigas_limite=(gigas_usadas>50)

#output
print("#############################################################")
print("#	BITEL- TELEFONIA DE TODOS			                   #")
print("#############################################################")
print("cliente:", usuario,             "operadora:", operadora)
print("#############################################################")
print("#")
print("#gigas usadas:", gigas_usadas)
print("#costo por giga:", costo_giga)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")
