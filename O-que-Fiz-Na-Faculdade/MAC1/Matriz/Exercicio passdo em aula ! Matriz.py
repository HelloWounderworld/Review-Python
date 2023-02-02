#a-) Faça uma funçao max que recebe um parametro v, uma lista com n (n=10) elementos reais e devolve o maior elemento:
#b-) Deda uma matrz quadrada An, faça um programa que leia A e que imprime maiores elementos de cada linha e coluna

def monta_matriz(M):
    n = int(input("Quantas linhas: "))
    m = int(input("Quantas colunas: "))
    for i in range(n):
        Cobaia = []
        for j in range(m):
            p = float(input("Entre com algum elemento: "))
            Cobaia.append(p)
        M.Cobaia
    return M

def maxx(v):
    maximo = v[0]
    i = 1
    while (i < len(v)):
        if v[i] > maximo:
            maximo = v[i]
        i = i + 1
    return maximo
def Max(v):
    maximo = v[0]
    for i in range(1,len(v)):
        if v[i]>maximo:
            maximo = v[i]
    return maximo

def main():
    n = 10
    A = []
    for i in range(n):
        A.append([0]*n)
        for j in range(j):
            A[i][j] = float(input("Entre com o elemento {}x{}: ". format(i,j)))
    print("Testando funçao maxx")
    for linha in A:
        print(maxx(linha))

    for j in range(n):
        Coluna = []
        for i in range(n):
            Coluna.append(A[i][j])
        print(maxx(Coluna))

    print("Testando funçao Max")
    for linha in A:
        print(Max(linha))

    for j in range(n):
        Cobaia = []
        for i in range(n):
            Cobaia.append(A[i][j])
        print(Max(Cobaia))
main()

#Testa Essa Porra !!!
        
    
