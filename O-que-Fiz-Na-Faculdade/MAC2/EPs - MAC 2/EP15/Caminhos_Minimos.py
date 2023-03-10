from grafo import Grafo
import copy 
     

class Caminhos_Minimos:
    
    def __init__(self,Grafo,origem):
        self.Grafo = Grafo
        self.origem = origem
        self.distancias = {}
        self.anteriores = {}
        self.ordem = {}
        self.ordem_reverse = {}
        self.vertice = self.Grafo.vertice.copy()
        if self.origem in self.vertice:
            conta = 0
            for i in self.vertice:
                self.ordem[i] = conta
                self.ordem_reverse[conta]=i
                conta += 1
            n = len(self.vertice)
            d = n*[n]
            d[self.ordem[self.origem]] = 0
            q = [self.ordem[self.origem]]
            while len(q) != 0:
                i = q.pop(0)
                for j in range(n):
                    if d[j] > d[i]+1 and self.ordem_reverse[j] in self.Grafo.adjacentes(self.ordem_reverse[i]):
                        d[j] = d[i]+1
                        self.anteriores[self.ordem_reverse[j]] = self.ordem_reverse[i]
                        q.append(j)
                q.sort()
            for i in range(len(d)):
                self.distancias[self.ordem_reverse[i]] = d[i]
            
                
        
            
        
    def __str__(self):
        x = 'Caminhos Minimos a partir de %s\n' %(self.origem)
        for i in self.vertice:
            x = x + i +': '
            if self.distancias[i] != 0:
                x = x + '%d, ' %(self.distancias[i]) +'%s\n' %(self.anteriores[i])
            else:
                x = x + '%d, ' %(self.distancias[i]) +'None\n'
        return x
    
    def distancia(self,v):
        if v not in self.vertice:
            return
        return self.distancias[v]
                
    def anterior(self,v):
        if v == self.origem:
            return
        return self.anteriores[v]
    
    def caminho(self,v):
        cobaia = [v]
        while v != self.origem:
            cobaia.append(self.anteriores[v])
            v = self.anteriores[v]
        lista = []
        for i in range(len(cobaia)):
            lista.append(cobaia[-i-1])
        return lista
    
def main():
    g = Grafo('grafo.txt')
    gr = Grafo('routes.txt')
    gm = Grafo('movies.txt', "/")
    print('Mostra os seus vertices')
    print()
    print(g.vertices())
    print()
    print(g)
    print()
    print(gr.vertices())
    print()
    print(gr)
    print('gm')
    print()
    print(gm.V())
    print()
    #print(gm.A())
    print()
    print('Teste init')
    print()
    caminhos_H = Caminhos_Minimos(g, "H")
    caminhos_LAS = Caminhos_Minimos(gr, "LAS")
    caminhos_X = Caminhos_Minimos(g, "X")
    print('Teste distancia')
    print()
    print(caminhos_H.distancia("A"))
    print()
    print(caminhos_H.distancia("G"))
    print()
    print(caminhos_H.distancia("H"))
    print()
    print(caminhos_LAS.distancia("JFK"))
    print()
    print(caminhos_LAS.distancia("MCO"))
    print()
    print('Teste anterior')
    print()
    print(caminhos_H.anterior("A"))
    print()
    print(caminhos_H.anterior("G"))
    print()
    print(caminhos_H.anterior("H"))
    print()
    print(caminhos_LAS.anterior("JFK"))
    print()
    print(caminhos_LAS.anterior("MCO"))
    print()
    print('Teste caminho')
    print()
    print(caminhos_H.caminho("A"))
    print()
    print(caminhos_H.caminho("G"))
    print()
    print(caminhos_H.caminho("H"))
    print()
    print(caminhos_LAS.caminho("JFK"))
    print()
    print(caminhos_LAS.caminho("MCO"))
    print()
    print('Teste str')
    print(caminhos_H)
    print()
    print(caminhos_LAS)
    print()
main()

