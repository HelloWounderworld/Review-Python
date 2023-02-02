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
    '''
    Implementação da classe Pymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem
    def __init__(self,nlins,ncolns,valor=0):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tricks = cria_imagem(self.nlins,self.ncolns,self.valor)
        self.lista_assistente = []   
        
    def __str__(self):
        if len(self.tricks) == 0:
            return show(self.lista_assistente)
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
    
    def recorta_imagem(self,lista,n,m,p,q):
        x = []
        for i in range(n,p):
            y = []
            for j in range(m,q):
                y.append(lista[i][j])
            x.append(y)
        return x

    def crop(self,n=0,m=0,p=0,q=0):
        if n==0 and m==0 and p==0 and q==0:
            self.tricks = clona_imagem(self.tricks)
            return Pymagem(len(self.tricks),len(self.tricks[0]),self.tricks[0][0])
        else:
            img_nova = Pymagem(p-n,q-m)
            for i in range(n,p):
                for j in range(m,q):
                    img_nova.put(i-n,j-m,self.tricks[i][j])
            return img_nova

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
    print("tipo da mg1", type(img1))
    print("Conteúdo de img2:")
    print(img2)
    print("tipo de img2", type(img2))

    print("\nChamadas da função size()")
    lins1, cols1 = img1.size()
    print("Resolução de img1: %d x %d"%(lins1, cols1))
    lins2, cols2 = img2.size()
    print("Resolução de img2: %d x %d"%(lins2, cols2))

    print("\nChamadas do método crop")
    img3 = img1.crop() ## cria uma cópia
    print("Conteúdo de img3:")
    print(img3)
    print("tipo da img3", type(img3))
    img4 = img2.crop(0, 1, lins2-1, cols2)  
    print("Conteúdo de img4:")
    print(img4)
    print("tipo da img4", type(img4))

    print("\nChamadas de put e get")
    col = 2
    img1.put(0, col, 11)
    for lin in range(1, lins1):
        img1.put(lin, col, img1.get(lin-1, col) + 10)
    print("Conteúdo de img1:")
    print(img1)
    print("tipo da img1", type(img1))
    # não deve alterar img3
    print("Conteúdo de img3:")
    print(img3)
    print("tipo da img3", type(img3))

    # modifica a linha 1 de img2
    lin = 1
    for col in range(0, cols2):
        print("alterando img2", img2)
        img2.put(lin, col, 11)
    print("Conteúdo de img2:")
    print(img2)
    print("tipo da img2", type(img2))
    # não deve alterar img4
    print("Conteúdo de img4:")
    print(img4)
    print("tipo da img4", type(img4))
    # mais testes
    print("Outro crop")
    print(img1.crop(1,1,3,4))
    print("tipo da img1", type(img1))

if __name__ == '__main__':
    main()

