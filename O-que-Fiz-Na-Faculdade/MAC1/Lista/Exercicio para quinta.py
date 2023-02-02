# Exercicio para quinta: Dado n valores float de um lista, me dê o seguimento de todos os tamanhos maximo de soma maxima
def pertence(item,lista):
    for i in range(len(lista)):
        if (lista[i] == item):
            return True
    return False

def somatorio(inicio,fim,lista):
    #print("Entramos na somatoria")
    soma = 0
    for i in range(inicio,fim):
        #print("Mostre - o range: ", range(inicio,fim))
        #print("indices iterados: ", i)
        soma = soma + lista[i]
        #print("Revele - me a lista: ", lista[i])
        #print("Revele - me a soma: ", soma)
        #print("-----------------------------------------")
    return soma

def main():
    x = [5,-2,-2,-7,3,14,10,-3,9,-6,4,1]
    max_inicio = 0
    max_fim = 0
    max_soma = -float('inf')
    termos = len(x)
    for inicio in range(len(x)):
        #print("Mostre-me os indices iterados do inicio: ", inicio)
        #print("-----------------------------------------")
        for fim in range(inicio + 1,len(x)+1): # o 1 colocado no len(x) possibilita para contar o ultimo termo da lista
            #print("Mostre-me o range que sera considerado: ", range(inicio + 1,len(x)))
            #print("Mostre-me os indices iterados do fim: ", fim)
            soma = somatorio(inicio,fim,x)
            #print("Valor da soma: ", soma)
            #print("-----------------------------------------")
            if (soma > max_soma):
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
                #print("Valor max_soma: ", max_soma)
                #print("Valor max_inicio: ", max_inicio)
                #print("Valor max_fim: ", max_fim)
                print("Valor maximo da soma = {}\nDo seguimento - lista = {}". format(max_soma,x[max_inicio:max_fim]))
                print("-----------------------------------------")
    
main()
          
