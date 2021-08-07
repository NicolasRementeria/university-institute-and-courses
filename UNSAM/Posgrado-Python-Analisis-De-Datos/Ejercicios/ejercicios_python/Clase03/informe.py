
# Ejercicio 3.11: Contadores

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/03_Contadores.md#ejercicio-311-contadores

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


# path_camion = '../Data/camion.csv'
# path_precios_venta = '../Data/precios.csv'
# 
# camion = leer_camion(path_camion)
# 
# costo_de_camion = costo_camion(path_camion)
# 
# recaudacion = 0
# for producto in camion:
#     recaudacion += buscar_precio(producto["nombre"]) * producto["cajones"]
# 
# 
# diferencia = recaudacion - costo_de_camion
# 
# mensaje = f"Costo de Camion: {costo_de_camion} | Recaudacion: {recaudacion} | Ganancia: {diferencia:.2f}"
# 
# print(mensaje)


########


camion = leer_camion('../Data/camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias)

# Output:

# Counter({'Mandarina': 250, 'Naranja': 150, 'Caqui': 150, 'Lima': 100, 'Durazno': 95})

print(tenencias["Naranja"])

# Output:

# 150

print(tenencias.most_common(3))

# Output:

# [('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)]

###

# Carguemos los datos de otro camión con cajones de fruta en un nuevo contador:

camion2 = leer_camion("../Data/camion2.csv")

tenencias2 = Counter()

for s in camion2:
    tenencias2[s["nombre"]] += s["cajones"]

print(tenencias2)

# Output:

# Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})

##### Y finalmente combinemos las tenencias de ambos camiones con una operación simple:

combinada = tenencias + tenencias2

print(combinada)

# Output:

# Counter({'Mandarina': 275, 'Frambuesa': 250, 'Durazno': 220, 'Lima': 150, 'Naranja': 150, 'Caqui': 150})
