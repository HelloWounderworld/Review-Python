#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   números binomiais = versão iterativa
'''

#------------------------------------------------------
def main(argv=None):
    n = int(input("binomial: digite n: "))
    k = int(input("binomial: digite k: "))
    print("binomial(%d,%d) = %d" %(n,k,binomial(n,k)))

#----------------------------------------------------
def binomial(n, k):
    '''(int, int) -> int

    Recebe dois inteiros não negativos n e k e retorna 
    o valor do número binomial(n,k).

    Cada posição [i][j] da matriz bin armazenará o valor
    de binomia(i,j).
    '''

    # matriz de zeros de dimensão (n+1)x(k+1)
    bin = crie_matriz(n+1, k+1, 0)

    # acerte a primeira coluna da tabela
    for i in range(n+1):
        bin[i][0] = 1

    # calcule o valor de cada posição da matriz
    for i in range(1,n+1):
        # calcule os valores 
        for j in range(1,k+1):
            bin[i][j] = bin[i-1][j] + bin[i-1][j-1]

    return bin[n][k]


#--------------------------------------------------
def crie_lista(n, valor):
    '''(int, objeto) -> list

    Recebe um inteiro não negativo n e um objeto valor e retorna cria
    e retorna uma lista com n itens em que cada item é uma referência
    para o valor.

    '''
    lista = []

    for i in range(n):
        lista.append(valor)

    return lista

#--------------------------------------------------
def crie_matriz(n, m, valor):
    '''(int, int, objeto) -> matriz (=lists de listss)

    Recebe inteiros não-negativos n e m e um objeto valor 
    e cria retorna uma matriz (lista de listas) de dimensão
    n x m em que cada elemento é uma referência a valor.
    '''
    matriz = []
    for i in range(n):
        linha = crie_lista(m, valor)
        matriz.append(linha)
    return matriz    


#--------------------------------------------------------------
if __name__ == "__main__":
    main()
