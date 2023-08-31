# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

lista = []

for i in range(10):
    lista.append(i)

print(lista)

lista = [1 for i in range(10)]
print(lista)

lista = [i for i in range(10)]
print(lista)

lista = [i * 2 for i in range(10)]
print(lista)

