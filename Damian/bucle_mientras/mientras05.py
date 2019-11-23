import os
#declarar las variables
cliente,empresa_azucarera,quintales_azucar,precio_quintal="","",0.0,0.0


#input
cliente=os.sys.argv[1]
empresa_azucarera=os.sys.argv[2]
quintales_azucar=int(os.sys.argv[3])
precio_quintal=float(os.sys.argv[4])

#validador de datos
cliente_incorrect=(cliente!="luis")
azucarera_incorrecta=(empresa_azucarera!="pomalca" and empresa_azucarera!="tuman" and empresa_azucarera!="pucala")
quintales_incorrect=(quintales_azucar<0)
precio_quintal_incorrect=(precio_quintal<0)

#mientras lo sdatos ingresados sean incorrectos
while(cliente_incorrect):
    cliente=input("ingresar cliente correcto:")
    cliente_incorrect=(cliente!="luis")

while(azucarera_incorrecta):
    empresa_azucarera=input("ingrese nombre azucarera correcta:")
    azucarera_incorrecta=(empresa_azucarera!="pomalca" and empresa_azucarera!="tuman" and empresa_azucarera!="pucala")

while(quintales_incorrect):
    quintales_azucar=int(input("ingresar los quintales de azucar correctos:"))
    quintales_incorrect=(quintales_azucar<0)

while(precio_quintal_incorrect):
    precio_quintal=float(input("ingresar elprecio correcto de cada quintal:"))
    precio_quintal_incorrect=(precio_quintal<0)

#fin_while
print("fin del bucle")

#processing
total=quintales_azucar*precio_quintal
igv=total*0.18
total_pagar=total+igv


#output
print("#############################################################")
print("#           AZUCAR       POMALCA		           #")
print("#############################################################")
print("cliente:", cliente          ,"empresa azucarera:", empresa_azucarera)
print("#############################################################")
print("#")
print("#item:", quintales_azucar, "quintales de azucar")
print("#P.U.:", precio_quintal)
print("#total:", total)
print("#IGV:", igv)
print("total a pagar:", total_pagar)
print("#############################################################")
