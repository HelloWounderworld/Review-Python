"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
print(lista)
print('--------------------')
lista.append('Luiz')
print(lista)
print('--------------------')
nome = lista.pop()
print(nome)
print(lista)
print('--------------------')
lista.append(1233)
print(lista)
print('--------------------')
del lista[-1]
print(lista)
print('--------------------')
# Note que, nem está definido o índice 100, mas foi add no último lugar da lista?
lista.insert(100, 50)
print(lista[4])
print(lista)
print('--------------------')
# Quando coloco um elemento novo no índice já definido, o restante dos outros índices
# são empurrados para frente.
lista.insert(2, 600)
print(lista[2])
print(lista)
print('--------------------')
lista.clear()
print(lista)
print('--------------------')
