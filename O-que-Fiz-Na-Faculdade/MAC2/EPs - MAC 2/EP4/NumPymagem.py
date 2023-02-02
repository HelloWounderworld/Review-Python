import numpy as np
def show(array): 
    nlins, ncolns = array.shape
    x = str()
    for i in range(nlins):
        y = str()
        for j in range(ncolns):
            if j == (ncolns - 1):
                y = y + str(array[i,j])
            else:
                y = y + str(array[i,j]) + ',' + ' '
        x = x + y + '\n'
    return x
#-------------------------------------------------------------------------- 

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''
    def __init__(self,nlins = 0,ncolns = 0,valor=0):
        self.compara = np.arange(1).reshape(1,)
        self.nlins = nlins
        self.ncolns = ncolns
        self.valor = valor
        self.tamanho = self.nlins*self.ncolns
        if type(self.valor)==type(self.compara):
            self.data = self.valor
        else:
            self.data = np.full((self.nlins,self.ncolns),self.valor)
        
    def __str__(self):
        return show(self.data)
        
    def size(self):
        return self.data.shape
    
    def get(self,lin,col):
        return self.data[lin,col]
    
    def put(self,lin,col,valor):
        self.data[lin,col] = valor
    
    def crop(self,tlx=0,tly=0,brx=0,bry=0):
        if tlx==0 and tly==0 and brx==0 and bry==0:
            array = NumPymagem(self.nlins,self.ncolns,0)
            nlin,ncol = self.data.shape
            for i in range(nlin):
                for j in range(ncol):
                    array.put(i,j,self.data[i,j])
            return array
        else:
            if len(self.data)<=brx or len(self.data[0,:])<= bry :
                nlin, ncoln = self.data.shape
                if len(self.data)<=brx and bry<len(self.data[0,:]):
                    img_nova = NumPymagem(nlin-tlx,bry-tly,0)
                    for i in range(tlx,nlin):
                        for j in range(tly,bry):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                elif brx<len(self.data) and len(self.data[0,:])<=bry:
                    img_nova = NumPymagem(brx-tlx,ncoln-tly)
                    for i in range(tlx,brx):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                else:
                    img_nova = NumPymagem(nlin-tlx,ncoln-tly,0)
                    for i in range(tlx,nlin):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
            else:
                nlin , ncoln = self.data.shape
                if brx == 0 and bry == 0:
                    img_nova = NumPymagem(nlin-tlx,ncoln-tly)
                    for i in range(tlx,nlin):
                        for j in range(tly,ncoln):
                            img_nova.put(i-tlx,j-tly,self.data[i,j])
                    return img_nova
                img_nova = NumPymagem(brx-tlx,bry-tly,0)
                for i in range(tlx,brx):
                    for j in range(tly,bry):
                        img_nova.put(i-tlx,j-tly,self.data[i,j])
                return img_nova
    
    def paste(self,other,tlin,tcol):
        if 0<=tlin<len(self.data) and 0<=tcol<len(self.data[0,:]):
            if len(other.data)<=len(self.data[tlin:]):
                if len(other.data[0,:])<=len(self.data[tlin,tcol:]):
                    self.data[tlin:len(other.data)+tlin,tcol:len(other.data[0,:])+tcol] = other.data
                else:
                    self.data[tlin:len(other.data)+tlin,tcol:]=other.data[:,:len(self.data[tlin,tcol:])]
            else:
                if len(other.data[0,:])<=len(self.data[tlin,tcol:]):
                    self.data[tlin:,tcol:len(other.data[0,:])+tcol] = other.data[:len(self.data[tlin:]),:]
                else:
                    self.data[tlin:,tcol:] = other.data[:len(self.data[tlin:]),:len(self.data[tlin,tcol:])]
        else:
            if 0<=tcol<len(self.data[0,:]):
                if 0<tlin:
                    self.data
                else:
                    if tlin+len(other.data)<0:
                        self.data
                    else:
                        if tlin+len(other.data)<len(self.data):
                            if len(other.data[0,:])<len(self.data[0,tcol:]):
                                self.data[:tlin+len(other.data),tcol:tcol+len(other.data[0,:])] = other.data[-tlin:,:]
                            else:
                                self.data[:tlin+len(other.data),tcol:]=other.data[-tlin:,:len(self.data[0,tcol:])]
                        else:
                            if len(other.data[0,:])<len(self.data[0,tcol:]):
                                self.data[:,tcol:tcol+len(other.data[0,:])] = other.data[-tlin:-tlin+len(self.data),:]
                            else:
                                self.data[:,tcol:]=other.data[-tlin:-tlin+len(self.data),:len(self.data[0,tcol:])]                            
            elif 0<=tlin<len(self.data):
                if 0<tcol:
                    self.data
                else:
                    if tcol+len(other.data[0,:])<0:
                        self.data
                    else:
                        if tcol+len(other.data[0,:])<len(self.data[tlin,:]):
                            if len(other.data)<len(self.data[tlin:]):
                                self.data[tlin:tlin+len(other.data),:tcol+len(other.data[0,:])] = other.data[:,-tcol:]
                            else:
                                self.data[tlin:,:tcol+len(other.data[0,:])] = other.data[:len(self.data),-tcol:]
                        else:
                            if len(other.data)<len(self.data[tlin:]):
                                self.data[tlin:tlin+len(other.data),:]=other.data[:,-tcol:-tcol+len(self.data[tlin,:])]
                            else:
                                self.data[tlin:,:] = other.data[:tlin+len(self.data),-tcol:-tcol+len(self.data[tlin,:])]
            else:
                if 0<tlin or 0<tcol:
                    self.data
                else:
                    if tlin+len(other.data)<0 or tcol+len(other.data[0,:])<0:
                        self.data
                    else:
                        if tlin+len(other.data)<len(self.data):
                            if tcol+len(other.data[0,:])<len(self.data[0,:]):
                                self.data[:tlin+len(other.data),:tcol+len(other.data[0,:])]=other.data[-tlin:,-tcol:]
                            else:
                                self.data[:tlin+len(other.data),:]=other.data[-tlin:,-tcol:-tcol+len(self.data[0,:])]
                        else:
                            if tcol+len(other.data[0,:])<len(self.data[0,:]):
                                self.data[:,:tcol+len(other.data[0,:])]=other.data[-tlin:-tlin+len(self.data),-tcol:]
                            else:
                                self.data[:,:]=other.data[-tlin:-tlin+len(self.data),-tcol:-tcol+len(self.data[0,:])]
                                    
    def __add__(self,other):
        lista = np.array([0.0])
        if other.data.dtype == lista.dtype:
            lista = NumPymagem(self.nlins,self.ncolns,0.0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]+other.data[i,j])
            return lista
        else:
           lista = NumPymagem(self.nlins,self.ncolns,0)
           for i in range(self.nlins):
               for j in range(self.ncolns):
                   lista.put(i,j,self.data[i,j]+other.data[i,j])
           return lista 
    
    def __mul__(self,alpha):
        if type(alpha)==float:
            lista = NumPymagem(self.nlins,self.ncolns,0.0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]*alpha)
            return lista
        else:
            lista = NumPymagem(self.nlins,self.ncolns,0)
            for i in range(self.nlins):
                for j in range(self.ncolns):
                    lista.put(i,j,self.data[i,j]*alpha)
            return lista
    
    def pinte_disco(self,lin,col,raio,valor):
        nlins , ncols = self.data.shape
        for i in range(lin-raio,lin+raio+1):
            for j in range(col-raio, col+raio+1):
                if 0<=i<=(nlins-1) and 0 <= j <= (ncols-1):
                    if ((i-lin)**2+(j-col)**2)<raio**2:
                        self.data[i,j] = valor
    
    def pinte_retangulo(self,tlx,tly,brx,bry,valor):
        nlin, ncol = self.data.shape
        for i in range(tlx,brx):
            for j in range(tly,bry):
                if (0<= i < nlin) and (0<= j < ncol):
                    self.data[i,j] = valor
    
    def transpoe(self):
        if len(self.data)==len(self.data[0]):
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    if j < i:
                        x = self.data[i,j]
                        self.data[i,j] = self.data[j,i]
                        self.data[j,i] = x
            return self.data
        else:
            lista = self.data.T
            self.data = self.data.ravel().reshape(len(self.data[0][:]),len(self.data))
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    self.data[i,j] = lista[i,j]
            return self.data
    
    def rearranja(self,nlin,ncol):
        if nlin*ncol != self.nlins*self.ncolns:
            pass
        else:
            self.data = self.data.ravel().reshape(nlin,ncol)
            
    def espelha(self,eixo):
        if eixo == 'h':
            self.data = np.flip(self.data,1)
        elif eixo == 'v':
            nova = np.flip(self.data,0)
            self.data = nova
            #return self.data
    
