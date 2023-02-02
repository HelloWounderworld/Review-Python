#str e uma forma de lista de algarismos, mas nao posso deletar com o comando "del".
#Metodos que operam em strings: Considerando x uma string
#x. format()
#x. upper() - deixa todas as letras em maiuscula
#x. lower() - deixa todas as letras que estao em maiusculo e muda para minusculo
#x. title() - Deixa somente os primeros algarismos em maiusculo que nem um titulo
#x. split(",") - Capta todas as virgulas de uma frase e cria uma lista considerando como elemento cada frase e/ou palavras como um elemento. Essa e uma forma de cnseguir criar uma lista a partir de strings
# split(",") no lugar da "," testa com alguma outra string.
# A priori uma string e imutavel.

def criptografa(texto,chave):
    print("Entrei na funçao critografa")
    resultado = ""
    for char in texto:
        print("Moste-me o caractere sendo iterado: ", char)
        print("Moste-me o valor inteiro correspondido pelo caractere: ", ord(char))
        codigo = ord(char) + chave #comando ord() fornece um valor inteiro que seria o codigo usado para codificar um simbolo, comando, string,... qualquer do python
        # Caso queira Descriptografar, poderia ter colocado o sinal "-" em ord(char) + chave
        print("Mostre-me o caractere do codigo usado: ", chr(codigo))
        resultado = resultado + chr(codigo) #chr(valor inteiro) fornece um simbolo dentro da UNICODE
    print()
    return resultado

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

#def soma_lista(texto,sep): #Isso levando em consideraçao que cada elemento da lista pode ser convertido em um float
    #soma = 0
    #lista = separa(texto,spe)
    #for valor in lista:
        #soma = soma + float(valor)
    #return soma

def soma_lista(texto,sep): # poderemos usar o comando "try" para conseguir verificar caso haja alguma string que nao tem como converter em algum float
    print("Entrei na funçao soma_lista")
    soma = 0
    lista = separa(texto,spe)
    print("Mostre-me a lista criada pela funçao separa: ", lista)
    for valor in lista:
        try: #O comando "try" processa algum comando que e colocado dentro dele
            soma = soma + float(valor)
            print("Mostre-me o valor que esta sendo somado: ", float(valor))
        except: # comando "except", uma consequencia do try, caso aconteça algum erro dentro do comando processado, simplesmete ignora isso e vai para a proxima
            print("{} nao e conversivel para float". format(valor))
    print()
    return soma

with open(C:\Downloads\'nome'.txt, r) as arq:
    #print(arq.read())
    for linha in arq: # o "arq" aqui pode ser qualquer uma linha que pode ser chamado por fora.
        soma = soma_lista(linha,",")
        print(soma)

def main(): #crie uma string e depois linque com as funçoes montadas para verificar como e feito
          

main()
        
