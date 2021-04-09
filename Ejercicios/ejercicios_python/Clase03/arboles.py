#### Ejercicio 3.18

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-318-lectura-de-los-%C3%A1rboles-de-un-parque

# import csv
# from pprint import pprint
# 
# def leer_parque(nombre_archivo, parque):
#     archivo = open(nombre_archivo, "r", encoding="UTF-8")
#     csv_file = csv.reader(archivo)
#     informacion_parque = []
#     headers = next(csv_file)
#     for item in csv_file:
#         if(parque in item):
#             informacion_parque.append(dict(zip(headers, item)))
#     return informacion_parque
# 
# 
# 
# parque = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# 
# pprint(parque)

# Output:
#  {'altura_tot': '14',
#  'coord_x': '95976.197949',
#  'coord_y': '107018.011373',
#  'diametro': '25',
#  'espacio_ve': 'GENERAL PAZ',
#  'id_arbol': '4701',
#  'id_especie': '45',
#  'inclinacio': '10',
#  'lat': '-34.5659985492',
#  'long': '-58.5071472579',
#  'nombre_cie': 'Casuarina cunninghamiana',
#  'nombre_com': 'Casuarina',
#  'nombre_fam': 'Casuarinaceas',
#  'nombre_gen': 'Casuarina',
#  'origen': 'Exótico',
#  'tipo_folla': 'Árbol Latifoliado Perenne',
#  'ubicacion': 'LARRALDE, CRISOLOGO, AV. - PAZ, GRAL., AV.- AIZPURUA'},
# {'altura_tot': '4',
#  'coord_x': '96073.54180199999',
#  'coord_y': '107108.18252',
#  'diametro': '11',
#  'espacio_ve': 'GENERAL PAZ',
#  'id_arbol': '4707',
#  'id_especie': '17',
#  'inclinacio': '0',
#  'lat': '-34.5651860953',
#  'long': '-58.5060860033',
#  'nombre_cie': 'Ailanthus altissima',
#  'nombre_com': 'Árbol del cielo (Ailanto o Árbol de los dioses)',
#  'nombre_fam': 'Simarrubáceas',
#  'nombre_gen': 'Ailanthus',
#  'origen': 'Exótico',
#  'tipo_folla': 'Árbol Latifoliado Caducifolio',
#  'ubicacion': 'LARRALDE, CRISOLOGO, AV. - PAZ, GRAL., AV.- AIZPURUA'},
#  (...)
#  (...)
#  (...)

#### Ejercicio 3.19 y 3.20

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-319-determinar-las-especies-en-un-parque
# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-320-contar-ejemplares-por-especie

# import csv
# from pprint import pprint
# from collections import Counter
# 
# def leer_parque(nombre_archivo, parque):
#     archivo = open(nombre_archivo, "r", encoding="UTF-8")
#     csv_file = csv.reader(archivo)
#     informacion_parque = []
#     headers = next(csv_file)
#     for item in csv_file:
#         if(parque in item):
#             informacion_parque.append(dict(zip(headers, item)))
#     return informacion_parque
# 
# def especies(lista_arboles):
#     dicc_numero_especies = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_numero_especies.keys():
#             dicc_numero_especies[arbol["nombre_com"]] = 1
#         else:
#             dicc_numero_especies[arbol["nombre_com"]] += 1
#     return dicc_numero_especies
# 
# arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# arboles_los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
# arboles_centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
# 
# especies_general_paz = especies(arboles_general_paz)
# especies_los_andes = especies(arboles_los_andes)
# especies_centenario = especies(arboles_centenario)
# 
# especies_general_paz = Counter(especies(arboles_general_paz))
# especies_los_andes = Counter(especies(arboles_los_andes))
# especies_centenario = Counter(especies(arboles_centenario))
# 
# print(especies_general_paz.most_common(5))
# print(especies_los_andes.most_common(5))
# print(especies_centenario.most_common(5))



# Output:

