# 2. Desarrolle el código fuente de un programa que permita calcular el área de un triángulo equilátero, 
# adicional visualizar `"DATOS NO VÁLIDOS"`, si el área es mayor a 1000.
#   La fórmula para calcular el área `A` de un triángulo equilátero de lado `a` es: ( raizQUAD(3) / 4 )* (a**2)

import math # call math fuction


base = float (input("ingrese la medida del lado 'a' del triangulo  :"))
area = ((math.sqrt(3) / 4 ) * math.pow(base,2))
if area > 1000:
    print(f""" 
    DATOS NO VÁLIDOS
    """)
else: 
    print(f""" 
    el area del triangulo es :{area}
    """)