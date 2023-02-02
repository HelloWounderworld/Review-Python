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
    if n < k: return 0
    if n == k or k == 0: return 1
    return binomial(n-1, k) + binomial(n-1, k-1)


#---------------------------------------------------------
def binomial_s(n, k, profundidade):
    '''(int,int,int) -> int

    Recebe inteiros não-negativos n e k e profundidade e retorna o
    valor do número binomial(n,k).
    O valor de profundidade indica o nível da chamada recursiva 
    e é usado para ilustrar a execução da função.

    Exemplo:
    >>> binomial_s(3,2,0)
    binomial(3,2)
      binomial(2,2)
      binomial(2,1)
        binomial(1,1)
        binomial(1,0)
    3
    '''
    for i in range(profundidade): print(end="  ")
    print("binomial(%d,%d)" %(n,k))

    if n < k: return 0
    if n == k or k == 0: return 1
    return binomial_s(n-1, k, profundidade+1) \
           + binomial_s(n-1, k-1, profundidade+1)