'''
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from grafo import Grafo
    >>> from caminhos_minimos import Caminhos_Minimos
    >>> g = Grafo("grafo.txt") 
    >>> gr = Grafo("routes.txt")
    >>> gm = Grafo("movies.txt", "/")
    >>> g.vertices()
    ['A', 'B', 'C', 'G', 'H']
    >>> gr.vertices()
    ['JFK', 'MCO', 'ORD', 'DEN', 'HOU', 'ATL', 'DFW', 'PHX', 'LAX', 'LAS']
    >>> print(g)
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B

    >>> print(gr)
    ATL | MCO, JFK, HOU, ORD
    DEN | ORD, PHX, LAS
    DFW | PHX, ORD, HOU
    HOU | ORD, ATL, DFW
    JFK | MCO, ATL, ORD
    LAS | DEN, LAX
    LAX | PHX, LAS
    MCO | JFK, ATL
    ORD | DEN, HOU, DFW, PHX, JFK, ATL
    PHX | DFW, ORD, DEN, LAX

    >>> gm.V()
    119429
    >>> gm.A()
    202927
    >>> caminhos_H = Caminhos_Minimos(g, "H")
    >>> caminhos_LAS = Caminhos_Minimos(gr, "LAS")
    >>> caminhos_X = Caminhos_Minimos(g, "X")
    Caminhos.__init__(): 'X' n??o ?? vertice do grafo
    >>> caminhos_GRU = Caminhos_Minimos(gr, "GRU")
    Caminhos.__init__(): 'GRU' n??o ?? vertice do grafo
    >>> caminhos_Bacon = Caminhos_Minimos(gm, "Bacon, Kevin")
    >>> 
    >>> caminhos_H.distancia("A")
    1
    >>> caminhos_H.distancia("G")
    2
    >>> caminhos_H.distancia("H")
    0
    >>> caminhos_LAS.distancia("JFK")
    3
    >>> caminhos_LAS.distancia("MCO")
    4
    >>> caminhos_Bacon.distancia("Chaplin, Charles")
    4
    >>> caminhos_Bacon.distancia("Kidman, Nicole")
    4
    >>> caminhos_H.anterior("A")
    'H'
    >>> caminhos_H.anterior("G")
    'A'
    >>> caminhos_H.anterior("H")
    >>> caminhos_LAS.anterior("JFK")
    'ORD'
    >>> caminhos_LAS.anterior("MCO")
    'JFK'
    >>> caminhos_Bacon.anterior("Chaplin, Charles")
    'Chaplin (1992)'
    >>> caminhos_Bacon.anterior("Kidman, Nicole")
    'Cold Mountain (2003)'
    >>> 
    >>> caminhos_H.caminho("A")
    ['H', 'A']
    >>> caminhos_H.caminho("G")
    ['H', 'A', 'G']
    >>> caminhos_H.caminho("H")
    ['H']
    >>> caminhos_LAS.caminho("JFK")
    ['LAS', 'DEN', 'ORD', 'JFK']
    >>> caminhos_LAS.caminho("MCO")
    ['LAS', 'DEN', 'ORD', 'JFK', 'MCO']
    >>> caminhos_Bacon.caminho("Chaplin, Charles")
    ['Bacon, Kevin', 'JFK (1991)', 'Matthau, Walter', 'Chaplin (1992)', 'Chaplin, Charles']
    >>> caminhos_Bacon.caminho("Kidman, Nicole")
    ['Bacon, Kevin', 'Animal House (1978)', 'Sutherland, Donald (I)', 'Cold Mountain (2003)', 'Kidman, Nicole']
    >>> caminhos_Bacon.caminho("Hanks, Tom")
    ['Bacon, Kevin', 'Apollo 13 (1995)', 'Hanks, Tom']
    >>> 
    >>> str(caminhos_H)
    "Caminhos M??nimos a partir de 'H'\nA: 1, H\nB: 1, H\nC: 2, A\nG: 2, A\nH: 0, None\n"
    >>> print(caminhos_H)
    Caminhos M??nimos a partir de 'H'
    A: 1, H
    B: 1, H
    C: 2, A
    G: 2, A
    H: 0, None

    >>> print(caminhos_LAS)
    Caminhos M??nimos a partir de 'LAS'
    ATL: 3, ORD
    DEN: 1, LAS
    DFW: 3, ORD
    HOU: 3, ORD
    JFK: 3, ORD
    LAS: 0, None
    LAX: 1, LAS
    MCO: 4, JFK
    ORD: 2, DEN
    PHX: 2, DEN

    >>> print(caminhos_Bacon)
    [... muitas linhas removidas ...]
    ??shima, Y??ko: 6, Ringu (1998)
    ??ta, Takako: 4, Kaze no tani no Naushika (1984)
    ??take, Hiroshi: 6, Akira (1988)
    ??tomo, Ry??zabur??: 6, Vampaia hant?? D (2000)
    ??tomo, T??ru: 6, Gohatto (1999)
    ??tsu, Yayoi: 6, ??dishon (1999)
    ??tsuka, Akio: 4, Kurenai no buta (1992)
    ??tsuka, Chihiro: 8, Honogurai mizu no soko kara (2002)
    ??tsuka, Chikao: 6, Vampaia hant?? D (2000)
    ??tsuka, H??ch??: 4, Kaze no tani no Naushika (1984)
    ??tsuki, Sh??ji: 6, Hana-bi (1997)
    ??rner, Ingvar: 4, Dogville (2003)
    ??ss, Eniko: 4, Dracula (1992)
    ??zat, Atilla: 6, Kurtlar vadisi - Irak (2006)
    ??zat, Perihan: 6, Kurtlar vadisi - Irak (2006)
    ??zben, Murat: 6, Kurtlar vadisi - Irak (2006)
    ??zberk, ??zge: 119429, None
    ??zcan, ??nder: 6, Kurtlar vadisi - Irak (2006)
    ??zdemir, Kemal: 6, Kurtlar vadisi - Irak (2006)
    ??zkul, M??nir: 119429, None
    ??zk??????k, G??zde: 6, Kurtlar vadisi - Irak (2006)
    ??zpinar, Esra: 6, Kurtlar vadisi - Irak (2006)
    ??zt??rk, Abdurrahman: 6, Kurtlar vadisi - Irak (2006)
    ??gendahl, Mick: 6, Madagascar (2005)
    ??igaard, Emil: 6, I Kina spiser de hunde (1999)
    ??nel, Birol: 4, Enemy at the Gates (2001)
    ??ner, Idil: 6, Im Juli. (2000)
    ??orsteinsson, J??n P??tur: 8, 101 Reykjav??k (2000)
    ??orvaldsd??ttir, El??n: 8, 101 Reykjav??k (2000)
    ??orvaldsson, Gu??mundur Ingi: 8, 101 Reykjav??k (2000)
    ????rarinsd??ttir, Lilja N??tt: 8, 101 Reykjav??k (2000)

    >>> 
'''

