def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            p = int(input("Entre com um valor que sera elemento da posiçao {}x{}: ". format(i+1,j+1)))
            Cobaia.append(p)
        M.append(Cobaia)
    return M

def imprima_matriz(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def Max_matriz(M):
    print("Entrei na funçao Max_matriz")
    Maior = 0
    for i in range(len(M)):
        Max = max(M[i])
        if (Max > Maior):
            Maior = Max
            for j in range(len(M[0])):
                if (Maior == M[i][j]):
                    Coordenada = []
                    The_Best = M[i][j]
                    linha = i
                    coluna = j
                    Coordenada.append(linha)
                    Coordenada.append(coluna)
                    print("Coordenada: ", Coordenada)
    print("O maior elemento {} da posiçao {}x{}". format(The_Best,linha+1,coluna+1))
    
    return Coordenada

def ordena_matriz(M):
    print("Entrei na funçao ordena_matriz")
    i = 1
    while (i <= (len(M)*len(M[0]))):
        posiçao = Max_matriz(M)
        M[posiçao[0]][posiçao[1]] = 0
        i = i + 1

def main():
    A = []
    Matriz_A = monta_matriz(A)
    Picture_A = imprima_matriz(Matriz_A)
    Ordena = ordena_matriz(Matriz_A)
main()
                    
