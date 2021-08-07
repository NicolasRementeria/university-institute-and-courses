# Ejercicio 5.4: Calcular pi

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/01_Random.md#ejercicio-54-calcular-pi

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N = 1000000
puntos = [generar_punto() for i in range(N)]

# x^2 + y^2 < 1
# M = avg_x ** 2 + avg_y ** 2 

M = [(coordenada[0], coordenada[1]) for coordenada in puntos if coordenada[0] ** 2 + coordenada[1] ** 2 < 1 ]

# avg_x = sum(x for x, y in M) / len(puntos)
# avg_y = sum(y for x, y in M) / len(puntos)

# pi ~ 4*M/N
pi = 4*len(M)/N

print(f"El valor aproximado de pi dado un circulo calculando {N} puntos aleatorios para obtener el área, es de: {pi}")