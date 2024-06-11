class Terrestre:
    def caminhar(self):
        return "Caminhando na terra"

class Aquatico:
    def nadar(self):
        return "Nadando na água"

class Anfibio(Terrestre, Aquatico):
    def mover(self):
        return f"{self.caminhar()} e {self.nadar()}"

# Criando uma instância de Anfibio
sapo = Anfibio()
print(sapo.mover())  # Saída: Caminhando na terra e Nadando na água