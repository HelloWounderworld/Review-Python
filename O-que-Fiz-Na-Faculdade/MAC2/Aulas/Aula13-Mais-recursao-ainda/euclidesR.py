'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   maximo divisor comum = algoritmo de Euclides - versao recursiva
'''



#---------------------------------------------------------
def euclidesR(m, n):
    '''(int,int) -> int

    Recebe inteiros m e n e retorna o máximo divisor
    comum de m e n. 

    Pré-condição: a função supões que m > 0.
    '''

    if n == 0: return m
    return euclidesR (n, m % n, profundidade + 1)


#---------------------------------------------------------
def euclidesR_s(m, n, profundidade):
    '''(int,int,int) -> int

    Recebe inteiros m e n e retorna o máximo divisor
    comum de m e n. 
    A função também recebe um inteiro profundidade 
    que indica a profundidade da recursão e é usado
    para ilustrar as chamadas recursivas.

    Pré-condição: a função supões que m > 0.

    Exemplo:
    >>> euclidesR_s(16,42,0)
    euclidesR(16,42)
      euclidesR(42,16)
        euclidesR(16,10)
          euclidesR(10,6)
            euclidesR(6,4)
              euclidesR(4,2)
                euclidesR(2,0)
    2
    >>> 
    '''

    for i in range(profundidade): print(end="  ")
    print("euclidesR(%d,%d)" %(m, n))

    if n == 0: return m
    return euclidesR_s (n, m % n, profundidade + 1)

