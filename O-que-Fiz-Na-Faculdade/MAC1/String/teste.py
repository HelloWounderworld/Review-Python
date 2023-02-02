def separa(texto,sep): #assumindo que o separador aqui seja ","
    print("Entrei na funçao separa")
    saida = []
    inicio = fim = 0
    while (fim < len(texto)):
        if (texto[fim] == sep):
            saida.append(texto[inicio:fim])
            print("Mostre-me a lista de string criado pela lista 'saida': ", saida)
            inicio = fim = fim + 1 # teste inicio = fim += 1

        else:
            fim = fim + 1

    saida.append(texto[inicio:])
    print("Mostre-me a lista criado pela lista 'saida': ", saida)
    print()
    return saida

def monta_lista(lista):
    n = ""
    while(n != "Fim"):
        n = str(input("Entre com uma frase ou palavra: "))
        if (n == "Fim"):
            break
        lista.append(n)
    return lista

def main():
    Lista =[]
    Montar = monta_lista(Lista)
    for texto in Montar:
        avalia = separa(texto,"a")
main()
