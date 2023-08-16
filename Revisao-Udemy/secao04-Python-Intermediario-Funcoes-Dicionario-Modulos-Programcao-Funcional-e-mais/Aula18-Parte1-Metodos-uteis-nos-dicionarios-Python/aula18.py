# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

print(pessoa['sobrenome'])
print(pessoa.__len__())
print(len(pessoa))

print(pessoa.keys())

print(tuple(pessoa.keys()))
print(tuple(pessoa.keys())[0])
print(tuple(pessoa.keys())[1])

print(list(pessoa.keys()))
print(list(pessoa.keys())[0])
print(list(pessoa.keys())[1])

for chave in pessoa:
    print(chave)

for chave in pessoa.keys():
    print(chave)

print(pessoa.values())
print(tuple(pessoa.values()))
print(list(pessoa.values()))

for chave in pessoa.values():
    print(chave)

print(pessoa.items())
print(tuple(pessoa.items()))
print(list(pessoa.items()))

for item in pessoa.items():
    print(item)
    print(item[0], item[1])

for chave, valor in pessoa.items():
    print(chave, valor)
