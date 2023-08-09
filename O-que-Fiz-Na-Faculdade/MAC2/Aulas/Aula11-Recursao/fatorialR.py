''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Fatorial: versão recursiva mais simples
'''

def fatorial(n):
    '''(int) -> int
   
    Recebe um inteiro n e retorna n!.
    '''
    if n == 0:
        return 1
    return n * fatorial(n-1)
