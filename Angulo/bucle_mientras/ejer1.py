# Mostrar mensaje "Desea continuar" si o no ?
import os
rpta=os.sys.argv[1]
rpta_invalida=(rpta!="si" and rpta!="no")
while(rpta_invalida==True):
    rpta=input("Desea continuar:")
    rpta_invalida=(rpta != "si" and rpta != "no")
#fin_while
print("La respuesta es :", rpta)
print("Fin del bucle")
