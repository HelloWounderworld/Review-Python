#-------------------------------------------------------------
class Fracao:
    #------------------------------------
    def __init__(self, num = 0, den = 1):
        """ (Fracao, int, int) -> Fracao

        Construtor: cria um objeto Fracao.
        Mágica: funcao retorna mas nao tem return.            
        """
        self.num = num
        self.den = den
        self.simplifique()

    #------------------------------------
    def __repr__(self):
        """ (Fracao) -> str

        Retorna a string representa self oficialmente.
        """
        return self.__str__()
    
    #------------------------------------
    def __str__(self):
        """ (Fracao) -> str

        Retorna o string que print() usa para imprimir um
        Fracao.
        """
        if self.den == 1:
            texto = "%d" %self.num
        else:
            texto = "%d/%d" %(self.num,self.den)
        return texto

    #-------------------------------------
    def simplifique(self):
        """ (Fracao) -> None

        Recebe um racional e altera a sua representacao
        para a forma irredutivel.
        """
        comum = mdc(self.num, self.den)
        self.num //= comum
        self.den //= comum
        if self.den < 0:
            self.den = -self.den
            self.num = -self.num

    #-------------------------------------
    def get(self):
        """ (Fracao) -> int, int

        Recebe um racional e retorna o seu numerador e o
        seu denominador.
        """
        return self.num, self.den

    #--------------------------------------
    def put(self, novo_num, novo_den):
        """ (Fracao) -> None

        Recebe um racional e dois inteiros novo_num e
        novo_den e modifica a fracao para representar
           novo_num/novo_den.
        """
        self.num = novo_num
        self.den = novo_den
        self.simplifique()
    
    #------------------------------------
    def __add__(self, other):
        """ (Fracao, Fracao ou int) -> Fracao

        Retorna a soma da fracao `self` e da fracao ou int `other`.
        Usado pelo Python quando escrevemos Fracao + Fracao ou
                                            Fracao + int
        """
        if type(other) == int:
            novo_num = self.num + self.den*other
            novo_den = self.den
        else:    
            novo_num = self.num*other.den + self.den*other.num
            novo_den = self.den*other.den
        f = Fracao(novo_num,novo_den)
        return f

    #------------------------------------
    def __radd__(self, other):
        """ (Fracao, int) -> Fracao

        Retorna a soma da fracao `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fracao
        """
        return self + other # self.__add__(other)
    
    #------------------------------------
    def __sub__(self, other):
        """ (Fraco, Fracao ou int) -> Fracao

        Retorna a diferenca das fracoes `self` e `other`.
        Usado pelo Python quando escrevemos Fracao - int
        """
        if type(other) == int:
            novo_num = self.num - self.den*other
            novo_den = self.den
        else:
            novo_num = self.num*other.den - self.den*other.num
            novo_den = self.den*other.den
        f = Fracao(novo_num,novo_den)
        return f

    #------------------------------------
    def __rsub__(self, other):
        """ (Fraco, int) -> Fracao

        Retorna a diferenca a fracao `self` e o int `other`.
        Usado pelo Python quando escrevemos int - Fracao
        """
        return self - other
     
    
    #------------------------------------
    def __mul__(self, other):
        """ (Fracao, Fracao ou int) -> Fracao

        Retorna o produto da fração `self` e a fração ou int `other`.
        Usado pelo Python quando escrevemos Fracao * Fracao 
                                         ou int    * Fracao
        """
        if type(other) == int:
            novo_num = self.num * other
            novo_den = self.den
        else:    
            novo_num = self.num * other.num
            novo_den = self.den * other.den
        f = Fracao(novo_num, novo_den)
        return f

    #------------------------------------
    def __rmul__(self, other):
        """ (Fracao, int) 
        Usado pelo Python quando escrevemos int * Fracao
        """
        return self * other 

    #-------------------------------------
    def __truediv__(self, other):
        if type(other) == int:
            novo_num = self.num
            novo_den = self.den * other
        else:
            novo_num = self.num * other.den
            novo_den = self.den * other.num
        f = Fracao(novo_num, novo_den)
        return f

    #-------------------------------------
    def __rtruediv__(self, other):
        return self / other
    
    #-------------------------------------
    def __eq__(self, other):
        if type(other) == int:
            prim_num = self.num
            seg_num = other * self.den
        else:    
            prim_num = self.num  * other.den
            seg_num  = other.num * self.den
        return prim_num == seg_num

    #-------------------------------------
    def __lt__(self, other):
        if type(other) == int:
            prim_num = self.num
            seg_num = other * self.den
        else:    
            prim_num = self.num  * other.den
            seg_num  = other.num * self.den
        return prim_num == seg_num
    
    #-------------------------------------
    def __invert__(self):
        return Fracao(-self.num, self.den)
        
#-----------------------------------------
def mdc(m,n):
    """ (int, int) -> int
    Recebe dois inteiros m e n e retorna o
    mdc de m e n.
    
    Se m = 0 = n retorna 0 para indicando erro.
    """
    if n <  0: n = -n    
    if m <  0: m = -m
    if n == 0: return m    
    r = m%n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

 

