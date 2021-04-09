import random
import numpy as np

# Datos:

# Álbum con 670 figuritas.
# Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
# Cada paquete trae cinco figuritas.

# si tuviéramos un álbum de seis figuritas vacío lo vamos a 
# representar como [0 0 0 0 0 0]
# Cuando consigamos la figurita 3 tendremos que indicarlo poniendo un 
# 1 en el tercer lugar de la lista, es decir album[2]=1 y el álbum 
# nos va a quedar [0 0 1 0 0 0], y si queremos representar que nos 
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
    pass