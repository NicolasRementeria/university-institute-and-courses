#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
#    Lo corregí cambiando esto por aquello.
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

# RTA:
# El error es lógico.
# Solo anda bien en el primer caso de prueba. El 'return False' debería estar fuera del while.

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

# RTA:
# Tiene error sintáctico. A la linea 31 de "def tiene_a(expresion)" le falta los dos puntos de cierre, quedando "def tiene_a(expresion):"

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
# %%

# RTA:
# El error es de tipo.
# El programa NO funciona con tipo número (int). 

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.

def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

# RTA:
# El problema está en que suma(a,b) no retorna nada.

#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

# RTA:
# El problema está en que cada vuelta del ciclo "for", al mismo encabezado estamos guardando el valor actual del índice en  for. Como el último elemento del "for" es "{'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}", eso es lo que guarda en todos los items de la lista.

# %%
