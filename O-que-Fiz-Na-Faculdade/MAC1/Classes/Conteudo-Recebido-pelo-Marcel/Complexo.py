class Complexo:# As variaveis com valores ja atribuidos "real = 0" e "imaginario = 0", e conhecido como valores "default", ou seja, padroniza para esse valor
#colocado caso nao seja atribuido algum outro valor.
    def __init__(self,real = 0,imaginario = 0): #O metodo "__ini__" e construtor
        self.__real = real #self.real = real
        ''' esses anderscore "_" colocado no self.__real significa que esta sendo usado como algo privado'''
        self.__imaginario = imaginario #self.imaginario = imaginario

    '''(1) def __init__(self,real,imaginario):
        self.__complexo = str(real) +'.'+str(imaginario), caso feito isso nao mudaria nada na operaçao do outro arquivo'''
   
    def real(self): #caso eu colocar x.real() <=> Complexo.real(x)
        return self.__real

    def imaginario(self):
        return self.__imaginario

    def __str__(self):
        return "{}{:+}i". format(self.__real,self.__imaginario)

    def __add__(self,outro):
        
        if isinstance(outro,Complexo): #isinstance = instancia de uma variavel
            return Complexo(self.real() + outro.real(),self.imaginario() + outro.imaginario())
        elif(isinstance(outro,(int,float))): #(,(,)) o "(,)" colocado e conhecido como tupla, ou seja, lista imutavel
            return Complexo(self.real() + outro,self.imaginario())
        else:
            return NotImplemented # Retorna o erro mesmo
        #return Complexo(self.real() + outro.real(),self.imaginario() + outro.imaginario()) --- maneira alternativa

    def __radd__(self,outro): # __radd__ ja troca automaticamente, ou seja, operaçao comutativa
        if isinstance(outro,(int,float)):
            return Complexo(self.real() + outro, self.imaginario())

        else:
            return NotImplemented

    def __eq__(self,outro): #__eq__ = igualdade
        return (self.real() == outro.real()) and (self.imaginario() == outro.imaginario()) # Mas essa forma montada nao verifica caso eu faça a seguinte comparaçao "x == 1"

    def conjugado(self):
        return Complexo(self.real(),-self.imaginario())
    
    # Caso eu nao queira colocar print(x.real()), e sim, print(x.real). Coloque @property
    @property
    def real(self):
        return self.__real

    '''@property
    def real(self):
        return float(self.complexo.split('.')[0]) maneira opcional para caso eu opte pelo metodo (1)'''
    
    @property
    def imaginario(self):
        return self.__imaginario
    
    @real.setter
    def real(self,valor):
        self.__real = valor
    
    @imaginario.setter
    def imaginario(self,valor):
        self.__imaginario = valor
