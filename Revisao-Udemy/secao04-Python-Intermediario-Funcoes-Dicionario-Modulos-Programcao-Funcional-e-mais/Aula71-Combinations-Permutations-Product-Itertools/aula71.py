# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(lista, nume):
    print(*list(combinations(lista, nume)), sep='\n')
    print()

def print_permu(lista, nume):
    print(*list(permutations(lista, nume)), sep='\n')
    print()

def print_prod(lista):
    print(len(list(product(*lista))))
    print(*list(product(*lista)), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print(combinations(pessoas, 2))
# print()
# for combinacao in combinations(pessoas, 2):
#     print(combinacao)
# print()
# print(list(combinations(pessoas, 2)))
# print()
# print(*list(combinations(pessoas, 2)), sep='\n')

print_iter(pessoas, 0)
print_iter(pessoas, 1)
print_iter(pessoas, 2)
print_iter(pessoas, 3)
print_iter(pessoas, 4)
print_iter(pessoas, 5)

print_permu(pessoas, 0)
print_permu(pessoas, 1)
print_permu(pessoas, 2)
print_permu(pessoas, 3)
print_permu(pessoas, 4)
print_permu(pessoas, 5)

print_prod(camisetas)