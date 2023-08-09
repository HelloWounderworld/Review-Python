def verifica(lista):
    for i in lista:
        if i != 0:
            return False
    return True
def clona_imagem(lista):
    x = []
    for i in range(len(lista)):
        x.append(lista[i])
    return x
class Polinomio:
    
    def __init__(self,coefs = []):
        self.coefs = coefs[:]
    
    def __str__(self):
        s = str()
        g = len(self.coefs)
        if g == 0:
            s += '0'
            return s
        for i in range(g):
            j = -i-1
            if j == -g:
                if self.coefs[j] < 0:
                    x = (-1)*self.coefs[j]
                    s = s+'-'+' '+str(x)
                elif self.coefs[j]>0:
                    s = s+'+'+' '+str(self.coefs[j])
                else:
                    if len(self.coefs)>1:
                        pass
                    elif len(self.coefs)==1:
                        s = s+str(self.coefs[j])
            elif j == -1:
                if self.coefs[j]<0:
                    x = (-1)*self.coefs[j]
                    s = s+'-'+' '+str(x)+'*x^%d'%(g+j)+' '
                elif self.coefs[j] > 0:
                    s = s + str(self.coefs[j])+'*x^%d'%(g+j)+' '
                else:
                    pass
            else:                
                if self.coefs[j]<0:
                    x = (-1)*self.coefs[j]
                    s = s + '-'+' '+str(x)+'*x^%d'%(g+j)+' '
                elif self.coefs[j]>0:
                    s = s+'+'+' '+str(self.coefs[j])+'*x^%d'%(g+j)+' '
                else:
                    pass
        return s
    
    def __call__(self,valor):
        soma = 0
        if valor == 0:
            return self.coefs[0]
        else:
            for i in range(len(self.coefs)):
                if i == 0:
                    soma = soma+self.coefs[i]
                else:
                    soma = soma + self.coefs[i]*(valor**i)
        return soma
    
    def __add__(self,other):
        if type(other) != int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(x,y):
                    polinomio.append(other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(y,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]+other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __radd__(self,other):
        if type(other)!= int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(x+1,y):
                    polinomio.append(other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                for j in range(y+1,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]+other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]+other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __sub__(self,other):
        if type(other) != int and type(other)!=float:
            x = len(self.coefs)
            y = len(other.coefs)
            polinomio = []
            if x < y:
                for i in range(x):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                for j in range(x,y):
                    polinomio.append((-1)*other.coefs[j])
                return Polinomio(polinomio)
            elif y<x:
                for i in range(y):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                for j in range(y,x):
                    polinomio.append(self.coefs[j])
                return Polinomio(polinomio)
            else:
                for i in range(x):
                    polinomio.append(self.coefs[i]-other.coefs[i])
                booleano = verifica(polinomio)
                if booleano == True:
                    return Polinomio([])
                return Polinomio(polinomio)
        else:
            polinomio = []
            x = self.coefs[0]-other
            polinomio.append(x)
            for i in range(1,len(self.coefs)):
                polinomio.append(self.coefs[i])
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __mul__(self,other):
        if type(other)!=int and type(other)!=float:
            z = Polinomio(self.coefs).grau()+Polinomio(other.coefs).grau()
            polinomio = []
            for i in range(0,z+1):
                soma = 0
                for j in range(len(self.coefs)):
                    for l in range(len(other.coefs)):
                        if j+l == i:
                            soma = soma + self.coefs[j]*other.coefs[l]
                polinomio.append(soma)
            return Polinomio(polinomio)
        else:
            polinomio = []
            for i in self.coefs:
                polinomio.append(i*other)
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def __rmul__(self,other):
        if type(other)!=int and type(other)!=float:
            z = Polinomio(self.coefs).grau()+Polinomio(other.coefs).grau()
            polinomio = []
            for i in range(0,z+1):
                soma = 0
                for j in range(len(self.coefs)):
                    for l in range(len(other.coefs)):
                        if j+l == i:
                            soma = soma + self.coefs[j]*other.coefs[l]
                polinomio.append(soma)
            return Polinomio(polinomio)
        else:
            polinomio = []
            for i in self.coefs:
                polinomio.append(i*other)
            booleano = verifica(polinomio)
            if booleano == True:
                return Polinomio([])
            return Polinomio(polinomio)
    
    def coeficientes(self):
        for i in range(len(self.coefs)):
            print(self.coefs[-i-1])
            if self.coefs[-i-1]!=0:
                if -i-1 == -1 :
                    lista = self.coefs[:]
                    self.coefs = lista
                    break
                else:
                    lista = self.coefs[:-i]
                    self.coefs = lista
                    break
        return self.coefs

    def grau(self):
        if len(self.coefs) == 0:
            return 0
        return len(self.coefs) - 1
    
    def derive(self):
        g = self.grau()
        if g <= 0:
            return Polinomio([])
        x = []
        for i in range(len(self.coefs)):
            x.append(self.coefs[i]*i)
        del(x[0])
        return Polinomio(x)

def main():
    # crie lista de coeficientes
    coefs = [5, 1, -2, 0, -3]

    # crie um objeto da classe polinomio
    print("1. criação de polinômios")
    p = Polinomio(coefs) # __init__()
    coefs = [-1, -1, -1]
    print("polinomio p: %s"%p)     # __str__()
    print("grau de p %s"%p.grau()) # grau()
    print("coeficientes e p: %s\n"%p.coeficientes()) # coeficientes()

    
    # crie um polinomio que represente a derivada de p
    print("2. derivada de polinômios")
    dp = p.derive()  # derive()
    print("derivada de p (=dp): %s"%dp) # __str__() 
   
    # crie um polinomio que represente a derivada de p
    ddp = dp.derive() # __derive__()
    print("derivada de dp (=ddp): %s"%ddp) # __str__()

    # coeficiente de p, dp e ddp 
    print("coeficientes de   p: %s"%p.coeficientes())
    print("coeficientes de  dp: %s"%dp.coeficientes())
    print("coeficientes de ddp: %s\n"%ddp.coeficientes())

    # calcule o valor dos polinômio
    print("3. valor de polinômios")
    valores = [0, 1, 0.5, 3] # depois tente com complex(1,1)
    for x in valores:
        print("p(%s) = %s," %(x, p(x)), end=" ")    # __call__() 
        print("dp(%s) = %s," %(x, dp(x)), end=" ")  # __call__() 
        print("ddp(%s) = %s" %(x, ddp(x)))          # __call__() 

    # calcule o valor dos polinômio
    print("\n4. adição de polinômios")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print("p1     : %s"%p1)
    print("p2     : %s"%p2)
    p3 = p1 + p2  # __add__()
    print("p1 + p2: %s"%p3)
    p4 = p1 - p1  # __sub__()
    print("p1 - p1: %s"%p4)
    p5 = p1 + 1   # __add__()
    print("p1 + 1 : %s"%p5)
    p6 = 2 + p1   # __radd__()
    print(" 2 + p1: %s"%p6)

    # calcule o produto de polinônios
    print("\n5. multiplicação de polinômios")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print("p1     : %s"%p1)
    print("p2     : %s"%p2)
    p3 = p1 * p2   # __mul__()
    print("p1 * p2: %s"%p3)
    p4 = p1 * p1   # __mul__()
    print("p1 * p1: %s"%p4)
    p5 = p1 * -2   # __mul__()
    print("p1 * -2: %s"%p5)
    p6 = 3 * p1    # __rmul__()
    print(" 3 * p1: %s"%p6)

    '''
    _init__, coeficientes, grau(): iniciando avaliação dos testes (vale 3 ponto(s))
    Polinomio([5, 1, -2, 0, -3]).__init__() deve clonar a lista.
    Polinomio([3]).__init__() deve clonar a lista.
    Polinomio([-1]).__init__() deve clonar a lista.
    Polinomio([1, 1, 0]).__init__() deve clonar a lista.
    Polinomio([1, 5]).__init__() deve clonar a lista.
    __init__, coeficientes, grau() não passou no(s) teste(s) acima
    __init__, coeficientes, grau(): avaliação encerrada... (nota 0.5)
    '''
    p1 = Polinomio([5, 1, -2, 0, -3]).__init__()
    print(p1)
    p2 = Polinomio([3]).__init__()
    print(p2)
    p3 = Polinomio([-1]).__init__()
    print(p3)
    p4 = Polinomio([1, 1, 0]).__init__()
    print(p4)
    p5 = Polinomio([1, 5]).__init__()
    print(p5)
    '''
    __add__(): iniciando avaliação dos testes (vale 1 ponto(s))
    (Polinomio([5, 1, -2, 0, -3])+Polinomio([3])).coeficientes() devia retornar [8, 1, -2, 0, -3].
    (Polinomio([-1])+Polinomio([0, 1, 1])).coeficientes() devia retornar [-1, 1, 1].
    (Polinomio([0, 1, 1])+Polinomio([1, 5])).coeficientes() devia retornar [1, 6, 1].
    (Polinomio([1, 5])+Polinomio([-1, -5])).coeficientes() devia retornar [].
    (Polinomio([-1])+1).coeficientes() devia retornar [].
    __add__() não passou no(s) teste(s) acima
    __add__(): avaliação encerrada... (nota 0)
    '''
    print((Polinomio([5, 1, -2, 0, -3])+Polinomio([3])).coeficientes())
    print((Polinomio([-1])+Polinomio([0, 1, 1])).coeficientes())
    print((Polinomio([0, 1, 1])+Polinomio([1, 5])).coeficientes())
    print((Polinomio([1, 5])+Polinomio([-1, -5])).coeficientes())
    print((Polinomio([-1])+1).coeficientes())
    '''
    __radd__(): iniciando avaliação dos testes (vale 1 ponto(s))
    (3+Polinomio([-3])).coeficientes() devia retornar [].
    __radd__() não passou no(s) teste(s) acima
    __radd__(): avaliação encerrada... (nota 0.5)
    '''
    print((3+Polinomio([-3])).coeficientes())
    '''
    _sub__(): iniciando avaliação dos testes (vale 1 ponto(s))
    (Polinomio([5, 1, -2, 0, -3])-Polinomio([3])).coeficientes() devia retornar [2, 1, -2, 0, -3].
    (Polinomio([-1])-Polinomio([0, 1, 1])).coeficientes() devia retornar [-1, -1, -1].
    (Polinomio([0, 1, 1])-Polinomio([1, 5])).coeficientes() devia retornar [-1, -4, 1].
    __sub__() não passou no(s) teste(s) acima
    __sub__(): avaliação encerrada... (nota 0)
    '''
    print((Polinomio([5, 1, -2, 0, -3])-Polinomio([3])).coeficientes())
    print((Polinomio([-1])-Polinomio([0, 1, 1])).coeficientes())
    print((Polinomio([0, 1, 1])-Polinomio([1, 5])).coeficientes())
    
#----------------------------------------------------------
if __name__ == "__main__":
    main()
    
'''
1. criação de polinômios
polinomio p:  - 3*x^4 - 2*x^2 + 1*x^1 + 5
grau de p 4
coeficientes e p: [5, 1, -2, 0, -3]

2. derivada de polinômios
derivada de p (=dp):  - 12*x^3 - 4*x^1 + 1
derivada de dp (=ddp):  - 36*x^2 - 4
coeficientes de   p: [5, 1, -2, 0, -3]
coeficientes de  dp: [1, -4, 0, -12]
coeficientes de ddp: [-4, 0, -36]

3. valor de polinômios
p(0) = 5, dp(0) = 1, ddp(0) = -4
p(1) = 1, dp(1) = -15, ddp(1) = -40
p(0.5) = 4.8125, dp(0.5) = -2.5, ddp(0.5) = -13.0
p(3) = -253, dp(3) = -335, ddp(3) = -328

4. adição de polinômios
p1     : 3*x^4 - 2*x^2 + 1*x^1 + 5
p2     : 1*x^2 + 5*x^1 - 2
p1 + p2: 3*x^4 - 1*x^2 + 6*x^1 + 3
p1 - p1: 0
p1 + 1 : 3*x^4 - 2*x^2 + 1*x^1 + 6
 2 + p1: 3*x^4 - 2*x^2 + 1*x^1 + 7

5. multiplicação de polinômios
p1     : 3*x^4 - 2*x^2 + 1*x^1 + 5
p2     : 1*x^2 + 5*x^1 - 2
p1 * p2: 3*x^6 + 15*x^5 - 8*x^4 - 9*x^3 + 14*x^2 + 23*x^1 - 10
p1 * p1: 9*x^8 - 12*x^6 + 6*x^5 + 34*x^4 - 4*x^3 - 19*x^2 + 10*x^1 + 25
p1 * -2:  - 6*x^4 + 4*x^2 - 2*x^1 - 10
 3 * p1: 9*x^4 - 6*x^2 + 3*x^1 + 15
'''
    

