# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {}

##
##
chave = 'nome_completo'
pessoa[chave] = 'Leonardo TT'
pessoa['sobrenome'] = 'Turing'

print(pessoa)
#print(pessoa['nome'])
print(pessoa[chave])

pessoa[chave] = 'Mumei'

print(pessoa)
print(pessoa[chave])

del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

#if pessoa['nome']:
#    print('Existe')

print(pessoa.get('nome_completo'))
print(pessoa.get('nome'))
print(pessoa.get('nome') is not None)
print(pessoa.get('nome') is None)
print(pessoa.get('nome', 'Não existe'))

if pessoa.get('nome'):
    print('Existe')

print('Aqui não executa!')
