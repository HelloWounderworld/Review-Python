#!/usr/bin/python3
# -*- coding: utf-8 -*-
''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   versão recursiva que calcula o número de fibonacci
'''
#------------------------------------------------------
def main():
    n = int(input("Digite n: "))
    print("fibonacci(%d) = %d" %(n, fibonacciR(n,0)))

#------------------------------------------------    
def fibonacciR(n, profundidade):
    '''(int) -> int

    Recebe um inteiro não negativos n e retorna o
    n-ésimo número de fibonacci.
    '''
    print("  "*profundidade, "fibonacciR(%s)"%(n))
    if n == 0:
        print("  "*(profundidade+1), "return 0")
        return 0
    if n == 1:
        print("  "*(profundidade+1), "return 1")
        return 1
    fib =  fibonacciR(n-1, profundidade+1) + \
           fibonacciR(n-2, profundidade+1)
    print("  "*(profundidade+1), "return %s"%fib)

    return fib
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
