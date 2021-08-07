import random
import numpy as np

# Datos:

# Álbum con 670 figuritas.
# Cada figurita se imprime en cantidades iguales y se distribuye 
# aleatoriamente.
# Cada paquete trae cinco figuritas.

# si tuviéramos un álbum de seis figuritas vacío lo vamos a 
# representar como [0 0 0 0 0 0]
# Cuando consigamos la figurita 3 tendremos que indicarlo poniendo un 
# 1 en el tercer lugar de la lista, es decir album[2]=1 y el álbum 
# nos va a quedar A, y si queremos representar que nos 
# tocó dos veces la figurita 3, asignamos album[2] += 1 y el álbum 
# queda [0 0 2 0 0 0].

# Primera simplificación
# 
# Suponé por ahora que las figuritas se compran individualmente (de a # una, no en un paquete con cinco). En este caso, la dinámica del # llenado es la siguiente:
# 
# Iniciamos con un álbum vacío y sin haber comprado ninguna figurita.
# Compramos figuritas (de a una) hasta llenar el álbum; es decir, se 
# repite la acción (el paso) de comprar y pegar figuritas mientras 
# (while) el álbum está incompleto.
# Al terminar nos interesa saber cuántas figuritas tuvimos que 
# comprar para llenar el álbum.

# Ejercicio 5.9: Crear

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-59-crear

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

############

# Ejercicio 5.10: Incompleto

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-510-incompleto

def album_incompleto(A):
    return True in (A == 0)

# vector = np.array([1, 1, 1, 1, 1])
# album_incompleto(vector)


############

# Ejercicio 5.11: Comprar

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-511-comprar

def comprar_figu(figus_total):
    # paquetito = []
    # for i in range(6):
    #     paquetito.append(random.randint(0, figus_total-1))
    # return paquetito
    return random.randint(0, figus_total-1)


############

# Ejercicio 5.12: Cantidad de compras

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-512-cantidad-de-compras

def cuantas_figus(figus_total):
    album_nuevo = crear_album(figus_total)
    count = 0
    #return np.count_nonzero(album_nuevo == 0)
    while album_incompleto(album_nuevo):
        figu_comprada = comprar_figu(figus_total)
        album_nuevo[figu_comprada] = 1
        count += 1
    return count
    

############

# Ejercicio 5.13:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-513

n_repeticiones = 1000 
figus_total = 6

resultados = [cuantas_figus(figus_total) for iteracion in range(n_repeticiones)]

promedio = np.mean(resultados)

print(f"Para {n_repeticiones} albumes de {figus_total} figuritas cada uno, se necesitaron en promedio {promedio} compras de figuritas")

############

# Ejercicio 5.14:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-514

n_repeticiones=100
figus_total=670

resultados = [cuantas_figus(figus_total) for iteracion in range(n_repeticiones)]

promedio = np.mean(resultados)

print(f"Para {n_repeticiones} albumes de {figus_total} figuritas cada uno, se necesitaron en promedio {promedio} compras de figuritas")

############

# Ejercicio 5.15:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-515

figus_total = 670

paquete = [comprar_figu(figus_total) for figu in range(5)]

############

# Ejercicio 5.16:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-516

def comprar_paquete(figus_total, figus_paquete):
    paquete = [comprar_figu(figus_total) for figu in range(figus_paquete)]
    return paquete

############

# Ejercicio 5.17:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-517

def cuantos_paquetes(figus_total, figus_paquete):
    album_nuevo = crear_album(figus_total)
    count = 0
    while album_incompleto(album_nuevo):
        paq_comprado = comprar_paquete(figus_total, figus_paquete)
        #album_nuevo = [1 for i, figu_nueva in album_nuevo, paq_comprado]
        for figu in paq_comprado:
            album_nuevo[figu] = 1
        count += 1
    return count

############

# Ejercicio 5.18:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-518

n_repeticiones=100
figus_total=670
figus_paquete = 5

resultados = [cuantos_paquetes(figus_total, figus_paquete) for iteracion in range(n_repeticiones)]

promedio = np.mean(resultados)

print(f"Para {n_repeticiones} albumes de {figus_total} figuritas cada uno, se necesitaron en promedio {promedio} compras de paquetes de {figus_paquete} figuritas cada uno")

############

# Graficar el llenado del álbum

from matplotlib import pyplot as plt

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()

############

# Ejercicio 5.19:

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-519


#################################


############

# Ejercicio 5.20: Plotear el histograma

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/03_Figuritas.md#ejercicio-520-plotear-el-histograma


plt.hist(calcular_historia_figus_pegadas(figus_total, figus_paquete), bins=200)
plt.show()