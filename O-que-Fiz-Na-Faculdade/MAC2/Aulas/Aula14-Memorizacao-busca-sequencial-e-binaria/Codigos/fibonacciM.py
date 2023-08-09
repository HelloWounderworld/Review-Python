#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o número de fibonacci
'''
#------------------------------------------------------
def main():
    n = int(input("Digite n: "))
    fib = [0 for i in range(n+1)]
    print("fibonacci(%d) = %d" %(n, fibonacciRM(n, fib)))

#------------------------------------------------    
def fibonacciRM(n, fib):
    '''(int) -> int

    Recebe um inteiro não negativos n e retorna o
    n-ésimo número de fibonacci.
    '''
    if n == 0: return 0
    if n == 1: return 1
    if fib[n] > 0: return fib[n]
    fib[n-1] = fibonacciRM(n-1, fib)
    # fib[n-2] = fibonacciRM(n-2) # já foi calculado
    fib[n] = fib[n-1] + fib[n-2]
    return fib[n]
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
