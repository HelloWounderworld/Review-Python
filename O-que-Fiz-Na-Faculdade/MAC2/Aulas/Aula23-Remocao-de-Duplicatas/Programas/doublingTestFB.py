#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
# Lê um string a partir de stdin e depois calcula uma substring repetido mais longa
# (longest repeated substring = LRS).
#
# % python doublingTestFB.py < ../txt/pi-1million.txt
# main(): lendo a string ...
# main(): string lida.
#     n      tempo  LRS 
#    32     0.001s  '26'
#    64     0.003s  '592'
#   128     0.016s  '592'
#   256     0.060s  '5028'
#   512     0.138s  '5028'
#  1024     0.533s  '23846'
#  2048     2.218s  '949129'
#  4096     9.700s  '949129'
#  8192    38.938s  '7111369'
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
    
    n = len(s)
    print("      n      tempo  LRS ")
    k = 32
    while k < n:
        sk = s[0:k]
        inicio = time.time()
        lrs = lrsFB(sk)
        fim = time.time()
        print("%7s %9.3fs  '%s'"%(k, (fim-inicio), lrs))
        k += k

#------------------------------------------------------------------------    
def lrsFB(s):
    '''(str) -> str
    RECEBE uma string s e RETORNA uma substring repedida mais longa de s.
    '''
    n = len(s)
    lrs = ''
    for i in range(n-1):
        si = s[i:]
        for j in range(i+1,n):
            sj = s[j:]
            x = lcp(si, sj)
            # print(si, sj, x)
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
