
# Ejercicio 4.11: Reducción de secuencias

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/03_Comprension_Listas.md#ejercicio-411-reducci%C3%B3n-de-secuencias

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
    next(file_content)
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


# Calculá el costo total de la carga del camión en un solo comando.

camion = leer_camion('../Data/camion.csv')
costo = sum([ s['cajones'] * s['precio'] for s in camion ])

# costo
# 47671.15

# Luego, leyendo la variable precios, calculá también el valor en el mercado de la carga del camión usando una sola línea de código.

precios = leer_precios('../Data/precios.csv')
valor = sum([ s['cajones'] * precios[s['nombre']] for s in camion ])

###############


# Ejercicio 4.12: Consultas de datos

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/03_Comprension_Listas.md#ejercicio-412-consultas-de-datos

# Probá los siguientes ejemplos de consultas (queries) de datos.
# Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.

mas100 = [ s for s in camion if s['cajones'] > 100 ]

# >>> mas100
# [{'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
#  {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23}]

# Ahora, una con la info sobre cajones de Mandarina y Naranja.

myn = [ s for s in camion if s['nombre'] in {'Mandarina','Naranja'} ]

# >>> myn
# [{'nombre': 'Naranja', 'precio': 91.1, 'cajones': 50}, {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200}, 
# {'nombre': 'Mandarina', 'precio': 65.1, 'cajones': 50}, {'nombre': 'Naranja', 'precio': 70.44, 'cajones': 100}]

# O una con la info de las frutas que costaron más de $10000.

costo10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]

# [{'nombre': 'Caqui', 'precio': 103.44, 'cajones': 150}, {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200}]


###################

# Ejercicio 4.13: Extracción de datos

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/03_Comprension_Listas.md#ejercicio-413-extracci%C3%B3n-de-datos

# Usando un comprensión de listas, construí una lista de tuplas (nombre, cajones) que indiquen la cantidad de cajones de cada fruta tomando los datos de camion.

nombre_cajones =[ (s['nombre'], s['cajones']) for s in camion ]

# >>> nombre_cajones
# [('Lima', 100), ('Naranja', 50), ('Caqui', 150), ('Mandarina', 200), ('Durazno', 95), ('Mandarina', 50), ('Naranja', 100)]


# Si cambiás los corchetes ([,]) por llaves ({, }), obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.
# Por ejemplo, si quisieras un listado de las frutas en el camión pordías usar:

nombres = { s['nombre'] for s in camion }

# >>> nombres
# {'Mandarina', 'Lima', 'Naranja', 'Durazno', 'Caqui'}

# Si especificás pares clave:valor, podés construir un diccionario. Por ejemplo, si queremos un diccionario con el total de cada fruta en el camión podemos comenzar con

stock = { nombre: 0 for nombre in nombres }

# >>> stock
# {'Mandarina': 0, 'Lima': 0, 'Naranja': 0, 'Durazno': 0, 'Caqui': 0}

# que es una comprensión de diccionario. Y seguir sumando los cajones:

for s in camion:
    stock[s['nombre']] += s['cajones']

# >>> stock
# {'Mandarina': 250, 'Lima': 100, 'Naranja': 150, 'Durazno': 95, 'Caqui': 150}

# Otro ejemplo útil podría ser generar un diccionario de precios de venta de aquellos productos que están efectivamente cargados en el camión:

camion_precios = { nombre: precios[nombre] for nombre in nombres }

# >>> camion_precios
# {'Mandarina': 80.89, 'Lima': 40.22, 'Naranja': 106.28, 'Durazno': 73.48, 'Caqui': 105.46}

###############

# Ejercicio 4.14: Extraer datos de una archivo CSV

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/03_Comprension_Listas.md#ejercicio-414-extraer-datos-de-una-arhcivo-csv

# Saber usar combinaciones de comprensión de listas, diccionarios y conjuntos resulta útil para 
# procesar datos en diferentes contextos. Aunque puede volverse medio críptico si no estás 
# habituade. Acá te mostramos un ejemplo de cómo extraer columnas seleccionadas de un archivo 
# CSV que tiene esas características. No es dificil cuando lo entendés, pero está muy 
# concentrado todo.
# 
# Primero, leamos el encabezado (header) del archivo CSV:

import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

# >>> headers
# ['nombre', 'fecha', 'hora', 'cajones', 'precio']

# Luego, definamos una lista que tenga las columnas que nos importan:

select = ['nombre', 'cajones', 'precio']

# >>> select
# ['nombre', 'cajones', 'precio']

indices = [ headers.index(ncolumna) for ncolumna in select ]

# >>> indices 
# [0, 3, 4]

row = next(rows)
record = { ncolumna: row[index] for ncolumna, index in zip(select, indices) }   # comprensión de diccionario

# >>> record
# {'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}

# Reducir la funcion leer_camion() a una sola linea:

camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]

# >>> camion
# [{'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}, 
# {'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}, 
# {'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}, 
# {'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}, 
# {'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}, 
# {'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}]
