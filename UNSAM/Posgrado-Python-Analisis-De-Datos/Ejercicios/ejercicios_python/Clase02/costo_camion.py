# costo_camion.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/01_Archivos.md#ejercicio-22-lectura-de-un-archivo-de-datos

# Ejercicio 2.2

# Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple con los datos leídos.
# 
# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, 
# y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
# lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
# 
# Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo como punto flotante, usá float(s).
# 
# Tu programa debería imprimir una salida como la siguiente:
# 
# Costo total 47671.15




# costo_total = 0
# 
# raw_file = open("../Data/camion.csv", "r")
# file_content = raw_file.read().split('\n')[1:-1]
# for item in file_content:
#     fila = item.split(",")
#     nombre_item = fila[0]
#     cajones_item = int(fila[1])
#     precio_item = float(fila[2])
#     costo_total += cajones_item * precio_item
# raw_file.close()

# print("Costo total", costo_total)





# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/02_Funciones.md#ejercicio-26-transformar-un-script-en-una-funci%C3%B3n

# Ejercicio 2.6

# Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) en una función costo_camion(nombre_archivo). 
# Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la 
# carga de frutas como una variable de punto flotante.
# 
# Para usar tu función, cambiá el programa de forma que se parezca a esto:
# 
# def costo_camion(nombre_archivo):
#     ...
#     # Tu código
#     ...
# 
# costo = costo_camion('../Data/camion.csv')
# print('Costo total:', costo)
# 
# Cuando ejecutás tu programa, deberías ver la misma salida impresa que antes. Una vez que lo hayas corrido, podés llamar interactivamente a la función escribiendo esto:
# 
# bash $ python3 -i costo_camion.py
# 
# Esto va a ejecutar el código en el programa y dejar abierto el intérprete interactivo.
# 
# >>> costo_camion('Data/camion.csv')
# 47671.15
# >>>
#
#Es útil para testear y debuguear poder interactuar interactivamente con tu código.




# def costo_camion(csv_file):
#     costo_total = 0
#     raw_file = open(csv_file, "r")
#     file_content = raw_file.read().split('\n')[1:-1]
#     for item in file_content:
#         fila = item.split(",")
#         nombre_item = fila[0]
#         cajones_item = int(fila[1])
#         precio_item = float(fila[2])
#         costo_total += cajones_item * precio_item
#     raw_file.close()
#     return costo_total
# 
# costo = costo_camion('../Data/camion.csv')
# print('Costo total:', costo)




########################

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/02_Funciones.md#ejercicio-29-funciones-de-la-biblioteca

# Ejercicio 2.9

# Python viene con una gran biblioteca estándar de funciones útiles. En este caso el módulo csv podría venirnos muy bien. 
# Podés usarlo cada vez que tengas que leer archivos CSV. Acá va un ejemplo de cómo funciona.
# 
# >>> import csv
# >>> f = open('Data/camion.csv')
# >>> rows = csv.reader(f)
# >>> headers = next(rows)
# >>> headers
# ['nombre', 'cajones', 'precio']
# >>> for row in rows:
#         print(row)
# 
# ['Lima', '100', '32.2']
# ['Naranja', '50', '91.1']
# ['Caqui', '150', '103.44']
# ['Mandarina', '200', '51.23']
# ['Durazno', '95', '40.37']
# ['Mandarina', '50', '65.1']
# ['Naranja', '100', '70.44']
# >>> f.close()
# >>>
# 
# Una cosa buena que tiene el módulo csv es que maneja solo una gran variedad de detalles de bajo nivel como el problema 
# de las comillas, o la separación con comas de los datos. En la salida del último ejemplo podés ver que el lector ya sacó 
# las comillas dobles de los nombres de las frutas de la primera columna.
# 
# Modificá tu programa costo_camion.py para que use el módulo csv para leer los archivos CSV y probalo en un par de los ejemplos anteriores.
import csv

def costo_camion(csv_file):
    costo_total = 0
    raw_file = open(csv_file, "r")
    file_content = csv.reader(raw_file)
    next(file_content) # Remove first item of csv, that will remove the headers
    for item in file_content:
        cajones_item = int(item[1])
        precio_item = float(item[2])
        costo_total += cajones_item * precio_item
    raw_file.close()
    return costo_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
