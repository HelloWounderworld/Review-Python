def imagem(nlins,ncolns,valor):
    x = []
    for i in range(nlins):
        y = []
        for j in range(ncolns):
            y.append(valor)
        x.append(y)
    return x
class Pymagem:
    
    def __init__(self,nlins,ncolns,valor=0):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
    
    def __str__(self):
        Lista1 = 
        x = str()
        for i in range(len(Lista1)):
            y = str()
            for j in range(len(Lista1[i])):
                if j == (len(Lista1[i]) - 1):
                    y = y + str(Lista1[i][j])
                else:
                    y = y + str(Lista1[i][j]) + ',' + ' '
            x = x + y + '\n'
        return x

    def put(self,nlins,ncolns,valor):
        return

def main():
    img1 = Pymagem(4, 5)
    print(img1)
    col = 2
    img1.put(0, col, 11)
    for lin in range(1, lins1):
        img1.put(lin, col, img1.get(lin-1, col) + 10)
    print("Conteúdo de img1:")
    print(img1)
    main()
