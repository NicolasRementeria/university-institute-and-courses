types = [str, int, float]

# >>> types
# [<class 'str'>, <class 'int'>, <class 'float'>]

import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

# >>> row
# ['Lima', '100', '32.2']

types[1](row[1])

# >>> types[1](row[1])
# 100

types[2](row[2])

# >>> types[2](row[2])
# 32.2

types[1](row[1])*types[2](row[2])

# >>> types[1](row[1])*types[2](row[2])
# 3220.0000000000005

r = list(zip(types, row))

# >>> r
# [(<class 'str'>, 'Lima'), (<class 'int'>, '100'), (<class 'float'>, '32.2')]

converted = []


# Por cada funcion en types, aplicar dicha funcion correspondiente en la tupla por cada 
# valor en row

for func, val in zip(types, row):
    converted.append(func(val))

converted
converted[1] * converted[2]

# >>> converted
# ['Lima', 100, 32.2]
# >>> converted[1] * converted[2]
# 3220.0000000000005

# types = [str, int, float]
# row = ["Lima", "100", "32.2"]
# zip = [(str, "Lima"), (int, "100"), (float, "32.2")]

# >>> zip(types, row) 
# <zip object at 0x01A8ABE8>
# >>> list(zip(types, row))
# [(<class 'str'>, 'Lima'), (<class 'int'>, '100'), (<class 'float'>, '32.2')]

# Elemento 0 en tupla == func
# Elemento 1 en tupla == val

# >>> list(zip(types, row))[0] 
# (<class 'str'>, 'Lima')


# Alternativa usando comprension de listas:

converted = [func(val) for func, val in zip(types, row)]

# converted
# ['Lima', 100, 32.2]
