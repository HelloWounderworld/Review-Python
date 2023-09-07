import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco']}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)

lista = [n for n in range(10) if n < 5]
p(lista)
