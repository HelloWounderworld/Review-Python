class Grafo:
    '''
    Amanha ver com o monitor sobre cast.G.txt
    Aproveita pergunta sobre o negócio do T(n)
    Tente algoritmizar mais o self.vertice de maneira que ele consiga
    pegar qualquer texto e tornar-la numa estrutura de um grafo usando
    bem as funçoes de set e dicionario
    '''
    def __init__(self,strings = '',caractere = ' '):
        self.strings = strings
        self.caractere = caractere
        self.vertice = {}
        if self.strings != '' and self.caractere == ' ':
            for i in self.strings:
                d = i.split('\n')
                p = d[0].split(self.caractere)
                if p[0] not in self.vertice:
                    self.vertice[p[0]] = []
                for j in range(1,len(p)):
                    self.vertice[p[0]].append(p[j])
        else:
            for i in self.strings:
                d = i.split('\n')
                p = d[0].split(self.caractere)
                if p[0] not in self.vertice:
                    self.vertice[p[0]] = []
                for j in range(1,len(p)):
                    self.vertice[p[0]].append(p[j])
                    if p[j] not in self.vertice:
                        self.vertice[p[j]] = []
                        self.vertice[p[j]].append(p[0])
                    else:
                        self.vertice[p[j]].append(p[0])
    
    def __str__(self):
        x = ''
        if len(self.vertice) == 0:
            return x
        if self.caractere == ' ':
            for i in self.vertice:
                x = x + i + ' | '
                self.vertice[i].sort()
                n = len(self.vertice[i])
                for j in range(n):
                    if j == n-1:
                        x = x + self.vertice[i][j] + '\n'
                    else:
                        x = x + self.vertice[i][j] + ', '
            return x
        else:
            for i in self.vertices:
                x = x + i + ' | '
                n = len(self.vertice[i])
                for j in range(n):
                    if j == n-1:
                        x = x + self.vertice[i][j] + '\n'
                    else:
                        x = x + self.vertice[i][j] + ', '
            return x
        
    def insira_aresta(self,v,w):
        if v == '' or w == '':
            return ''
        else:
            if len(self.vertice) == 0:
                self.vertice[v] = [w]
                self.vertice[w] = [v]
            else:
                if v not in self.vertice:
                    self.vertice[v] = [w]
                    if w not in self.vertice:
                        self.vertice[w] = [v]
                    else:
                        self.vertice[w].append(v)
                        
                else:
                    self.vertice[v].append(w)
                    if w not in self.vertice:
                        self.vertice[w] = [v]
                    else:
                        self.vertice[w].append(v)
    
    def tem_vertice(self,v):
        if v not in self.vertice:
            return False
        return True
    
    def V(self):
        return len(self.vertice)
    
    def A(self):
        aresta = 0
        contados = []
        for i in self.vertice:
            for j in self.vertice[i]:
                if j not in contados:
                    aresta += 1
            contados.append(i)
        return aresta
    
    def vertices(self):
        return list(self.vertice)
    
    def adjacentes(self,v):
        if v not in self.vertice:
            return 
        return self.vertice[v]
    
    def grau(self,v):
        if v not in self.vertice:
            return 0
        return len(self.vertice[v])
    
    def tem_aresta(self,v,w):
        if v not in self.vertice:
            return False
        else:
            if w in self.vertice[v]:
                return True
            else:
                return False
'''   
def main():
    f = open('grafo.txt','r',encoding = 'utf-8')
    p = open('cast.G.txt','r',encoding = 'utf-8')
    print('Teste init')
    g0 = Grafo() # grafo vazio
    g1 = Grafo(f) # carrega o grafo representado em grafo.txt
    g2 = Grafo(p,"/") # carrega o grafo em cast.G.txt, "/" é o caractere separador
    print()
    print('Teste String')
    print(g0)
    print()
    print(g1)
    print()
    #print(g2)
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
    print(g0.V())
    print(g1.V())
    print(g2.V())
    print('Teste A()')
    print(g0.A())
    print(g1.A())
    print(g2.A())
    print('Teste vertices()')
    print(g0.vertices())
    print(g1.vertices())
    #print(g2.vertices())
    print('Teste adjacente')
    print(g0.adjacentes("www.ime.usp.br/dcc"))
    print(g0.adjacentes("www.ime.usp.br"))
    print(g1.adjacentes("A"))
    print(g1.adjacentes("Z"))
    print(g2.adjacentes("Chaplin, Charles"))
    print(g2.adjacentes("Andrews, Julie (I)"))
    print('Teste grau()')
    print(g0.grau("www.ime.usp.br/dcc"))
    print(g0.grau("www.ime.usp.br"))
    print(g1.grau("A"))
    print(g1.grau("Z"))
    print(g2.grau("Chaplin, Charles"))
    print(g2.grau("Andrews, Julie (I)"))
    print('Teste tem_aresta')
    print(g0.tem_aresta("www.ime.usp.br", "www.ime.usp.br/dcc"))
    print(g0.tem_aresta("www.ime.usp.br/mae", "www.ime.usp.br/dcc"))
    print(g1.tem_aresta("A","Z"))
    print(g1.tem_aresta("A","B"))
    print(g2.tem_aresta("Chaplin, Charles", "Great Dictator, The (1940)"))
    print(g2.tem_aresta("Sound of Music, The (1965)", "Andrews, Julie (I)"))
    print(g2.tem_aresta("Great Dictator, The (1940)", "Andrews, Julie (I)"))
main()


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
    www.ime.usp.br | www.ime.usp.br/bib, www.ime.usp.br/dcc, www.ime.usp.br/mae, www.ime.usp.br/map, www.ime.usp.br/mat
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
    ['www.ime.usp.br/bib', 'www.ime.usp.br/dcc', 'www.ime.usp.br/mae', 'www.ime.usp.br/map', 'www.ime.usp.br/mat']
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
    
    



