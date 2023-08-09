def main():
    n = int(input("Digite n: "))

    hn1 = harmonico_ED(n)
    print("1 + ... + 1/%d + 1/%d = " %(n-1,n), hn1)

    hn2 = harmonico_DE(n)
    print("1/%d + 1/%d + ... + 1 = " %(n,n-1), hn2)    

#----------------------------------------------------
def harmonico_ED(n):
    '''(int) -> float
 
    Recebe um inteiro n e retorna o número harmônico 
    de ordem n que foi calculado adicionando-se os termos
    da esquerda para a direita.
    '''
    soma = 0
    i = 1
    while i < n+1:
        soma += 1/i
        i += 1
    return soma


#----------------------------------------------------
def harmonico_DE(n):
    '''(int) -> float
 
    Recebe um inteiro n e retorna o número harmônico 
    de ordem n que foi calculado adicionando-se os termos
    da direita para a esquerda.
    '''
    soma = 0
    i = n
    while i > 0:
        soma += 1/i
        i -= 1
    return soma


#---------------------------------------------------
# início da execução do programa
main()
