class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

# Criando objetos
biblioteca = Biblioteca("Biblioteca Central")
livro1 = Livro("1984")
livro2 = Livro("Brave New World")

# Agregando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Listando livros na biblioteca
for livro in biblioteca.livros:
    print(f"{livro.titulo} está na {biblioteca.nome}")