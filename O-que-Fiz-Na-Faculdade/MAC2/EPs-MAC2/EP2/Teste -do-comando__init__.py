def cria_imagem(n,m,p):
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(p)
        x.append(y)
    return x

class Pymagem:

    def __init__(self,nlins,ncolns,valor):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
    
    def __str__(self):
        print("Entrei na string_imagem")
        lista = clona_imagem(cria_imagem(self.nlins,self.ncolns,self.valor))
        x = str()
        for i in range(len(lista)):
            y = str()
            for j in range(len(lista)):
                if j == (len(lista) - 1):
                    y = y + str(lista[i][j])
                else:
                    y = y + str(lista[i][j]) + ',' + ' '
            x = x + y + '\n'
        return x

    def __str__(self):
        lista = 
