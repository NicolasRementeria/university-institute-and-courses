import numpy as np

a = np.array([1, 2, 3])

# >>> a
# array([1, 2, 3])

np.zeros(2)

# >>> np.zeros(2)
# array([0., 0.])

np.ones(2)

# >>> np.ones(2)
# array([1., 1.])

###### np.empty es mas rapido para inicializar una lista ya que cada valor es aleatorio basado en el estado de la memoria
np.empty(2)

# >>> np.empty(2)
# array([1., 1.])

# arange crea un vector a partir de un rango
np.arange(4)

# >>> np.arange(4)
# array([0, 1, 2, 3])

###### También un vector que contiene elementos equiespaciados, 
###### especificando el primer número, el límite, y el paso.
###### El límite derecho nunca está en la lista.

np.arange(2, 9, 2)

# >>> np.arange(2, 9, 2) # o np.arange(2, 10, 2)
# array([2, 4, 6, 8])

###### También podés usar np.linspace() para crear un vector especificando 
###### el primer número, el último número, y la cantidad de elementos:

np.linspace(0, 10, num=5)

# >>> np.linspace(0, 10, num=5)
# array([ 0. ,  2.5,  5. ,  7.5, 10. ])

###### Ordenar Arreglo

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

np.sort(arr)

# >>> np.sort(arr)
# array([1, 2, 3, 4, 5, 6, 7, 8])

###### Concatenacion:

a = np.array([1, 2, 3, 4])

b = np.array([5, 6, 7, 8])

np.concatenate((a, b))

# >>> np.concatenate((a, b))
# array([1, 2, 3, 4, 5, 6, 7, 8])

###### Concatenar array mas complejo:

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

np.concatenate((x, y), axis=0)

# array([[1, 2],
#        [3, 4],
#        [5, 6]])

###### Conocer tamaños, dimensiones y forma de un arreglo
array_ejemplo = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

## Cantidad de dimensiones
array_ejemplo.ndim
# 3

## Cantidad de elementos en cada eje
array_ejemplo.shape
# (3, 2, 4)

## total de elementos 3*2*4
array_ejemplo.size
# 24

###### Cambiar la forma de un arreglo

a = np.arange(6)
# array([0, 1, 2, 3, 4, 5])

b = a.reshape(3, 2)
# array([[0, 1],
#        [2, 3],
#        [4, 5]])

###### Agregar un nuevo eje al arreglo

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
# (6,)

## Nueva fila
vec_fila = a[np.newaxis, :]
vec_fila.shape
# (1, 6)

## Nueva columna
vec_col = a[:, np.newaxis]
vec_col.shape
# (6, 1)



###### Indices y slices

data = np.array([1, 2, 3])

data[1]
# 2
data[0:2]
# array([1, 2])
data[1:]
# array([2, 3])
data[-2:]
# array([2, 3])

###### Seleccionar por condicion

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a < 5])
# [1 2 3 4]

five_up = (a >= 5)

print(five_up)
# array([[False, False, False, False],
#        [ True,  True,  True,  True],
#        [ True,  True,  True,  True]])

print(a[five_up])
# [ 5  6  7  8  9 10 11 12]

c = a[(a > 2) & (a < 11)]
print(c)
# [ 3  4  5  6  7  8  9 10]

five_up = (a > 5) | (a == 5)
print(five_up)
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True True]]

###### Obtener coordenadas basado en condiciones

b = np.nonzero(a < 5)
print(b)
# (array([0, 0, 0, 0], dtype=int32), array([0, 1, 2, 3], dtype=int32))

# El primer elemento representa las filas de los elementos que 
# satisfacen la condicion, y el segundo sus columnas

# Para obtener la lista de coordenadas:


lista_de_coordenadas = list(zip(b[0], b[1]))
# [(0, 0), (0, 1), (0, 2), (0, 3)]

## Usar np.nonzero() para imprimir o seleccionar elementos que 
# son menores a 5

print(a[b])
# [1 2 3 4]

