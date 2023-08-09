def separa(texto,sep):
    separa = texto.split(",")
    return separa

def maior_palavra(lista):
    Comprimentos = []
    for i in lista:
        Comprimentos.append(len(i))
    Maior = max(Comprimentos)
    for j in lista:
        if (len(j) == Maior):
            print("O maior comprimento dentre as listas de string: ", j)

def main():
    frase = str(input("Entre com uma frase: "))
    print(separa(frase,"," ))
    print(maior_palavra(separa(frase, ",")))
main()
