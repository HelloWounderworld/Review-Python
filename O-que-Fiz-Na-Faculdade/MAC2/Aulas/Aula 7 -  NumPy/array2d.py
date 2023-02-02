class Array2D:
    def __init__(self, shape, valor = 0):
        self.shape = shape
        nlins      = shape[0]
        ncols      = shape[1]
        self.size  = nlins*ncols
        self.ndim  = 2
        self.dtype = type(valor)
        self.data  = self.size*[valor]

    def __str__(self):
        size  = self.size
        ncols = self.shape[1]
        data  = self.data
        s = "Array2D(["
        for i in range(0, size, ncols):
            s += str(data[i:i+ncols]) + ","
        s = s[:-1] + ")]"    
        return s

    def __add__(self, other):
        shape = self.shape
        size  = self.size
        soma  = Array2D(shape)
        data  = soma.data
        for i in range(size):
            data[i] = self.data[i]+other.data[i]
        return soma        

    def __mul__(self, other):
        '''supõe other é int ou float'''
        shape = self.shape
        size  = self.size
        soma  = Array2D(shape)
        data  = soma.data
        for i in range(size):
            data[i] = other * data[i]
        return soma        

    def __rmul__(self, other):
        return self * other