# $ python -i arboles.py 
# [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
# [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
# [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]

#### Ejercicio 3.21

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-321-alturas-de-una-especie-en-una-lista

# import csv
# from pprint import pprint
# from collections import Counter
# 
# def string_to_number(number):
#     # Will try to convert the string "number" to a int or float, if not possible will not modify it
#     try:
#         if number[0] == "-" and "." not in number:
#             # is negative int
#             return int(number)
#         if number[0] != "-" and "." not in number:
#             # is positive int
#             return int(number)
#         if number[0] == "-" and "." in number:
#             # is negative float
#             return float(number)
#         if number[0] != "-" and "." in number:
#             # is positive float
#             return float(number)
#     except:
#         return number
# 
# def leer_parque(nombre_archivo, parque):
#     archivo = open(nombre_archivo, "r", encoding="UTF-8")
#     csv_file = csv.reader(archivo)
#     informacion_parque = []
#     headers = next(csv_file)
#     for item in csv_file:
#         if(parque in item):
#             informacion_parque.append(dict(zip(headers, item)))
#     for item in range(len(informacion_parque)):
#         for key in informacion_parque[item]:
#             #print(informacion_parque[item][key])
#             informacion_parque[item][key] = string_to_number(informacion_parque[item][key])
#     return informacion_parque
# 
# def especies(lista_arboles):
#     dicc_numero_especies = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_numero_especies.keys():
#             dicc_numero_especies[arbol["nombre_com"]] = 1
#         else:
#             dicc_numero_especies[arbol["nombre_com"]] += 1
#     return dicc_numero_especies
# 
# def obtener_alturas(lista_arboles, especie):
#     #lista_tipo_arboles = list(especies(lista_arboles).keys())
#     lista_alturas = []
#     for arbol in lista_arboles:
#          if arbol["nombre_com"] == especie:
#             lista_alturas.append(float(arbol["altura_tot"]))
#     return lista_alturas
# 
# arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# arboles_los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
# arboles_centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
# 
# especies_general_paz = especies(arboles_general_paz)
# especies_los_andes = especies(arboles_los_andes)
# especies_centenario = especies(arboles_centenario)
# 
# alturas_general_paz = obtener_alturas(arboles_general_paz, "Jacarandá")
# print(f"General Paz | Altura Máxima de Jacarandá: {max(alturas_general_paz)}, Altura Promedio de Jacarandá: {sum(alturas_general_paz) / len(alturas_general_paz):.2f}")
# 
# alturas_los_andes = obtener_alturas(arboles_los_andes, "Jacarandá")
# print(f"Los Andes | Altura Máxima de Jacarandá: {max(alturas_los_andes)}, Altura Promedio de Jacarandá: {sum(alturas_los_andes) / len(alturas_los_andes):.2f}")
# 
# alturas_centenario = obtener_alturas(arboles_centenario, "Jacarandá")
# print(f"Centenario | Altura Máxima de Jacarandá: {max(alturas_centenario)}, Altura Promedio de Jacarandá: {sum(alturas_centenario) / len(alturas_centenario):.2f}")

# Output:

# $ python arboles.py
# General Paz | Altura Máxima de Jacarandá: 16.0, Altura Promedio de Jacarandá: 10.20
# Los Andes | Altura Máxima de Jacarandá: 25.0, Altura Promedio de Jacarandá: 10.54
# Centenario | Altura Máxima de Jacarandá: 18.0, Altura Promedio de Jacarandá: 8.96


#### Ejercicio 3.22

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-322-inclinaciones-por-especie-de-una-lista