'''
Nota
Revisado em quinta, 28 nov 2019, 13:39 por Atribui????o autom??tica de nota
grade: 1,0 / 10,0

Relat??rio de avalia????o[-]
Grafo('grafo.txt'): iniciando avalia????o (vale 3 ponto(s))
Caminhos_Minimos(Grafo('grafo.txt'), 'A') explodiu: 'Grafo' object 
has no attribute 'vertice'
n??o passou no(s) teste(s) acima
Grafo('grafo.txt'): avalia????o encerrada... (nota 0)

Grafo('routes.txt'): iniciando avalia????o (vale 3 ponto(s))
Caminhos_Minimos(Grafo('routes.txt'), 'JFK') explodiu: 'Grafo' 
object has no attribute 'vertice'
n??o passou no(s) teste(s) acima
Grafo('routes.txt'): avalia????o encerrada... (nota 0)

Grafo('grafoX.txt'): iniciando avalia????o (vale 3 ponto(s))
Caminhos_Minimos(Grafo('grafoX.txt'), 'A') explodiu: 'Grafo' 
object has no attribute 'vertice'
n??o passou no(s) teste(s) acima
Grafo('grafoX.txt'): avalia????o encerrada... (nota 0)

__str__(): vale 1 ponto
m??todo encontrado :-)
__str__(): avalia????o encerrada... (nota 1)

Seu programa n??o passou no(s) teste(s) acima. :-(

Fim da avalia????o.
'''


