"""
Tipo tupla - Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Luiz'
print(nomes)
print('-----------------')
nomes = ('Maria', 'Helena', 'Luiz')
print(nomes)
print('-----------------')
nomes = ['Maria', 'Helena', 'Luiz']
print(nomes)
print('-----------------')
nomes1 = tuple(nomes)
nomes2 = list(nomes)
print(nomes1[-1])
print(nomes1)
print('-----------------')
print(nomes2[-1])
print(nomes2)
print('-----------------')
