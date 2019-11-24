#impresion de fecha de nacimiento
import os
dia=int(os.sys.argv[1])
mes=(os.sys.argv[2]).lower()
año=int(os.sys.argv[3])
dia_invalido=(dia<1 or dia>30)
mes_invalido=(mes != "enero" and mes != "febrero" and
              mes != "marzo" and mes != "abril" and
              mes != "mayo" and mes != "junio" and
              mes != "julio" and mes != "agosto" and
              mes != "setiembre" and mes != "ocubre" and
              mes != "noviembre" and mes != "diciembre")

año_invalido=(año<2000 or año>2020)
while(dia_invalido==True):
    dia=int(input("ingrese dia correcto:"))
    dia_invalido = (x < 1 or x > 30)
while(mes_invalido==True):
    mes=int(input("ingrese numero de mes correcto :")).lower()
    mes_invalido = (mes != "enero" and mes != "febrero" and
                    mes != "marzo" and mes != "abril" and
                    mes != "mayo" and mes != "junio" and
                    mes != "julio" and mes != "agosto" and
                    mes != "setiembre" and mes != "ocubre" and
                    mes != "noviembre" and mes != "diciembre")

while(año_invalido==True):
    año=int(input("ingrese año correcto:"))
    año_invalido = (año < 2002 or año > 2020)
coleccion={"dia":dia,"mes":mes,"año":año}
for i in coleccion:
   print(coleccion[i])
