#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o numero binomial
             n-escolhe-k
'''
#------------------------------------------------------
def main(argv=None):
    n = int(input("binomial: digite n: "))
    k = int(input("binomial: digite k: "))
    print("binomial(%d,%d) = %d" %(n,k,binomial(n,k)))
    
#------------------------------------------------    
def binomialR(n,k,profundidade):
    '''(int,int) -> int

    Recebe inteiros não negativos n e k e retorna o
    número binomial de n e k.
    '''
    
    print("  "*profundidade, end="")
    print("binomial(%d,%d)" %(n,k))

    if n == 0 and k  > 0: return 0
    if n >= 0 and k == 0: return 1
    return binomialR(n-1, k,   profundidade+1) + \
           binomialR(n-1, k-1, profundidade+1)
        
#--------------------------------------------------------------
if __name__ == "__main__":
    main()
