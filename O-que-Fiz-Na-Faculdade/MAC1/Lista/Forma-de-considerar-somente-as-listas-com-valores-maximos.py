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
    lista = []
    for inicio in range(len(x)):
        for fim in range(inicio + 1,len(x)+1):
            print("Mostre-me o seguimento considerado do range: ", range(inicio + 1,len(x) +1))
            soma = somatorio(inicio,fim,x)
            #print("Mostre-me: ", incio, fim, x[inicio,fim])
            if soma > max_soma:
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
                lista = [[inicio,fim]]
                print("Revele-me a nova lista: ", lista)

            elif(soma == max_soma):
                max_soma = soma
                max_inicio = inicio
                max_fim = fim
                lista.append([inicio,fim])

    for elemento in lista:
        print(x[elemento[0]:elemento[1]])

main()
                
                
