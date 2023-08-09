''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos

   Fatorial: versão recursiva
'''


def fatorial(n, profundidade):
    ''' (int, int) -> int

    Recebe como parametros n e profundidade e 
    retorna o valor de n!. Alem disso a funcao
    imprime cada chamada exibindo o (nivel) profundidade
    da recursao.
    '''

    print("  "*profundidade, end="")
    print("fatorial(%d)" %(n))

    if n == 0: return 1
    return n * fatorial(n-1, profundidade+1)


