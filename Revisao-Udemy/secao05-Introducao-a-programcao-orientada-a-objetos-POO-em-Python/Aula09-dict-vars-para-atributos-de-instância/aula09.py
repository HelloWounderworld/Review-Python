class Pessoa:
    # atributo = 'valor'
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# p1.nome = 'Eita'
# print(p1.nome)

# del p1.nome
# print(p1.nome)

print(p1.__dict__)
print(p2.__dict__)

p1.__dict__['outra'] = 'coisa'
print(p1.__dict__)

del p1.__dict__['outra']
print(p1.__dict__)

dados = {'nome': 'Leonardo', 'idade': 27}
p3 = Pessoa(**dados)
print(p3.__dict__)