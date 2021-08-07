# rebotes.py
# Archivo de ejemplo
# Ejercicio

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/01_Introduccion/06_CierreClase.md

# Ejercicio 1.5

altura = 100
rebotes = 10
count = 1

# Version sin round() con 4 digitos

#while rebotes >= count:
#    altura *= 3/5
#    print(count, altura)
#    count += 1

# Version con round() con 4 digitos

while rebotes >= count:
    altura *= 3/5
    print(count, round(altura, 4))
    count += 1