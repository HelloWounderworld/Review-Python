import time

def rotas(grid):
    L = [1] * grid
    for i in range(grid):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[-1]


n = 50
for i in range(15):
    n *= 2
    init = time.time()
    r = rotas(n)
    tempo = time.time() - init
    print("N: {} --> tempo: {:.5f} s".format(n, tempo))