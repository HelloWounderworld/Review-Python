class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.alugado_por = None

    def alugar(self, pessoa):
        self.alugado_por = pessoa
        pessoa.livros_alugados.append(self)
        print(f"{self.titulo} foi alugado por {pessoa.nome}")

class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    def empresta_livro(self, livro):
        print(f"{self.nome} emprestou o livro {livro.titulo}")

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.livros_alugados = []

    def aluga_livro(self, livro):
        livro.alugar(self)

# Instâncias
livro1 = Livro("1984 - George Orwell")
aluno1 = Aluno("Maria")

# Associação sendo utilizada
aluno1.aluga_livro(livro1)

# Associação bidirecional sendo utilizada
aluno1.aluga_livro(livro1)
print(f"O livro {livro1.titulo} está alugado por {livro1.alugado_por.nome}")
