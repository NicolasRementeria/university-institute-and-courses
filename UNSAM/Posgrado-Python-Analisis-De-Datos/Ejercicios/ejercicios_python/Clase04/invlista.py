# %%

# Ejercicio 4.8: Invertir una lista

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/02_IteradoresLista.md#ejercicio-48-invertir-una-lista

# Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los mismos elementos pero en el orden inverso. 
# Es decir, el que era el primer elemento de la lista de entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.

# Probala en:
#    [1, 2, 3, 4, 5]
#    ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']


def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])

# Output:

# >>> invertir_lista([1, 2, 3, 4, 5])
# [5, 4, 3, 2, 1]
# >>> invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']