def monta_matriz_quadrada(M):
    n = int(input("Quantas linha x coluna: "))
    for i in range(n):
        Cobaia = []
        for j in range(n):
            p = float(input("Entre com um valor que sera o elemento da posiçao {}x{}: ". format(i+1,j+1)))
            Cobaia.append(p)
        M.append(Cobaia)
    return M

def visualiza(M):
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

def simetrica(M):
    Transp = Transposta(M)
    if (Transp == M):
        return True and print("E simetrica")
    else:
        return False and print("Nao e simetrica")

def main():
    A = []
    Matriz_A = monta_matriz_quadrada(A)
    Picture = visualiza(Matriz_A)
    Avalia = simetrica(Matriz_A)
main()
            
