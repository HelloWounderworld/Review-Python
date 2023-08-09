'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
  maximo divisor comum = algoritmo de Euclide, versao iterativa
'''

#-------------------------------------------
def euclidesI(m, n):
    '''(int, int) -> int
 
    Recebe inteiros não negativos m e n e retorna 
    o seu máximo divisor comum.

    Pré-condição: a função supões que n > 0.
    '''
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
        
    return n
