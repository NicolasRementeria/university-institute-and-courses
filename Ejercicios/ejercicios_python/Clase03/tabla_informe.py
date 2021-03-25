
# tabla_informe.py

# Ejercicio 3.13: 

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/05_Formato.md#ejercicio-313-recolectar-datos

# import csv
# from pprint import pprint
#  
# def leer_camion(nombre_archivo):
#     diccionario_camion = []
#     with open(nombre_archivo, 'rt', encoding="utf-8") as raw_file:
#         csv_content = csv.reader(raw_file)
#         next(csv_content)
#         for item in csv_content:
#              nombre = item[0]
#              numero_cajones = int(item[1])
#              precio = float(item[2])
#              diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
#              diccionario_camion.append(diccionario_item)
#     return diccionario_camion
# 
# def leer_precios(nombre_archivo):
#     diccionario_precios = {}
#     with open(nombre_archivo, "rt", encoding="utf-8") as csv_file:
#         csv_content = csv.reader(csv_file)
#         for item in csv_content:
#             try:
#                 nombre = item[0]
#                 precio = float(item[1])
#                 diccionario_precios[nombre] = precio
#             except:
#                 continue
#     return diccionario_precios
# 
# def costo_camion(csv_file):
#     costo_total = 0
#     raw_file = open(csv_file, "r")
#     file_content = csv.reader(raw_file)
#     next(file_content) # Remove first item of csv, that will remove the headers
#     for item in file_content:
#         cajones_item = int(item[1])
#         precio_item = float(item[2])
#         costo_total += cajones_item * precio_item
#     raw_file.close()
#     return costo_total
# 
# def buscar_precio(fruta):
#     precio = 0
#     with open('../Data/precios.csv', 'r') as csv_file:
#         csv_content = csv.reader(csv_file)
#         for item in csv_content:
#             nombre_csv = item[0]
#             precio_csv = item[1]
#             if nombre_csv == fruta:
#                 precio = precio_csv
#         return float(precio)
# 
# 
# def hacer_informe(lista_cajones, dicc_precios):
#     # Nombre, Cajones, Precio, Cambio
#     # ('Lima', 100, 32.2, 8.019999999999996)
#     informe = []
#     for item in lista_cajones:
#         nombre = item["nombre"]
#         cajones = item["cajones"]
#         precio = dicc_precios[nombre]
#         cambio = precio - item["precio"]
#         tupla_item = (nombre, cajones, precio, cambio)
#         informe.append(tupla_item)
#     return informe
# 
# 
# dicc_precios = leer_precios("../Data/precios.csv")
# camion = leer_camion("../Data/camion.csv")
# informe = hacer_informe(lista_cajones=camion, dicc_precios=dicc_precios)
# 
# for r in informe:
#     print(r)

# Output:

# ('Lima', 100, 40.22, 8.019999999999996)
# ('Naranja', 50, 106.28, 15.180000000000007)
# ('Caqui', 150, 105.46, 2.019999999999996)
# ('Mandarina', 200, 80.89, 29.660000000000004)
# ('Durazno', 95, 73.48, 33.11000000000001)
# ('Mandarina', 50, 80.89, 15.790000000000006)
# ('Naranja', 100, 106.28, 35.84)

#### Ejercicio 3.14

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/05_Formato.md#ejercicio-314-imprimir-una-tabla-con-formato

