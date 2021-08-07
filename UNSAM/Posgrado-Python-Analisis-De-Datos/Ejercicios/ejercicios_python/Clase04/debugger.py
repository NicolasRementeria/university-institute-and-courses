
# %%

# Ejercicio 4.1: Debugger

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/01_Debugger.md#ejercicio-41-debugger


def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i=len(lista)
    while i > 0:    # tomo el último elemento 
        i=i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

# La lista "l" está siendo modificada al utilizarse en la llamada de 
# "invertir_lista", al referenciarse como nombre de variable "lista"
# y luego utilizando el método ".pop()" que efectivamente remueve el objeto
# en "lista", que al ser una referencia de "l", también remueve esa posición
# en la lista "l".

# Para solucionarlo, una forma sería que "lista" se convierta en otra variable,
# como "lista_aux" y sobre esa variable se utilice el método ".pop()", 
# esa misma variable seria la que se retorne.

# %%

# Ejercicio 4.2: Más debugger

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/01_Debugger.md#ejercicio-42-m%C3%A1s-debugger

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# Con cada vuelta del for, al cambiar "registro", estás también cambiando todas
# las apariciones de dicho registro dentro de camion.
# Para solucionarlo, cambiaría la inicialización de registro como diccionario
# vacio justo debajo del for, en su primera linea de ejecucion.

# %%

