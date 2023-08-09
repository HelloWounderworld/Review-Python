#1-) Os elementos aij de uma matriz A nxn representam os custos de transporte de uma cidade i para cidade j
#Dado um itinerario com k cidades, k > 1, calcular custo total para este itinerario.

def custo(A,v):
    soma  = 0
    for origem in range(len(v) - 1):
        destino = origem + 1
        soma = soma + A[v[origem]][v[destino]]
    return soma

def main():
    A = [[4,1,2,3],[5,2,1,400],[2,1,3,8],[7,1,2,5]]
    v = [0,3,1,3,3,2,1,0]
    print("custo total = {}". format(custo(A,v)))
main()
