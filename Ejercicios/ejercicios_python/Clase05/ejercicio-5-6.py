# Ejercicio 5.6: arange() y linspace()

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/02_NumPy_Arrays.md#ejercicio-56-arange-y-linspace

import numpy as np

np.arange(1, 20)

# Output:

# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#       18, 19])

np.linspace(1, 19, dtype=np.int64, axis=1)

# Output:

# array([ 1,  1,  1,  2,  2,  2,  3,  3,  3,  4,  4,  5,  5,  5,  6,  6,  6,
#         7,  7,  7,  8,  8,  9,  9,  9, 10, 10, 10, 11, 11, 12, 12, 12, 13,
#        13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 19],
#       dtype=int64)

