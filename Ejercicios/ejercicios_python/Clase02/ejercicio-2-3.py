# ejercicio-2-3.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/01_Archivos.md#ejercicio-23-precio-de-la-naranja

# Ejercicio 2.3

# El archivo Data/precios.csv contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:
# 
# "Lima",40.22
# "Uva",24.85
# "Ciruela",44.85
# "Cereza",11.27
# "Frutilla",53.72
# ...
# 
# Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.
# 
# >>> f = open('../Data/precios.csv', 'rt')
# ...
# >>> f.close()
# 
# El precio de la naranja es:  106.28

import csv

csv_file = open('../Data/precios.csv', 'rt')

csv_content = csv.reader(csv_file)

precio = 0

for item in csv_content:
    nombre_csv = item[0]
    precio_csv = item[1]
    if nombre_csv == "Naranja":
        precio = precio_csv

csv_file.close()

print("El precio de la naranja es:", precio)

# Output:

# El precio de la naranja es: 106.28