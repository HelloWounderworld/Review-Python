#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
  maximo divisor comum = algoritmo de Euclide, versao iterativa
'''

# sys.argv
import sys

#------------------------------------------------------
def main(argv=None):

    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome programa    
    nome_programa = argv[0]

    # argc = número de argumentos 
    argc = len(argv)
    if argc != 3:
        help(nome_programa)
        return None

    try:
        # pegue o argumento na linha de comando
        m = int(argv[1])
        n = int(argv[2])
    except:
        help(nome_programa)
        return None
    
    print("mdc(%d,%d) = %d" %(n,m,euclidesI(m,n)))

#-------------------------------------------
def euclidesI(m, n):
    '''(int, int) -> int
 
    Recebe inteiros não negativos m e n e retorna 
    o seu máximo divisor comum.

    Pré-condição: a função supões que n > 0.
    '''
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
        
    return n

#--------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"n k") 
   print("   m = número inteiro não negativo")
   print("   n = número inteiro positivo")
        

#---------------------------------------------------------
if __name__ == "__main__":
    main()
