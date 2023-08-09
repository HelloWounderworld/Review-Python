def separa(texto,sep):
    saida = []
    inicio = 0
    fim = 0
    while(fim < len(texto)):
        posiçao = texto[fim]
        if(posiçao == sep):
            saida.append(texto[inicio:fim])
            fim = fim + 1
            inicio = fim
        else:
            fim = fim + 1
    saida.append(texto[inicio:])
    return saida

def maior_string(lista):
    maior = 0
    for palavra in lista:
        if(len(palavra) > maior):
            maior = len(palavra)
            word = palavra
    return word

def monta_lista(lista):
    n = ""
    while(n != "Fim"):
        n = str(input("Entre com uma frase ou palavra: "))
        if(n == "Fim"):
            break
        lista.append(n)
    return lista

def main():
    lista = []
    lista_pronta = monta_lista(lista)
    Dami = []
    for linha in lista_pronta:
        sub_string = separa(linha,",")
        Dami.append(sub_string)
    for i in range(len(Dami)):
        maior_word = maior_string(Dami[i])
        print("Maior string dessa sublista {} e: {}". format(Dami[i],maior_word))
main()
