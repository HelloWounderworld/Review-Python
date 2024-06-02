# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Leonardo'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Leonardo', 'Teramatsu')
# p1.nome = 'Leonardo'
# p1.sobrenome = 'Teramatsu'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

class Carro:
    def __init__(self, alguma_coisa='Sei la'):
        self.nome = alguma_coisa

fusca = Carro()
print(fusca.nome)
print()
fusca.nome = "Fusca"
print(fusca.nome)
print()
fusca.alguma_coisa = "Fusca"
print(fusca.nome)
print(fusca.alguma_coisa)

# Porem, como uma boa pratica, e recomendavel que coloque o nome dos parametros de forma igual
# sem algum valor padrao.
# Claro, pelo fato de nao definirmos algum valor padrao ao atributo, sempre que a classe for instanciado
# precisara atribuir algum valor dentro dela.

# Basicamente, o que se define dentro do inicializador e uma funcao
# A unica coisa que difere, e que nela, como primeiro parametro, vem o "self"
class Carro2:
    def __init__(self, nome):
        self.nome = nome

# fusca = Carro2() # Isso dara erro
fusca = Carro2('Beatles')
print(fusca.nome)
print()
fusca.nome = "Fusca"
print(fusca.nome)
print()
fusca.alguma_coisa = "Fusca"
print(fusca.nome)
print(fusca.alguma_coisa)

celta = Carro2('Celta')
print(celta.nome)
print()
celta.nome = "Celtinha"
print(celta.nome)
print()
celta.alguma_coisa = "Celtao"
print(celta.nome)
print(celta.alguma_coisa)
