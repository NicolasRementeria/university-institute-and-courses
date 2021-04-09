#### Ejercicio 5.24: Histograma de altos de Jacarandás

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/04_Arboles3_plt.md#ejercicio-524-histograma-de-altos-de-jacarand%C3%A1s


import csv
import os
from matplotlib import pyplot as plt

def leer_parque(nombre_archivo, parque):
    archivo = open(nombre_archivo, "r", encoding="UTF-8")
    csv_file = csv.reader(archivo)
    informacion_parque = []
    headers = next(csv_file)
    for item in csv_file:
        if(parque in item):
            informacion_parque.append(dict(zip(headers, item)))
    return informacion_parque


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "r", encoding="UTF-8") as archivo:
        csv_file = csv.reader(archivo)
        headers = next(csv_file)
        lista_arboles = [{header: value for header, value in zip(headers, fila)} for fila in csv_file]
    return lista_arboles    

# parque = leer_parque("../Data/arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
# arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
# 
# lista_alturas_jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
plt.hist(altos,bins=200)
plt.show()

##########

# Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/04_Arboles3_plt.md#ejercicio-525-scatterplot-di%C3%A1metro-vs-alto-de-jacarand%C3%A1s

import numpy as np

lista_tuplas_alturas_y_diametro_jacaranda = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

numpy_tuplas_alturas_y_diametro_jacaranda = np.array(lista_tuplas_alturas_y_diametro_jacaranda)

d = numpy_tuplas_alturas_y_diametro_jacaranda[:,0]
h = numpy_tuplas_alturas_y_diametro_jacaranda[:,1]

colors = np.random.rand(len(numpy_tuplas_alturas_y_diametro_jacaranda))

plt.scatter(d,h, alpha=1, c=colors, s=35)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.grid()
plt.show()

##########

# Ejercicio 5.26: Scatterplot para diferentes especies

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/04_Arboles3_plt.md#ejercicio-526-scatterplot-para-diferentes-especies


# def medidas_de_especies(especies,arboleda):
#     '''Simil Oneliner, sin creacion de registro, pero aun con un for que recorre cada especie'''
#     dicc_medidas = {}
#     for especie in especies:
#         dicc_medidas = {dicc_medidas[especie]: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol["nombre_com"] == especie]}
#     return dicc_medidas

def medidas_de_especies(especies, arboleda):
    '''Otra forma de crear el registro'''
    dicc_medidas = {}  
    for especie in especies:
        registro=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
        dicc_medidas[especie]=registro
    return dicc_medidas

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

for tipo_arbol in list(medidas.keys()):
    tupla_altura_diametro = np.array(medidas[tipo_arbol])
    d = tupla_altura_diametro[:,0]
    h = tupla_altura_diametro[:,1]
    colors = np.random.rand(len(medidas[tipo_arbol]))
    plt.scatter(d,h, alpha=1, c=colors, s=35)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {tipo_arbol}")
    plt.xlim(0,30) 
    plt.ylim(0,100)
    plt.grid()
    plt.show()

data_1 = np.array(medidas[especies[0]])
d1 = data_1[:,0]
h1 = data_1[:,1]
data_2 = np.array(medidas[especies[1]])
d2 = data_2[:,0]
h2 = data_2[:,1]
data_3 = np.array(medidas[especies[2]])
d3 = data_3[:,0]
h3 = data_3[:,1]



plt.scatter(d1,h1, alpha=1)
plt.scatter(d2,h2, alpha=1)
plt.scatter(d3,h3, alpha=1)
plt.legend([especies[0], especies[1], especies[2]])
# plt.xlim(0,30) 
# plt.ylim(0,100) 
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title(f"Relación diámetro-alto para {especies}")
plt.show()