# Ejercicio 6.14: Búsqueda binaria

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/05_BusqBinaria.md#ejercicio-614-b%C3%BAsqueda-binaria

#%%

# def busqueda_lineal(lista, e):
#     '''Si e está en la lista devuelve su posición, de lo
#     contrario devuelve -1.
#     '''
#     pos = -1  # comenzamos suponiendo que e no está
#     for i, z in enumerate(lista): # recorremos la lista
#         if z == e:   # si encontramos a e
#             pos = i  # guardamos su posición
#             break    # y salimos del ciclo
#     return pos
# 
# def busqueda_lineal_lordenada(lista,e):
#     sorted_list = sorted(lista)
#     pos = -1  # comenzamos suponiendo que e no está
#     for i, z in enumerate(sorted_list): # recorremos la lista
#         if z == e:   # si encontramos a e
#             pos = i  # guardamos su posición
#             break    # y salimos del ciclo
#     return pos
# 
# def busqueda_binaria(lista, x, verbose = False):
#     '''Búsqueda binaria
#     Precondición: la lista está ordenada
#     Devuelve -1 si x no está en lista;
#     Devuelve p tal que lista[p] == x, si x está en lista
#     '''
#     if verbose:
#         print(f'[DEBUG] izq |der |medio')
#     pos = -1 # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if verbose:
#             print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
#         if lista[medio] == x:
#             pos = medio     # elemento encontrado!
#         if lista[medio] > x:
#             der = medio - 1 # descarto mitad derecha
#         else:               # if lista[medio] < x:
#             izq = medio + 1 # descarto mitad izquierda
#     return pos
# 
# def donde_insertar(lista, x):
#     pos = -1 # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if lista[medio] == x:
#             pos = medio     # elemento encontrado!
#         if lista[medio] > x:
#             der = medio - 1 # descarto mitad derecha
#             var = True
#         else:               # if lista[medio] < x:
#             izq = medio + 1 # descarto mitad izquierda
#             var = False
#     if pos == -1:
#         pos = medio if var == True else medio+1
#     return pos


# import random
# import time
# lista = [1, 2, 5, 6, 7]
# e = 100
# 
# 
# donde_insertar(random_list, e)

#%%

# Ejercicio 6.15: Insertar un elemento en una lista

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organización_y_Complejidad/06_Complejidad.md

# def busqueda_lineal(lista, e):
#     '''Si e está en la lista devuelve su posición, de lo
#     contrario devuelve -1.
#     '''
#     pos = -1  # comenzamos suponiendo que e no está
#     for i, z in enumerate(lista): # recorremos la lista
#        if z == e:   # si encontramos a e
#            pos = i  # guardamos su posición
#            break    # y salimos del ciclo
#     return pos
# 
# def busqueda_lineal_lordenada(lista,e):
#     sorted_list = sorted(lista)
#     pos = -1  # comenzamos suponiendo que e no está
#     for i, z in enumerate(sorted_list): # recorremos la lista
#         if z == e:   # si encontramos a e
#             pos = i  # guardamos su posición
#             break    # y salimos del ciclo
#     return pos
# 
# def busqueda_binaria(lista, x, verbose = False):
#     '''Búsqueda binaria
#     Precondición: la lista está ordenada
#     Devuelve -1 si x no está en lista;
#     Devuelve p tal que lista[p] == x, si x está en lista
#     '''
#     if verbose:
#         print(f'[DEBUG] izq |der |medio')
#     pos = -1 # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if verbose:
#             print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
#         if lista[medio] == x:
#             pos = medio     # elemento encontrado!
#         if lista[medio] > x:
#             der = medio - 1 # descarto mitad derecha
#         else:               # if lista[medio] < x:
#             izq = medio + 1 # descarto mitad izquierda
#     return pos
# 
# def donde_insertar(lista, x):
#     pos = -1 # Inicializo respuesta, el valor no fue encontrado
#     izq = 0
#     der = len(lista) - 1
#     while izq <= der:
#         medio = (izq + der) // 2
#         if lista[medio] == x:
#             pos = medio     # elemento encontrado!
#         if lista[medio] > x:
#             der = medio - 1 # descarto mitad derecha
#             var = True
#         else:               # if lista[medio] < x:
#             izq = medio + 1 # descarto mitad izquierda
#             var = False
#     if pos == -1:
#         pos = medio if var == True else medio+1
#     return pos
# 
# def insertar(lista, x):
#     pos = busqueda_binaria(lista, x)
#     if pos == -1:
#         pos = donde_insertar(lista, x)
#         lista.insert(pos, x)
#     return pos

# mi_lista = [1, 2, 4, 5, 999, 1000]
# valor = 100
# insertar(mi_lista, valor)
# 
# print(mi_lista)

# Output:

# >>> mi_lista
# [1, 2, 3, 4, 5]


# mi_lista = [1, 2, 4, 5, 999, 1000]
# valor = 100
# insertar(mi_lista, valor)

# print(mi_lista)

# Output:

# >>> print(mi_lista)
# [1, 2, 4, 5, 100, 999, 1000]

###########

#%%

# Ejercicio 6.19: Contar comparaciones en la búsqueda binaria

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/07_gr%C3%A1ficos_de_complejidad.md#ejercicio-619-contar-comparaciones-en-la-b%C3%BAsqueda-binaria


def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
       if z == e:   # si encontramos a e
           pos = i  # guardamos su posición
           break    # y salimos del ciclo
    return pos

def busqueda_lineal_lordenada(lista,e):
    sorted_list = sorted(lista)
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(sorted_list): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    n_comparaciones = 0
    while izq <= der:
        n_comparaciones += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, n_comparaciones

def donde_insertar(lista, x):
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            var = True
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            var = False
    if pos == -1:
        pos = medio if var == True else medio+1
    return pos

def insertar(lista, x):
    pos = busqueda_binaria(lista, x)[0]
    if pos == -1:
        pos = donde_insertar(lista, x)
        lista.insert(pos, x)
    return pos


def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

mi_lista = [1, 2, 4, 5, 999, 1000]
valor = 100
insertar(mi_lista, valor)

print(mi_lista)