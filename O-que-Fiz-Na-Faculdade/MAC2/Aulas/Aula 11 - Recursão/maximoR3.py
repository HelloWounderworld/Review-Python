''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Maximo: versão recursiva que encontra o maior elemento de 
           um lista.
'''

def maximoR(i,n,v):
    '''(int,int,list) -> item

    Recebe inteiros positivos i e n e uma lista v e retorna 
    o maior elemento das posições de índices entre i e n-1.
    '''
    if i == n-1:
        return v[i]
    x = maximoR(i+1,n,v)
    if x > v[i]:
        return x
    return v[i]

#------------------------------------------------------
def maximo(v):
    '''(list) -> item

    Recebe uma lista v e retorna o maior elemento
    da lista.
    '''
    # pegue o comprimento da lista
    n = len(v)

    # retorne o maior elemento
    return maximoR(0,n,v)
        
