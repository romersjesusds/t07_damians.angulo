import os
temp=int(os.sys.argv[1])
# Validar la temperatura (37 - 40)
temp_invalida=(temp < 37 or temp > 40)
while (temp_invalida==True):
    temp=int(input("Ingrese temperatura (37-40):"))
    temp_invalida =(temp < 37 or temp > 40)
print("Temperatura:", temp)
if(temp==37):
  print("Normal")
if(temp==38):
  print("fiebre")
if(temp==39):
  print("fiebre alta")
if(temp==40):
  print("riesgo de convulsion")
