class Veiculo:
    # Atributo de classe (compartilhado por todas as instâncias)
    numero_de_rodas = 4

    def __init__(self, marca, modelo):
        # Atributos de instância (específicos para cada instância)
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalhes(self):
        # Método de instância que acessa tanto atributos de instância quanto de classe
        return f"{self.marca} {self.modelo} tem {Veiculo.numero_de_rodas} rodas."

    @classmethod
    def mudar_numero_de_rodas(cls, novas_rodas):
        # Método de classe que modifica um atributo de classe
        cls.numero_de_rodas = novas_rodas

# Criando instâncias da classe Veiculo
carro1 = Veiculo("Toyota", "Corolla")
carro2 = Veiculo("Honda", "Civic")

# Acessando método de instância
print(carro1.mostrar_detalhes())  # Toyota Corolla tem 4 rodas.

# Modificando o atributo de classe usando método de classe
Veiculo.mudar_numero_de_rodas(6)

# Acessando o método de instância novamente para ver o efeito da mudança
print(carro1.mostrar_detalhes())  # Toyota Corolla tem 6 rodas.
print(carro2.mostrar_detalhes())  # Honda Civic tem 6 rodas.
