#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o número de fibonacci
'''
#------------------------------------------------------
def main():
    n = int(input("fibonacciR: digite n"))
    print("fibonacci(%d) = %d" %(n, fibonacciR(n, 0)))

#------------------------------------------------    
def fibonacciR(n, profundidade):
    '''(int) -> int

    Recebe um inteiro não negativos n e retorna o
    n-ésimo número de fibonacci.
    '''
    
    print("  "*profundidade, end="")
    print("fibonacciR(%d)"%(n))

    if n == 0: return 0
    if n == 1: return 1
    return fibonacciR(n-1, profundidade+1) + \
           fibonacciR(n-2, profundidade+1)
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
