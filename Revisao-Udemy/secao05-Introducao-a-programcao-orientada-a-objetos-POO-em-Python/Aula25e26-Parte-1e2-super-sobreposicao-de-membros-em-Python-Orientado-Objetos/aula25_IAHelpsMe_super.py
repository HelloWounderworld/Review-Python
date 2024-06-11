class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe Animal
        self.raca = raca

# Instanciando um objeto Cachorro
dog = Cachorro("Rex", "Labrador")
print(dog.nome)  # Saída: Rex
print(dog.raca)  # Saída: Labrador