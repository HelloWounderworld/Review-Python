'''
   MAC0122 Princípios de Desenvolvomento de Algoritmos

   Cliente para a classe Caminhos_Minimos
'''
# representação de grafos
from grafo import Grafo

# representação de caminhos mínimos
from caminhos_minimos import Caminhos_Minimos

#-------------------------------------------------------------------
#  Cliente
#  
# CONSTANTES
ARQUIVO = 'grafo.txt'

#------------------------------------------------------------
def main():
    ''' (None) -> None
    Essa função main está aqui para testar a classe Caminhos_Minimos.
    Você pode alterá-la e incluir os seus próprios testes.
    '''
    g = Grafo( ARQUIVO )
    print(g)

    # crie objetos Caminhos_Minimos
    caminhos_A = Caminhos_Minimos(g, "A")
    caminhos_B = Caminhos_Minimos(g, "B")
    caminhos_C = Caminhos_Minimos(g, "C")
    caminhos_G = Caminhos_Minimos(g, "G")    
    caminhos_H = Caminhos_Minimos(g, "H")

    # representação dos caminhos
    print(caminhos_A)
    print(caminhos_B)
    print(caminhos_C)
    print(caminhos_G)
    print(caminhos_H)
    
    # distâncias 
    print("distância de 'A' a 'B':", caminhos_A.distancia("B"))
    print("distância de 'B' a 'A':", caminhos_B.distancia("A"))
    print("distância de 'H' a 'G':", caminhos_H.distancia("G"))
    print("distância de 'G' a 'H':", caminhos_G.distancia("H"))
    print("distância de 'C' a 'H':", caminhos_C.distancia("H"))

    # anterior 
    print("vertice anterior a 'B' nos caminhos mínimos com origem em 'A':", caminhos_A.anterior("B"))
    print("vertice anterior a 'A' nos caminhos mínimos com origem em 'A':", caminhos_A.anterior("A"))
    print("vertice anterior a 'G' nos caminhos mínimos com origem em 'H':", caminhos_H.anterior("G"))
    print("vertice anterior a 'A' nos caminhos mínimos com origem em 'H':", caminhos_H.anterior("G"))
    print("vertice anterior a 'H' nos caminhos mínimos com origem em 'H':", caminhos_H.anterior("G"))

    # caminho mínimo
    print("caminho mínimo de 'A' a 'B'", caminhos_A.caminho("B"))
    print("caminho mínimo de 'B' a 'A'", caminhos_B.caminho("A"))
    print("caminho mínimo de 'B' a 'G'", caminhos_B.caminho("G"))

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
    
