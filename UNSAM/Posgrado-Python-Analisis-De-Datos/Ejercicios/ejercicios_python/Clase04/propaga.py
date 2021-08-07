# %%

# Ejercicio 4.9: Propagación

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/02_IteradoresLista.md#ejercicio-49-propagaci%C3%B3n

# Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en 
# tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos esta 
# situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 
# (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente de un 
# fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados 
# no se encienden nuevamente.
# 
# Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva 
# un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo 
# propaga.py.
# 
# Por ejemplo:
# 
# >>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
# >>> propagar([ 0, 0, 0, 1, 0, 0])
# [ 1, 1, 1, 1, 1, 1]

def propagar(lista):
    tamaño_lista = len(lista)
    lista_indices = [indice for indice, estado in enumerate(lista) if estado == -1]
    lista_splitteada = []
    limites = lista_indices + [tamaño_lista]
    for principio, fin in zip([0] + lista_indices, limites):
        lista_splitteada.append(lista[principio : fin])
    for segmento in lista_splitteada:
        if 1 in segmento:
            for fosforo, estado in enumerate(segmento):
                if estado == 0:
                    segmento[fosforo] = 1
    lista_propagada = []
    for segmento in lista_splitteada:
        for fosforo in segmento:
            lista_propagada.append(fosforo)
    return lista_propagada
    
# Output:
# >>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# >>> propagar([ 0, 0, 0, 1, 0, 0])
# [1, 1, 1, 1, 1, 1]
