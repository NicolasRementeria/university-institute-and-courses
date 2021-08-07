# Ejercicio 3.6: Contar

#%%
for n in range(10):            # Contar 0 ... 9
    print(n, end=' ')

#%%
# 0 1 2 3 4 5 6 7 8 9
for n in range(10,0,-1):       # Contar 10 ... 1
    print(n, end=' ')

# 10 9 8 7 6 5 4 3 2 1

#%%
for n in range(0,10,2):        # Contar 0, 2, ... 8
    print(n, end=' ')

#0 2 4 6 8

# %%

# Ejercicio 3.7: Más operaciones con secuencias

data = [4, 9, 1, 25, 16, 100, 49]
min(data)
# 1
max(data)
# 100
sum(data)
# 204

# %%

# Probá iterar sobre los datos.

for x in data:
    print(x)

# 4
# 9
# ...

for n, x in enumerate(data):
    print(n, x)

# 0 4
# 1 9
# 2 1
# ...


# %%

for n in range(len(data)):
    print(data[n])

# 4
# 9
# 1
# ...

# %%
