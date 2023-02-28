"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']

# nome1, nome2, nome3 = nomes
# print(nome1)
# print(nome2)
# print(nome3)

# nome1, *resto = nomes
# nome1, *_ = nomes
_, nome2, *_ = nomes
_, _, nome3, *resto = nomes
# print(nome1)
# print(nome2)
print(nome3)
print(resto)
print(_)
