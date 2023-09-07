# Dictionary Comprehension e Set Comprehension
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}
p(produto.items())

novos_produtos = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
    if chave != 'categoria'
}

p(novos_produtos)

tupla_produto = (
    (chave, produto)
    for chave, produto in produto.items()
)

p(tuple(tupla_produto))

lista = [
    ('nome', 'Leonardo'),
    ('altura', 1.84),
    ('profissao', 'Engenheiro de Sistema'),
    ('formacao', 'Matemática pura')
]

dc = {
    chave: valor
    for chave, valor in lista
}

p(dc)
p(dict(lista))

s1 = {i for i in range(10)}
p(s1)
p(set(range(10)))
