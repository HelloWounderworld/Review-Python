def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            p = float(input("Entre com um valor que sera o elemeno da posiçao {}x{}: ". format(i+1,j+1)))
            Cobaia.append(p)
        M.append(Cobaia)
    return M

def imprima_matriz(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")

        print()

def conta_nulos(M):
    linha = 0
    for i in M:
        soma = 0
        for j in i:
            soma = soma + j
        if (soma == 0):
            linha = linha + 1

    coluna = 0 
    for j in range(len(M[0])):
        summ = 0
        for i in range(len(M)):
            summ = summ + M[i][j]
        if (summ == 0):
            coluna = coluna +1

    return print("Nº de linhas nulas: {}\nNº de colunas nulas: {}". format(linha,coluna))

def main():
    A = []
    Matriz_A = monta_matriz(A)
    Picture_A = imprima_matriz(Matriz_A)
    Nulos = conta_nulos(Matriz_A)
main()
