import os
#declarar las variables
cliente,vendedor,kg_papas,precio_kg="","",0.0,0.0
total_pagar=False

#input
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
kg_papas=int(os.sys.argv[3])
precio_kg=float(os.sys.argv[4])

#validador de datos
cliente_incorrect=(cliente!="jesus")
vendedor_incorrect=(vendedor!="omar")
kg_papas_incorect=(kg_papas<0)
precio_kg_incorect=(precio_kg<0)

#mientras los datos ingresados sean incorrectos ingresar de nuevo
while(cliente_incorrect):
    cliente=input("ingresar cliente correcto:")
    cliente_incorrect=(cliente!="jesus")

while(vendedor_incorrect):
    vendedor=input("ingresar el vendedor correcto:")
    vendedor_incorrect=(vendedor!="omar")

while(kg_papas_incorect):
    kg_papas=int(input("ingresar los kg de papas correctos:"))
    kg_papas_incorect=(kg_papas<0)

while(precio_kg_incorect):
    precio_kg=float(input("ingresar el precio correcto:"))
    precio_kg_incorect=(precio_kg<0)

#fin_while
print("fin del bucle")

#processing
consumo_total=kg_papas*precio_kg
igv=consumo_total*0.18
total_pagar=consumo_total+igv


#output
print("#############################################################")
print("#	BODEGA  -       MI FERNANDITO			    #")
print("#############################################################")
print("cliente:", cliente,    "     vendedor:", vendedor)
print("#############################################################")
print("#")
print("#item:", kg_papas, "kg de papas")
print("#Precio por kg: s/.", precio_kg)
print("#consumo: s/.", consumo_total)
print("#IGV: s/.", igv)
print("total a pagar: s/.", total_pagar)
print("#############################################################")
