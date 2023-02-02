class ContaBancaria:
    def __init__(self,nome):
        self.__nome = nome
        self.__saldo = 0

    def deposito(self,valor):
        self.__saldo = self.__saldo + valor
        return self.__saldo

    def saque(self,valor):
        
        if (valor <= self.__saldo):
            self.__saldo = self.__saldo - valor
            return self.__saldo

        else:
            raise ValueError("Saldo insuficiente")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return "Nome = {}, Saldo = {}". format(self.__nome,self.__saldo)

    
