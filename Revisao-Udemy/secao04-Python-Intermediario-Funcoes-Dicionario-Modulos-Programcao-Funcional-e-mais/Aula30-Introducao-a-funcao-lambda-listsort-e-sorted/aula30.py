# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]

lista.sort(reverse=True)
print(lista)

sorted(lista)
print(lista)

lista.sort()
print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#lista.sort()

# Tenta testar apenas com 'return item' para verificar o que está sendo devolvido o tipo de erro.
#def ordena(item):
    #print('Objeto a ser ordenado: ', item)
    #return item['nome']

#lista.sort(key=ordena)

#for i in lista:
    #print(i)

#lista.sort(key=lambda item: item['nome'])

def exibition(lista):
    for i in lista:
        print(i)
    print()

# Note que, l1 e l2 faz uma copia da lista, mas com cópia fraca.
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibition(l1)
exibition(l2)

print('Curiosidades')
print('Copia completa')
l1.pop()
exibition(l1)
exibition(l2)
exibition(lista)

print('Mas e fraca')
l1[0]['nome'] = 'Leonardo'
exibition(l1)
exibition(l2)
exibition(lista)
