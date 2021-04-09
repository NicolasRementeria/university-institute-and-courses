# Ejercicio 5.5: Gaussiana

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/01_Random.md#ejercicio-55-gaussiana

# import random
# 
# n = 99
# media = 37.5
# 
# # for i in range(n):
# #     print(f"{random.normalvariate(media, 0.2):.2f}", end=", ")
# 
# termometro = [random.normalvariate(media, 0.2) for i in range(n)]
# 
# minimo = min(termometro)
# maximo = max(termometro)
# promedio = sum(termometro) / n
# media = sorted(termometro)[int(len(termometro)/2)]
# 
# print(f"Minimo: {minimo} | Maximo: {maximo} | Promedio: {promedio} | Media: {media}")
# 
# from matplotlib import pyplot as plt
# 
# # plt.plot(termometro)
# plt.hist(termometro, bins = 200)
# plt.show()

# termometro = [random.gauss(media, 0.2) for i in range(n)]
# 
# plt.plot(termometro)
# plt.show()

# plt.hist(termometro)
# plt.show()

##################

# Ejercicio 5.7: Guardar temperaturas

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/02_NumPy_Arrays.md#ejercicio-57-guardar-temperaturas

import random
import numpy as np

n = 999
media = 37.5

# for i in range(n):
#     print(f"{random.normalvariate(media, 0.2):.2f}", end=", ")

termometro = [random.normalvariate(media, 0.2) for i in range(n)]

minimo = min(termometro)
maximo = max(termometro)
promedio = sum(termometro) / n
media = sorted(termometro)[int(len(termometro)/2)]

print(f"Minimo: {minimo} | Maximo: {maximo} | Promedio: {promedio} | Media: {media}")

np.save('../Data/Temperaturas.npy', termometro)