def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return 1
        else:
            return 0
    else:
        transpos = 0
        lista = []
        esquerda = 0
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
                transpos = transpos + len(v[esquerda:m])
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return transpos

def bubble(lista):   
    transposicao = 0
    for i in range(0,len(lista)):
        for j in range(0,len(lista)-1):
            if lista[j] > lista[j+1]:
                x = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = x
                transposicao += 1
    return transposicao

def intercala(v, e, m, d):
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return v
        else:
            return v
    else:
        lista = []
        esquerda = 0
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return v

def mergesort(v,e,d):
    if e < d-1:
        m = (d+e)//2
        mergesort(v,e,m)
        mergesort(v,m,d)
        intercala(v,e,m,d)
    
def main():
    A = [3,  7, 10, 14, 18]
    B = [2, 11, 16, 20, 23]
    C = A + B
    D = A+B
    print(C)
    print(mergeX(C,0,5,10))
    print(bubble(D))
    A = [6,7,8,9,10,1,2,3,4,5]
    B = A[:]
    print(A)
    print(mergeX(A,0,5,10))
    print(bubble(B))
    V = [10, 14, 18, 7, 3, 20, 23, 11, 2, 16]
    print(V)
    print(bubble(V))
    V = [10, 14, 18, 7, 3, 20, 23, 11, 2, 16]
    mergesort(V,0,len(V))
    print(V)
main()
    
    
    

