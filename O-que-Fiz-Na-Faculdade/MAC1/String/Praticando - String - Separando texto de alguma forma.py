def monta_lista(lista):
    n = ""
    while(n != "Fim"):
        n = str(input("Entre com alguma frase ou palavra: "))
        if (n == "Fim"):
            break
        else:
            lista.append(n)
            print("lista sendo construido: ", lista)
    return lista

'''def separa(texto,sep):
    conteudo = texto.split(sep)
    return conteudo'''

def separa(texto,sep):
    saida = []
    inicio = 0
    fim = 0
    while(fim < len(texto)):
        if(texto[fim] == sep):
            saida.append(texto[inicio:fim])
            fim = fim + 1
            inicio = fim
        else:
            fim = fim + 1
    saida.append(texto[inicio:])
    return saida
        
    

def main():
    Lista = []
    Montar = monta_lista(Lista)
    for linha in Montar:
        Separa = separa(linha,'a')
        print(Separa)
main()
