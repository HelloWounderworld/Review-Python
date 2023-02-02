import time

def rotas(grid):
    L = [1] * grid
    for i in range(grid):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[-1]


n = int(input("Digite o tamanho do lado do grid:"))
init = time.time()
r = rotas(n)
tempo = time.time() - init
print("Encontrei {} caminhos em {:5f} segundos".format(r, tempo))