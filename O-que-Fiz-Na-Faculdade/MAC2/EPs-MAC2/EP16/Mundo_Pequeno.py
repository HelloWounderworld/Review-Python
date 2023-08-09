from grafo import Grafo
from caminhos_minimos import Caminhos_Minimos
import copy
import math

class Mundo_Pequeno:
    
    def __init__(self,Grafo):
        '''
            para ser criado, o construtor de um objeto Mundo_Pequeno deve 
            receber um objeto Grafo. O consumo de tempo da construção de um 
            objeto dessa classe deve ser O(V × T(V, A)) onde V é o número de 
            vértices e A é o número de arestas do grafo e T(V, A) é o consumo 
            de tempo para encontrarmos caminhos mínimos a partir de um vértice 
            origem (= consumo de tempo para criarmos um objeto Caminhos_Minimos).
        '''
        self.Grafo = Grafo
        pass
    
    def __str__(self):
        return ''
    
    def grau_medio(self):
        '''
            retorna o grau médio dos vértices do grafo. 
            O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
    def distancia_media(self):
        '''
            retorna a distância média entre os vértices do grafo. 
            Se não existir nenhum caminho entre algum par de vértices o método 
            deve retorna o número V de vértices do grafo. Para todos os efeitos, 
            V funciona como infinito. 
            O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
    def distancia_mediaX(self):
        '''
            semelhante a distancia_media(), entretanto, para efeito da média, 
            leva em consideração apenas os pares de vértices ligados por algum 
            caminho. O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
    def coeficiente_agrupamento_local(self,v):
        '''
            recebe como argumento um vértice v e retorna o coeficiente de 
            agrupamento local de v. 
            O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
    def coeficiente_agrupamento(self):
        '''
             retorna o coeficiente de agrupamento do grafo. 
             O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
    def mundo_pequeno(self):
        '''
            retorna True se o grafo é mundo pequeno e False em caso contrário. 
            Para isso esse método não leva em consideração o numero de vértices 
            do grafo, apenas leva em consideração as propriedades de 
            esparsidade, distância média e coeficiente de agrupamento. 
            Note que, por alguma razão misteriosa, não estamos levando em 
            consideração o número de vértices do grafo (V > 1000) e 
            nem sua conexidade. O consumo de tempo desse método deve ser O(1).
        '''
        pass
    
def main():
    g  = Grafo("grafo.txt")
    gX = Grafo("grafoX.txt")      
    gr = Grafo("routes.txt")
    print('Teste __str__')
    print()
    print(g)
    print()
    print(gX)
    print()
    print(gr)
    print()
    mundo_g = Mundo_Pequeno(g)
    mundo_gX = Mundo_Pequeno(gX)
    mundo_gr = Mundo_Pequeno(gr)
    print('Teste grau_medio')
    print()
    print(mundo_g.grau_medio())
    print()
    print(mundo_gX.grau_medio())
    print()
    print(mundo_gr.grau_medio())
    print()
    print('Teste distancia_media')
    print()
    print(mundo_g.distancia_media())
    print()
    print(mundo_gX.distancia_media())
    print()
    print(mundo_gr.distancia_media())
    print()
    print('Teste distancia_mediaX()')
    print()
    print(mundo_g.distancia_mediaX())
    print()
    print(mundo_gX.distancia_mediaX())
    print()
    print(mundo_gr.distancia_mediaX())
    print()
    print('Teste coeficiente_agrupamento_local')
    print()
    print(mundo_g.coeficiente_agrupamento_local("A"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("B"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("C"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("G"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("H"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("G"))
    print()
    print(mundo_g.coeficiente_agrupamento_local("H"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("A2"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("B2"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("C2"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("G2"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("H2"))
    print()
    print(mundo_gX.coeficiente_agrupamento_local("A"))
    print()
    print(mundo_gr.coeficiente_agrupamento_local("JFK"))
    print()
    print(mundo_gr.coeficiente_agrupamento_local("ATL"))
    print()
    print(mundo_gr.coeficiente_agrupamento_local("LAX"))
    print()
    print(mundo_gr.coeficiente_agrupamento_local("LAS"))
    print()
    print(mundo_gr.coeficiente_agrupamento_local("ORD"))
    print()
    print('Teste coeficiente_agrupamento')
    print()
    print(mundo_g.coeficiente_agrupamento())
    print()
    print(mundo_gX.coeficiente_agrupamento())
    print()
    print(mundo_gr.coeficiente_agrupamento())
    print()
    print('Teste mundo_pequeno')
    print()
    print(mundo_g.mundo_pequeno())
    print()
    print(mundo_gX.mundo_pequeno())
    print()
    print(mundo_gr.mundo_pequeno())
    print()
    print('Teste __str__')
    print()
    print(mundo_g)
    print()
    print(mundo_gX)
    print()
    print(mundo_gr)
    
main()

'''
    Teste __str__
    >>> g  = Grafo("grafo.txt")
    >>> gX = Grafo("grafoX.txt")      
    >>> gr = Grafo("routes.txt")
    >>> print(g)
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B

    >>> print(gX)
    A | B, C, G, H
    A2 | B2, C2, G2, H2
    B | A, C, H
    B2 | A2, C2, H2
    C | A, G, B
    C2 | A2, G2, B2
    G | C, A
    G2 | C2, A2
    H | A, B
    H2 | A2, B2
        
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

    >>> mundo_g = Mundo_Pequeno(g)
    >>> mundo_gX = Mundo_Pequeno(gX)
    >>> mundo_gr = Mundo_Pequeno(gr)
    >>> 
    
    Teste grau_medio
    >>> mundo_g.grau_medio()
    2.8
    >>> mundo_gX.grau_medio()
    2.8
    >>> mundo_gr.grau_medio()
    3.2
    >>> 
    Teste distancia_media
    >>> mundo_g.distancia_media()
    1.3
    >>> mundo_gX.distancia_media()
    10
    >>> mundo_gr.distancia_media()
    1.9555555555555555
    
    Teste distancia_mediaX
    >>> mundo_g.distancia_mediaX()
    1.3
    >>> mundo_gX.distancia_mediaX()
    1.3
    >>> mundo_gr.distancia_mediaX()
    1.955555
    
    Teste coeficiente_agrupamento_local
    >>> mundo_g.coeficiente_agrupamento_local("A")
    0.5
    >>> mundo_g.coeficiente_agrupamento_local("B")
    0.6666666666666666
    >>> mundo_g.coeficiente_agrupamento_local("C")
    0.6666666666666666
    >>> mundo_g.coeficiente_agrupamento_local("G")
    1.0
    >>> mundo_g.coeficiente_agrupamento_local("H")
    1.0
    >>> mundo_g.coeficiente_agrupamento_local("G")
    1.0
    >>> mundo_g.coeficiente_agrupamento_local("H")
    1.0
    >>> mundo_gX.coeficiente_agrupamento_local("A2")
    0.5
    >>> mundo_gX.coeficiente_agrupamento_local("B2")
    0.6666666666666666
    >>> mundo_gX.coeficiente_agrupamento_local("C2")
    0.6666666666666666
    >>> mundo_gX.coeficiente_agrupamento_local("G2")
    1.0
    >>> mundo_gX.coeficiente_agrupamento_local("H2")
    1.0
    >>> mundo_gX.coeficiente_agrupamento_local("A")
    0.5
    >>> mundo_gr.coeficiente_agrupamento_local("JFK")
    0.6666666666666666
    >>> mundo_gr.coeficiente_agrupamento_local("ATL")
    0.5
    >>> mundo_gr.coeficiente_agrupamento_local("LAX")
    0.0
    >>> mundo_gr.coeficiente_agrupamento_local("LAS")
    0.0
    >>> mundo_gr.coeficiente_agrupamento_local("ORD")
    0.3333333333333333
    
    Teste coeficiente_agrupamento
    >>> mundo_g.coeficiente_agrupamento()
    0.7666666666666666
    >>> mundo_gX.coeficiente_agrupamento()
    0.7666666666666667
    >>> mundo_gr.coeficiente_agrupamento()
    0.4499999999999999
    >>> 
    
    Teste mundo_pequeno
    >>> mundo_g.mundo_pequeno()
    True
    >>> mundo_gX.mundo_pequeno()
    True
    >>> mundo_gr.mundo_pequeno()
    True
    
    Teste __str__
    >>> print(mundo_g)
    Mundo Pequeno:
    V = 5,  A = 7
    grau médio = 2.800
    distância média = 1.300
    distância médiaX = 1.300
    coeficiente de agrupamento = 0.767
    mundo pequeno: True

    >>> print(mundo_gX)
    Mundo Pequeno:
    V = 10,  A = 14
    grau médio = 2.800
    distância média = 10.000
    distância médiaX = 1.300
    coeficiente de agrupamento = 0.767
    mundo pequeno: True

    >>> print(mundo_gr)
    Mundo Pequeno:
    V = 10,  A = 16
    grau médio = 3.200
    distância média = 1.956
    distância médiaX = 1.956
    coeficiente de agrupamento = 0.450
    mundo pequeno: True
'''
    






