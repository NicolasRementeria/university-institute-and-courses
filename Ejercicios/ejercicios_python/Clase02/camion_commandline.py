# camion_commandline.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/02_Funciones.md#ejercicio-210-ejecuci%C3%B3n-desde-la-l%C3%ADnea-de-comandos-con-par%C3%A1metros

# Ejercicio 2.10

# En el programa costo_camion.py, el nombre del archivo de entrada '../Data/camion.csv' fue escrito en el código.
# # costo_camion.py
# import csv
# 
# def costo_camion(nombre_archivo):
#     ...
#     # Tu código
#     ...
# 
# costo = costo_camion('../Data/camion.csv')
# print('Costo total:', costo)
# 
# Esto está bien para ejercitar, pero en un programa real probablemente no harías eso ya que querrías una mayor 
# flexibilidad. Una posibilidad es pasarle al programa el nombre del archivo que querés procesar como un parámetro 
# cuando lo llamás desde la línea de comandos.
# 
# Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de 
# parámetros por línea de comando según la sugerencia del siguiente ejemplo:
# 
# # camion_commandline.py
# import csv
# import sys
# 
# def costo_camion(nombre_archivo):
#     ...
#     # Tu código
#     ...
# 
# if len(sys.argv) == 2:
#     nombre_archivo = sys.argv[1]
# else:
#     nombre_archivo = '../Data/camion.csv'
# 
# costo = costo_camion(nombre_archivo)
# print('Costo total:', costo)
# 
# sys.argv es una lista que contiene los argumentos que le pasamos al script al momento de llamarlo desde la línea 
# de comandos (si es que le pasamos alguno). Por ejemplo, desde una terminal de Unix (en Windows es similar), 
# para correr nuestro programa y que procese el mismo archivo podríamos escribir:
# 
# bash $ python3 camion_commandline.py ../Data/camion.csv
# Costo total: 47671.15
# bash $
# 
# O con el archivo missing.csv:
# 
# bash $ python3 camion_commandline.py ../Data/missing.csv
# ...
# Costo total: 30381.15
# bash $
# 
# Si no le pasamos ningún archivo, va a mostrar el resultado para camion.csv porque lo indicamos con la línea nombre_archivo = '../Data/camion.csv'.


import csv
import sys

def costo_camion(csv_file):
    costo_total = 0
    raw_file = open(csv_file, "r")
    file_content = csv.reader(raw_file)
    next(file_content) # Remove first item of csv, that will remove the headers
    for item in file_content:
        cajones_item = item[1]
        if cajones_item == "":
            cajones_item = 0
        else:
            cajones_item = float(cajones_item)
        precio_item = float(item[2])
        costo_total += cajones_item * precio_item
    raw_file.close()
    return costo_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

# Output:

# $ python camion_commandline.py ../Data/missing.csv
 #Costo total: 30381.15