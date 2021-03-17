# buscar_precios.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/02_Funciones.md#ejercicio-27-buscar-precios

# Ejercicio 2.7

# A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo 
# ../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.
# 
# >>> buscar_precio('Frambuesa')
# El precio de un cajón de Frambuesa es: 34.35
# >>> buscar_precio('Kale')
# Kale no figura en el listado de precios.

import csv

def buscar_precio(fruta):
    precio = 0
    with open('../Data/precios.csv', 'rt') as csv_file:
        csv_content = csv.reader(csv_file)
        for item in csv_content:
            nombre_csv = item[0]
            precio_csv = item[1]
            if nombre_csv == fruta:
                precio = precio_csv
        if float(precio) == 0:
            return f"{fruta} no figura en la lista de precios."
        else:
            return f"El precio de un cajón de {fruta} es: {precio}"


buscar_precio("Naranja")

# Output:

# 'El precio de un cajón de Naranja es: 106.28'

buscar_precio("Kale")

# Output:

# 'Kale no figura en la lista de precios.'
