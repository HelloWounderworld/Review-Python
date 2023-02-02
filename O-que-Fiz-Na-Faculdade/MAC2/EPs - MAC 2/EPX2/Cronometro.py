#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   Problema da fatia de soma maxima: 

       dado:      uma lista v de números inteiros;
       encontrar: uma fatia v[e:d] de soma máxima.
'''
# importa todas as funções do módul fatiamax
from fatia import *

# para o cronômetro
import time

# para o gerador de numeros aleatórios
import random

#------------------------------------------------------
# CONSTANTES

# numero de elementos
NMIN = 0x0100      # = 4096  
NMAX = 0x80000#00   # = 134217728 ~ 135 milhões

# semente default para o gerador de no. aleatorios
SEMENTE = 1234567

# no. de experimentos default.
NO_EXPERIMENTOS = 1

# para testes
MOSTRE = False

#
MIN = -4096
MAX =  4096

#------------------------------------------------------
def main(argv=None):
    #------------------------------------------------
    # valores default para os parâmetros
    semente = SEMENTE   # para o gerador de numeros aleatorios 
    no_experimentos = 1 # número de repeticoes de uma função
    max = NMAX   # numero maximo de elementos da lista 
    min = NMIN   # numero mínimo de elementos na lista
    
    # inicialize a semente do gerador de numeros aleatorios 
    random.seed(semente)

    # crie uma vetor com lista de max ints
    print("Criando lista com %d ints" %max)
    v = lista_int_rand(max)
    print("Lista criada.\n")

    # para teste
    if MOSTRE:
        print("semente = %d" %(semente))
        mostre_lista(v)

    # imprima cabeçalho 
    print("         n ", end="")
    print("    div_conq ", end="")
    print("   fatia_max \n", end="")

    n = min
    while n <= max:
        # cronometre algoritmo por divisão e conquista
        inicio = time.time()
        soma_max1, e1, d1 = fatia_max_div_conq(0, n, v)
        fim = time.time()
        t1 = fim-inicio
            
        # cronometre algoritmo quadrático
        inicio = time.time()
        soma_max2, e2, d2 = fatia_max(0, n, v)
        fim = time.time()
        t2 = fim-inicio

        print("%10d" %n, end="")
        print("%11.2fs "%t1, end="")
        print("%11.2fs\n"%t2, end="")

        if soma_max1 != soma_max2:
            print("SOCORRO! soma_max1 = %s != %s soma_max2"%(soma_max1,soma_max2))
            
        # proximo valor de n
        n *= 2

#------------------------------------------------------------
#  F U N C O E S    A U X I L I A R E S 
#------------------------------------------------------------
def lista_int_rand(n):
    '''(int) -> list

    Recebe um inteiro não nagtivo n e cria e retorna uma 
    lista com n número inteiros gerados aleatoriamente no
    intervalo [MIN,MAX[.
    '''
    lista = []
    for i in range(n):
        valor = random.randrange(MIN,MAX)
        lista.append(valor)
    return lista

#------------------------------------------------------------
def mostre_lista(v):
    '''(list) -> None

    Recebe uma lista v de números inteiros e mostra o seu conteudo
    de uma maneira conveniente.
    '''
    print("Lista:")
    n = len(v)
    for i in range(n):
        print("%8d: %d" %(i,v[i]))


#-----------------------------------------------------------    
if __name__ == "__main__":
    main()
    
'''
         n     div_conq    fatia_max 
       256       0.00s        0.00s
       512       0.00s        0.01s
      1024       0.00s        0.04s
      2048       0.00s        0.16s
      4096       0.01s        0.62s
      8192       0.02s        2.45s
     16384       0.04s        9.82s
     32768       0.08s       39.37s
     65536       0.16s      161.20s
    131072       0.33s      663.06s
    262144       0.68s     2581.96s
    524288       1.40s    10163.39s
'''
    
    
