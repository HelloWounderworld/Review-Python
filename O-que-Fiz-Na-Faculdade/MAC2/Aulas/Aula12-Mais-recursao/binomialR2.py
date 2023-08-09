''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Binomial: versões recursivas e iterativas que calculam o 
             número binomial(n,k).
             binomial(n,k) = número de maneiras diferentes de agrupar
             n objetos em grupos de k objetos.
'''

#---------------------------------------------------------
def binomial(n, k):
    '''(int,int) -> int

    Recebe inteiros não-negativos n e k e retorna o valor
    do número binomial(n,k).

    Pré-cndição: função supões que n >= k >= 1
    Exemplos:
    >>> binomial(3,2)
    3
    >>> binomial(5,1)
    5
    >>> binomial(1,5)
    0
    >>> binomial(4,2)
    6
    >>> 
    '''
    if k == 1: return n
    return binomial(n-1, k-1) * n // k


#---------------------------------------------------------
def binomial_s(n, k, profundidade):
    '''(int,int,int) -> int

    Recebe inteiros não-negativos n e k e profundidade e retorna o
    valor do número binomial(n,k).
    O valor de profundidade indica o nível da chamada recursiva 
    e é usado para ilustrar a execução da função.

    Exemplo:
    >>> binomial_s(20,10,0)
    binomial(20,10)
      binomial(19,9)
        binomial(18,8)
          binomial(17,7)
            binomial(16,6)
              binomial(15,5)
                binomial(14,4)
                  binomial(13,3)
                    binomial(12,2)
                      binomial(11,1)
    184756    
    '''
    print("  "*profundidade, end="")
    print("binomial(%d,%d)" %(n,k))

    if k == 1: return n
    return binomial_s(n-1, k-1, profundidade+1) * n // k
