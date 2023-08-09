#1) Uma matriz A, de dimensões n x n, é chamado de quadrado latino de ordem n, se em cada linha e cada coluna aparecem todos os inteiros 1, 2, 3, ..., n.
#Ou seja, cada coluna ou linha é uma permutação dos inteiros 1, 2, 3, ..., n. Escreva as seguintes funções em Python:

#a) estaNaLista(), que recebe um inteiro x e uma lista de inteiros e verifica se x ocorre na lista;
#b) temTodos(), que, usando a função acima, recebe como parâmetro uma lista a com n inteiros e verifica se em a ocorrem todos os inteiros de 1 ate n;
#c) eLatino(), que, utilizando a função acima, verifica se uma dada matriz A, n x n, é um quadrado latino de ordem n.

def repetiçao(M):
    print("Entrei na funçao repetiçao")
    linha = len(M)
    coluna = len(M[0])
    Matriz_coluna = []
    m = 1
    for i in range(linha):
        for j in range(coluna):
            Comparo = M[i][j]
            print("Mostre-me o elemento que sera comparado com outros elementos da Matriz: ", Comparo)
            for k in M[i][j+1:]:
                print("Mostre-me o elemento que sera comparado: ", k)
                if (Comparo == k):
                    print("Nao e matriz Latino\n")
                    return False
                else:
                    print("Elementos repetidos nao encontrados na linha\n")
                
    for i in range(linha):            
        for l in M[i+1:]:
            print("A sublista", l," que sera comparado com a sublista:", M[i])
            if (M[i] == l):
                print("Nao e matriz Latino\n")
                return False
            else:
                print("Linhas repetidas nao encontrada\n")

    for j in range(coluna):
        Matriz_cobaia = []
        for i in range(linha):
            Matriz_cobaia.append(M[i][j])
            print("Mostre-me a Matriz_cobaia sendo construido: ", Matriz_cobaia)
        Matriz_coluna.append(Matriz_cobaia)
        print("Mostre-me a Matriz_coluna construida: ", Matriz_coluna)
        
    print("Mostre-me a Matriz_coluna = Transpota:")
    for i in Matriz_coluna:
        for j in i:
            print("{}". format(j). rjust(5), end ="")
        print()
        
    for j in range(coluna):
        for i in range(linha):
            Compara_coluna = Matriz_coluna[j][i]
            print("Mostre-me o elemento da Matriz_coluna que sera comparada com outros elementos da coluna: ", Compara_coluna)
            for k in Matriz_coluna[j][i+1:]:
                print("Mostre-me os elementos que foi selecionado", k," para comparar com o elemento : ", Matriz_coluna[j][i])
                if (Compara_coluna == k):
                    print("Nao e matriz Latino\n")
                    return False
                else:
                    print("Elementos repetidos nao encontrado na coluna\n")
    for j in range(coluna):
        for l in Matriz_coluna[j+1:]:
            print("A sublista da Matriz_coluna", l," que sera comparado com a sublista da Matriz_coluna: ", Matriz_coluna[j])
            if (Matriz_coluna[j] == l):
                print("Nao e matriz Latino\n")
                return False
            else:
                print("Colunas repetidas nao encontrada\n")
    print("Bom, pelo menos, nao achei nenhum elemento repetido\n")
    return True

def quadrado(M):
    print("Entrei na funçao quadrado")
    if len(M) == len(M[0]):
        return True
    else:
        return print("Nao e uma matriz quadrada\n")

def elementos_latinos(M):
    print("Entrei na funçao elementos_latinos")
    linha = len(M)
    coluna = len(M[0])
    for i in range(linha):
        for j in range(coluna):
            print("Mostre-me o elemento da matriz que sera comparado: ", M[i][j])
            if (M[i][j] <= 0 or M[i][j] > len(M)):
                return print("Nao e matriz Latino\n")

            elif ((M[i][j] - int(M[i][j])) != 0):
                return print("Nao e matriz Latino\n")
    return print("E matriz Latino\n")

def Matriz(linha,coluna):
    print("Entrei na funçao Matriz")
    M = []
    for i in range(linha):
        Dami = []
        for j in range(coluna):
            valor = float(input("Entre com um valor que sera o elemento da Matriz {}x{}: ". format(i+1,j+1)))
            Dami.append(valor)
            print("Mostre-me a Matriz Dami sendo construida: ", Dami)
        M.append(Dami)
        print("Mostre-me a Matriz que foi construida: ", M)
        print()

    print("Matriz construida:")
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()
    print("E ai cara, acha mesmo que essa matriz vai ser uma quadrada latina ????")
    return M

def main():
    linha = int(input("Qual sera o numero de linhas: "))
    coluna = int(input("Qual sera o numero de colunas: "))
    if (linha != coluna):
        return print("Nao e sera um quadrado latino")
    else:
        print("Sera uma matriz quadrada")
        
    Matriz_latino = Matriz(linha,coluna)
    if (quadrado(Matriz_latino) == True):
        print("Avalia se existe elementos repetidos em cada linha e coluna: ", repetiçao(Matriz_latino))
        if(repetiçao(Matriz_latino) == False):
            return print("Nao e matriz Latino")
        else:
            print(elementos_latinos(Matriz_latino))

    else:
        return print("Nao e matriz quadrada")
main()
        
                
