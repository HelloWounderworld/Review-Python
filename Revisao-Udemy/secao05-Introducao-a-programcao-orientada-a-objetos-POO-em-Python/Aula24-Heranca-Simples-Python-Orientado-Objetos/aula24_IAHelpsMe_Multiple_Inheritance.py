class Terrestre:
    def caminhar(self):
        return "Caminhando..."

class Aquatico:
    def nadar(self):
        return "Nadando..."

class Anfibio(Terrestre, Aquatico):
    pass

# Uso
sapo = Anfibio()
print(sapo.caminhar())  # Saída: Caminhando...
print(sapo.nadar())  # Saída: Nadando...