# import csv
# from pprint import pprint
#  
# def leer_camion(nombre_archivo):
#     diccionario_camion = []
#     with open(nombre_archivo, 'rt', encoding="utf-8") as raw_file:
#         csv_content = csv.reader(raw_file)
#         next(csv_content)
#         for item in csv_content:
#              nombre = item[0]
#              numero_cajones = int(item[1])
#              precio = float(item[2])
#              diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
#              diccionario_camion.append(diccionario_item)
#     return diccionario_camion
# 
# def leer_precios(nombre_archivo):
#     diccionario_precios = {}
#     with open(nombre_archivo, "rt", encoding="utf-8") as csv_file:
#         csv_content = csv.reader(csv_file)
#         for item in csv_content:
#             try:
#                 nombre = item[0]
#                 precio = float(item[1])
#                 diccionario_precios[nombre] = precio
#             except:
#                 continue
#     return diccionario_precios
# 
# def costo_camion(csv_file):
#     costo_total = 0
#     raw_file = open(csv_file, "r")
#     file_content = csv.reader(raw_file)
#     next(file_content) # Remove first item of csv, that will remove the headers
#     for item in file_content:
#         cajones_item = int(item[1])
#         precio_item = float(item[2])
#         costo_total += cajones_item * precio_item
#     raw_file.close()
#     return costo_total
# 
# def buscar_precio(fruta):
#     precio = 0
#     with open('../Data/precios.csv', 'r') as csv_file:
#         csv_content = csv.reader(csv_file)
#         for item in csv_content:
#             nombre_csv = item[0]
#             precio_csv = item[1]
#             if nombre_csv == fruta:
#                 precio = precio_csv
#         return float(precio)
# 
# 
# def hacer_informe(lista_cajones, dicc_precios):
#     # Nombre, Cajones, Precio, Cambio
#     # ('Lima', 100, 32.2, 8.019999999999996)
#     informe = []
#     for item in lista_cajones:
#         nombre = item["nombre"]
#         cajones = item["cajones"]
#         precio = item["precio"]
#         cambio = dicc_precios[nombre] - precio
#         tupla_item = (nombre, cajones, precio, cambio)
#         informe.append(tupla_item)
#     for nombre, cajones, precio, cambio in informe:
#         print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')
# 
# 
# dicc_precios = leer_precios("../Data/precios.csv")
# camion = leer_camion("../Data/camion.csv")
# hacer_informe(lista_cajones=camion, dicc_precios=dicc_precios)

# Output:

#       Lima        100      40.22       8.02
#    Naranja         50     106.28      15.18
#      Caqui        150     105.46       2.02
#  Mandarina        200      80.89      29.66
#    Durazno         95      73.48      33.11
#  Mandarina         50      80.89      15.79
#    Naranja        100     106.28      35.84

#### Ejercicio 3.15

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/05_Formato.md#ejercicio-315-agregar-encabezados

import csv
from pprint import pprint
 
def leer_camion(nombre_archivo):
    diccionario_camion = []
    with open(nombre_archivo, 'rt', encoding="utf-8") as raw_file:
        csv_content = csv.reader(raw_file)
        next(csv_content)
        for item in csv_content:
             nombre = item[0]
             numero_cajones = int(item[1])
             precio = float(item[2])
             diccionario_item = {"nombre": nombre, "precio": precio, "cajones": numero_cajones}
             diccionario_camion.append(diccionario_item)
    return diccionario_camion

def leer_precios(nombre_archivo):
    diccionario_precios = {}
    with open(nombre_archivo, "rt", encoding="utf-8") as csv_file:
        csv_content = csv.reader(csv_file)
        for item in csv_content:
            try:
                nombre = item[0]
                precio = float(item[1])
                diccionario_precios[nombre] = precio
            except:
                continue
    return diccionario_precios

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

def buscar_precio(fruta):
    precio = 0
    with open('../Data/precios.csv', 'r') as csv_file:
        csv_content = csv.reader(csv_file)
        for item in csv_content:
            nombre_csv = item[0]
            precio_csv = item[1]
            if nombre_csv == fruta:
                precio = precio_csv
        return float(precio)


def hacer_informe(lista_cajones, dicc_precios):
    # Nombre, Cajones, Precio, Cambio
    # ('Lima', 100, 32.2, 8.019999999999996)
    informe = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    for item in lista_cajones:
        nombre = item["nombre"]
        cajones = item["cajones"]
        precio = item["precio"]
        cambio = dicc_precios[nombre] - precio
        tupla_item = (nombre, cajones, precio, cambio)
        informe.append(tupla_item)
    mostrar_encabezado(headers)
    for nombre, cajones, precio, cambio in informe[1:]:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

def mostrar_encabezado(header):
    header = f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}'
    lineas = '---------- ---------- ---------- ----------'
    print(header, "\n", lineas)
    

dicc_precios = leer_precios("../Data/precios.csv")
camion = leer_camion("../Data/camion.csv")
hacer_informe(lista_cajones=camion, dicc_precios=dicc_precios)

# Output:

#     Nombre    Cajones     Precio     Cambio 
#  ---------- ---------- ---------- ----------
#    Naranja         50      91.10      15.18
#      Caqui        150     103.44       2.02
#  Mandarina        200      51.23      29.66
#    Durazno         95      40.37      33.11
#  Mandarina         50      65.10      15.79
#    Naranja        100      70.44      35.84