# import csv
# from pprint import pprint
# from collections import Counter
# 
# def string_to_number(number):
#     # Will try to convert the string "number" to a int or float, if not possible will not modify it
#     try:
#         if number[0] == "-" and "." not in number:
#             # is negative int
#             return int(number)
#         if number[0] != "-" and "." not in number:
#             # is positive int
#             return int(number)
#         if number[0] == "-" and "." in number:
#             # is negative float
#             return float(number)
#         if number[0] != "-" and "." in number:
#             # is positive float
#             return float(number)
#     except:
#         return number
# 
# def leer_parque(nombre_archivo, parque):
#     archivo = open(nombre_archivo, "r", encoding="UTF-8")
#     csv_file = csv.reader(archivo)
#     informacion_parque = []
#     headers = next(csv_file)
#     for item in csv_file:
#         if(parque in item):
#             informacion_parque.append(dict(zip(headers, item)))
#     for item in range(len(informacion_parque)):
#         for key in informacion_parque[item]:
#             #print(informacion_parque[item][key])
#             informacion_parque[item][key] = string_to_number(informacion_parque[item][key])
#     return informacion_parque
# 
# def especies(lista_arboles):
#     dicc_numero_especies = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_numero_especies.keys():
#             dicc_numero_especies[arbol["nombre_com"]] = 1
#         else:
#             dicc_numero_especies[arbol["nombre_com"]] += 1
#     return dicc_numero_especies
# 
# def obtener_alturas(lista_arboles, especie):
#     lista_alturas = []
#     for arbol in lista_arboles:
#          if arbol["nombre_com"] == especie:
#             lista_alturas.append(float(arbol["altura_tot"]))
#     return lista_alturas
# 
# def obtener_inclinaciones(lista_arboles, especie):
#     lista_inclinaciones = []
#     for arbol in lista_arboles:
#          if arbol["nombre_com"] == especie:
#             lista_inclinaciones.append(float(arbol["inclinacio"]))
#     return lista_inclinaciones
# 
# 
# arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# arboles_los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
# arboles_centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
# 
# especies_general_paz = especies(arboles_general_paz)
# especies_los_andes = especies(arboles_los_andes)
# especies_centenario = especies(arboles_centenario)
# 
# alturas_general_paz = obtener_alturas(arboles_general_paz, "Jacarandá")
# alturas_los_andes = obtener_alturas(arboles_los_andes, "Jacarandá")
# alturas_centenario = obtener_alturas(arboles_centenario, "Jacarandá")
# 
# print(f"General Paz | Altura Máxima de Jacarandá: {max(alturas_general_paz)}, Altura Promedio de Jacarandá: {sum(alturas_general_paz) / len(alturas_general_paz):.2f}")
# print(f"Los Andes | Altura Máxima de Jacarandá: {max(alturas_los_andes)}, Altura Promedio de Jacarandá: {sum(alturas_los_andes) / len(alturas_los_andes):.2f}")
# print(f"Centenario | Altura Máxima de Jacarandá: {max(alturas_centenario)}, Altura Promedio de Jacarandá: {sum(alturas_centenario) / len(alturas_centenario):.2f}")
# 
# inclinaciones_general_paz = obtener_inclinaciones(arboles_general_paz, "Jacarandá")
# inclinaciones_los_andes = obtener_inclinaciones(arboles_los_andes, "Jacarandá")
# inclinaciones_centenario = obtener_inclinaciones(arboles_centenario, "Jacarandá")
# 
# print(f"General Paz | Inclinaciones: {inclinaciones_general_paz}")
# print(f"Los Andes | Inclinaciones: {inclinaciones_los_andes}")
# print(f"Centenario | Inclinaciones: {inclinaciones_centenario}")



#### Ejercicio 3.23

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-323-especie-con-el-ejemplar-m%C3%A1s-inclinado

