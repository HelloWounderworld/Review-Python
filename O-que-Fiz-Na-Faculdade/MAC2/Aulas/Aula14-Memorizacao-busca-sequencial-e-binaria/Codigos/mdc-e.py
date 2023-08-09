#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
  MAC0122 Principios de Desenvolvimento de Algoritmos
 
  maximo divisor comum = versão Introducao a Computacao
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
    
    print("mdc(%d,%d) = %d" %(n,m,mdc(m,n)))

#----------------------------------------------
def mdc(m, n):
    '''(int,int) -> int

    Recebe inteiros positivos m e n e retorna
    o máximo divisor comum de m e n.
    '''

    # condidato a divisor
    d =  min(m,n)

    while m % d != 0 or n % d != 0:
        d -= 1

    return d

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
