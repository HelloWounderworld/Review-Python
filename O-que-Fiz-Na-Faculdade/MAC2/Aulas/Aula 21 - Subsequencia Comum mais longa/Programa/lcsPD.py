#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
  MAC0122 Princípios de Desenvolvimento de Algoritmos 
'''

import numpy as np

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
    if argc != 3: 
        mostre_uso(nome_prog)
        return None

    # apelidos para as strings
    with open(argv[1], "r", encoding="utf-8") as arq:
        s = arq.read().strip()
        
    with open(argv[2], "r", encoding="utf-8") as arq:
        t = arq.read().strip()
 
    lcs_st = get_lcs(s, t, lcs(s, t))
    print(lcs_st)

#----------------------------------------------------------    
# Implementação de programação dinâmica para o problema LCS
# Computa o comprimento do LCS para todo subproblema
def lcs(s, t):
    '''(str, str) -> array

    RECEBE uma string s de comprimento e uma string t e 
    RETORNA a matriz opt com o comprimento dos lcs para todo 
    subproblema.
    '''
    # encontre os comprimentos dos strings
    m = len(s)
    n = len(t)

    # declarando o array para amazenar os valores 
    # opt = [[0]*(n+1) for i in range(m+1)] # crie_matriz(m+1, n+1, 0)
    opt = np.zeros((m+1,n+1))
    
    # compute as entradas da matriz opt[][] de uma maneira 'bottom up'
    # opt[i,j] contém o comprimento de uma LCS de s[0:i] e t[0:j]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                opt[i,j] = opt[i-1,j-1] + 1
            else:
                opt[i,j] = max(opt[i-1,j] , opt[i,j-1])
 
    # opt[m,n] contém o comprimento da LCS de s[0:n] e t[0:m]
    return opt

#---------------------------------------------------------
def get_lcs(s, t, opt):
    '''(str, str, array) -> str

    RECEBE uma string s e uma string t e um array opt com o
    comprimento dos lcs para todo subproblema e RETORNA uma
    lcs de s e t.
    '''
    lcs = ''        
    m, n = len(s), len(t)
    i, j  = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs = s[i-1] + lcs
            i -= 1
            j -= 1
        elif opt[i-1,j] >= opt[i,j-1]:
            i -= 1
        else:
            j -= 1
    return lcs

#----------------------------------------------
def crie_matriz(nlin, ncol, valor = 0):
    matriz = []
    for i in range(nlin):
        matriz.append([valor]*ncol)
    return matriz    
            
#------------------------------------------------------------
def mostre_uso (nome_programa):
    '''(str) -> None

    Recebe o nome do programa e mostra mensagem mostrado
    o seu uso.
    '''    
    msg = "Uso: python %s s_arq t_arq [-a]\n"%nome_programa +\
          "    s_arq = arquivo com string\n" +\
          "    t_arq = arquivo com string\n"
    print(msg)

    

#----------------------------------------------------
if __name__ == "__main__":
    main()
    
