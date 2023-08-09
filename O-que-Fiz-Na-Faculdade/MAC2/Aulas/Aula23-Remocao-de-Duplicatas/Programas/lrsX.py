#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#  Lê um string a partir de stdin e depois calcula uma substring repetida mais longa
#  (longest repeated substring = LRS).
# 
#
#-----------------------------------------------------------------------------------
# para cronometrar o tempo gasto
import time

# string com vista e não clone 
from mystring import MyString

#------------------------------------------------------------------------
def main():
    nome_arq = input("Digite o nome do arquivo com a string: ")
    
    print("main(): lendo a string ...")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        s = arq.read()
    s = MyString(s)
    print("main(): string lida")

    print("main(): procurando uma LRS...")
    inicio = time.time()
    lrs = lrsX(s)
    fim = time.time()
    print("main(): LRS encontrada...")
    print("'%s'"%lrs)
    print("elapsed time     = %.3f"%(fim-inicio))


#------------------------------------------------------------------------    
def lrsX(s):
    '''(MyString) -> MyString
    Recebe uma string s e RETORNA uma substring repetida mais longa de s.
    '''
    n = len(s)
    
    # cria um lista com os sufixo de s
    sufixo = [s[i:] for i in range(n)]
    
    # ordena os sufixo de s
    sufixo.sort() 

    # encontra o lrs comparando sufixo adjacentes
    lrs = ''
    for i in range(n-1):
            x = lcp(sufixo[i], sufixo[i+1])
            # print(s[i:], s[i+1:], '"%s"'%x)
            if len(x) > len(lrs):
                lrs = x
    return lrs

#------------------------------------------------------------------------
def lcp(s, t):
    '''(MyString, MyString) -> str
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
