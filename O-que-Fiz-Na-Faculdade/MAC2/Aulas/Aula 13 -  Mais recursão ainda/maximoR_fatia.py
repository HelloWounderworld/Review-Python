''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Maximo: versão recursiva com fatia. 
           consumo de tempo é quadrático
'''

def maximoR(v):
    '''(list) -> item

    Recebe inteiros positivos i e n e uma lista v e retorna 
    o maior elemento das posições de índices entre i e n-1.
    '''
    n = len(v)
    if n == 1: return v[0]
    x = maximoR(v[0:n-1])
    if x > v[n-1]: return x
    return v[n-1]

#------------------------------------------------------
def maximo(v):
    '''(list) -> item

    Recebe uma lista v e retorna o maior elemento
    da lista.
    '''
    # pegue o comprimento da lista
    n = len(v)

    # retorne o maior elemento
    return maximoR(v)
        
