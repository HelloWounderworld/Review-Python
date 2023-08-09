def imagem2(Lista,valor):    
    x = []
    for i in range(len(Lista)):
        y = []
        for j in range(len(Lista[i])):
            if Lista[i][j] == valor:
                y.append(Lista[i][j])
            else:
                y.append(valor)
            x.append(y)
    return x
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
        Lista = imagem(self.nlins,self.ncolns,self.valor)
    
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
    
    def size(self):
        return self.nlins , self.ncolns
    
    def get(self,nlins,ncolns):
        return
        
    def put(self,nlins,ncolns,valor):
        
        return 
    
    def crop(self,n = 0,m = 0,p = 0,q = 0):
        
        if n == 0 and m == 0 and p == 0 and q == 0:
            return Pymagem(self.nlins,self.ncolns,self.valor)
        else:
            x = []
            for i in range(n,p):
                y = []
                for j in range(m,q):
                    y.append(0)
                x.append(y)
                
            return Pymagem(len(x),len(x[0]),self.valor)

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
