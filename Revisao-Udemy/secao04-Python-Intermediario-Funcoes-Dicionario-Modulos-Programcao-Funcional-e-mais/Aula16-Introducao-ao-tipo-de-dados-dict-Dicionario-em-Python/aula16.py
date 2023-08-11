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

pessoa = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu',
    'idade': 26,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'bla bla bla', 'numero': 123},
        {'rua': 'ta ta ta', 'numero': 456}
    ]
}
    
print(pessoa, type(pessoa))
print()

print(pessoa['nome'])
print(pessoa['sobrenome'])
print(pessoa['idade'])
print(pessoa['altura'])
print(pessoa['enderecos'])
print(pessoa['enderecos'][0])
print(pessoa['enderecos'][1])
print(pessoa['enderecos'][0]['rua'])
print(pessoa['enderecos'][0]['numero'])
print(pessoa['enderecos'][1]['rua'])
print(pessoa['enderecos'][1]['numero'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
