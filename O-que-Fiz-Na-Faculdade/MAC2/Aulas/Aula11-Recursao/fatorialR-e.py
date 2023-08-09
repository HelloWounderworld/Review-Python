#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' 
   MAC0122 Principios de Desenvolvimento de Algoritmos
  
   Fatorial: versão recursiva mais simples
             pega argumento da linha de comando
'''

# sys.argv
import sys

#------------------------------------------------------
def main(argv=None):

    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome programa    
    nome_programa = "fatorialR-e.py" # argv[0]

    # argc = número de argumentos 
    argc = len(argv)
    if argc < 2:
        help(nome_programa)
        return None

    try:
        # pegue o argumento na linha de comando
        n = int(argv[1])
    except:
        help(nome_programa)
        return None

    if argc == 3:
        print("fatorial(%d) = %d" %(n,fatorial_s(n, 0)))
    else:    
        print("fatorial(%d) = %d" %(n,fatorial(n)))


#--------------------------------------------------------    
def fatorial(n):
    '''(int) -> int
   
    Recebe um inteiro n e retorna n!.
    '''
    if n == 0:
        return 1
    return n * fatorial(n-1)

def fatorial_s(n, profundidade):
    ''' (int, int) -> int

    Recebe como parametros n e profundidade e 
    retorna o valor de n!. Alem disso a funcao
    imprime cada chamada exibindo o (nivel) profundidade
    da recursao.
    '''

    for i in range(profundidade):
        print("  ", end="")

    print("fatorial(%d)" %(n))

    if n == 0:
        return 1
    
    return n * fatorial_s(n-1, profundidade+1)

#--------------------------------------------------------
def help(nome_prog):
   """ Erro message explaning how to run the program
   """
   print("Uso: python3",nome_prog,"n [-s]") 
   print("   n = número inteiro")
   print("   s = simulação")
        

#--------------------------------------------------------------
if __name__ == "__main__":
    main()
