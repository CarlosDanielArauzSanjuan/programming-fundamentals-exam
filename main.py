# 4. Desarrolle el código fuente de un programa que permita ingresar y 
# leer el valor correspondiente a una distancia en metros y la visualice expresadas en km.                                                 REQUEST
# 1 kilómetro es igual a 1000 metros, así que simplemente divides la cantidad de metros entre 1000 para obtener el valor en kilómetros.

print(f""" 
convertidor de metros a kilometros \n """)

meters = float(input("ingrese la cantidad en metros:   "))

print(f"""
    {meters} 'metro(s)', equivale(n) a :{meters/1000} 'kilometro(s)' "

    {meters} m. = {meters/1000} km.
""")