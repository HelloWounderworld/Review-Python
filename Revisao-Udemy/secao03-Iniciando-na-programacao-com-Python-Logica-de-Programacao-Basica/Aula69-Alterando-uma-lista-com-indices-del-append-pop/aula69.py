"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
print(lista)
print('----------------------')
lista[2] = 300
print(lista)
print('----------------------')
del lista[2]
print(lista)
print(lista[2])
print('----------------------')
lista.append(50)
print(lista)
print('----------------------')
lista.pop()
print(lista)
print('----------------------')
lista.append(60)
print(lista)
print('----------------------')
lista.append(70)
print(lista)
print('----------------------')
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)