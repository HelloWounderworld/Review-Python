# Problema: Decidir se z[0:m] é subsequência de x[0:n]

#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
  MAC0122 Princípios de Desenvolvimento de Algoritmos 
'''

# sys.argv: pega argumento da linha de comando
import sys

#------------------------------------------------------
def main(argv=None):

    # pegue argumentos da linha de comando
    if argv == None:
       argv = sys.argv

    # nome do programa    
    nome_prog = argv[0]  

    # número de argumentos
    argc = len(argv)
    # print(argc)
    
    # uso do programa 
    if argc < 3: 
        mostre_uso(nome_prog)
        return None

    # apelidos para as strings
    s = argv[1]
    t = argv[2]
    m = len(s)
    n = len(t)
    if argc == 4:
        if argv[3] == "-s":
            ss = sub_seq_sim(s, t)
        else:
            mostre_uso(nome_prog)
            return None
    else:
        ss = sub_seq(s, t)
    print('Resposta: ', ss)
 
 #------------------------------------------------------------
def mostre_uso (nome_programa):
    '''(str) -> None

    Recebe o nome do programa e mostra mensagem mostrado
    o seu uso.
    '''    
    msg = "Uso: python %s s t [-s]\n"%nome_programa +\
          "    s = string\n" +\
          "    t = string\n" +\
          "    [-s] = mostra casamentos"
    print(msg)

#----------------------------------------------------

def sub_seq_sim(z, x):
    ''' (str, str) -> bool 
    Recebe duas strings e verifica se z é uma subsequência de x.
    '''
    i = len(z)-1
    j = len(x)-1
    while i >= 0 and j >= 0:
        if z[i] == x[j]: 
            print(">", z[i])
            i -= 1
        else:
            print(" ", x[j])

        j -= 1 
    return i < 0

#----------------------------------------------------

def sub_seq (z, x):
    ''' (str, str) -> bool 
    Recebe duas strings e verifica se z é uma subsequência de x.
    '''
    i = len(z)-1
    j = len(x)-1
    while i >= 0 and j >= 0:
        if z[i] == x[j]: 
            i -= 1
        j -= 1 
    return i < 0    

#----------------------------------------------------
if __name__ == "__main__":
    main()
 