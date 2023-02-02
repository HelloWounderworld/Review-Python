# Temos duas implmentações de uma rede
# from rede import Rede
# from rede_listas_adjacencia import Rede

import numpy as np
from queue import Queue

def main():
    nome_arquivo = input("Digite o arquivo com a rede: ")
    rede = leia_rede(nome_arquivo)
    origem = int(input("Qual é a cidade origem: "))

    # calcule as distancias
    d = distancias(origem, rede)

    # imprima as distancias
    print("Distância da cidade %d a cidade:" %origem)
    for i in range(len(d)):
        print("   ", i, ":", d[i]) 
    
    
#----------------------------------------------------------
def distancias(c, rede):
    '''(int, Rede) - list

    Recebe o índice c de uma cidade e uma rede de estradas
    com n cidades.
    
    A função cria e retorna uma lista d[0:n] tal que para 
    i = 0,...,n-1, d[i] é a distância da cidade c a cidade i.

    Se não existe caminho da cidade c a cidade i então d[i]=n.
    '''
    # pegue o número de cidades da rede
    n = len(rede)

    # crie o vetor de distancia com 'infinito' em cada posição
    d = np.full(n, n)

    # a distancia da origem a si mesma e zero
    d[c] = 0

    # crie a fila de cidades
    q = Queue()

    # coloque a cidade origem na fila
    q.enqueue(c)

    while not q.isEmpty():
        # i será o 1a. cidade na fila
        i = q.dequeue()
            
        # examine as cidades vizinhas da cidade i
        for j in range(n):
            if rede[i, j] and d[j] > d[i]+1:
                d[j] = d[i] + 1
                q.enqueue(j)
        
    return d


#---------------------------------------------------------        
def leia_rede(nome_arquivo):
    '''(str) -> Rede
   
    Recebe um string nome_arquivo com o nome de um arquivo e 
    lê desse arquivo a representação de uma rede de estradas.
 
    A primeira linha do arquivo contém o número n de cidades.

    A segunda linha do arquivo contém o número m de estradas.

    As demais m linhas contém pares de inteiros i e j entre 0..n-1 
    indicando que existe uma estrada de i para j.

    Exemplo:

    6
    10
    0 2
    0 3
    0 4
    1 2
    1 4
    2 4
    3 4
    3 5
    4 5
    5 1 # esta linha é o fim do arquivo
        
    A rede tem 6 cidades 0,1,...,5 e 10 estradas.
    '''
    # abra o arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:

        # leia do arquivo o número de cidades 
        n = int(arquivo.readline())

        # leia do arquivo o número de estradas
        m = int(arquivo.readline())
        
        # crie uma rede com n cidades e sem estradas
        # rede = Rede(n)
        rede = np.full( (n, n), False)
        
        for k in range(m):
            linha  = arquivo.readline()
            cidade = linha.split()
            i = int(cidade[0])
            j = int(cidade[1])
            rede[i, j] = True

    # retorne a rede
    return rede

#---------------------------------------------------------
if __name__ == "__main__":
    main()
