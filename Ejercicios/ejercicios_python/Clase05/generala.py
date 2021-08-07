# Ejercicio 5.1: Generala servida
# 
# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/01_Random.md#ejercicio-51-generala-servida
 

import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada

def es_generala(tirada):
    generala = True
    for dado in tirada:
        if dado != tirada[0]:
            generala = False
    return generala


N = 100000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala ervida.   ')
print(f'Podemos estimar la probabilidad de sacar generala ervida mediante {prob:.6f}.')



# Ejercicio 5.2: Generala no necesariamente servida

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/01_Random.md#ejercicio-52-generala-no-necesariamente-servida

def generala_servida_en_3_tiradas():
    G = sum([es_generala(tirar()) for i in range(3)])
    return True if G > 0 else False


N = 100000
G = sum([generala_servida_en_3_tiradas() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala ervida.')
print(f'Podemos estimar la probabilidad de sacar generala servida en rondas de 3 tiradas mediante {prob:.6f}.')

# RTA:

# Hay hasta 3 veces mas de probabilidad de obtener generala servida con 3 tiradas por jugada.

# Output:
# $ python -i generala.py 
# Tiré 1000000 veces, de las cuales 786 saqué generala servida.
# Podemos estimar la probabilidad de sacar generala servida # mediante 0.000786.
# Tiré 1000000 veces, de las cuales 2309 saqué generala servida.
# Podemos estimar la probabilidad de sacar generala servida en # rondas de 3 tiradas mediante 
# 0.002309.

# EXTRA:

# Hay gente que, si en la primera tirada le salen todos dados diferentes, los mete al cubilete y tira los cinco nuevamente. Otras personas, eligen uno de esos dados diferentes, lo guardan, y tiran sólo los cuatro restantes. ¿Podés determinar, por medio de simulaciones, si hay una de estas estrategias que sea mejor que la otra?

def son_todos_distintos(tirada):
    return not all(dado == tirada[0] for dado in tirada)

def tirar_4():
    tirada = []
    for i in range(4):
        tirada.append(random.randint(1, 6))
    return tirada

def generala_3_tiradas_inteligente():
    tirada = tirar()
    if son_todos_distintos(tirada):
        cabecera = tirada[0]
        resto = tirar_4()
        if son_todos_distintos([cabecera] + resto):
            resto = tirar_4()
            if son_todos_distintos([cabecera] + resto):
                return False
    return True

N = 100000
G = sum([generala_3_tiradas_inteligente() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala ervida.')
print(f'Podemos estimar la probabilidad de sacar generala en rondas de 3 de forma inteligente tiradas mediante {prob:.6f}.')

# Output:

# $ python -i generala.py 
# Tiré 100000 veces, de las cuales 75 saqué generala ervida.   
# Podemos estimar la probabilidad de sacar generala ervida mediante 0.000750.
# Tiré 100000 veces, de las cuales 221 saqué generala ervida.
# Podemos estimar la probabilidad de sacar generala servida en rondas de 3 tiradas mediante 0.002210.
# Tiré 100000 veces, de las cuales 217 saqué generala ervida.
# Podemos estimar la probabilidad de sacar generala en rondas de 3 de forma inteligente tiradas mediante 0.002170.

# RTA del EXTRA: Las probabilidades son iguales de sacar generala servida que de tomar un dado y tirar los otros 4 probandolo dos veces