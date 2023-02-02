def separa(texto,sep):
    saida = []
    repara = texto.split(sep)
    Cobaia = []
    for i in repara:
        if("\n" in i):
            sub_lista = i.split("\n")
            Cobaia.append(sub_lista[0])
            saida.append(Cobaia)
            if(len(sub_lista) <= 2):
                if(len(sub_lista) == 1):
                    break
                else:
                    Cobaia = []
                    Cobaia.append(sub_lista[1])
            elif(len(sub_lista) == 3):
                Morumotto = []
                Morumotto.append(sub_lista[1])
                saida.append(Morumotto)
                Cobaia = []
                Cobaia.append(sub_lista[2])
        else:
            Cobaia.append(i)
    return saida

def soma(lista):
    soma = 0
    for i in lista:
        try:
            soma = soma + float(i)
        except:
            print("Esse elemento nao tem como converter em uma float: ", i)
    return soma

arquivo = input("Entre com um nome do arquivo no formato '.txt':")
with open (arquivo, 'r', encoding = 'utf-8') as arq_entrada:
    conteudo = arq_entrada.read()
print(conteudo)

def main():
    sub_lista = separa(conteudo," ")
    Total = 0
    for i in range(len(sub_lista)):
        summ = soma(sub_lista[i])
        Total = Total + summ
        print("Soma total dos elementos reais que existem na linha {}: {}". format(sub_lista[i],summ))
    print("Soma Total de todos elementos reais existentes no texto: ", Total)
main()
