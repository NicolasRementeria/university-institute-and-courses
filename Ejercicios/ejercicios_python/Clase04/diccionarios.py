import csv

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, int, float]
converted = [func(val) for func, val in zip(types, row)]

dict(zip(headers, converted))

# >>> dict(zip(headers, converted))
# {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}

# ALTERNATIVA:

{ name: func(val) for name, func, val in zip(headers, types, row) }

# >>> { name: func(val) for name, func, val in zip(headers, types, row) }
# {'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}