def main():
    a1 = np.arange(25).reshape(5,5)
    img1 = NumPymagem(valor=a1)
    img2 = NumPymagem(4, 3, 100)
    print(img1)
    
    nlins, ncolns = img1.size()
    print("Este aqui é o tamanho da baronga")
    print((nlins,ncolns))
    
    img1.put(1, 3, 99)
    img2.put(0, 2, 99)
    print("NumPymagens criadas:")
    print(img1)
    print(img2)

    print("teste com transpoe:")
    img1.transpoe()
    img2.transpoe()
    print(img1)
    print(img2)

    print("teste com rearranja:")
    img1.rearranja(5,6)
    img2.rearranja(2,6)
    print(img1)
    print(img2)

    print("teste com espelha na horizontal:")
    img1.espelha('h')
    print(img1)
    print("teste com espelha na vertical:")
    img1.espelha('v')
    print(img1)
    
    img1 = NumPymagem(6, 8, 200)
    img2 = NumPymagem(6, 8, 121)
    
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

    img7 = NumPymagem(8, 8, 2)
    img8 = img7.crop()

    img7.pinte_disco(2, 2, 5, 0)
    print("teste disco:")
    print(img7)

    img8.pinte_retangulo(-1, 3, 5, 6, 0)
    print("teste retangulo:")
    print(img8)

    print("teste cirulo com retangulo:")
    print(img7*0.5 + img8)
    
    img1 = NumPymagem(4, 5)
    img2 = NumPymagem(3, 3, 88)

    print("\nChamadas da função print()")
    print("Conteúdo de img1:")
    print(img1)
    print("Conteúdo de img2:")
    print(img2)

    print("\nChamadas da função size()")
    lins1, cols1 = img1.size
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
    

