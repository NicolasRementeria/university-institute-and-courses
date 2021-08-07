#### Ejercicio 3.17

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/05_Formato.md#ejercicio-317-tablas-de-multiplicar


# Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings. 
# Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.
# 
#        0   1   2   3   4   5   6   7   8   9
# ---------------------------------------------
#  0:    0   0   0   0   0   0   0   0   0   0
#  1:    0   1   2   3   4   5   6   7   8   9
#  2:    0   2   4   6   8  10  12  14  16  18
#  3:    0   3   6   9  12  15  18  21  24  27
#  4:    0   4   8  12  16  20  24  28  32  36
#  5:    0   5  10  15  20  25  30  35  40  45
#  6:    0   6  12  18  24  30  36  42  48  54
#  7:    0   7  14  21  28  35  42  49  56  63
#  8:    0   8  16  24  32  40  48  56  64  72
#  9:    0   9  18  27  36  45  54  63  72  81

from pprint import pprint

def mult(numero, multiplicador):
    resultado = 0
    while multiplicador > 0:
        resultado += numero
        multiplicador -= 1
    return resultado

def fila_multiplicacion(numero):
    dicc_numero = {0: 0, 1: 0, 2: 0, 3: 0,4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for m in range(0, 10):
        dicc_numero[m] = mult(numero, m)
    return dicc_numero

def tabla_multiplicacion():
    tabla_resultado = []
    for m in range(0, 10):
        tabla_resultado.append(fila_multiplicacion(m))
    return tabla_resultado

def formatear_tabla(tabla):
    tabla_aux = []
    for multiplo in tabla:
        multiplo_en_0 = multiplo[0]
        multiplo_en_1 = multiplo[1]
        multiplo_en_2 = multiplo[2]
        multiplo_en_3 = multiplo[3]
        multiplo_en_4 = multiplo[4]
        multiplo_en_5 = multiplo[5]
        multiplo_en_6 = multiplo[6]
        multiplo_en_7 = multiplo[7]
        multiplo_en_8 = multiplo[8]
        multiplo_en_9 = multiplo[9]
        tupla_multiplo = (multiplo_en_0, multiplo_en_1, multiplo_en_2, multiplo_en_3, multiplo_en_4, multiplo_en_5, multiplo_en_6, multiplo_en_7, multiplo_en_8, multiplo_en_9)
        tabla_aux.append(tupla_multiplo)
    header = f'{0:>9d} {1:>4d} {2:>4d} {3:>4d} {4:>4d} {5:>4d} {6:>4d} {7:>4d} {8:>4d} {9:>4d}'
    lineas = f'{"---------------------------------------------":>52s}'
    print(header, "\n", lineas)
    count = 0
    for multiplo_en_0, multiplo_en_1, multiplo_en_2, multiplo_en_3, multiplo_en_4, multiplo_en_5, multiplo_en_6, multiplo_en_7, multiplo_en_8, multiplo_en_9 in tabla_aux:
        print(f'{count:>2d}: {multiplo_en_0:>5d} {multiplo_en_1:>4d} {multiplo_en_2:>4d} {multiplo_en_3:>4d} {multiplo_en_4:>4d} {multiplo_en_5:>4d} {multiplo_en_6:>4d} {multiplo_en_7:>4d} {multiplo_en_8:>4d} {multiplo_en_9:>4d}')
        count += 1



tabla = tabla_multiplicacion()

formatear_tabla(tabla)

# Output:

# >>> formatear_tabla(tabla)
#         0    1    2    3    4    5    6    7    8    9 
#         ---------------------------------------------
#  0:     0    0    0    0    0    0    0    0    0    0
#  1:     0    1    2    3    4    5    6    7    8    9
#  2:     0    2    4    6    8   10   12   14   16   18
#  3:     0    3    6    9   12   15   18   21   24   27
#  4:     0    4    8   12   16   20   24   28   32   36
#  5:     0    5   10   15   20   25   30   35   40   45
#  6:     0    6   12   18   24   30   36   42   48   54
#  7:     0    7   14   21   28   35   42   49   56   63
#  8:     0    8   16   24   32   40   48   56   64   72
#  9:     0    9   18   27   36   45   54   63   72   81