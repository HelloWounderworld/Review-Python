# Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saque inválido.")

    def get_saldo(self):
        return self.__saldo

# Public
class Carro:
    def __init__(self, marca):
        self.marca = marca  # Atributo público

    def dirigir(self):
        print("Carro está sendo dirigido")

# Protected
class Carro:
    def __init__(self, marca):
        self._marca = marca  # Atributo protegido

    def _dirigir_privado(self):
        print("Método protegido, uso interno ou em subclasses")

# Private
class Carro:
    def __init__(self, marca):
        self.__marca = marca  # Atributo privado

    def __dirigir_privado(self):
        print("Método privado, acesso restrito à própria classe")