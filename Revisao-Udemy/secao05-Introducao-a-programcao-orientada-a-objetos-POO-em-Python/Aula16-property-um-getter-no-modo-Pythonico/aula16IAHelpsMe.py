class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        self._raio = valor

    @property
    def area(self):
        return 3.14159 * self._raio ** 2

# Uso da classe
circulo = Circulo(5)
print(circulo.raio)  # Saída: 5
print(circulo.area)  # Saída: 78.53975

circulo.raio = 10
print(circulo.raio)  # Saída: 10
print(circulo.area)  # Saída: 314.159

# Tentativa de definir um raio negativo
try:
    circulo.raio = -5
except ValueError as e:
    print(e)  # Saída: O raio não pode ser negativo