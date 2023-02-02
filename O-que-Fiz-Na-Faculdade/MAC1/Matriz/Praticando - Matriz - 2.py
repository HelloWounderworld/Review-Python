def monta_matriz(linha,coluna,M):
    for i in range(linha):
        Cobaia = []
        for j in range(coluna):
            p = float(input("Entre com um valor: "))
            Cobaia.append(p)
        M.append(Cobaia)
    return M

def visualiza(M):
    print("Matriz {}x{}". format(len(M),len(M[0])))
    for i in M:
        for j in i:
            print("{}". format(j). rjust(5), end = "")
        print()

def conta_nulos(sublista):
    soma = 0
    for i in sublista:
        soma = soma + i
    return soma

def coluna_matriz(M):
    Transposta = []
    for j in range(len(M[0])):
        Dami = []
        for i in range(len(M)):
            elemento = M[i][j]
            Dami.append(elemento)
        Transposta.append(Dami)
    return Transposta

def main():
    n = int(input("Quantas linhas : "))
    m = int(input("Quantas colunas : "))
    i = 1
    j = 1
    lines = 0
    coluns = 0
    Matriz = []
    Monta = monta_matriz(n,m,Matriz)
    Picture = visualiza(Monta)
    
    for linha in Monta:
        linhas_nulas = conta_nulos(linha)
        if (linhas_nulas == 0):
            lines = lines + 1

    Coluna_Matriz = coluna_matriz(Monta)

    for coluna in Coluna_Matriz:
        colunas_nulas = conta_nulos(coluna)
        if (colunas_nulas == 0):
            coluns = coluns + 1
        

    print("Nº de linhas nulas: ",lines)
    print("Nº de colunas nulas: ", coluns)
main()
