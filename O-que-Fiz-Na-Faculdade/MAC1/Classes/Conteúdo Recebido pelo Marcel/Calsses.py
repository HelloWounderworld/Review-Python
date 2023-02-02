class Complexo:
    def __init__(self,real = 0,imaginario = 0): 
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return "{}{:+}i".format(self.real,self.imaginario)

    def __add__(self,outro):
        return Complexo(self.real+outro.real,self.imagem+outro.imagem)

    def __radd__(self,outro):
        
        if isinstance(outro,(int,float)):
            return Complexo(self.real + outro, self.imaginario)
        
        elif isinstance(outro,(int,float)):
            return Complexo(self.real,self.imaginario + outro)
        
        else:
            return NotImplemented

    def Associatividade(self,outro,other):
        
        if (self.real + outro.real) + other.real == self.real + (outro.real + other.real) and (self.imaginario + outro.imaginario) + other.imaginario = self.imaginario + (outro.imaginario + other.imaginario):
            return print("Confere !")

        else:
            return NotImplemented

    def Existencia_Neutro_Somas(self):

        if ((self.real + 0 == self.real) and (self.imaginario + 0 == self.imaginario)):
            return print("Confere !")

        else:
            return NotImplemented

    def __mult__(self,outro):
        return Complexo((self.real)*(outro.real) - (self.imaginario)*(outro.imaginario),(self.real)*(outro.imaginario) + (self.imaginario)*(outro.real))

    def comutatividade_produto(self,outro):

        if isinstance(outro,(int,float)):
            return Complexo(self.real

    
    
    def conjugado(self,imaginario):
        return Complexo(self.real,-self.imaginario)

    

#Exercicio: Crie uma classe que de vetores e dentro dessa classe crie as funçoes que sera as operaçoes aritmeticas usuais de um espaço vetorial inclusive o produto escalar
        
