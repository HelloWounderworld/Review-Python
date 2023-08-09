#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   binomial: versão recursiva que calcula o número de fibonacci
   mais eficiente, que devolve dois últimos valores.
'''
#------------------------------------------------------
def main(argv=None):
    # pegue argumentos da linha de comando
    n = int(input("Digite n: "))
    print("fibonacci(%d) = %d" %(n, fibonacciR(n)[-1] ))

#------------------------------------------------    
def fibonacciR(n):
    '''(int) -> int, int

    Recebe um inteiro positivo n >0 e retorna o
    n-ésimo número de fibonacci e seu anterior
    '''
    if n == 0: return 0, 0   # 
    if n == 1: return 0, 1
    ant, ult = fibonacciR(n-1)
    return ult, ant + ult

#--------------------------------------------------------------
if __name__ == "__main__":
    main()
