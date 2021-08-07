# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas.

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/05_BusqBinaria.md#ejercicio-613-b%C3%BAsqueda-lineal-sobre-listas-ordenadas

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
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

# import random
# import time
# tamaño = 1000000
# random_list = random.sample(range(0, tamaño), tamaño)
# ordenada = sorted(random_list)
# e = 999
# 
# print(f"Tamaño de array: {tamaño} | valor a buscar: {e}" )
# 
# start = time.time()
# print(busqueda_lineal(random_list, e))
# end = time.time()
# print(f"Tiempo tardado para busqueda lineal: {end - start}")
# 
# start = time.time()
# print(busqueda_lineal_lordenada(random_list, e))
# end = time.time()
# print(f"Tiempo tardado para busqueda lineal ordenada: {end - start}")
# 
# start = time.time()
# print(busqueda_binaria(ordenada, e))
# end = time.time()
# print(f"Tiempo tardado para busqueda binaria: {end - start}")
