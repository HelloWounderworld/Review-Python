class SistemaOperacional:
    def __init__(self, nome):
        self.nome = nome
        self.programas = []

    def instalar_programa(self, programa):
        self.programas.append(programa)

class Programa:
    def __init__(self, nome):
        self.nome = nome

windows = SistemaOperacional("Windows")
word = Programa("Word")
windows.instalar_programa(word)