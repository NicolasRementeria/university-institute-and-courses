import csv

f = open('../Data/dowstocks.csv')

rows = csv.reader(f)

headers = next(rows)

row = next(rows)

# >>> headers
# ['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
# >>> row
# ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']


types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func, val in zip(types, row)]

# >>> converted
# ['AA', 39.48, '6/11/2007', '9:36am', -0.18, 39.67, 39.69, 39.45, 181800]

record = dict(zip(headers, converted))

# >>> record
# {'name': 'AA', 'price': 39.48, 'date': '6/11/2007', 'time': '9:36am', 'change': -0.18, 
# 'open': 39.67, 'high': 39.69, 'low': 39.45, 'volume': 181800}

# >>> record["name"]
# 'AA'
# >>> record["price"] 
# 39.48

# Bonus: ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como 
# (6, 11, 2007)?

tuple(func(val) for func, val in zip((int, int, int), record["date"].split("/")))

# >>> tuple(func(val) for func, val in zip((int, int, int), record["date"].split("/")))
# (6, 11, 2007)