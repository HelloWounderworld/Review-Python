def main():
    n = int(input("Digite n: "))

    num, den = harmonico(n)
    print("1 + ... + 1/%d + 1/%d = %d/%d = %f" %(n-1,n,num,den,num/den))


#---------------------------------------------------------------
def harmonico(n):    
    ''' (int) -> int, int

    Recebe um numero inteiro positivo e retorna o número harmônico
    de ordem n representado como um racional. 
    O numero harmônico e calculado somando os termos
    da esquerda para a direita.
    '''
    num, den = 0, 1 # numerador e denominador
    i = 1
    while i < n+1:
        num, den = soma_fracoes(num, den, 1, i)
        i += 1
    return num, den

#---------------------------------------------------------------
def soma_fracoes(n1, d1, n2, d2):
    ''' (int, int, int, int) -> int, int

    Recebe quatro números inteiros n1, d1, n2 e d2 representando
    as frações n1/d1 e n2/d2 e retorna um par (num,den)
    que representa a soma desses numeros.

    Pré-condição: supõe que d1 e d2 são diferentes de zero.
    '''
    den = d1 * d2
    num = n1*d2 + n2*d1
    return num, den


#---------------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    main()
