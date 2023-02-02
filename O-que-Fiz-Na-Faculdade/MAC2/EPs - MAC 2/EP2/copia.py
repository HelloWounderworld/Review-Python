def imagem(n,m,p):
    x = str()
    for i in range(n):
        y = str()
        for j in range(m):
            if j == m-1:
                y = y + str(p)
            else:
                y = y + str(p)+','+' '
        x = x + y+'\n'
    return x

def imagem2(nlins,ncolns,valor):
    x = []
    for i in range(nlins):
        y = []
        for j in range(ncolns):
            y.append(valor)
        x.append(y)
    return x

def copia(n,m,p,q):
    
    
