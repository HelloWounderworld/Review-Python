def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            p = float(input("Entre com um valor: "))
            Cobaia.append(p)
        M.append(Cobaia)
        print("Mostre-me a Matriz sendo construida: ", M)
    return M

def imprima_matriz(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def Transposta(M):
    transposta = []
    for j in range(len(M[0])):
        Dami = []
        for i in range(len(M)):
            Dami.append(M[i][j])
        transposta.append(Dami)
    return transposta

def multiplica(A,D):
    C = []
    B = Transposta(D)
    for i in range(len(A)):
        Sub_C = []
        for l in range(len(B)):
            soma = 0
            for j in range(len(B[0])):
                soma = soma + A[i][j]*B[l][j]
            Sub_C.append(soma)
        C.append(Sub_C)
    return C

def main():
    A = []
    B = []
    Matriz_A = monta_matriz(A)
    Matriz_B = monta_matriz(B)
    Picture_A = imprima_matriz(Matriz_A)
    Picture_B = imprima_matriz(Matriz_B)
    if(len(Matriz_A[0]) == len(Matriz_B)):
        Matriz_C = multiplica(Matriz_A,Matriz_B)
        return imprima_matriz(Matriz_C)
    else:
        return print("Essas duas Matrizes {} e {}, não tem como ser multiplicada". format(Matriz_A,Matriz_B))
main()
                
