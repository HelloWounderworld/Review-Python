# importa a classe Cliente e as funções mergeX() e mergesortX()
from Cliente import Cliente

# para teste da classe Cliente
import random  

# math.log2
import math

# para cronometrar
import time

NMAX = 2**18

#------------------------------------------------------------
def main(args=None):
    # para podermos reproduzir os testes
    random.seed(0)

    # lst de filmes
    n = 2**8
    print("     n   distancia  distanciaX  transposicoes     n(n-1)/2       n lg n")
    #while n < NMAX:
        #print("%6s"%n, end="")
        
        # crie listas representando as classificações
    lst0 = []
    for i in list('ABCDEFGHIJKL'):
        lst0.append(i) # [ 0, 1, 2, ..., n-1
    lst1 = lst0[:]               # [ 0, 1, 2, ..., n-1]
    random.shuffle(lst1)         # permutação aleatória de [ 0, 1, ..., n-1]
        
        # crie clientes 
    cliente0 = Cliente("cliente 0")
    cliente0.put_classificacao(lst0)
        
    cliente1 = Cliente("cliente 1")
    cliente1.put_classificacao(lst1)
    print('clientes')
    print(cliente0)
    print(cliente1)
    print('sua distancia')
    print(cliente0.distancia(cliente1))
    print('sua distanciaX')
    print(cliente0.distanciaX(cliente1))
        # cronometre tempo de distancia()
    inicio = time.time()
    dist = cliente0.distancia(cliente1)
    fim = time.time()
    print("%10.3fs"%(fim-inicio), end="")
        
        # cronometre tempo de distanciaX()
    inicio = time.time()
    distX = cliente0.distanciaX(cliente1)
    fim = time.time()
    print(" %10.3fs"%(fim-inicio), end="")

    print("    %10d    %10d   %10d"%(dist,n*(n-1)/2, int(n*math.log2( n))))
        
    if dist != distX:
        print("SOCORRO! distancia() = %s != %s = distanciaX()"%(dist, distX))

    n *= 2

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()
