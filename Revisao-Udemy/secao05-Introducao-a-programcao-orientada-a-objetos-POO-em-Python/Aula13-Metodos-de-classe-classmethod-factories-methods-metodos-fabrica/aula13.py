class Pessoa:
    ano = 2024 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_classe(self):
        print('Howdy!')

    @classmethod
    def metodo_de_classe_sem_self(cls):
        print('Hello!')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)

print(Pessoa.ano)

p1 = Pessoa('Joao', 34)
p1.metodo_de_classe()

# Pessoa.metodo_de_classe() # precisa passar algo dentro do argumento
Pessoa.metodo_de_classe(p1)

Pessoa.metodo_de_classe_sem_self()

p2 = Pessoa.criar_com_50_anos('Miyami')
print(p2.nome, p2.idade)

p3 = Pessoa.criar_sem_nome(27)
print(p3.nome, p3.idade)
