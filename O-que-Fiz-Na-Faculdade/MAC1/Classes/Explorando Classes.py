def cria_imagem(n,m,p):
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(p)
        x.append(y)
    return x

def show(lista): #coloca dentro de __str__
    x = str()
    for i in range(len(lista)):
        y = str()
        for j in range(len(lista[i])):
            if j == (len(lista[i]) - 1):
                y = y + str(lista[i][j])
            else:
                y = y + str(lista[i][j]) + ',' + ' '
        x = x + y + '\n'
    return x

class imagem:

    def __init__(self,lin,col,valor=0):
        self.lin = lin
        self.col = col
        self.valor = valor

    def __str__(self):
        lista = cria_imagem(self.lin,self.col,self.valor)
        return show(lista)
    def dicionario(self):
        x = {}
        lista = cria_imagem(self.lin,self.col,self.valor)
        for i in range(len(lista)*len(lista[0])):
            x[i] = self.valor
        return x

def main():
    img = imagem(4,5)
    print(img)
    img = 11
    print(img)

main()
