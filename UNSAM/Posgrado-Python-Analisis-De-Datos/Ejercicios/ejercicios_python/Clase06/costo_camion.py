# Ejercicio 6.12: Un poco más allá

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/06_Organizaci%C3%B3n_y_Complejidad/04_Modulos.md#ejercicio-612-un-poco-m%C3%A1s-all%C3%A1

import informe_funciones as informe

# def costo_camion(csv_file):
#     costo_total = 0
#     raw_file = open(csv_file, "r")
#     file_content = raw_file.read().split('\n')[1:-1]
#     for item in file_content:
#         fila = item.split(",")
#         nombre_item = fila[0]
#         cajones_item = int(fila[1])
#         precio_item = float(fila[2])
#         costo_total += cajones_item * precio_item
#     raw_file.close()
#     return costo_total

def costo_camion(csv_file):
    costo_total = 0
    camion = informe.leer_camion(csv_file)
    for item in camion:
        costo_total += item['cajones'] * item['precio']
    return costo_total

# costo = costo_camion('../Data/camion.csv')
# print('Costo total:', costo)