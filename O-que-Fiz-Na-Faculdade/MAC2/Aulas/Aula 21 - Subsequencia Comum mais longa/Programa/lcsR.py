#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
  MAC0122 Principios de Desenvolvimento de Algoritmos 
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
            lcs_st = lcs_rec_sim(s, m, t, n, 0)
        else:
            mostre_uso(nome_prog)
            return None
    else:
        lcs_st = lcs_rec(s, m, t, n)
    print(lcs_st)
    
#----------------------------------------------
def lcs_rec(s, m, t, n):
    '''(str, str) -> str

    Recebe uma string s de comprimento m e uma string t de 
    comprimento n e retorna uma longest common substring de 
    de s e t.
    '''
    if m == 0 or n == 0:
        return ""
    
    if s[m-1] == t[n-1]:
        return lcs_rec(s, m-1, t, n-1) + s[m-1]
    
    lcs_1 = lcs_rec(s, m-1, t,   n)
    lcs_2 = lcs_rec(s,   m, t, n-1)
    if len(lcs_1) > len(lcs_2): return lcs_1
    return lcs_2

#----------------------------------------------            
def lcs_rec_sim(s, m, t, n, depth):
    '''(str, str) -> str

    Recebe uma string s de comprimento m e uma string t de 
    comprimento n e retorna uma longest common substring de 
    de s e t.
    '''

    # imprime deslocamento
    print("  "*depth + "lcs_rec(s[0:%d],t[0:%d])"%(m,n))
    if m == 0 or n == 0:
        print("  "*depth + "return ''")
        return ""

    if s[m-1] == t[n-1]:
        lcs = lcs_rec_sim(s, m-1, t, n-1, depth+1) + s[m-1]
        print("  "*depth + "return '" + lcs + "'")
        return lcs
    
    lcs_1 = lcs_rec_sim(s, m-1, t,   n, depth+1)
    lcs_2 = lcs_rec_sim(s,   m, t, n-1, depth+1)
    
    if len(lcs_1) > len(lcs_2): lcs = lcs_1
    else: lcs = lcs_2
    print("  "*depth + "return '" + lcs + "'")
    return lcs

#----------------------------------------------
def crie_matriz(n_lin, n_col, valor = 0):
    matriz = []
    for i in range(n_lin):
        matriz.append([valor]*n_col)
    return matriz    
            
#------------------------------------------------------------
def mostre_uso (nome_programa):
    '''(str) -> None

    Recebe o nome do programa e mostra mensagem mostrado
    o seu uso.
    '''    
    msg = "Uso: python %s s t [-s]\n"%nome_programa +\
          "    s = string\n" +\
          "    t = string\n" +\
          "    [-s] = mostra chamadas recursivas"
    print(msg)



    

#----------------------------------------------------
if __name__ == "__main__":
    main()
    
