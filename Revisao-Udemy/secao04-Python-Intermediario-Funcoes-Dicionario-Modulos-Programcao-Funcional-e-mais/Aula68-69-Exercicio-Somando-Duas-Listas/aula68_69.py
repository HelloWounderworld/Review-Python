"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# Minha solução
lista_1 = [10, 2, 3, 40, 5, 6, 7]
lista_2 = [1, 2, 3, 4]
lista_somada = [lista_1[i] + lista_2[i] for i in range(min(len(lista_1), len(lista_2)))]
print(lista_somada)

# O que tava no github do prof
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# Usando zip_longest
from itertools import zip_longest

lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)