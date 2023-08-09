import random
import time
import math
def mergeX(v, e, m, d):
    ''' (list, int, int, int) -> int

    RECEBE uma lista v tal que v[e:m] e v[m:d] estão em ordem crescente. 
    A função intercala essas fatias de forma que v[e:d] esteja em ordem crescente.

    RETORNA o número de transposições necessários para ordenar v[e:d].
    '''
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return 1
        else:
            return 0
    else:
        transpos = 0
        lista = []
        esquerda = 0
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
                transpos = transpos + len(v[esquerda:m])
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return transpos

def intercala(v, e, m, d):
    if len(v) == 2:
        if v[1] < v[0]:
            x = v[1]
            v[1] = v[0]
            v[0] = x
            return v
        else:
            return v
    else:
        lista = []
        esquerda = e
        direita = m
        while esquerda < m and direita < d:
            if v[esquerda] < v[direita]:
                lista.append(v[esquerda])
                esquerda += 1
            else:
                lista.append(v[direita])
                direita += 1
        while esquerda < m:
            lista.append(v[esquerda])
            esquerda += 1
        while direita < d:
            lista.append(v[direita])
            direita += 1
        j = 0
        for i in range(e,d):
            v[i] = lista[j]
            j += 1
        return v
    
def mergesortX(v, e=None, d=None):
    ''' (list, int, int) -> int

    Recebe uma lista v e dois inteiros que definem 
    um segmento de v que deve ser ordenado. 

    Quando e e d são None, a lista inteira deve ser ordenada.

    A função retorna o número de transposições resultantes da ordenação 
    de v[e:d].
    '''
    if e == None and d == None:
        return mergesortX(v,0,len(v))
    else:
        n = d-e
        if n <= 1:
            return 0
        p = 0
        q = 0
        r = 0
        m = (e+d) // 2
        p = p+mergesortX(v,e,m)
        q = q+mergesortX(v,m,d)
        r = r+mergeX(v[e:d],0,len(v[e:d])//2,len(v[e:d]))
        v[e:d] = intercala(v[e:d],0,len(v[e:d])//2,len(v[e:d]))
        return p+q+r
    
def interseccao(elemento,lista): 
    if len(lista)== 1:
        if lista[0] == elemento:
            print('retornei esse')
            print(lista[0])
            return lista[0]
        else:
            print('retornei None')
            return
    else:
        if len(lista)%2 != 0:
            meio = len(lista[:len(lista)-1])//2
            print(lista[:meio])
            print(lista[meio:len(lista)-1])
            p = interseccao(elemento,lista[:meio])
            r = interseccao(elemento,lista[meio:len(lista)-1])
            t = interseccao(elemento,lista[len(lista)-1:len(lista)])
            if  p != None or r != None:
                if p != None:
                    print('retornei p')
                    print(p)
                    return p
                else:
                    print('retornei r')
                    print(r)
                    return r
            elif t != None:
                print('retornei t')
                print(t)
                return t
            else:
                print('nao tem o elemento')
                return 
        else:
            meio = len(lista)//2
            print(lista[:meio])
            print(lista[meio:])
            l = interseccao(elemento,lista[:meio])
            k = interseccao(elemento,lista[meio:])
            if  l != None or  k != None:
                if l != None:
                    return l
                else:
                    k
            else:
                return 


def mergesort(v,e,d):
    n = d-e
    if n<=1:
        return
    m = (d+e)//2
    mergesort(v,e,m)
    mergesort(v,m,d)
    intercala(v,e,m,d)
    

#-----------------------------------------------------------
class Cliente:
    '''
        Copie a sua classe Cliente do EP10 para aqui.

        Estenda essa classe adicionando os métodos:
           em_comum() e distanciaX()
        como especifado no enunciado.
 
        Coloque o seu código a seguir.
    '''
    def __init__(self,nome):
            self.nome = nome
            self.classificacao = {}
            self.classificacao_reverse = {}
            self.lista = []
    
    def put_classificacao(self,filmes):
        for i in range(len(filmes)):
            self.classificacao[i] = filmes[i]
            self.classificacao_reverse[filmes[i]] = i
        for j in range(len(self.classificacao)):
            self.lista.append(self.classificacao[j])
    
    def __str__(self):
        x = self.nome+'\n'
        for i in range(len(self.classificacao)):
            x = x + '%d: %s\n' %(i,self.classificacao[i])
        return x
    
    def get_nome(self):
        return self.nome
    
    def get_classificacao(self):
        return self.lista[:]
    
    def distancia(self,other):
        if self.lista == other.lista:
            return 0
        else:
            lista_modelo = {}
            lista_compara = []
            ordem = 0
            for i in range(len(self.lista)):
                if self.lista[i] in other.lista:
                    lista_modelo[self.lista[i]] = ordem
                    ordem += 1
            for j in range(len(other.lista)):
                if other.lista[j] in lista_modelo:
                    lista_compara.append(lista_modelo[other.lista[j]])
            if len(lista_modelo) == 1 or len(lista_modelo) == 2:
                return 0
            else:
                transposicao = 0
                for i in range(0,len(lista_compara)):
                    for j in range(0,len(lista_compara)-1):
                        if lista_compara[j] > lista_compara[j+1]:
                            x = lista_compara[j+1]
                            lista_compara[j+1] = lista_compara[j]
                            lista_compara[j] = x
                            transposicao += 1
                return transposicao

    def em_comum(self,other):
        comum = []
        for i in other.classificacao_reverse:
            if i in self.classificacao_reverse:
                comum.append(self.classificacao_reverse[i])
        return comum
    
    '''
    def distanciaX(self,other):
        comum = []
        for i in range(len(self.lista)):
            if self.lista[i] in other.classificacao_reverse:
                comum.append(other.classificacao_reverse[self.lista[i]])
        return mergesortX(comum,None,None)
    '''
    def distanciaX(self,other):
        comum = []
        for i in other.classificacao_reverse:
            if i in self.classificacao_reverse:
                comum.append(self.classificacao_reverse[i])
        return mergesortX(comum,None,None)
    
FILMES = list('ABCDEFGHIJKL') # = ['A', 'B', ..., 'L']

#------------------------------------------------------------
def main(args=None):
    # para podermos reproduzir os testes
    random.seed(0)

    # lst de filmes
    lst_filmes = args
    if lst_filmes == None: lst_filmes = FILMES
    n_filmes = len(lst_filmes)
    
    print("Cliente(), EP10: iniciando teste...")
    lst_clientes = []
    lst_clientes.append(Cliente("T'Challa"))
    lst_clientes.append(Cliente('Nakia'))
    lst_clientes.append(Cliente('Natasha Romanoff'))
    print("Cliente() não explodiu... sorriso")
    
    print("put_classificacao(), EP10: iniciando teste...")
    lst_clientes[0].put_classificacao(lst_filmes[:5]) 
    random.shuffle(lst_filmes)
    lst_clientes[1].put_classificacao(lst_filmes[:10])
    random.shuffle(lst_filmes) 
    lst_clientes[2].put_classificacao(lst_filmes[:7])
    print("put_classificao() não explodiu... sorriso")

    print("__str__(), EP10: iniciando teste:")
    for cliente in lst_clientes:
        print(cliente)
    print("__str__(): não explodiu... sorriso\n")
    
    print("get_nome() e get_classificacao(), EP10: iniciando teste")
    for cliente in lst_clientes:
        print("    %s: %s"%(cliente.get_nome(), cliente.get_classificacao())) 
    print("get_nome() e get_classificacao() não explodiu sorriso\n")
        
    print("distancia(), EP10: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    distancia(%s,%s)= %s"%(cliente0.get_nome(),
                                          cliente1.get_nome(),
                                          cliente0.distancia(cliente1)))
    print("distancia(): não explodiu... sorriso\n")

    print("mergeX(), EP11: iniciando teste...")
    A = [3,  7, 10, 14, 18]
    B = [2, 11, 16, 20, 23]
    C = A + B
    print("    A: ", A)
    print("    B: ", B)
    print("    C  antes: ", C)
    print("    mergeX('A+B'): retornou ", mergeX(C, 0, 5, 10) )
    print("    C depois: ", C)
    print("mergeX(): não explodiu sorriso\n")

    print("mergesortX(), EP11: iniciando teste...")
    V = [6,7,8,9,10,1,2,3,4,5]
    print("V  antes: ", V)
    print("mergesortX(V): ", mergesortX(V,0,10))
    print("V depois: ", V)
    print("mergesortX(): não explodiu sorriso\n")

    print("em_comum(), EP11: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    em_comum(%s, %s)= %s"%(cliente0.get_nome(),
                                             cliente1.get_nome(),
                                             cliente0.em_comum(cliente1)))
    print("em_comum(): não explodiu... sorriso\n")

    
    print("distanciaX(), EP11: iniciando teste...")
    for cliente0 in lst_clientes:
        for cliente1 in lst_clientes:
            print("    distanciaX(%s, %s)= %s"%(cliente0.get_nome(),
                                               cliente1.get_nome(),
                                               cliente0.distanciaX(cliente1)))
    print("distanciaX(): não explodiu... sorriso\n")
    
#------------------------------------------------------------
        
if __name__ == '__main__':
    main()
'''
Cliente(), EP10: iniciando teste...
Cliente() não explodiu... :-)
put_classificacao(), EP10: iniciando teste...
put_classificao() não explodiu... :-)
__str__(), EP10: iniciando teste:
T'Challa
0: A
1: B
2: C
3: D
4: E

Nakia
0: B
1: J
2: I
3: F
4: K
5: C
6: D
7: H
8: E
9: A

Natasha Romanoff
0: C
1: B
2: F
3: H
4: D
5: G
6: A

__str__(): não explodiu... sorriso

get_nome() e get_classificacao(), EP10: iniciando teste
    T'Challa: ['A', 'B', 'C', 'D', 'E']
    Nakia: ['B', 'J', 'I', 'F', 'K', 'C', 'D', 'H', 'E', 'A']
    Natasha Romanoff: ['C', 'B', 'F', 'H', 'D', 'G', 'A']
get_nome() e get_classificacao() não explodiu :-)

distancia(), EP10: iniciando teste...
    distancia(T'Challa,T'Challa)= 0
    distancia(T'Challa,Nakia)= 4
    distancia(T'Challa,Natasha Romanoff)= 4
    distancia(Nakia,T'Challa)= 4
    distancia(Nakia,Nakia)= 0
    distancia(Nakia,Natasha Romanoff)= 3
    distancia(Natasha Romanoff,T'Challa)= 4
    distancia(Natasha Romanoff,Nakia)= 3
    distancia(Natasha Romanoff,Natasha Romanoff)= 0
distancia(): não explodiu... :-)

mergeX(), EP11: iniciando teste...
    A:  [3, 7, 10, 14, 18]
    B:  [2, 11, 16, 20, 23]
    C  antes:  [3, 7, 10, 14, 18, 2, 11, 16, 20, 23]
    mergeX('A+B'): retornou  8
    C depois:  [2, 3, 7, 10, 11, 14, 16, 18, 20, 23]
mergeX(): não explodiu :-)

mergesortX(), EP11: iniciando teste...
V  antes:  [10, 14, 18, 7, 3, 20, 23, 11, 2, 16]
mergesortX(V):  22
V depois:  [2, 3, 7, 10, 11, 14, 16, 18, 20, 23]
mergesortX(): não explodiu :-)

em_comum(), EP11: iniciando teste...
    em_comum(T'Challa, T'Challa)= [0, 1, 2, 3, 4]
    em_comum(T'Challa, Nakia)= [1, 2, 3, 4, 0]
    em_comum(T'Challa, Natasha Romanoff)= [2, 1, 3, 0]
    em_comum(Nakia, T'Challa)= [9, 0, 5, 6, 8]
    em_comum(Nakia, Nakia)= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    em_comum(Nakia, Natasha Romanoff)= [5, 0, 3, 7, 6, 9]
    em_comum(Natasha Romanoff, T'Challa)= [6, 1, 0, 4]
    em_comum(Natasha Romanoff, Nakia)= [1, 2, 0, 4, 3, 6]
    em_comum(Natasha Romanoff, Natasha Romanoff)= [0, 1, 2, 3, 4, 5, 6]
em_comum(): não explodiu... :-)

distanciaX(), EP11: iniciando teste...
    distanciaX(T'Challa, T'Challa)= 0
    distanciaX(T'Challa, Nakia)= 4
    distanciaX(T'Challa, Natasha Romanoff)= 4
    distanciaX(Nakia, T'Challa)= 4
    distanciaX(Nakia, Nakia)= 0
    distanciaX(Nakia, Natasha Romanoff)= 3
    distanciaX(Natasha Romanoff, T'Challa)= 4
    distanciaX(Natasha Romanoff, Nakia)= 3
    distanciaX(Natasha Romanoff, Natasha Romanoff)= 0
distanciaX(): não explodiu... :-)
'''

NMAX = 2**18

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
        cliente0.put_classificacao(lst0)
        cliente1 = Cliente("cliente 1")
        cliente1.put_classificacao(lst1)
        cliente2 = Cliente("cliente 2")
        cliente2.put_classificacao(lst2)

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

        print("    %10d    %10d   %10d"%(dist,n*(n-1)/2, int(n*math.log2(n))))
        
        if dist != distX:
            print("SOCORRO! distancia() = %s != %s = distanciaX()"%(dist, distX))

        n *= 2

#------------------------------------------------------------
        
if __name__ == '__main__':
    main()
'''
       n   distancia  distanciaX  transposicões     n(n-1)/2       n lg n
        16     0.000s      0.000s            57           120           64
        32     0.000s      0.000s           235           496          160
        64     0.000s      0.000s           986          2016          384
       128     0.000s      0.000s          4040          8128          896
       256     0.003s      0.001s         14671         32640         2048
       512     0.009s      0.001s         67048        130816         4608
      1024     0.037s      0.002s        268099        523776        10240
      2048     0.141s      0.004s       1047562       2096128        22528
      4096     0.565s      0.009s       4193792       8386560        49152
      8192     2.286s      0.019s      16933586      33550336       106496
     16384     9.147s      0.043s      67154125     134209536       229376
     32768    36.156s      0.092s     268038659     536854528       491520
     65536   147.602s      0.196s    1079833182    2147450880      1048576
    131072   626.293s      0.482s    4306961144    8589869056      2228224
'''





