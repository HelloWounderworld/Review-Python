# classe Racional
from fracao import *

#---------------------------------------------------------------
def main():
    n = int(input("Digite n: "))

    hn = harmonico(n)
    print("1 + ... + 1/%d + 1/%d = " %(n-1,n), hn)

#---------------------------------------------------------------
def harmonico(n):    
    ''' (int) -> Fracao

    Recebe um numero inteiro positivo e retorna o numero harmonico
    de ordem n representado como fração. 
    O numero harmonico e calculado somando os termos
    da esquerda para a direita.
    '''
    soma = Fracao(0)
    for i in range(1,n+1):
        soma += Fracao(1,i)
    return soma
    

#-------------------------------------
if __name__ == "__main__":
    main()
