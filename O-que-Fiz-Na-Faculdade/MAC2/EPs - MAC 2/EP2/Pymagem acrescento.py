def cria_imagem(n,m,p):
    x = []
    for i in range(n):
        y = []
        for j in range(m):
            y.append(p)
        x.append(y)
    return x

def clona_imagem(lista):
    x = []
    for i in range(len(lista)):
        y = []
        for j in range(len(lista[i])):
            y.append(lista[i][j])
        x.append(y)
    return x

def recorta_imagem(lista,n,m,p,q):
    x = []
    for i in range(n,p):
        y = []
        for j in range(m,q):
            y.append(lista[i][j])
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

class Pymagem:

    def __init__(self,nlins,ncolns,valor=0, lista = []):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tricks = lista
        if len(self.tricks) == 0:
            self.tricks = cria_imagem(self.nlins,self.ncolns,self.valor)

    def __str__(self):
        return show(self.tricks)

    def size(self):
        return self.nlins , self.ncolns

    def get(self,lin,col):
        lista = self.tricks
        posicao = lista[lin][col]
        return posicao

    def put(self,lin,col,valor):
        self.tricks[lin][col] = valor
        return self.tricks

    def crop(self,n=0,m=0,p=0,q=0):
        if n==0 and m==0 and p==0 and q==0:
            lista = clona_imagem(self.tricks)
            return Pymagem(0,0,0,lista)
        else:
            Lista = self.tricks
            Lista1 = recorta_imagem(Lista,n,m,p,q)
            return Pymagem(0,0,0,Lista1)

def main():
    ''' (None) -> None
    Essa função apenas testa a classe Pymagem.
    Coloque aqui outros testes que desejar.
    '''
    # testa construtor
    img1 = Pymagem(4, 5)
    img2 = Pymagem(3, 3, 88)

    print("\nChamadas da função print()")
    print("Conteúdo de img1:")
    print(img1)
    print("Conteúdo de img2:")
    print(img2)

    print("\nChamadas da função size()")
    lins1, cols1 = img1.size()
    print("Resolução de img1: %d x %d"%(lins1, cols1))
    lins2, cols2 = img2.size()
    print("Resolução de img2: %d x %d"%(lins2, cols2))

    print("\nChamadas do método crop")
    img3 = img1.crop() ## cria uma cópia
    print("Conteúdo de img3:")
    print(img3)
    img4 = img2.crop(0, 1, lins2-1, cols2)  
    print("Conteúdo de img4:")
    print(img4)

    print("\nChamadas de put e get")
    col = 2
    img1.put(0, col, 11)
    for lin in range(1, lins1):
        img1.put(lin, col, img1.get(lin-1, col) + 10)
    print("Conteúdo de img1:")
    print(img1)
    # não deve alterar img3
    print("Conteúdo de img3:")
    print(img3)

    # modifica a linha 1 de img2
    lin = 1
    for col in range(0, cols2):
        img2.put(lin, col, 11)
    print("Conteúdo de img2:")
    print(img2)
    # não deve alterar img4
    print("Conteúdo de img4:")
    print(img4)

    # mais testes
    print("Outro crop")
    print(img1.crop(1,1,3,4))

if __name__ == '__main__':
    main()

