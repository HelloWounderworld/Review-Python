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

    def __init__(self,nlins,ncolns,valor=0):
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tricks = cria_imagem(self.nlins,self.ncolns,self.valor)
              

    def __str__(self):
        return show(self.tricks)
    
    def __add__(self,other):
        x = []
        for i in range(len(self.tricks)):
            y = []
            for j in range(len(self.tricks[i])):
                y.append(self.tricks[i][j]+other.tricks[i][j])
            x.append(y)
        img_nova = Pymagem(len(x),len(x[0]))
        for i in range(len(x)):
            for j in range(len(x[i])):
                img_nova.put(i,j,x[i][j])
        return img_nova
    
    def __mul__(self,alfa):
        x = []
        for i in range(len(self.tricks)):
            y = []
            for j in range(len(self.tricks[i])):
                z = self.tricks[i][j]*alfa - int(self.tricks[i][j]*alfa)
                w = z*100 - int((z*10))*10
                if w >= 5:
                    z = (int(z*10) + 1)/10
                    t = int(self.tricks[i][j]*alfa) + z
                    y.append(t)
                else:
                    z = (int(z*10))/10
                    t = int(self.tricks[i][j]*alfa) + z
                    y.append(t)
            x.append(y)
        img_nova = Pymagem(len(x),len(x[0]))
        for i in range(len(x)):
            for j in range(len(x[i])):
                img_nova.put(i,j,x[i][j])
        return img_nova
    
    def paste(self,other,tlin,tcol):
        n,m = other.size()
        for i in range(n):
            for j in range(m):
                self.tricks[tlin+i][tcol+j] = other.get(i,j)
        return self.tricks
    
    def pinte_disco(self,lin,col,raio,val):
        for i in range(lin-raio,lin+raio+1):
            for j in range(col-raio, col+raio+1):
                if 0<=i<=(len(self.tricks)-1) and 0 <= j <= (len(self.tricks[i])-1):
                    if ((i-lin)**2+(j-col)**2)<raio**2:
                        self.tricks[i][j] = val
        return self.tricks
                    
    
    def pinte_retangulo(self,tlx,tly,brx,bry,val):
        for i in range(tlx,brx):
            for j in range(tly,bry):
                if (0<= i <= len(self.tricks)) and (0<= j <=len(self.tricks[i])):
                    self.tricks[i][j] = val
        return self.tricks
    
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
            clone = clona_imagem(self.tricks)
            return Pymagem(len(clone),len(clone[0]),clone[0][0])
        else:
            img_nova = Pymagem(p-n,q-m)
            for i in range(n,p):
                for j in range(m,q):
                    img_nova.put(i-n,j-m,self.tricks[i][j])
            return img_nova


def main():

    img1 = Pymagem(6, 8, 200)
    img2 = Pymagem(6, 8, 121)
    
    img3 = img1.crop(3,2,6,7)
    print("teste crop:")
    print(img3)

    img2.paste(img3, 1, 2)
    print("teste paste:")
    print(img2)

    img4 = img1 + img2
    print("teste __add__:")
    print(img4)

    img5 = img1*0.3
    print("teste __mul__:")
    print(img5)

    img6 = img5 + img2*0.7
    print("teste __add__ e __mul__ :")
    print(img6)

    img7 = Pymagem(8, 8, 2)
    img8 = img7.crop()

    img7.pinte_disco(2, 2, 5, 0)
    print("teste disco:")
    print(img7)

    img8.pinte_retangulo(-1, 3, 5, 6, 0)
    print("teste retangulo:")
    print(img8)

    print("teste cirulo com retangulo:")
    print(img7*0.5 + img8)

main()

