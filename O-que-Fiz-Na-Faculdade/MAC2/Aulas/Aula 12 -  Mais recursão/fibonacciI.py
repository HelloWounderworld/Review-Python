#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o número de fibonacci
'''

#------------------------------------------------------
def main():

    n = int(input("fibonacciI: digite n: "))
    print("fibonacci(%d) = %d" %(n, fibonacciI(n)))

#------------------------------------------------    
def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e retorna o
    n-ésimo número de fibonacci.
    '''
    if n == 0: return 0
    if n == 1: return 1
    anterior = 0
    atual    = 1
    for i in range(1,n):
        proximo = atual + anterior
        anterior = atual
        atual = proximo
    return atual

        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
