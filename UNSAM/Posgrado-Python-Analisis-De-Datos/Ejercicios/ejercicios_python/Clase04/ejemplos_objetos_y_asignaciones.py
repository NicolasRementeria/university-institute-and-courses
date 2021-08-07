# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/04_Listas_y_Listas/04_Objetos.md#44-objetos

a = [1,2,3]
b = a
c = [a,b]

a.append(999)

# >>> a
# [1, 2, 3, 999]
# >>> b
# [1, 2, 3, 999]
# >>> c
# [[1, 2, 3, 999], [1, 2, 3, 999]]

# Son todos punteros de "a", por eso al modificarse "a", tambien se modifican "b" y "c"

b.append(0)

# >>> a
# [1, 2, 3, 999, 0]
# >>> b
# [1, 2, 3, 999, 0]
# >>> c
# [[1, 2, 3, 999, 0], [1, 2, 3, 999, 0]]

# La reasignación de valores nunca sobreescribe la memoria ocupada por un valor anterior.

a = [1, 2, 3]
b = a
a = [4, 5, 6]

print(a)
print(b)

# >>> print(a)
# [4, 5, 6]
# >>> print(b)
# [1, 2, 3]

# Podés usar el operador is (es) para verificar si dos valores corresponden al mismo objeto.

a = [1, 2, 3]
b = a
a is b

# >>> a is b
# True

# is compara la identidad del objeto (que está representada por un número entero). 
# Esta # identidad también la podés obtener usando id().

id(a)
id(b)

# >>> id(a)
# 34834856
# >>> id(b)
# 34834856

# Observación: Para ver si dos valores son iguales, es mejor usar el ==. 
# El comportamiento de is puede dar resultados inesperados:

a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b
a is c
a == c

# >>> a is b
# True
# >>> a is c
# False
# >>> a == c
# True

#########


# Copias superficiales
 
# Las listas y diccionarios tienen métodos para hacer copias 
# (no meras referencias, sino duplicados):

a = [2, 3, [100, 101], 4]
b = list(a) # Hacer una copia
a is b

# >>> a  is b
# False

# Ahora b es una nueva lista.

a.append(5)

# >>> a
# [2, 3, [100, 101], 4, 5]
# >>> b
# [2, 3, [100, 101], 4]

# A pesar de esto, los elementos de a y de b siguen siendo compartidos.

a[2].append(102)
b[2]

# >>> b[2]
# [100, 101, 102]

a[2] is b[2]

# >>> a[2] is b[2]
# True

# En este ejemplo, la lista interna [100, 101, 102] es compartida por ambas variables. 
# La copia que hicimos con el comando b = list(a) es un copia superficial 
# (superficial en el sentido de poco profunda, en inglés se dice shallow copy). 

#######

# Copias Profundas

# A veces vas a necesitar hacer una copia de un objeto así como de todos los objetos que 
# contenga. Llamamos a esto una copia pofunda (deep copy). 
# Podés usar la función deepcopy del módulo copy para esto:

a = [2, 3, [100, 101], 4]

import copy

b = copy.deepcopy(a)
a[2].append(102)
b[2]
a[2] is b[2]

# >>> b[2]
# [100, 101]
# >>> a[2] is b[2]
# False

######

# Verificación de tipos

a = 42
b = "Hello World"

if isinstance(a, list):
    print("a es una lista")

if isinstance(a, (list, tuple)):
    print("a es una lista o una tupla")