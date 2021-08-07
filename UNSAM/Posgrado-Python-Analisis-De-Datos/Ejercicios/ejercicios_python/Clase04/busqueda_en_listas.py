# %%

# Ejercicio 4.6: Búsquedas de un elemento

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/02_IteradoresLista.md#ejercicio-46-b%C3%BAsquedas-de-un-elemento

# En este primer ejercicio tenés que escribir una función buscar_u_elemento() que reciba una lista y un elemento y 
# devuelva la posición de la última aparición de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
# 
# Probá tu función con algunos ejemplos:
# 
# >>> buscar_u_elemento([1,2,3,2,3,4],1)
# 0
# >>> buscar_u_elemento([1,2,3,2,3,4],2)
# 3
# >>> buscar_u_elemento([1,2,3,2,3,4],3)
# 4
# >>> buscar_u_elemento([1,2,3,2,3,4],5)
# -1
# 
# Agregale a tu programa busqueda_en_listas.py una función buscar_n_elemento() que reciba una lista y un elemento y 
# devuelva la cantidad de veces que aparece el elemento en la lista. Probá también esta función con algunos ejemplos.

# def buscar_u_elemento(lista, elem):
#     pos = -1
#     index = 0
#     for valor in lista:
#         if valor == elem:
#             pos = index
#         index += 1
#     return pos
# 
# print(buscar_u_elemento([1,2,3,2,3,4],1))
# print(buscar_u_elemento([1,2,3,2,3,4],2))
# print(buscar_u_elemento([1,2,3,2,3,4],3))
# print(buscar_u_elemento([1,2,3,2,3,4],5))
# 
# # Output:
# # 0
# # 3 
# # 4 
# # -1
# 
# def buscar_n_elemento(lista, elem):
#     count = 0
#     for valor in lista:
#         if valor == elem:
#             count += 1
#     return count
# 
# print(buscar_n_elemento([1,2,3,2,3,4],1))
# print(buscar_n_elemento([1,2,3,2,3,4],2))
# print(buscar_n_elemento([1,2,3,2,3,4],3))
# print(buscar_n_elemento([1,2,3,2,3,4],5))

# Output:
# 1
# 2
# 2
# 0

# %%

# Ejercicio 4.7: Búsqueda de máximo y mínimo

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/02_IteradoresLista.md#ejercicio-47-b%C3%BAsqueda-de-m%C3%A1ximo-y-m%C3%ADnimo

# Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque el valor máximo de una lista 
# de números positivos. Python tiene el comando max que ya hace esto, pero como práctica te proponemos 
# que completes el siguiente código
#
# Probá tu función con estos ejemplos:

# >>> maximo([1,2,7,2,3,4])
# 7
# >>> maximo([1,2,3,4])
# 4
# >>> maximo([-5,4])
# 4
# >>> maximo([-5,-4])
# 0

def buscar_u_elemento(lista, elem):
    pos = -1
    index = 0
    for valor in lista:
        if valor == elem:
            pos = index
        index += 1
    return pos

def buscar_n_elemento(lista, elem):
    count = 0
    for valor in lista:
        if valor == elem:
            count += 1
    return count

# def maximo(lista):
#     '''Devuelve el máximo de una lista, 
#     la lista debe ser no vacía y de números positivos.
#     '''
#     # m guarda el máximo de los elementos a medida que recorro la lista. 
#     m = 0 # Lo inicializo en 0
#     for e in lista: # Recorro la lista y voy guardando el mayor
#         if e > m:
#             m = e
#     return m
# 
# maximo([1,2,7,2,3,4])
# maximo([1,2,3,4])
# maximo([-5,4])
# maximo([-5,-4])
# 
# # Output:
# # >>> maximo([1,2,7,2,3,4])
# # 7
# # >>> maximo([1,2,3,4])
# # 4
# # >>> maximo([-5,4])
# # 4
# # >>> maximo([-5,-4])
# # 0

# Falla porque el valor minimo en el código es 0, por lo cual dada una lista de 
# números negativos, ningún número superará a 0.
# Para arreglarlo, el valor por defecto no será 0, sino el primer valor del array.

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])

# Output:
# >>> maximo([1,2,7,2,3,4])
# 7
# >>> maximo([1,2,3,4])
# 4
# >>> maximo([-5,4])
# 4
# >>> maximo([-5,-4])
# -4

def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m

minimo([1,2,7,2,3,4])
minimo([1,2,3,4])
minimo([-5,4])
minimo([-5,-4])

# Output:
# >>> minimo([1,2,7,2,3,4])
# 1
# >>> minimo([1,2,3,4])
# 1
# >>> minimo([-5,4])
# -5
# >>> minimo([-5,-4])
# -5

