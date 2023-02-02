#----------------------------------------------------------------------------------
#
#  MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#  Lê uma lista de números inteiros a partir de stdin e
#  determina o número de pares que somam zero.
#
# % python doblingTest.py < ../txt/pi-1million.txt
#
#-----------------------------------------------------------------------------------
# todos os algoritmos
from dois_soma import *

# para cronometrar o tempo gasto
import time

# sys.stdin.read()
import sys


#---------------------------------------------------------------------
def main(args=None):
    
    if args == None:
        args = sys.argv

    if len(args) < 3:
        help()
        return

    opcao = args[1]
    if   args[1] == "-q":
        soma_zero = soma_zero_n2
    elif args[1] == "-o":
        soma_zero = soma_zero_nlgn
    elif args[1] == "-l":
        soma_zero = soma_zero_n
    else:
        help()
        return
    
    # lst = leia_lista()
    try:
        print("main(): lendo lista de inteiros...")
        with open(args[2], "r", encoding="utf-8") as arq:
            lst_str = arq.read().split()
        lst = [int(x) for x in lst_str] 
        print("main(): lista com %s ints lida\n"%len(lst))
    except:
        print("main(): arquivo '%s' não encontrado"%args[2])
        help()
        return

    n = len(lst)
    print("      n      tempo  pares ")
    i = 8
    while True:
        if i > n: i = n
        lsti = lst[0:i]
        inicio = time.time()
        k = soma_zero(lsti)
        fim = time.time()
        print("%7s %9.3fs     %s"%(i, (fim-inicio), k))
        if i == n: break
        i += i

#------------------------------------------------------------------------    
def help():
    s = "uso: python doublingTest.py [-q | -o | -l] nome_arq\n" +\
        "     -q = algoritmo quadrático (força bruta)\n" +\
        "     -o = algoritmo n lg n (ordenação + busca binária)\n"+\
        "     -l = algoritmo linear esperado\n"
    print(s)
    
#------------------------------------------------------------------------
    
#------------------------------------------
if __name__ == "__main__":
    main()
