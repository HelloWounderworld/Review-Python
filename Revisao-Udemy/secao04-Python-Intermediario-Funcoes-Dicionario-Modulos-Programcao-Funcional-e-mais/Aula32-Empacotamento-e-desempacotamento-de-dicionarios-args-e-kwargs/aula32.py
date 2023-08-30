# Empacotamento e desempacotamento de dicionarios.
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Hayashi'
}

a, b = pessoa
c, d = pessoa.values()
e, f = pessoa.items()
(g1, g2), h = pessoa.items()
print(a, b)
print(c, d)
print(e, f)
print(g1, g2, h)

for chave, valor in pessoa.items():
    print(chave, valor)

pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

dados_pessoa = {
    'idade': 26,
    'altura': 1.84
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa, dados_pessoa)
print(pessoa_completa)

# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEADOS: ', args)
    print(kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Leonardo', qlq=1236)
mostro_argumentos_nomeados(1, 2, 3, nome='Leonardo', qlq=1236)
mostro_argumentos_nomeados(**pessoa_completa)
