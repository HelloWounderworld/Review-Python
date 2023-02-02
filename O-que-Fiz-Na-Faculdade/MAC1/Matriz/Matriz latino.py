#1) Uma matriz A, de dimensões n x n, é chamado de quadrado latino de ordem n, se em cada linha e cada coluna aparecem todos os inteiros 1, 2, 3, ..., n.
#Ou seja, cada coluna ou linha é uma permutação dos inteiros 1, 2, 3, ..., n. Escreva as seguintes funções em Python:

#a) estaNaLista(), que recebe um inteiro x e uma lista de inteiros e verifica se x ocorre na lista;
#b) temTodos(), que, usando a função acima, recebe como parâmetro uma lista a com n inteiros e verifica se em a ocorrem todos os inteiros de 1 ate n;
#c) eLatino(), que, utilizando a função acima, verifica se uma dada matriz A, n x n, é um quadrado latino de ordem n.

def repetiçao(M):
    linha = len(M)
    coluna = len(M[0])
    Matriz_coluna = []
    for i in range(linha):
        for j in range(coluna):
            Comparo = M[i][j]
            if (Comparo == M[i][for j in range(coluna+1)]):
                return print("Nao e matriz Latino")

            elif (M[i] == M[for i in range(linha+1)]):
                return print("Nao e matriz Latino")

    for j in range(coluna):
        Matriz_cobaia = []
        for i in range(linha):
            Matriz_cobaia.append(M[i][j])
        Matriz_coluna.append(Matriz_cobaia)

    for j in range(coluna):
        for i in range(linha):
            Compara_coluna = Matriz_coluna[j][i]
            if (Compara_coluna == Matriz_coluna[j][for i in range(linha+1)]):
                return print("Nao e matriz Latino")
            elif (Matriz_coluna[j] == Matriz_coluna[for k in range(coluna+1)]):
                return print("Nao e matriz Latino")
    
    return print("Bom, pelo menos, nao achei nenhum elemento repetido")

def quadrado(M):
    if len(M) == len(M[0]) and print("E uma matriz quadrada")
        return True

def elementos_latinos(M):
    linha = len(M)
    coluna = len(M[0])
    for i in range(linha):
        for j in range(coluna):
            if (M[i][j] <= 0 or M[i][j] > len(M)):
                return print("Nao e matriz Latino")

            elif ((M[i][j] - int(M[i][j])) != 0):
                return print("Nao e matriz Latino")
    return print("E matriz Latino")

def Matriz(linha,coluna):
    M = [[]]*linha
    for i in range(linha):
        for j in range(coluna):
            valor = float(input("Entre com um valor que sera o elemento da Matriz {}x{}: ". format(i,j)))
            M[i][j] = valor
    return M

def main():
    linha = int(input("Qual sera o numero de linhas: "))
    coluna = int(input("Qual sera o numero de colunas: "))
    Matriz = Matriz(linha,coluna)
    print("Avalia se existe elementos repetidos em cada linha e coluna: ", repetiçao(Matriz))
    print("Avalia se e uma matriz quadrada: ", quadrado(Matriz))
    if (quadrado(Matriz) == True):
        print("Avalia se e uma matriz quadrada latina: ", elementos_latinos(Matriz))

    else:
        print("Nao e matriz quadrada")
main()
        
                
