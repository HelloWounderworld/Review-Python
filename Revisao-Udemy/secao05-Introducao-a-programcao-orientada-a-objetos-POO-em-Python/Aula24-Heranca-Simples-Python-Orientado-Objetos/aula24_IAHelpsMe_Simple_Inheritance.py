class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "Som genérico de animal"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

# Uso
animal = Animal("Bicho")
cachorro = Cachorro("Rex")
print(animal.falar())  # Saída: Som genérico de animal
print(cachorro.falar())  # Saída: Au au!