# import csv
# from pprint import pprint
# from collections import Counter
# 
# def string_to_number(number):
#     # Will try to convert the string "number" to a int or float, if not possible will not modify it
#     try:
#         if number[0] == "-" and "." not in number:
#             # is negative int
#             return int(number)
#         if number[0] != "-" and "." not in number:
#             # is positive int
#             return int(number)
#         if number[0] == "-" and "." in number:
#             # is negative float
#             return float(number)
#         if number[0] != "-" and "." in number:
#             # is positive float
#             return float(number)
#     except:
#         return number
# 
# def leer_parque(nombre_archivo, parque):
#     archivo = open(nombre_archivo, "r", encoding="UTF-8")
#     csv_file = csv.reader(archivo)
#     informacion_parque = []
#     headers = next(csv_file)
#     for item in csv_file:
#         if(parque in item):
#             informacion_parque.append(dict(zip(headers, item)))
#     for item in range(len(informacion_parque)):
#         for key in informacion_parque[item]:
#             informacion_parque[item][key] = string_to_number(informacion_parque[item][key])
#     return informacion_parque
# 
# def especies(lista_arboles):
#     dicc_numero_especies = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_numero_especies.keys():
#             dicc_numero_especies[arbol["nombre_com"]] = 1
#         else:
#             dicc_numero_especies[arbol["nombre_com"]] += 1
#     return dicc_numero_especies
# 
# def obtener_alturas(lista_arboles, especie):
#     lista_alturas = []
#     for arbol in lista_arboles:
#          if arbol["nombre_com"] == especie:
#             lista_alturas.append(float(arbol["altura_tot"]))
#     return lista_alturas
# 
# def obtener_inclinaciones(lista_arboles, especie):
#     lista_inclinaciones = []
#     for arbol in lista_arboles:
#          if arbol["nombre_com"] == especie:
#             lista_inclinaciones.append(float(arbol["inclinacio"]))
#     return lista_inclinaciones
# 
# def especimen_mas_inclinado(lista_arboles):
#     dicc_inclinaciones = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_inclinaciones.keys():
#             dicc_inclinaciones[arbol["nombre_com"]] = arbol["inclinacio"]
#         elif arbol["nombre_com"] in dicc_inclinaciones.keys() and arbol["inclinacio"] > dicc_inclinaciones[arbol["nombre_com"]]:
#             dicc_inclinaciones[arbol["nombre_com"]] = arbol["inclinacio"]
#     mayor_inclinacion = ["", 0]
#     for nombre_arbol in list(dicc_inclinaciones.keys()):
#         inclinacion = dicc_inclinaciones[nombre_arbol]
#         if inclinacion > mayor_inclinacion[1]:
#             mayor_inclinacion[0] = nombre_arbol
#             mayor_inclinacion[1] = inclinacion
#     return mayor_inclinacion
# 
# arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# arboles_los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
# arboles_centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")
# 
# especies_general_paz = especies(arboles_general_paz)
# especies_los_andes = especies(arboles_los_andes)
# especies_centenario = especies(arboles_centenario)
# 
# alturas_general_paz = obtener_alturas(arboles_general_paz, "Jacarandá")
# alturas_los_andes = obtener_alturas(arboles_los_andes, "Jacarandá")
# alturas_centenario = obtener_alturas(arboles_centenario, "Jacarandá")
# 
# print(f"General Paz | Altura Máxima de Jacarandá: {max(alturas_general_paz)}, Altura Promedio de Jacarandá: {sum(alturas_general_paz) / len(alturas_general_paz):.2f}")
# print(f"Los Andes | Altura Máxima de Jacarandá: {max(alturas_los_andes)}, Altura Promedio de Jacarandá: {sum(alturas_los_andes) / len(alturas_los_andes):.2f}")
# print(f"Centenario | Altura Máxima de Jacarandá: {max(alturas_centenario)}, Altura Promedio de Jacarandá: {sum(alturas_centenario) / len(alturas_centenario):.2f}")
# 
# inclinaciones_general_paz = obtener_inclinaciones(arboles_general_paz, "Jacarandá")
# inclinaciones_los_andes = obtener_inclinaciones(arboles_los_andes, "Jacarandá")
# inclinaciones_centenario = obtener_inclinaciones(arboles_centenario, "Jacarandá")
# 
# print(f"General Paz | Inclinaciones: {inclinaciones_general_paz}")
# print(f"Los Andes | Inclinaciones: {inclinaciones_los_andes}")
# print(f"Centenario | Inclinaciones: {inclinaciones_centenario}")
# 
# mayor_inclinacion_centenario = especimen_mas_inclinado(arboles_centenario)
# print(f"Centenario | Mayor Inclinacion: Arbol = {mayor_inclinacion_centenario[0]}, Inclinacion = {mayor_inclinacion_centenario[1]}°")

