import math
def pertence(item,lista):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

def somatorio(inicio,fim,lista):
    soma = 0
    for i in range(inicio,fim):
        soma = soma + lista[i]
    return soma

def main():
    x = [5,-2,-2,-7,3,14,10,-3,9,-6,4,1]
    max_soma = -math.inf
    max_inicio = 0
    max_fim = 0
    for inicio in range(len(x)):
        for fim in range(inicio + 1,len(x)+1):
            soma = somatorio(inicio,fim,x)
            if soma > max_soma:
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
    print("soma = {}, lista = {}". format(max_soma,x[max_inicio:max_fim]))
main()
