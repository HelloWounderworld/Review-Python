def somatorio(inicio,fim,lista):
    print("Entramos na somatoria")
    soma = 0
    for i in range(inicio,fim):
        print("Mostre - o range: ", range(inicio,fim))
        print("indices iterados: ", i)
        soma = soma + lista[i]
        print("Revele - me a soma: ", soma)
    return soma

def main():
    x = [-2,2,-2,2]
    max_soma = -float('inf')
    max_inicio = 0
    max_fim = 0
    max_len = 0
    for inicio in range(len(x)):
        for fim in range(inicio + 1,len(x)+1):
            print("Mostre-me o seguimento considerado do range: ", range(inicio + 1,len(x) +1))
            soma = somatorio(inicio,fim,x)
            print("Mostre-me: ", inicio, fim, x[inicio:fim])
            if soma > max_soma:
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
                max_len = fim - inicio

            elif(soma == max_soma and fim - inicio > max_len):
                print("Mostre-me o valor da soma: ", soma)
                print("Mostre-me o valor do seguimento: ", fim - inicio)
                max_inicio = inicio
                max_fim = fim
                max_len = fim - inicio
    print("soma = {}, lista = {}". format(max_soma,x[max_inicio:max_fim]))
main()
