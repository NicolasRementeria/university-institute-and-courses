# Ejercicio 6.6: Parsear un archivo CSV

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/03_Funciones.md#ejercicio-66-parsear-un-archivo-csv

# %%
# import csv
#
# def parse_csv(nombre_archivo):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows = csv.reader(f)
#         # Lee los encabezados
#         headers = next(rows)
#         registros = []
#         for row in rows:
#             if not row:    # Saltea filas sin datos
#                 continue
#             registro = dict(zip(headers, row))
#             registros.append(registro)
#     return registros
#
# camion = parse_csv('../Data/camion.csv')

# %%

# Ejercicio 6.7: Selector de Columnas

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/03_Funciones.md#ejercicio-67-selector-de-columnas

# import csv
# 
# 
# def parse_csv(nombre_archivo, select=None):
#     '''
#     Parsea un archivo CSV en una lista de registros.
#     Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
#     '''
#     with open(nombre_archivo) as f:
#         filas = csv.reader(f)
#         # Lee los encabezados del archivo
#         encabezados = next(filas)
#         # Si se indicó un selector de columnas,
#         #    buscar los índices de las columnas especificadas.
#         # Y en ese caso achicar el conjunto de encabezados para diccionarios
#         if select:
#             indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#             encabezados = select
#         else:
#             indices = []
#         registros = []
#         for fila in filas:
#             if not fila:    # Saltear filas vacías
#                 continue
#             # Filtrar la fila si se especificaron columnas
#             if indices:
#                 fila = [fila[index] for index in indices]
#             # Armar el diccionario
#             registro = dict(zip(encabezados, fila))
#             registros.append(registro)
#     return registros
# 
# 
# camion = parse_csv('../Data/camion.csv')
# camion = parse_csv('../Data/camion.csv', select=["nombre"])
# camion = parse_csv('../Data/camion.csv', select=["nombre", "precio"])

#%%

# Ejercicio 6.8: Conversión de tipo

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/03_Funciones.md#ejercicio-68-conversi%C3%B3n-de-tipo

# import csv
# 
# 
# def parse_csv(nombre_archivo, select=None, types=None):
#     '''
#     Parsea un archivo CSV en una lista de registros.
#     Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
#     '''
#     with open(nombre_archivo) as f:
#         filas = csv.reader(f)
#         # Lee los encabezados del archivo
#         encabezados = next(filas)
#         # Si se indicó un selector de columnas,
#         #    buscar los índices de las columnas especificadas.
#         # Y en ese caso achicar el conjunto de encabezados para diccionarios
#         if select:
#             indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#             encabezados = select
#         else:
#             indices = []
#         registros = []
#         for fila in filas:
#             if not fila:    # Saltear filas vacías
#                 continue
#             # Filtrar la fila si se especificaron columnas
#             if indices:
#                 fila = [fila[index] for index in indices]
#             if types:
#                 fila = [func(val) for func, val in zip(types, fila)]
#             # Armar el diccionario
#             registro = dict(zip(encabezados, fila))
#             registros.append(registro)
#     return registros
# 
# camion = parse_csv('../Data/camion.csv', types=[str, int, float])


#%%

# Ejercicio 6.9: Trabajando sin encabezados

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/03_Funciones.md#ejercicio-69-trabajando-sin-encabezados

import csv


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if has_headers == False:
        with open(nombre_archivo) as f:
            filas = csv.reader(f)
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Armar el diccionario
                registro = (fila[0], fila[1])
                registros.append(registro)
    else:
        with open(nombre_archivo) as f:
            filas = csv.reader(f)
            # Lee los encabezados del archivo
            encabezados = next(filas)
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
    return registros

# precios = parse_csv('../Data/precios.csv')
# precios = parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)

