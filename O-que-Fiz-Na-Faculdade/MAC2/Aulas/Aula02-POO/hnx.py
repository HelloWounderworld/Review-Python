def main():
    n = int(input("Digite n: "))

    num, den = harmonico(n)
    print("1 + ... + 1/%d + 1/%d = %d/%d = %f" %(n-1,n,num,den,num/den))

#---------------------------------------------------------------
def harmonico(n):    
    ''' (int) -> int, int

    Recebe um numero inteiro positivo e retorna o numero harmonico
    de ordem n representado como uma racional. 
    O numero harmonico e calculado somando os termos
    da esquerda para a direita.
    '''
    num, den = 0, 1 # numerador e denominador
    for i in range (1, n+1):
        num, den = soma_fracoes(num,den,1,i)
    return num, den

#---------------------------------------------------------------
def soma_fracoes(n1, d1, n2, d2):
    ''' (int, int, int, int) -> int, int

    Recebe quatro numeros inteiros n1, d1, n2 e d2 representando
    duas fracoes n1/d1 e n2/d2 e retorna um par (num,den)
    que representa a soma desses números.

    Pre-condicao: a função supõe que os quadro números dados nao
    sao nulos.
    '''
    den = d1 * d2
    num = n1*d2 + n2*d1
    return simplifique(num, den)
    

#--------------------------------------------
def simplifique(n, d):
    '''(int, int) -> int, int

    Recebe uma racional n/d e retorna a correspondente
    racional irredutível.
    '''
    comum = mdc(n,d)
    n //= comum  # precisa ser //
    d //= comum  # precisa ser //
    if d < 0:
        d = -d
        n = -n
    return n, d

#-----------------------------------------
def mdc(m,n):
    """ (int, int) -> int
    Recebe dois inteiros m e n e retorna o
    mdc de m e n.

    Pré-condição: a função supõe que pelo menos um dos
        parâmetros é não nulo.
    """
    if n == 0: return m
    if n <  0: n = -n    
    if m <  0: m = -m
    # calcule o mdc()
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d

#---------------------------------------------------
# início da execução do programa
main()
