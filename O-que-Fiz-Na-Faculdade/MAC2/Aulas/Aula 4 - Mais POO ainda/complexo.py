import math

class Complexo:
    def __init__(self, real = 0, imag = 0):
        '''(Complexo, int|float, int|float) -> None
 
        Usado pelo contrutor para montar um número complexo.
        '''
        self.real = real
        self.imag = imag

    def __str__(self):
        '''(Complexo) -> str

        Recebe um referência `self` a um Complexo e retorna
        o string usado por print() para exibi-lo.
        '''
        if self.real == self.imag == 0: return "0"
        s = ""
        if self.real != 0:
            s = str(self.real)
            if self.imag > 0: s += "+"
        if self.imag != 0:
            s += str(self.imag) + "i"
        return s

    def __repr__(self):
        '''(Complexo) -> str '''
        return str(self)
    
    def __eq__(self, other):
        '''(Complexo, Complexo) -> bool

        Recebe referência `self` e `other`para números complexos
        e retorna True se forem iguais e False em casocontrário.

        Usado pelo Python quando escrevemos "Complexo == Complexo"
        '''
        return self.real == other.imag and self.imag == other.imag


    def __add__(self, other):
        '''(Complexo, Complexo|int|float) -> Complexo

        Recebe Complexos `self` e `other` e retorna a
        sua soma

        Usado pelo Python quando escrevemos "Complexo + [Complexo|int|float]"
        '''
        if type(other) in [int, float]:
            real = self.real + other
            imag = self.imag
        else:    
            real = self.real + other.real
            imag = self.imag + other.imag
        return Complexo(real, imag)

    def __radd__(self, other):
        '''(Complexo, int|float) -> Complexo

        Recebe Complexos `self` e `other` e retorna a
        sua soma

        Usado pelo Python quando escrevemos "[int|float]+Complexo"
        '''
        return self + other

    def __sub__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Usado pelo Python quando escrevemos "Complexo - [Complexo|int|float]"
        '''
        if type(other) in [int, float]:
            real = self.real - other
            imag = self.imag
        else:    
            real = self.real - other.real
            imag = self.imag - other.imag
        return Complexo(real, imag)

    def __rsub__(self, other):
        '''(Complexo, int|float) -> Complexo

        Recebe Complexos `self` e `other` e retorna a
        sua soma

        Usado pelo Python quando escrevemos "[int|float]-Complexo"
        '''
        return self - other
    
    def __mul__(self, other):
        '''(Complexo, Complexo|int|float) -> Complexo

        Usado pelo Python quando escrevemos "Complexo * [Complexo|int|float]"
        '''
        if type(other) in [int, float]:
            real = self.real*other
            imag = self.imag*other
        else:    
            real = self.real*other.real - self.imag*other.imag
            imag = self.real*other.imag + self.imag*other.real
        return Complexo(real, imag)

    def __rmul__(self, other):
        '''(Complexo, Complexo|int|float) -> Complexo

        Usado pelo Python quando escrevemos "[Complexo|int|float]*Complexo"
        '''
        return self * other

    def __truediv__(self, other):
        '''(Complexo, Complexo/int/float) -> Complexo

        Usado pelo Python quando escrevemos "Complexo / Complexo|int|float"
        '''
        if type(other) in [int, float]:
            real = self.real / other
            imag = self.imag / other
        else:    
            other_conj = other.conjugado()
            z_num = self  * other_conj
            z_den = other * other_conj
            real  = z_num.real / z_den.real
            imag  = z_num.imag / z_den.real
        return Complexo(real, imag)

    def __rtruediv__(self, other):
        '''(Complexo, Complexo/int/float) -> Complexo

        Usado pelo Python quando escrevemos "Complexo / Complexo|int|float"
        '''
        return self / other
    
    def norma(self):
        '''(Complexo) -> float

        Retorna a norma do Complexo `self`
        '''
        return math.sqrt(self.real*self.real + self.imag*self.imag)
    
    def conjugado(self):
        '''(Complexo) -> Complexo
        '''
        return Complexo(self.real, -self.imag)

    
