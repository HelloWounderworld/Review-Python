def monta_matriz(linha,coluna,M):
    for i in range(linha):
        Cobaia = []
        for j in range(coluna):
            p = float(input("Entre com um valor: "))
            Cobaia.append(p)
        M.append(Cobaia)
    return M

def vizualiza(M):
    print("Matriz {}x{}: ". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def conta_nulos(M):
    soma = 0
    summ = 0
    
    for i in range(len(M)):
        for j in range(len(M[0])):
            soma = soma + M[i][j]

    for j in range(len(M[0])):
        for i in range(len(M)):
            summ = summ + M[i][j]

def main():
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    Matriz = []
    B = monta_matriz(n,m,Matriz)
    C = vizualiza(B)
    D = conta_nulos(B)
    
main()
