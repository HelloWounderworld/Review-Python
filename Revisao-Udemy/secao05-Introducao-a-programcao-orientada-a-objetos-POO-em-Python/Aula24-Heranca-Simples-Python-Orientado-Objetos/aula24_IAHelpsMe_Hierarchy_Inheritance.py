class Veiculo:
    def descricao(self):
        return "Veículo genérico"

class Carro(Veiculo):
    def descricao(self):
        return "Carro"

class Motocicleta(Veiculo):
    def descricao(self):
        return "Motocicleta"

# Uso
veiculo = Veiculo()
carro = Carro()
motocicleta = Motocicleta()
print(veiculo.descricao())  # Saída: Veículo genérico
print(carro.descricao())  # Saída: Carro
print(motocicleta.descricao())  # Saída: Motocicleta