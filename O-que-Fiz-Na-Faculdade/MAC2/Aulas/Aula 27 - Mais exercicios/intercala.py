
def intercala(listas):
    '''
    [[]] -> []
    Recebe uma lista A com k listas ordenadas que somam n itens. Devolve
    a lista A modificada como uma única lista ordenada com os n itens.
    '''
    while len(listas) > 1:
        i, j = 0, 0
        lista_A, lista_B = listas.pop(0), listas.pop(0)
        temp_lista = []
        while i < len(lista_A) and j < len(lista_B):
            if lista_A[i] <= lista_B[j]:
                temp_lista.append(lista_A[i])
                i += 1
            else:
                temp_lista.append(lista_B[j])
                j += 1
        while i < len(lista_A):
            temp_lista.append(lista_A[i])
            i += 1
        while j < len(lista_B):
            temp_lista.append(lista_B[j])
            j += 1
        listas.append(temp_lista)
    return listas.pop()


intercala([[1,2,5,8],[0,3,3,6],[2,8,9]])            


    