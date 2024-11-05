#3. Desarrolle un programa que solicite ingrese tres voltajes distintos e indique 
# si el promedio de los voltajes ingresados es menor a 115 visualice `"VOLTAJE CORRECTO"`, REQUEST|1
# caso contrario sea mayor a 115 y menor a 220 visualice `"ALTO VOLTAJE"`,                 REQUEST|2
#  y si es mayor a 220 visualice `"PELIGRO"`                                               REQUEST|3

first =float(input("ingrese el voltaje 1  :"))
second =float(input("ingrese el voltaje 2  :"))
third = float(input("ingrese el voltaje 3  :"))
speed = ((first+second+third )/ 3)
if speed < 115:                                 #REQUEST 1
    print("VOLTAJE CORRECTO")     
else:
    if 115< speed < 220:                        #REQUEST 2
        print("ALTO VOLTAJE")
    elif speed >220 :                           #REQUEST 3
         print("PELIGRO") 