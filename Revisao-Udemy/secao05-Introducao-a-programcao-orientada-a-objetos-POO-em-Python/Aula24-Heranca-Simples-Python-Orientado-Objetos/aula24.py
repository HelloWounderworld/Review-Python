# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# object
class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    # Visto que exite esse metodo aqui, nao sera buscado esse mesmo metodo na classe Pessoa.
    def falar_nome_classe(self):
        print('Eita... Nem sai da classe cliente...')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = '1234Aluno'

help(Pessoa)

c1 = Cliente('Leonardo', 'Teramatsu')
help(Cliente)
c1.falar_nome_classe()
print(c1.cpf)
print()

a1 = Aluno('Alan', 'Turing')
help(Aluno)
a1.falar_nome_classe()
print(a1.cpf)
print()
