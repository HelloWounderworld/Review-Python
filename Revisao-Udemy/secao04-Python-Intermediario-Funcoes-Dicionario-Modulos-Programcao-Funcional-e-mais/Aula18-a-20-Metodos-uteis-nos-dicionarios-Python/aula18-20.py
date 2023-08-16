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

pessoa.setdefault('idade')
pessoa.setdefault('altura', 1.8)
print(pessoa['idade'])
print(pessoa['altura'])

pessoa.setdefault('nome', 'Alan')
print(pessoa['nome'])

import copy

dic1 = {
    'd1': 1,
    'd2': 2,
    'd3': [
        'Leo', 'Louco', 'Medo'
    ]
}

dic2 = dic1
dic3 = copy.copy(dic1)
dic4 = copy.deepcopy(dic1)

dic2['d1'] = 1000
dic3['d1'] = 2000
dic4['d3'][0] = 'Turing'
print(dic1)
print(dic2)
print(dic3)
print(dic4)

p1 = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

print(p1.get('nome'))
print(p1.get('idade'))
print(p1.get('idade', 'Não tem a chave idade'))

p2 = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

name = p2.pop('nome')
print(name)
print(p2)

p3 = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

ultima_chave = p3.popitem()
print(ultima_chave)
print(p3)

p4 = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

print(p4)

p4.update({
    'idade': 26,
    'altura': 1.8
})
print(p4)

p4.update({
    'nome': 'Alan'
})

print(p4)

p4.update({
    'sobrenome': 'Turing',
    'cidade': 'London'
})

print(p4)

p4.update(job='Mathematician', college='Cambridge')

print(p4)

p5 = {
    'nome': 'Leonardo Takashi',
    'sobrenome': 'Teramatsu'
}

tupla = ('invention', 'Turing Machine'), ('job', 'Solve Enigma')
p5.update(tupla)

print(p5)
