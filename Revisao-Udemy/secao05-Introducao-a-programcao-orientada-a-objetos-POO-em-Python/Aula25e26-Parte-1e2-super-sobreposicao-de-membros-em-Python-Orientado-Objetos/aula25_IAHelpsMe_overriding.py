class Animal:
    def falar(self):
        return "Som genérico de animal"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Instanciando objetos
animal = Animal()
dog = Cachorro()
cat = Gato()

print(animal.falar())  # Saída: Som genérico de animal
print(dog.falar())     # Saída: Au au!
print(cat.falar())     # Saída: Miau!