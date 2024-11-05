# Ejercicios por realizar
#1. Desarrolle el código fuente de un programa que permita ingresar cinco voltajes, 
# obtener su promedio y visualizar `"ALTO VOLTAJE"`, si su promedio es mayor a 220, caso contrario sea menor mostrar `"VOLTAJE CORRECTO"`.
   
print ("CALCULAR VOLTAJE")
n1 =float(input("ingrese el voltaje 1  :"))
n2 =float(input("ingrese el voltaje 2  :"))
n3 = float(input("ingrese el voltaje 3  :"))
n4 = float(input("ingrese el voltaje 4  :"))
n5 = float(input("ingrese el voltaje 5  :"))
vol= (n1+n2+n3+n4+n5)/5
if vol>220 :
    print(" ALTO VOLTAJE")
else  :
    print("VOLTAJE CORRECTO")