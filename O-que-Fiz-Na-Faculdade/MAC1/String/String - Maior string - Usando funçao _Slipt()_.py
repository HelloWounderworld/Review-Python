def separa(texto,sep):
    saida = texto.split(sep)
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
    Lista = []
    Lista_pronta = monta_lista(Lista)
    Dami = []
    for linha in Lista_pronta:
        sub_string = separa(linha,",")
        Dami.append(sub_string)
    for i in range(len(Dami)):
        maior_word = maior_string(Dami[i])
        print("A maior string dessa sub_lista {} e: {}". format(Dami[i],maior_word))
main()
