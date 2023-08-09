#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   maximo divisor comum = algoritmo de Euclides - versao recursiva
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
    
    print("mdc(%d,%d) = %d" %(n,m,euclidesR(m,n)))

#---------------------------------------------------------
def euclidesR(m, n):
    '''(int,int) -> int

    Recebe inteiros m e n e retorna o máximo divisor
    comum de m e n. 

    Pré-condição: a função supões que m > 0.
    '''

    if n == 0: return m
    return euclidesR (n, m % n)


#---------------------------------------------------------
def euclidesR_s(m, n, profundidade):
    '''(int,int,int) -> int

    Recebe inteiros m e n e retorna o máximo divisor
    comum de m e n. 
    A função também recebe um inteiro profundidade 
    que indica a profundidade da recursão e é usado
    para ilustrar as chamadas recursivas.

    Pré-condição: a função supões que m > 0.

    Exemplo:
    >>> euclidesR_s(16,42,0)
    euclidesR(16,42)
      euclidesR(42,16)
        euclidesR(16,10)
          euclidesR(10,6)
            euclidesR(6,4)
              euclidesR(4,2)
                euclidesR(2,0)
    2
    >>> 
    '''

    for i in range(profundidade): print(end="  ")
    print("euclidesR(%d,%d)" %(m, n))

    if n == 0: return m
    return euclidesR_s (n, m % n, profundidade + 1)

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
