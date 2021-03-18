# camion_commandline.py

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/02_Estructuras_y_Funciones/03_TiposDatos.md#ejercicio-214-diccionario-geringoso

# Ejercicio 2.14

# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
# Las claves del diccionario deben las palabras de la lista y los valores deben ser sus traducciones 
# al geringoso (como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']. 
# Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.
#
# codigo geringoso.py:
#
# cadena = 'Geringoso'
# capadepenapa = ''
# 
# vocales = "aeiou"
# 
# for c in cadena:
#     if c in vocales:
#         capadepenapa += c + "p" + c 
#     else:
#         capadepenapa += c
# 
# print(capadepenapa)

######

def conversion_a_geringoso(palabra):
    conversion = ""
    vocales = "aeiou"
    for c in palabra:
        if c in vocales:
            conversion += c + "p" + c
        else:
            conversion += c
    return conversion

def geringoso_de_lista_a_diccionario(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = conversion_a_geringoso(palabra)
    return diccionario

lista = ['banana', 'manzana', 'mandarina']

geringoso_de_lista_a_diccionario(lista)