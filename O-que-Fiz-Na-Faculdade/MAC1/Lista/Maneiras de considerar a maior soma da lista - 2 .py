import math
def seq_max(lista):
    max_soma = -math.inf
    max_inicio = 0
    max_fim = 0
    for inicio in range(len(x)):
        for fim in range(inicio + 1,len(x)):
            soma = somatorio(inicio,fim,x)
            if soma > max_soma:
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
    return max_soma, max_inicio, max_fim

def main():
    x = [5,-2,-2,-7,3,14,10,-3,9,-6,4,1]
    u,v,w = seq_max(x)
    print(u,x[v:w])

main()
