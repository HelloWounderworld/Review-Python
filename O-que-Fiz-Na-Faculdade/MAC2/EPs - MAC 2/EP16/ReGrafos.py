class Grafo:
    '''
        Construa de novo a classe Grafos seguindo apenas a lógica que vem em 
        mente sem se preocupar muito com o detalhe.
    '''
    def __init__(self,strings = '',caractere = ' '):
        '''
            um objeto Grafo pode ser criado vazio escrevendo-se Grafo(). 
            Um objeto Grafo também pode ser criado lendo-se a sua descrição 
            de um arquivo. Os vértices de um objeto Grafo serão strings; 
            os nomes dos vértices. Cada linha de um arquivo com a descrição 
            de um grafo deve conter strings separadas por um certo caractere 
            separador. A primeira string na linha define o nome de um vértice
            e as demais strings correspondem aos vértices que são seus vizinhos. 
            Suponha que o conteúdo de um arquivo grafo.txt seja:
        '''
        self.strings = strings
        self.caractere = caractere
        self.vertice = {}
        if self.strings != '':
            texto = open(self.strings,'r',encoding = 'utf-8')
            for i in texto:
                l = i.split('\n')
                lista = l[0].split(self.caractere)
                if lista[0] not in self.vertice:
                    self.vertice[lista[0]]=set()
                self.vertice[lista[0]].update(lista[1:])
                for j in lista[1:]:
                    if j not in self.vertice:
                        self.vertice[j] = set()
                        self.vertice[j].add(lista[0])
                    else:
                        self.vertice[j].add(lista[0])
    
    def __str__(self):
        x = ''
        if len(self.vertice) == 0:
            return x
        lista = list(self.vertice)
        lista.sort()
        for i in lista:
            x = x+'%s | ' %(i)
            lista = list(self.vertice[i])
            lista.sort()
            for j in range(0,len(lista)):
                if j == len(lista)-1:
                    x = x +'%s\n' %(lista[j])
                else:
                    x = x +'%s, ' %(lista[j])
        return x
        
    def insira_aresta(self,v,w):
        '''
            uma aresta entre um vértice de nome v e um vértice de nome w pode 
            ser inserida no grafo através do método insira_aresta(v, w). 
            Os nomes v e w devem ser strings não vazias (!= '') sem espaços 
            no início ou no final.
        '''
        if v == '' or w == '':
            return ''
        else:
            if ' ' in v:
                lista = v.split(' ')
                for i in lista:
                    if i != '':
                        v = i
            if ' ' in w:
                lista = w.split(' ')
                for i in lista:
                    if i != '':
                        w = i
            if len(self.vertice) == 0:
                self.vertice[v] = set()
                self.vertice[v].add(w)
                self.vertice[w] = set()
                self.vertice[w].add(v)
            else:
                if v not in self.vertice:
                    self.vertice[v] = set()
                    self.vertice[v].add(w)
                    if w not in self.vertice:
                        self.vertice[w] = set()
                        self.vertice[w].add(v)
                    else:
                        self.vertice[w].add(v)
                        
                else:
                    self.vertice[v].add(w)
                    if w not in self.vertice:
                        self.vertice[w] = set()
                        self.vertice[w].add(v)
                    else:
                        self.vertice[w].add(v)
    
    def tem_vertice(self,v):
        '''
            retorna True se v em um vértice do grafo e 
            False em caso contrário; e
        '''
        if v not in self.vertice:
            return False
        return True
    
    def V(self):
        '''
            retorna o número de vértices do grafo;
        '''
        return len(self.vertice)
    
    def A(self):
        '''
            retorna o número de arestas do grafo;
        '''
        aresta = 0
        contados = []
        for i in self.vertice:
            for j in self.vertice[i]:
                if j not in contados:
                    aresta += 1
            contados.append(i)
        return aresta
    
    def vertices(self):
        '''
            retorna a lista dos vértices do grafo;
        '''
        lista = list(self.vertice)
        lista.sort()
        return lista
    
    def adjacentes(self,v):
        '''
            retorna a lista dos vértices adjacentes ao vértice v;
        '''
        if v not in self.vertice:
            return 
        lista = list(self.vertice[v])
        lista.sort()
        return lista
    
    def grau(self,v):
        '''
            retorna o número de vizinhos de v;
        '''
        if v not in self.vertice:
            return 0
        return len(self.vertice[v])
    
    def tem_aresta(self,v,w):
        '''
            retorna True se v-w é uma aresta do grafo e False em caso contrário
        '''
        if v not in self.vertice:
            return False
        else:
            if w in self.vertice[v]:
                return True
            else:
                return False

