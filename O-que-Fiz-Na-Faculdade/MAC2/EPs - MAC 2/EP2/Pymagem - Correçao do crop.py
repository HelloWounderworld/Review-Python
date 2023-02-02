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
            img_nova = Pymagem(p-n,q-m) #Esse assume somente n<=p e m<=q, nao generaliza
            #criar mais alguns condicionais para caso em que p == 0 ou q == 0
            print(img_nova.size())
            print(img_nova)
            for i in range(n,p):
                for j in range(m,q):
                    img_nova.put(i-n,j-m,self.tricks[i][j])
            return img_nova
        
def main():
    print(Pymagem(4,5,0))
    print(Pymagem(4,5,0).crop(2,1)) 
    print(Pymagem(4,5,0).crop().get(0,1))
main()
