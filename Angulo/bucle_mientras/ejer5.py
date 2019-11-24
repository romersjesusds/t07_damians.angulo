import os
mes=(os.sys.argv[1]).lower()
mes_invalida=(mes != "enero" and mes != "febrero" and
              mes != "marzo" and mes != "abril" and
              mes != "mayo" and mes != "junio" and
              mes != "julio" and mes != "agosto" and
              mes != "setiembre" and mes != "ocubre" and
              mes != "noviembre" and mes != "diciembre")
while(mes_invalida==True):
    mes=input("Ingrese el mes: ").lower()
    mes_invalida = (mes != "enero" and mes != "febrero" and
                    mes != "marzo" and mes != "abril" and
                    mes != "mayo" and mes != "junio" and
                    mes != "julio" and mes != "agosto" and
                    mes != "setiembre" and mes != "ocubre" and
                    mes != "noviembre" and mes != "diciembre")
#fin_while
print("mes:",mes)