def main():
    #f = open('grafo.txt','r',encoding = 'utf-8')
    #p = open('cast.G.txt','r',encoding = 'utf-8')
    print('Teste init')
    g0 = Grafo() # grafo vazio
    g1 = Grafo('grafo.txt') # carrega o grafo representado em grafo.txt
    g2 = Grafo('cast.G.txt','/') # carrega o grafo em cast.G.txt, "/" é o caractere separador
    g3 = Grafo('routes.txt')
    g4 = Grafo('grafoX.txt')
    print()
    print('Teste String')
    print(g0)
    print()
    print(g1)
    print()
    #print(g2)
    print()
    print('Teste drive')
    print(g3)
    print()
    print(g4)
    print()
    print('Teste de insira_aresta')
    g0.insira_aresta('', 'x')
    print(g0)
    print()
    g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/bib')
    g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/dcc')
    g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mae')
    g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/map')
    g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mat')
    print(g0)
    print()
    g1.insira_aresta('H','X') # vértices devem ser strings
    print(g1)
    print()
    g1.insira_aresta('Z','X') # espaços devem ser removidos
    print(g1)
    print()
    print('Teste tem_vertice')
    print(g0.tem_vertice('www.ime.usp.br/mac'))
    print()
    print(g0.tem_vertice('www.ime.usp.br/dcc'))
    print()
    print(g1.tem_vertice('blá'))
    print()
    print(g1.tem_vertice('Z'))
    print()
    print(g2.tem_vertice("Chaplin, Charles"))
    print()
    print(g2.tem_vertice("Streep, Meryl"))
    print()
    print(g2.tem_vertice("Andrews, Julie (I)"))
    print()
    print('Teste V()')
    print()
    print(g0.V())
    print()
    print(g1.V())
    print()
    print(g2.V())
    print()
    print('Teste drive')
    print(g3.V())
    print()
    print(g4.V())
    print()
    print('Teste A()')
    print()
    print(g0.A())
    print()
    print(g1.A())
    print()
    print(g2.A())
    print()
    print('Teste drive')
    print(g3.A())
    print()
    print(g4.A())
    print()
    print('Teste vertices()')
    print()
    print(g0.vertices())
    print()
    print(g1.vertices())
    print()
    #print(g2.vertices())
    print()
    print('Teste adjacente')
    print()
    print(g0.adjacentes("www.ime.usp.br/dcc"))
    print()
    print(g0.adjacentes("www.ime.usp.br"))
    print()
    print(g1.adjacentes("A"))
    print()
    print(g1.adjacentes("Z"))
    print()
    print(g2.adjacentes("Chaplin, Charles"))
    print()
    print(g2.adjacentes("Andrews, Julie (I)"))
    print()
    print('Teste grau()')
    print()
    print(g0.grau("www.ime.usp.br/dcc"))
    print()
    print(g0.grau("www.ime.usp.br"))
    print()
    print(g1.grau("A"))
    print()
    print(g1.grau("Z"))
    print()
    print('Teste drive')
    print(g1.grau('H'))
    print()
    print(g2.grau("Chaplin, Charles"))
    #print(g2.vertice["Chaplin, Charles"])
    print()
    print(g2.grau("Andrews, Julie (I)"))
    #print(g2.vertice["Andrews, Julie (I)"])
    print()
    print('Teste tem_aresta')
    print()
    print(g0.tem_aresta("www.ime.usp.br", "www.ime.usp.br/dcc"))
    print()
    print(g0.tem_aresta("www.ime.usp.br/mae", "www.ime.usp.br/dcc"))
    print()
    print(g1.tem_aresta("A","Z"))
    print()
    print(g1.tem_aresta("A","B"))
    print()
    print(g2.tem_aresta("Chaplin, Charles", "Great Dictator, The (1940)"))
    print()
    print(g2.tem_aresta("Sound of Music, The (1965)", "Andrews, Julie (I)"))
    print()
    print(g2.tem_aresta("Great Dictator, The (1940)", "Andrews, Julie (I)"))
    print()
