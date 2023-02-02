def imagem(n,m,p):
    lista = imagem2(n,m,p)
    x = str()
    for i in range(len(lista)):
        y = str()
        for j in range(len(lista[i])):
            if j == m-1:
                y = y + str(p)
            else:
                y = y + str(p)+','+' '
        x = x + y+'\n'
    return x

def imagem2(n,m,p):
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(p)
        x.append(y)
    return x


