# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
string = 'Leonardo'  # str
print(string.upper())
print(string.capitalize())
print(string.count)
print(isinstance(string.count,int))
print(isinstance(string.count,str))
print(isinstance(string.count,float))
print(isinstance(string, str))
class Pessoa:
    ...

p1 = Pessoa('Leonardo', 'Teramatsu')
p1.nome = 'Leonardo'
p1.sobrenome = 'Teramatsu'

p2 = Pessoa('Maria', 'Joana')
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)