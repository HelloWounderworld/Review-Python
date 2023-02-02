def pertence(item,lista):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

def indice(item,lista):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None # None = vazio, nenhum, nada