# Output:

# Centenario | Mayor Inclinacion: Arbol = Falso Guayabo (Guayaba del Brasil), Inclinacion = 80°




#### Ejercicio 3.24

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/06_Arboles1.md#ejercicio-324-especie-m%C3%A1s-inclinada-en-promedio

# %%

import csv
from pprint import pprint
from collections import Counter

def string_to_number(number):
    # Will try to convert the string "number" to a int or float, if not possible will not modify it
    try:
        if number[0] == "-" and "." not in number:
            # is negative int
            return int(number)
        if number[0] != "-" and "." not in number:
            # is positive int
            return int(number)
        if number[0] == "-" and "." in number:
            # is negative float
            return float(number)
        if number[0] != "-" and "." in number:
            # is positive float
            return float(number)
    except:
        return number

def leer_parque(nombre_archivo, parque):
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    csv_file = csv.reader(archivo)
    informacion_parque = []
    headers = next(csv_file)
    for item in csv_file:
        if(parque in item):
            informacion_parque.append(dict(zip(headers, item)))
    for item in range(len(informacion_parque)):
        for key in informacion_parque[item]:
            informacion_parque[item][key] = string_to_number(informacion_parque[item][key])
    return informacion_parque

def especies(lista_arboles):
    dicc_numero_especies = {}
    for arbol in lista_arboles:
        if arbol["nombre_com"] not in dicc_numero_especies.keys():
            dicc_numero_especies[arbol["nombre_com"]] = 1
        else:
            dicc_numero_especies[arbol["nombre_com"]] += 1
    return dicc_numero_especies

def obtener_alturas(lista_arboles, especie):
    lista_alturas = []
    for arbol in lista_arboles:
         if arbol["nombre_com"] == especie:
            lista_alturas.append(float(arbol["altura_tot"]))
    return lista_alturas

def obtener_inclinaciones(lista_arboles, especie):
    lista_inclinaciones = []
    for arbol in lista_arboles:
         if arbol["nombre_com"] == especie:
            lista_inclinaciones.append(float(arbol["inclinacio"]))
    return lista_inclinaciones

# def especimen_mas_inclinado(lista_arboles):
#     dicc_inclinaciones = {}
#     for arbol in lista_arboles:
#         if arbol["nombre_com"] not in dicc_inclinaciones.keys():
#             dicc_inclinaciones[arbol["nombre_com"]] = arbol["inclinacio"]
#         elif arbol["nombre_com"] in dicc_inclinaciones.keys() and arbol["inclinacio"] > dicc_inclinaciones[arbol["nombre_com"]]:
#             dicc_inclinaciones[arbol["nombre_com"]] = arbol["inclinacio"]
#     mayor_inclinacion = ["", 0]
#     for nombre_arbol in list(dicc_inclinaciones.keys()):
#         inclinacion = dicc_inclinaciones[nombre_arbol]
#         if inclinacion > mayor_inclinacion[1]:
#             mayor_inclinacion[0] = nombre_arbol
#             mayor_inclinacion[1] = inclinacion
#     return mayor_inclinacion

def especimen_mas_inclinado(lista_arboles):
    mayor_inclinacion = ["", 0]
    for arbol in lista_arboles:
        if max(obtener_inclinaciones(lista_arboles, arbol["nombre_com"])) > mayor_inclinacion[1]:
            mayor_inclinacion[0] = arbol["nombre_com"]
            mayor_inclinacion[1] = max(obtener_inclinaciones(lista_arboles, arbol["nombre_com"]))
    return mayor_inclinacion    

