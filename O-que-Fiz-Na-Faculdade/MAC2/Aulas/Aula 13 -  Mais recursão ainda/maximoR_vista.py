''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Maximo: versão recursiva com array. 
           consumo de tempo é linear.
'''

def maximoR(v):
    '''(array) -> item

    Recebe inteiros positivos i e n e um array v e retorna 
    o maior elemento em v.
    '''
    n = len(v)
    if n == 1: return v[0]
    x = maximoR(v[0:n-1]) # vista
    if x > v[n-1]: return x
    return v[n-1]

#------------------------------------------------------
def maximo(v):
    '''(list) -> item

    Recebe uma lista v e retorna o maior elemento
    da lista.
    '''
    # pegue o comprimento do array
    n = len(v)

    # retorne o maior elemento
    return maximoR(n)
        
