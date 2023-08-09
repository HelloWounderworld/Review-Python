
''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Maximo: versão recursiva que encontra o maior elemento de 
           um lista.
'''

def maximoR(n,v):
    '''(int,list) -> item

    Recebe um inteiro positivo n e uma lista v e retorna 
    o maior elemento das n primeiras posições.
    '''
    if n == 1:
        return v[0]
    else:
        x = maximoR(n-1,v)
        if x > v[n-1]:
            return x
        else:
            return v[n-1]

        
