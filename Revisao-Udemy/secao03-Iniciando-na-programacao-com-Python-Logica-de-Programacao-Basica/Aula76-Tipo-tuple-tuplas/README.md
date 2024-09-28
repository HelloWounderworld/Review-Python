# Aula 76 - Tipo tuple (tuplas):
Bom, como na aula anterior não discutimos muito bem sobre tuplas, vamos ver isso nessa aula.

No caso, a tupla a sua sintaxe se dá pelo ()

    nomes = ('Maria', 'Helena', 'Luiz')

Podemos definir uma tupla sem usar o (), tbm

    nomes = ('Maria', 'Helena', 'Luiz')

Ela é uma lista imutável.

Bom, tudo o que vc pode fazer numa lista, na qual não altere os elementos definidos dentro dela e/ou que modifique a quantidade da lista, vc pode fazer numa tupla.

Uma outra forma de criarmos uma tupla seria convertendo de uma lista

    nomes = ['Maria', 'Helena', 'Luiz']
    print(nomes)
    print('-----------------')
    nomes1 = tuple(nomes)
    nomes2 = list(nomes)
    print(nomes1[-1])
    print(nomes1)
    print('-----------------')
    print(nomes2[-1])
    print(nomes2)
    print('-----------------')
