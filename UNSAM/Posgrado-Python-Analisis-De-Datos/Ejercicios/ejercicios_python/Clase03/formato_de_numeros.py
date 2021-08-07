# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/03_Datos/05_Formato.md#ejercicio-312-formato-de-n%C3%BAmeros

# Ejercicio 3.12

# Un problema usual cuando queremos imprimir números es especificar el número de dígitos decimales. Los f-strings nos permiten hacerlo. Probá los siguientes ejemplos:
# 
# >>> value = 42863.1
# >>> print(value)
# 42863.1
# >>> print(f'{value:0.4f}')
# 42863.1000
# >>> print(f'{value:>16.2f}')
#         42863.10
# >>> print(f'{value:<16.2f}')
# 42863.10
# >>> print(f'{value:*>16,.2f}')
# *******42,863.10
# >>>

value = 42863.1
print(value)

print(f'{value:0.4f}')

print(f'{value:<16.2f}')

print(f'{value:*>16,.2f}')

# La documentación completa sobre los códigos de formato usados en f-strings puede consultarse acá. El formato puede aplicarse también usando el operador % de cadenas.

# >>> print('%0.4f' % value)
# 42863.1000
# >>> print('%16.2f' % value)
#         42863.10
# >>>

print('%0.4f' % value)

print('%16.2f' % value)

# La documentación sobre códigos usados con % puede encontrarse acá.
# 
# A pesar de que suelen usarse dentro de un print, el formato de cadenas no está necesariamente ligado a la impresión. Por ejemplo, podés simplemente asignarlo a una variable.
# 
# >>> f = '%0.4f' % value
# >>> f
# '42863.1000'
# >>>

f = '%0.4f' % value
print(f)