#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   versão recursiva que calcula o número de fibonacci
   guardando valores intermediários em uma lista.
'''
#------------------------------------------------------
def main(argv=None):
    n = int(input("Digite n: "))
    print("fibonacci(%d) = %d" %(n, fibonacciR(n)))

#------------------------------------------------    
def fibonacciR(n):

    return fibonacciRCache(n, [0]*(n+1))

#------------------------------------------------    
def fibonacciRCache(n, cache ):
    '''(int) -> int

    Recebe um inteiro não negativos n e retorna o
    n-ésimo número de fibonacci.
    '''
    if n == 0: return 0
    if n == 1: return 1
    if cache[n] != 0: return cache[n] # já calculei

    cache[n-2] = fibonacciRCache(n-2, cache)
    cache[n-1] = fibonacciRCache(n-1, cache)
    cache[n] = cache[n-2] + cache[n-1]
    return cache[n]
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
