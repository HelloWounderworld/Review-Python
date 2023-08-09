def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            p = int(input("Entre com um valor inteiro que sera o elemento da posiçao {}x{}: ". format(i+1,j+1)))
            Cobaia.append(p)
        M.append(Cobaia)
        print("Matriz sendo construida: ", M)
    return M

def imprima_matriz(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def Max_matriz(M):
    Maior = 0
    for i in range(len(M)):
        Max = max(M[i])
        if(Max > Maior):
            Maior = Max
            for j in range(len(M[0])):
                if(Maior == M[i][j]):
                    The_Best = M[i][j]
                    linha = i
                    coluna = j
                    sublista = M[i]
    return print("Maior elemento {} da posiçao {}x{}". format(The_Best,linha,coluna))

def main():
    A = []
    Matriz_A = monta_matriz(A)
    Picture_A = imprima_matriz(Matriz_A)
    Maior_elemento = Max_matriz(Matriz_A)
main()
