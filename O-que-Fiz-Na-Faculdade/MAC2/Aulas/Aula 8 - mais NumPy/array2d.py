def main():
    a = Array2D( (2,3), 3)
    b = Array2D( (2,3), 4)
    print(a)
    print("soma:\n", a + b)
    print("mult:\n", a * 2)
    print("get: ", a[0, 1])
    c = a.reshape(3,2)
    print("c reshape:\n", c)
    print("a antes:\n", a)
    c[1,0] = 0
    print("a depois:\n", a)
    d = c.copy()
    d[2,1] = -1
    print("d:\n", d)
    print("c:\n", c)


class Array2D:

    def __init__(self, shape, val):
        nlin, ncol = shape
        self.shape = shape
        self.dtype = type(val)
        self.size  = nlin*ncol
        self.data = [val]*self.size

    def __getitem__(self, shape):
        nlin, ncol = self.shape
        lin, col = shape
        return self.data[lin*ncol + col]

    def __setitem__(self, shape, val):
        nlin, ncol = self.shape
        lin, col = shape
        self.data[lin*ncol + col] = val

    def __str__(self):
        s = ''
        k = 0
        nlin, ncol = self.shape
        for lin in range(nlin):
            for col in range(ncol):
                s += str(self.data[k]) + ' '
                k += 1
            s += '\n' 
        return s

    def __add__(self, other):
        ''' (Array2D, Array2D) -> Array2D
        soma elemento a elemento
        '''
        nova = Array2D(self.shape, 0)
        for i in range(self.size):
            nova.data[i] = self.data[i] + other.data[i]
        return nova

    def __mul__(self, other):
        ''' (Array2D, Array2D) -> Array2D
        multiplica elemento a elemento
        (Array2D, float ou int) -> Array2D
        multiplica por escalar (int ou float)
        '''
        nova = Array2D(self.shape, 0)

        if type(other) == int or type(other) == float:                
            for i in range(self.size):
                nova.data[i] = self.data[i] * other
        else: 
             for i in range(self.size):
                nova.data[i] = self.data[i] * other.data[i]

        return nova

    def reshape(self, nlin, ncol):
        '''(Array2D, int, int) -> vista '''
        vista = Array2D( (0,0), 0)  # array de tamanho zero
        if nlin * ncol != self.size:
            return None
        vista.shape = (nlin, ncol)
        vista.size  = nlin * ncol
        vista.dtype = self.dtype
        vista.data = self.data   # compartilha os mesmos dados!!
        return vista

    def copy(self):
        '''(Array2D) -> Array2D '''
        copia = Array2D( self.shape, self.dtype(0) ) # array de mesmo tamanho e tipo       
        # errado
        #copia.data = self.data # fazer primeiro como ;-) !!! 

        # correto
        for i in range(self.size):
            copia.data[i] = self.data[i]
        return copia
       

main()