def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones_por_arbol = {}
    for arbol in lista_arboles:
        if arbol["nombre_com"] not in inclinaciones_por_arbol.keys():
            inclinaciones_por_arbol[arbol["nombre_com"]] = obtener_inclinaciones(lista_arboles, arbol["nombre_com"])
    mayor_inclinacion = ["", 0]
    for arbol in list(inclinaciones_por_arbol.keys()):
        lista_inclinacion = inclinaciones_por_arbol[arbol]
        promedio_inclinacion = sum(lista_inclinacion) / len(lista_inclinacion)
        if mayor_inclinacion[1] < promedio_inclinacion:
            mayor_inclinacion[0] = arbol
            mayor_inclinacion[1] = promedio_inclinacion
    return mayor_inclinacion

arboles_general_paz = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
arboles_los_andes = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "ANDES, LOS")
arboles_centenario = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "CENTENARIO")

especies_general_paz = especies(arboles_general_paz)
especies_los_andes = especies(arboles_los_andes)
especies_centenario = especies(arboles_centenario)

alturas_general_paz = obtener_alturas(arboles_general_paz, "Jacarandá")
alturas_los_andes = obtener_alturas(arboles_los_andes, "Jacarandá")
alturas_centenario = obtener_alturas(arboles_centenario, "Jacarandá")

print(f"General Paz | Altura Máxima de Jacarandá: {max(alturas_general_paz)}, Altura Promedio de Jacarandá: {sum(alturas_general_paz) / len(alturas_general_paz):.2f}")
print(f"Los Andes | Altura Máxima de Jacarandá: {max(alturas_los_andes)}, Altura Promedio de Jacarandá: {sum(alturas_los_andes) / len(alturas_los_andes):.2f}")
print(f"Centenario | Altura Máxima de Jacarandá: {max(alturas_centenario)}, Altura Promedio de Jacarandá: {sum(alturas_centenario) / len(alturas_centenario):.2f}")

inclinaciones_general_paz = obtener_inclinaciones(arboles_general_paz, "Jacarandá")
inclinaciones_los_andes = obtener_inclinaciones(arboles_los_andes, "Jacarandá")
inclinaciones_centenario = obtener_inclinaciones(arboles_centenario, "Jacarandá")

print(f"General Paz | Inclinaciones: {inclinaciones_general_paz}")
print(f"Los Andes | Inclinaciones: {inclinaciones_los_andes}")
print(f"Centenario | Inclinaciones: {inclinaciones_centenario}")

mayor_inclinacion_centenario = especimen_mas_inclinado(arboles_centenario)
print(f"Centenario | Mayor Inclinacion: Arbol = {mayor_inclinacion_centenario[0]}, Inclinacion = {mayor_inclinacion_centenario[1]}°")

mayor_inclinacion_los_andes = especimen_mas_inclinado(arboles_los_andes)
print(f"Los Andes | Mayor Inclinacion: Arbol = {mayor_inclinacion_los_andes[0]}, Inclinacion = {mayor_inclinacion_los_andes[1]}°")

inclinacion_promedio_general_paz = especie_promedio_mas_inclinada(arboles_general_paz)
inclinacion_promedio_los_andes = especie_promedio_mas_inclinada(arboles_los_andes)
inclinacion_promedio_centenerio = especie_promedio_mas_inclinada(arboles_centenario)

print(f"General Paz | Inclinaciones Promedio  del arbol mas inclinado: Nombre = {inclinacion_promedio_general_paz[0]}, Promedio = {inclinacion_promedio_general_paz[1]}")
print(f"Los Andes | Inclinaciones Promedio del arbol mas inclinado: Nombre = {inclinacion_promedio_los_andes[0]}, Promedio = {inclinacion_promedio_los_andes[1]}")
print(f"Centenario | Inclinaciones  del arbol mas inclinado: Nombre = {inclinacion_promedio_centenerio[0]}, Promedio = {inclinacion_promedio_centenerio[1]}")
# %%
