class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    def empresta_livro(self, livro):
        print(f"{self.nome} emprestou o livro {livro.titulo}")

# Instâncias
livro1 = Livro("1984")
bibliotecario = Bibliotecario("João")

# Associação sendo utilizada
bibliotecario.empresta_livro(livro1)