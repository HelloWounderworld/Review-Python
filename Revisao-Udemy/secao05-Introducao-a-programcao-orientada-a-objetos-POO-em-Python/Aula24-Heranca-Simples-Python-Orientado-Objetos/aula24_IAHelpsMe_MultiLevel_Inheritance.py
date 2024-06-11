class Veiculo:
    def descricao(self):
        return "Veículo genérico"

class Carro(Veiculo):
    def descricao(self):
        return "Carro"

class Sedan(Carro):
    def descricao(self):
        return "Sedan"

# Uso
veiculo = Veiculo()
carro = Carro()
sedan = Sedan()
print(veiculo.descricao())  # Saída: Veículo genérico
print(carro.descricao())  # Saída: Carro
print(sedan.descricao())  # Saída: Sedan