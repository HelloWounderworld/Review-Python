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
        print(x)
    return x