## Si no satisface la condicion, el arreglo sera vacio

no_hay = np.nonzero(a == 42)
print(no_hay)
# (array([], dtype=int64), array([], dtype=int64))



###### Generar vistas de arreglos y nuevas copias

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
arr1 = a[3:8]
arr1
# array([4, 5, 6, 7, 8])

arr1[0] = 44
print(a)
# [ 1  2  3 44  5  6  7  8  9 10]

# "arr1" es una vista de "a", no es una nueva variable. Si se modifica 
# "arr1", tambien se modificará "a".

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
b1
# array([1, 2, 3, 4])
b1[0] = 99
b1
# array([99,  2,  3,  4])
a
# array([[99,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

## Metodo copy para crear una nueva variable, no una vista

b2 = a[1, :].copy()
b2
# array([5, 6, 7, 8])
b2[0] = 95
b2
# array([95,  6,  7,  8])
a
# array([[99,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

# Cambiar b2 NO modificó a "a"

###### Operaciones basicas sobre arreglos

data = np.array([1, 2])
# array([1, 2])
ones = np.ones(2, dtype=int)
# array([1, 1])
data + ones
# array([2, 3])

data - ones
# array([0, 1])
data * data
# array([1, 4])
data / data
# array([1., 1.])

a = np.array([1, 2, 3, 4])
a.sum()
# 10

## Sumar valores por fila o columna especificando el eje
b = np.array([[1, 1], [2, 2]])
# Suma columna:
b.sum(axis=0)
# array([3, 3])
# Suma fila:
b.sum(axis=1)
# array([2, 4])

###### Broadcasting, o cambiar todos los valores con un multiplo

data = np.array([1.0, 2.0])
data * 1.6
# array([1.6, 3.2])

###### Otras operaciones:

data.max()
# 2.0
data.min()
# 1.0
data.sum()
# 3.0

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

# Sumar absolutamente todos los valores

a.sum()
# 4.8595784

# Obtener el menor valor en todo el arreglo

a.min()
# 0.05093587

# Especificar el eje

# Columna:
a.min(axis=0)
# array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])

###### Crear matrices

data = np.array([[1, 2], [3, 4]])
# array([[1, 2],
#        [3, 4]])

data = np.array([[1, 2], [3, 4], [5, 6]])
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
data[0, 1]
# 2

data[1:3]
# array([[3, 4],
#        [5, 6]])

data[0:2, 0]
# array([1, 3])

data.max()
# 6
data.min()
# 1
data.sum()
# 21

## Procesar por fila
data.max(axis=0)
# array([5, 6])

## Procesar por columna
data.max(axis=1)
# array([2, 5, 6])

## Aritmetica con pares de matrices del mismo tamaño
data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
data + ones
# array([[2, 3],
#        [4, 5]])

## Sumar matrices de tamaños distintos es solo posible si una 
## de ellas es de una sola fila o columna.

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
data + ones_row
# array([[2, 3],
#        [4, 5],
#        [6, 7]])

###### Formulas matemáticas

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/02_NumPy_Arrays.md#f%C3%B3rmulas-matem%C3%A1ticas


###### Guardar y cargar objetos de numpy

## Util cuando uno quiere reutilizar objetos de numpy ya creados
## O que uno quiera guardar

a = np.array([1, 2, 3, 4, 5, 6])
np.save('filename', a)
# Creará un archivo en tu path actual con el nombre "filename.npy", 
# con el contenido de "a"

# Para cargar el archivo:

b = np.load('filename.npy')
b
# array([1, 2, 3, 4, 5, 6])


## Para guardarlo en  texto plano como .txt o .csv:

csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Salvar:
np.savetxt('new_file.csv', csv_arr)

# Cargar:

csv_loaded = np.loadtxt('new_file.csv')
csv_loaded
# array([1., 2., 3., 4., 5., 6., 7., 8.])

# Nota: Si bien los archivos de texto son sencillos para compartir, 
# los archivos .npy (y .npz) son más pequeños y se leen más 
# rápidamente.