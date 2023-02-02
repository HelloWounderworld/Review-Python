#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
# Lê um string a partir de stdin e depois calcula uma substring repetido mais longa
# (longest repeated substring = LRS).
# 
#  % python lrs.py 
#  aaaaaaaaa
#  'aaaaaaaa'
#
#  % python lrs.py
#  abcdefg
#  ''
#
#-----------------------------------------------------------------------------------
# para cronometrar o tempo gasto
import time

#------------------------------------------------------------------------
def main():
    nome_arq = input("Digite o nome do arquivo com a string: ")
    
    print("main(): lendo a string ...")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        s = arq.read()
    print("main(): string lida")

    print("main(): procurando uma LRS...")
    inicio = time.time()
    lrs = lrs(s)
    fim = time.time()
    print("main(): LRS encontrada...")
    print("'%s'"%lrs)
    print("elapsed time     = %.3f"%(fim-inicio))


#------------------------------------------------------------------------    
def lrs(s):
    '''(str) -> str
    Recebe uma string s e RETORNA uma substring repedida mais longa de s.
    '''
    n = len(s)
    
    # cria um listar com os sufixo de s
    sufixo = [s[i:] for i in range(n)]

    # ordena os sufixo de s
    sufixo.sort()

    # encontra o lrs comparando sufixo adjacentes
    lrs = ''
    for i in range(n-1):
            x = lcp(sufixo[i], sufixo[i+1])
            if len(x) > len(lrs):
                lrs = x
                
    return lrs            

#------------------------------------------------------------------------
def lcp(s, t):
    '''(str, str) -> str
    RECEBE duas strings s e t e RETORNA o prefixo comum mais longo
    de s e t
    '''
    n = min(len(s), len(t))
    for i in range(n):
        if s[i] != t[i]:
            return s[0:i]
    return s[0:n]    

    
#------------------------------------------
if __name__ == "__main__":
    main()
