# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, hp):
        super().__init__(marca, ano)
        self.hp = hp

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Potência: {self.hp} HP")

class Bicicleta(Veiculo):
    def __init__(self, marca, ano, tipo):
        super().__init__(marca, ano)
        self.tipo = tipo

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f"Tipo: {self.tipo}")

# Criando instâncias
carro = Carro("Toyota", 2021, 150)
bicicleta = Bicicleta("Trek", 2020, "Mountain")

# Mostrando detalhes
carro.mostrar_detalhes()
bicicleta.mostrar_detalhes()
