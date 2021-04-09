# Ejercicio 5.3: Envido

# https://github.com/python-unsam/Programacion_en_Python_UNSAM/blob/master/Notas/05_Random_Plt_Dbg/01_Random.md#ejercicio-53-envido

import random
import copy
from collections import Counter

# posibilidades_un_palo = [carta for carta in naipes if "oro" in carta]

# [carta for carta in posibilidades_un_palo if 7 in carta  or 6 in carta

# def repartir(naipes):
#     naipes_aux = copy.copy(naipes)
#     random.shuffle(naipes_aux)
#     mano = naipes_aux[:3]
#     mazo = naipes_aux[3:]
#     return {"mano": mano, "mazo": mazo}

### Analisis Envido 31

def se_puede_cantar_envido(mano):
    tipos_distintos = list(set([carta[1] for carta in mano]))
    if len(tipos_distintos) >= 2:
        return True
    else:
        return False

# def eliminar_carta_solitaria(mano):
#     if mano[0][1] == mano[1][1]:
#         mano.pop(2)
#     if mano[0][1] == mano[2][1]:
#         mano.pop(1)
#     else:
#         mano.pop(0)
        
def cartas_mismo_palo(mano):
    cartas = {}
    for valor, tipo in mano:
        if tipo in cartas:
            cartas[tipo].append(valor)
        else:
            cartas[tipo] = [valor]
    if len(cartas) == 2:
        #clave_carta_unica = min(cartas, key=cartas.get)
        #clave_carta_unica = min(cartas.items())[0]
        clave_carta_unica = [tipo for tipo in list(cartas.keys()) if len(cartas[tipo]) == 1][0]
        cartas.pop(clave_carta_unica)
        return cartas
    else:
        return cartas


def reemplazo_figuras(cartas, tipo):
        return [0 if carta == 10 or carta == 11 or carta == 11 else carta for carta in cartas[tipo]]

def es_envido_31(mano):
    canto_31 = False
    if se_puede_cantar_envido(mano):
        cartas = cartas_mismo_palo(mano)
        tipo_carta = list(cartas.keys())[0]
        cartas = reemplazo_figuras(cartas, tipo_carta)
        suma = sum(cartas) + 20
        if suma == 31:
            canto_31 = True
        else:
            canto_31 = False
    return canto_31

def crear_mazo_mezclado():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    random.shuffle(naipes)
    return naipes

def obtener_mano(naipes):
    return naipes[-3:]

def probar_envido_31():
    naipes = crear_mazo_mezclado()
    mano = obtener_mano(naipes)
    return es_envido_31(mano)

N = 10000
G = sum([probar_envido_31() for i in range(N)])
prob = G/N
print(f'Probé {N} veces a jugar una mano en {N} mazos nuevos, de las cuales {G} saqué envido 31')
print(f'Podemos estimar la probabilidad de envido en una mano es {prob:.6f}.')



# ### Analisis Envido 32
# valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
# palos = ['oro', 'copa', 'espada', 'basto']
# naipes = [(valor,palo) for valor in valores for palo in palos]

def es_envido_32(mano):
    canto_32 = False
    if se_puede_cantar_envido(mano):
        cartas = cartas_mismo_palo(mano)
        tipo_carta = list(cartas.keys())[0]
        cartas = reemplazo_figuras(cartas, tipo_carta)
        suma = sum(cartas) + 20
        if suma == 32:
            canto_32 = True
        else:
            canto_32 = False
    return canto_32

def probar_envido_32():
    naipes = crear_mazo_mezclado()
    mano = obtener_mano(naipes)
    return es_envido_32(mano)

N = 10000
G = sum([probar_envido_32() for i in range(N)])
prob = G/N
print(f'Probé {N} veces a jugar una mano en {N} mazos nuevos, de las cuales {G} saqué envido 32')
print(f'Podemos estimar la probabilidad de envido en una mano es {prob:.6f}.')

# ### Analisis Envido 33
# valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
# palos = ['oro', 'copa', 'espada', 'basto']
# naipes = [(valor,palo) for valor in valores for palo in palos]

def es_envido_33(mano):
    canto_33 = False
    if se_puede_cantar_envido(mano):
        cartas = cartas_mismo_palo(mano)
        tipo_carta = list(cartas.keys())[0]
        cartas = reemplazo_figuras(cartas, tipo_carta)
        suma = sum(cartas) + 20
        if suma == 33:
            canto_33 = True
        else:
            canto_33 = False
    return canto_33

def probar_envido_33():
    naipes = crear_mazo_mezclado()
    mano = obtener_mano(naipes)
    return es_envido_33(mano)

N = 10000
G = sum([probar_envido_33() for i in range(N)])
prob = G/N
print(f'Probé {N} veces a jugar una mano en {N} mazos nuevos, de las cuales {G} saqué envido 33')
print(f'Podemos estimar la probabilidad de envido en una mano es {prob:.6f}.')