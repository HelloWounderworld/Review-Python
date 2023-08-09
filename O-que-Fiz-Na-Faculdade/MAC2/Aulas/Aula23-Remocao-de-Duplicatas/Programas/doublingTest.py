#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
# Lê um string a partir de stdin e depois calcula uma substring
# repetida mais longa (longest repeated substring = LRS).
#
# % python doblingTest.py < ../txt/pi-1million.txt
# main(): lendo o string ...
# main(): string lida.
#       n      tempo  LRS 
#      32     0.000s  '26'
#      64     0.001s  '592'
#     128     0.002s  '230'
#     256     0.002s  '0582'
#     512     0.006s  '0348'
#    1024     0.009s  '23846'
#    2048     0.009s  '922796'
#    4096     0.013s  '284886'
#    8192     0.028s  '7111369'
#   16384     0.074s  '52637962'
#   32768     0.224s  '23533829'
#   65536     0.774s  '201890888'
#  131072     2.828s  '008173039'
#  TRAVOU AQUI
#
#-----------------------------------------------------------------------------------
# para cronometrar o tempo gasto
import time


#---------------------------------------------------------------------
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
        lrs = lrsX(sk)
        fim = time.time()
        print("%7s %9.3fs  '%s'"%(k, (fim-inicio), lrs))
        k += k

#------------------------------------------------------------------------    
def lrsX(s):
    '''(str) -> str
    RECEBE uma string s e RETORNA uma substring repedida mais longa de s.
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
