# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/02_Secuencias.md#ejercicio-38-un-ejemplo-pr%C3%A1ctico-de-enumerate

# Ejercicio 3.8

#%%

# import csv
# 
# def costo_camion(csv_file):
#     costo_total = 0
#     raw_file = open(csv_file, "r")
#     file_content = csv.reader(raw_file)
#     next(file_content) # Remove first item of csv, that will remove the headers
#     for n_fila, item in enumerate(file_content, start=1):
#         try:
#             cajones_item = int(item[1])
#             precio_item = float(item[2])
#             costo_total += cajones_item * precio_item
#         except:
#             print(f"Fila {n_fila}: No pude interpretar: {item}")
#     raw_file.close()
#     return costo_total
# 
# costo = costo_camion('../Data/missing.csv')
# print('Costo total:', costo)
# %%

# Output:

# Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
# Fila 7: No pude interpretar: ['Naranja', '', '70.44']
# Costo total: 30381.15

######################


# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/02_Secuencias.md#ejercicio-39-la-funci%C3%B3n-zip

# Ejercicio 3.9

#%%

import csv

def costo_camion(csv_file):
    costo_total = 0
    raw_file = open(csv_file, "r")
    file_content = csv.reader(raw_file)
    encabezados = next(file_content) # Remove first item of csv, that will remove the headers
    for n_fila, fila in enumerate(file_content, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    raw_file.close()
    return costo_total

costo = costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)

# Output:

# Costo total: 47671.15
# Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
# Fila 7: No pude interpretar: ['Naranja', '', '70.44']
# Costo total: 30381.15
# Costo total: 47671.15

# %%
