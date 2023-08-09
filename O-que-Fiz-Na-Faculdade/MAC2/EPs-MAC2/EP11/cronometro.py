# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#
# MAC0122 Princípios de Desenvolvimento de Algoritmos
#
#--------------------------------------------------------------------

# importa a classe Cliente e as funções mergeX() e mergesortX()
from Cliente import Cliente

# para teste da classe Cliente
import random  

# math.log2
import math

# para cronometrar
import time

NMAX = 2**5

#------------------------------------------------------------
def main(args=None):
    ''' (None) -> None
    Essa função main() compara os tempos de execuções dos 
    métodos Cliente.distancia() e Cliente.distanciaX().
    Cliente.distanciaX() é baseado em uma adaptação do 
    mergesort().

    Você pode alterá-la e incluir os seus próprios testes.
    '''
    # para podermos reproduzir os testes
    random.seed(0)

    # lst de filmes
    n = 16
    print("     n   distancia  distanciaX  transposicões     n(n-1)/2      n lg(n)")
    while n < NMAX:
        print("%6s"%n, end="")
        
        # crie listas representado as classificações
        lst0 = [i for i in range(n)]
        lst1 = lst0[:]
        random.shuffle(lst0)
        lst2 = lst1[:] # clone
        
        # crie clientes 
        cliente0 = Cliente("cliente 0")
        print(cliente0)
        cliente0.put_classificacao(lst0)
        print(cliente0)
        cliente1 = Cliente("cliente 1")
        cliente1.put_classificacao(lst1)
        print(cliente1)
        cliente2 = Cliente("cliente 2")
        cliente2.put_classificacao(lst2)

        # cronometre tempo de distancia()
        print(cliente0.distancia(cliente1))
        inicio = time.time()
        dist = cliente0.distancia(cliente1)
        fim = time.time()
        print("%10.3fs"%(fim-inicio), end="")
        
        # cronometre tempo de distanciaX()
        inicio = time.time()
        distX = cliente0.distanciaX(cliente1)
        fim = time.time()
        print(" %10.3fs"%(fim-inicio), end="")

        print("    %10d    %10d   %10d"%(dist,n*(n-1)/2, int(n*math.log2(n))))
        
        if dist != distX:
            print("SOCORRO! distancia() = %s != %s = distanciaX()"%(dist, distX))

        n *= 2

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()

