'''
  MAC0122 Principios de Desenvolvimento de Algoritmos
 
  maximo divisor comum = versão Introducao a Computacao
'''

#----------------------------------------------
def mdc(m, n):
    '''(int,int) -> int

    Recebe inteiros positivos m e n e retorna
    o máximo divisor comum de m e n.
    '''

    # condidato a divisor
    d =  min(m,n)

    while m % d != 0 or n % d != 0:
        d -= 1

    return d
