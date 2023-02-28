"""
enumerate - enumera iteráveis (índices)
"""
# O enumerate faz algo do tipo de baixo numa lista
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
print(enumerate(lista))
print(list(enumerate(lista)))
# Podemos definir a partir de qual índice começará a ser enumerado.
print(list(enumerate(lista, start=19)))
print('-----------------------')
# Curioso que quando colocamos o enumerate no for, não precisamos colocar o list para iterar
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
print('-----------------------')

for item in enumerate(lista):
    print(item)
    indice, nome = item
    print(indice, nome)
print('-----------------------')

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
print('-----------------------')    
    