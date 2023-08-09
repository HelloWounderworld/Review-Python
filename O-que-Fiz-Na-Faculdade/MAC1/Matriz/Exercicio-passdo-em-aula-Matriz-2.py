def max_lista(v):
    maximo = v[0]
    for i in range(1,len(v)):
        if (v[i] > maximo):
            maximo = v[i]
    return maximo

def Max_matriz(A):
    
    for i in range(len(A)):
        Maior_linha = max_lista(A[i])
        print("Maior elemeto dessa lista {} sera: {}". format(A[i],Maior_linha))
    for j in range(len(A[0])):
        coluna = []
        for i in range(len(A)):
            coluna.append(A[i][j])
        Maior_coluna = max_lista(coluna)
        print("Maior elemento dessa coluna {} sera: {}". format(coluna,Maior_coluna))

def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            elemento = float(input("Entre com um elemento que sera da posiçao {}x{}: ". format(i+1,j+1)))
            Cobaia.append(elemento)
        M.append(Cobaia)
    return M

def imprima_matriz(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def main():
    A = []
    Matriz_A = monta_matriz(A)
    Picture_A = imprima_matriz(Matriz_A)
    Avalia = Max_matriz(Matriz_A)
main()