main()


'''
     Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from grafo import Grafo
    >>> g0 = Grafo() # grafo vazio
    >>> g1 = Grafo("grafo.txt") # carrega o grafo representado em grafo.txt
    >>> g2 = Grafo("cast.G.txt","/") # carrega o grafo em cast.G.txt, "/" é o caractere separador
    >>> 
     >>> str(g0)
    ''
    >>> print(g0)

    >>> str(g1)
    'A | B, C, G, H\nB | A, C, H\nC | A, B, G\nG | A, C\nH | A, B\n'
    >>> print(g1)
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B

    >>> str(g2)
    [... trecho removido ...]Incredible\nÉmile/Coutu, | Nikki,\nÉva/Tolnay, 
    | Szerelmi\nÓscar/De | Royal\nÓscar/Lillo, 
    | Yo\nÖllegård | På\nÖllegård/Ericks, | Pippi\nÖllegård/Nilsson, 
    | Pippi\nÖllegård/Trooger, | Här\nà | Flûte, Un\nálmok | Szerelmi\n"
    >>> print(g2)
    [... muitas linhas removidas ...]
    Öllegård/Nilsson, | Pippi
    Öllegård/Trooger, | Här
    à | Flûte, Un
    álmok | Szerelmi

    >>> 
     >>> g0.insira_aresta('', 'x')
    >>> print(g0)

    >>> g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/bib')
    >>> g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/dcc')
    >>> g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mae')
    >>> g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/map')
    >>> g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mat')
    >>> print(g0)
    www.ime.usp.br | www.ime.usp.br/bib, www.ime.usp.br/dcc, www.ime.usp.br/mae, 
    www.ime.usp.br/map, www.ime.usp.br/mat
    www.ime.usp.br/bib | www.ime.usp.br
    www.ime.usp.br/dcc | www.ime.usp.br
    www.ime.usp.br/mae | www.ime.usp.br
    www.ime.usp.br/map | www.ime.usp.br
    www.ime.usp.br/mat | www.ime.usp.br
    
    >>> g1.insira_aresta('H','X') # vértices devem ser strings
    >>> print(g1)
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B, X
    X | H

    >>> g1.insira_aresta(' Z ',' X ') # espaços devem ser removidos
    >>> print(g1)
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B, X
    X | H, Z
    Z | X

    >>> 
    >>> g0.tem_vertice('www.ime.usp.br/mac')
    False
    >>> g0.tem_vertice('www.ime.usp.br/dcc')
    True
    >>> g1.tem_vertice('blá')
    False
    >>> g1.tem_vertice('Z')
    True
    >>> g2.tem_vertice("Chaplin, Charles")
    True
    >>> g2.tem_vertice("Streep, Meryl")
    False
    >>> g2.tem_vertice("Andrews, Julie (I)")
    True
    >>> g0.V()
    6
    >>> g1.V()
    7
    >>> g2.V()
    22465
    >>> 
    >>> g0.A()
    5
    >>> g1.A()
    9
    >>> g2.A()
    28485
    >>> 
    >>> g0.vertices()
    ['www.ime.usp.br', 'www.ime.usp.br/bib', 'www.ime.usp.br/dcc', 
    'www.ime.usp.br/mae', 'www.ime.usp.br/map', 'www.ime.usp.br/mat']
    >>> g1.vertices()
    ['A', 'B', 'C', 'G', 'H', 'X', 'Z']
     >> g2.vertices()
    [ ..., Gabriella', 'Maksimova, Yekaterina', 'Gall, Axelle', 'Cei, Pina', 
    'Stratas, Teresa', 'Wild Country, The (1970)', 'Miller, F. Ben', 'Chambliss, 
    Woody']
     >>> g0.adjacentes("www.ime.usp.br/dcc") 
    ['www.ime.usp.br']
    >>> g0.adjacentes("www.ime.usp.br")     
    ['www.ime.usp.br/bib', 'www.ime.usp.br/dcc', 'www.ime.usp.br/mae', 
    'www.ime.usp.br/map', 'www.ime.usp.br/mat']
    >>> g1.adjacentes("A")  
    ['B', 'C', 'G', 'H']
    >>> g1.adjacentes("Z")  
    ['X']
    >>> g2.adjacentes("Chaplin, Charles")   
    ['Circus, The (1928)', 'City Lights (1931)', 'Countess from Hong Kong, 
    A (1967)', 'Gentleman Tramp, The (1975)', 'Great Dictator, The (1940)', 
    "It's Showtime (1976)", 'King in New York, A (1957)', 'Limelight (1952)']
    >>> g2.adjacentes("Andrews, Julie (I)")
    ['Darling Lili (1970)', 'Mary Poppins (1964)', 
    'Princess Diaries 2: Royal Engagement, The (2004)', 
    'Princess Diaries, The (2001)', 'Sound of Music, The (1965)', 
    'Star! (1968)', 'Thoroughly Modern Millie (1967)']
     >>> g0.grau("www.ime.usp.br/dcc")       
    1
    >>> g0.grau("www.ime.usp.br")   
    5
    >>> g1.grau("A")        
    4
    >>> g1.grau("Z")        
    1
    >>> g2.grau("Chaplin, Charles") 
    8
    >>> g2.grau("Andrews, Julie (I)")
    7
    >>> 
     >>> g0.tem_aresta("www.ime.usp.br", "www.ime.usp.br/dcc")       
    True
    >>> g0.tem_aresta("www.ime.usp.br/mae", "www.ime.usp.br/dcc")   
    False
    >>> g1.tem_aresta("A","Z")
    False
    >>> g1.tem_aresta("A","B")
    True
    >>> g2.tem_aresta("Chaplin, Charles", "Great Dictator, The (1940)")
    True
    >>> g2.tem_aresta("Sound of Music, The (1965)", "Andrews, Julie (I)")
    True
    >>> g2.tem_aresta("Great Dictator, The (1940)", "Andrews, Julie (I)")
    False
'''    
'''
Nota
Revisado em quarta, 27 nov 2019, 11:28 por Atribuição automática de nota
grade: 7,8 / 10,0

Relatório de avaliação[-]
O retorno do método V() é diferente do esperado para o arquivo grafo.txt. (-0.417)
Valor esperado: 5
Saída do seu programa: 6

O retorno do método A() é diferente do esperado para o arquivo grafo.txt. (-0.417)
Valor esperado: 7
Saída do seu programa: 8

O retorno do método grau(H) é diferente do esperado para o arquivo grafo.txt. (-0.083)
Valor esperado: 2
Saída do seu programa: 3

O retorno do método __str__ é diferente do esperado para o arquivo grafo.txt. (-0.417)
Saída do seu programa:
| H
A | B, C, G, H
B | A, C, H
C | A, B, G
G | A, C
H | , A, B

Valor esperado:
A | B, C, G, H
B | A, C, H
C | A, B, G
G | A, C
H | A, B


O retorno do método V() é diferente do esperado para o arquivo grafoX.txt. (-0.417)
Valor esperado: 10
Saída do seu programa: 11

O retorno do método __str__ é diferente do esperado para o arquivo grafoX.txt. (-0.417)
Saída do seu programa:
| A | B, C, G, H
A2 | B2, C2, G2, H2
B | A, C, H
B2 | A2, C2, H2
C | A, B, G
C2 | A2, B2, G2
G | A, C
G2 | A2, C2
H | A, B
H2 | A2, B2

Valor esperado:
A | B, C, G, H
A2 | B2, C2, G2, H2
B | A, C, H
B2 | A2, C2, H2
C | A, B, G
C2 | A2, B2, G2
G | C, A
G2 | A2, C2
H | A, B
H2 | A2, B2
'''

