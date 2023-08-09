#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#  Lê um string a partir de stdin e depois calcula uma substring
#  repetida mais longa (longest repeated substring = LRS).
#
#
#-----------------------------------------------------------------------------------
# para cronometrar o tempo gasto
import time

# implementação de string em que fatia é vista e não clone
from mystring import MyString

def main():
    nome_arq = input("Digite o nome do arquivo com a string: ")
    
    print("main(): lendo a string ...")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        s = arq.read()
    s = MyString(s) # str é transformada em MyString
    print("main(): string lida")
    
    n = len(s)
    print("      n      tempo  LRS ")
    k = 32
    while k < n:
        sk = s[0:k]
        inicio = time.time()
        lrs = lrsX(sk)
        fim = time.time()
        print("%7s %9.3fs  '%s'"%(k, (fim-inicio), lrs))
        k += k

#------------------------------------------------------------------------    
def lrsX(s):
    '''(MyString) -> MyString
    RECEBE uma string s e RETORNA uma substring repetida mais longa de s.
    '''
    n = len(s)
    
    # crie um lista com vista dos sufixo de s
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
