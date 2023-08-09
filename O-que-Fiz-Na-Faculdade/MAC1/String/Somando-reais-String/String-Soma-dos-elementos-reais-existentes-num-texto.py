def separa(texto,sep):
    saida = texto.split(sep)
    return saida

def soma(lista):
    soma = 0
    for i in lista:
        try:
            soma = soma + float(i)
        except:
            print("{} nao e conversivel para float". format(i))
    return soma

def main():
    arquivo = input("Entre com um nome do arquivo no formato '.txt':")
    with open (arquivo, 'r', ecoding = 'utf-8') as arq_entrada:
        conteudo = arq_entrada.read()
    print(conteudo)

    Dami = []
    for linha in conteudo:
        sub_lista = separa(linha," ")
        Dami.append(sub_lista)

    Total = 0
    for i in range(len(Dami)):
        summ = soma(Dami[i])
        Total = Total + summ
        print("Soma total dos elementos reais que existem na linha {}: {}". format(Dami[i],summ))
    print("Soma Total de todos elementos reais existentes no texto: ", Total)
main()
