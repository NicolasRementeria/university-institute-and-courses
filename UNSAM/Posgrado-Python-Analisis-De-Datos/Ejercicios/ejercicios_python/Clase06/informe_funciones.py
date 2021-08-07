#%%
# Ejercicio 6.4: Estructurar un programa como una colección de funciones

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/02_Scripts.md#ejercicio-64-estructurar-un-programa-como-una-colecci%C3%B3n-de-funciones

# import csv
# 
# def leer_camion(nombre_archivo):
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         contenido_camion = []
#         for n_row, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             try:
#                 contenido_camion.append({'nombre': record['nombre'], 'cajones': int(
#                     record['cajones']), 'precio': float(record['precio'])})
#             except ValueError:
#                 print(f'Fila {n_row}: No pude interpretar: {row}')
#     return contenido_camion
# 
# def leer_precios(nombre_archivo):
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         lista_precios = {}
#         for n_row, row in enumerate(rows, start=1):
#             try:
#                 nombre = row[0]
#                 try:
#                     precio = float(row[1])
#                 except:
#                     print(f'el precio de la fila {n_row} es inválido.')
#             except:
#                 print(f'nombre vacío en la fila {n_row}')
#             lista_precios[nombre] = precio
#         return lista_precios
# 
# def hacer_informe(carga, precios):
#     informe = []
#     for registro in carga:
#         cambio = precios[registro['nombre']]-registro['precio']
#         tupla = (registro['nombre'], registro['cajones'], registro['precio'], cambio)
#         informe.append(tupla)
#     return informe
# 
# def imprimir_informe(informe):
#     headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in informe:
#         print('%10s %10d %10.2f %10.2f' % row)
# 
# 
# 
# camion = leer_camion('../Data/camion.csv')
# precios = leer_precios('../Data/precios.csv')
# informe = hacer_informe(camion, precios)
# 
# imprimir_informe(informe)

#%%

# Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/02_Scripts.md#ejercicio-65-crear-una-funci%C3%B3n-de-alto-nivel-para-la-ejecuci%C3%B3n-del-programa

# import csv
# 
# def leer_camion(nombre_archivo):
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         contenido_camion = []
#         for n_row, row in enumerate(rows, start=1):
#             record = dict(zip(headers, row))
#             try:
#                 contenido_camion.append({'nombre': record['nombre'], 'cajones': int(
#                     record['cajones']), 'precio': float(record['precio'])})
#             except ValueError:
#                 print(f'Fila {n_row}: No pude interpretar: {row}')
#     return contenido_camion
# 
# def leer_precios(nombre_archivo):
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         lista_precios = {}
#         for n_row, row in enumerate(rows, start=1):
#             try:
#                 nombre = row[0]
#                 try:
#                     precio = float(row[1])
#                 except:
#                     print(f'el precio de la fila {n_row} es inválido.')
#             except:
#                 print(f'nombre vacío en la fila {n_row}')
#             lista_precios[nombre] = precio
#         return lista_precios
# 
# def hacer_informe(carga, precios):
#     informe = []
#     for registro in carga:
#         cambio = precios[registro['nombre']]-registro['precio']
#         tupla = (registro['nombre'], registro['cajones'], registro['precio'], cambio)
#         informe.append(tupla)
#     return informe
# 
# def imprimir_informe(informe):
#     headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
#     print('%10s %10s %10s %10s' % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in informe:
#         print('%10s %10d %10.2f %10.2f' % row)
# 
# def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
#     camion = leer_camion(nombre_archivo_camion)
#     precios = leer_precios(nombre_archivo_precios)
#     informe = hacer_informe(camion, precios)
#     imprimir_informe(informe)
# 
# informe_camion('../Data/camion.csv', '../Data/precios.csv')
# 
# # informe_camion('../Data/camion2.csv', '../Data/precios.csv')
# # 
# # files = ['../Data/camion.csv', '../Data/camion2.csv']
# # for name in files:
# #     print(f'{name:-^43s}')
# #     informe_camion(name, '../Data/precios.csv')
# #     print()


# %%

# Ejercicio 6.11: Usemos tu módulo

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/04_Modulos.md#ejercicio-611-usemos-tu-m%C3%B3dulo


import csv
import fileparse

def leer_camion(nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, types=[str, int, float])

def leer_precios(nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, types=[str, float], has_headers=False)

def hacer_informe(carga, precios):
    informe = []
    for registro in carga:
        #cambio = precios[registro['nombre']]-registro['precio']
        cambio = dict(precios)[registro["nombre"]] - registro["precio"]
        tupla = (registro['nombre'], registro['cajones'], registro['precio'], cambio)
        informe.append(tupla)
    return informe

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

# informe_camion('../Data/camion.csv', '../Data/precios.csv')
