from contabancaria import ContaBancaria
class ContaVip(ContaBancaria):
    
    def __init__(self,nome):
        
        super(ContaVip,self).__init__(self,nome)
        #self.__saldo = saldo

    def saque(self,valor):
        self.__saldo = self.__saldo - valor
        
def main():
    x = ContaBancaria("Leonardo")
    x.deposito(1000.50)
    x.saque(100)
    print(x)

    y = ContaVip("Takashi")
    y.deposito(100)
    y.saque(200)
    
main()
