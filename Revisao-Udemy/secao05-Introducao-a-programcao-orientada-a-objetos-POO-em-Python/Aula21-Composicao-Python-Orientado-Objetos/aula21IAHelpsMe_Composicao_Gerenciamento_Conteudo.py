class Elemento:
    def __init__(self, tipo):
        self.tipo = tipo

class Pagina:
    def __init__(self, titulo):
        self.titulo = titulo
        self.elementos = []

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

pagina = Pagina("Página Inicial")
texto = Elemento("Texto")
imagem = Elemento("Imagem")
pagina.adicionar_elemento(texto)
pagina.adicionar_elemento(imagem)