"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()
print(lista_a)
print(lista_b)
print('--------------------')

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
print('--------------------')
