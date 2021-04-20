def incrementar(s):
    carry = 1
    l = len(s)
    for i in range(l-1, -1, -1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    # n es la longitud
    s = [0]*n
    lista = []
    lista.append(s)
    contador = 0
    cantidad = (2**n)-1
    while contador < cantidad:
        s = incrementar(s)
        contador = contador+1
        copia = s.copy()
        lista.append(copia)
    return lista

listar_secuencias(5)
listar_secuencias(15)
listar_secuencias(20)
