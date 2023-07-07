# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista1 = ['Maria', 'Helena', 'Eduarda']
lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# a1, b1, c1 = lista1
# a2, b2, *_, c2 = lista2
# a3, b3, *_, c3, d3 = lista2
# print(a1, c1)
# print(a2, c2)
# print(a3, c3, d3)

# for nome in lista2:
#     print(nome)

# for nome in lista2:
#     print(nome, end=' ') # Caso vc quer que ele exiba em uma linha, ele tira o \n, quebra de linha

# for nome in lista2:
#     print(nome, sep=' ') # Caso vc quiser que seja exibido sem o separador

# for nome in lista2:
#     print(nome, end=' ', sep=' ') # Caso vc quiser que seja exibido em uma lista e sem o separador

print(*lista2)
print(*string)
print(*tupla)
print(salas)
print(*salas, end='\n')
print(*salas)
print(*salas, end='\n')
print(*salas, sep='\n')
