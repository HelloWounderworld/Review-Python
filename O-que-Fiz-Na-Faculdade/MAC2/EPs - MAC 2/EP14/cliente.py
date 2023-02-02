'''
   MAC0122 Princípios de Desenvolvimento de Algoritmos

   Cliente para o EP14: Mundo Pequeno

'''
from Grafos import Grafo
#####################################################################
# CONSTANTES
ARQUIVO = open('grafo.txt','r',encoding = 'utf-8')

#------------------------------------------------------------
def main():
    ''' (None) -> None
    Essa função main está aqui para testar a classe Grafo.
    Você pode alterá-la e incluir os seus próprios testes.
    Você deve entregar a função main() nesse mesmo arquivo.
    '''
    v, w, x = 'C', 'H', 'X'
    g = Grafo( ARQUIVO )
    print(g)

    print("V(): %d"%g.V())
    print("A(): %d"%g.A())
    print("Vertices: ", g.vertices())

    print("Adjacentes de %s: "%v, g.adjacentes(v))
    print("Grau de %s: "%v, g.grau(v))
    print("Tem vertice %s: "%v, g.tem_vertice(v))
    print("Tem vertice %s: "%w, g.tem_vertice(w))
    print("Tem vertice %s: "%x, g.tem_vertice(x))
    print("Tem aresta %s-%s:"%(v, w), g.tem_aresta(v,w) )
    print("Tem aresta %s-%s:"%(x, w), g.tem_aresta(x,w) )

    print("\nInserindo aresta H-x")
    g.insira_aresta('X', 'H')
    print(g)
    print("V(): %d"%g.V())
    print("A(): %d"%g.A())
    print("Vertices: ", g.vertices())

    print("Adjacentes de %s: "%v, g.adjacentes(v))
    print("Grau de %s: "%v, g.grau(v))
    print("Tem vertice %s: "%v, g.tem_vertice(v))
    print("Tem vertice %s: "%w, g.tem_vertice(w))
    print("Tem vertice %s: "%x, g.tem_vertice(x))
    print("Tem aresta %s-%s:"%(v, w), g.tem_aresta(v,w) )
    print("Tem aresta %s-%s:"%(x, w), g.tem_aresta(x,w) )
main()
'''
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B

    V(): 5
    A(): 7
    Vertices:  ['A', 'B', 'C', 'G', 'H']
    Adjacentes de C:  ['A', 'B', 'G']
    Grau de C:  3
    Tem vertice C:  True
    Tem vertice H:  True
    Tem vertice X:  False
    Tem aresta C-H: False
    Tem aresta X-H: False

    Inserindo aresta H-x
    A | B, C, G, H
    B | A, C, H
    C | A, B, G
    G | A, C
    H | A, B, X
    X | H

    V(): 6
    A(): 8
    Vertices:  ['A', 'B', 'C', 'G', 'H', 'X']
    Adjacentes de C:  ['A', 'B', 'G']
    Grau de C:  3
    Tem vertice C:  True
    Tem vertice H:  True
    Tem vertice X:  True
    Tem aresta C-H: False
    Tem aresta X-H: True
'''


