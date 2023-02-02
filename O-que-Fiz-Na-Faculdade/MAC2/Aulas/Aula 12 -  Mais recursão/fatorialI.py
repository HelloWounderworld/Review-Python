''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Fatorial: versão iterativa
'''

def fatorial(n):
    '''(int) -> int
   
    Recebe um inteiro n e retorna n!.
    '''
    fat = 1
    i = 2
    while i <= n:
        fat *= i
        i += 1
    return fat
