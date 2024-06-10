class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor(potencia=120)  # Motor é criado junto com o Carro

    def __del__(self):
        print("O carro e o motor foram destruídos.")