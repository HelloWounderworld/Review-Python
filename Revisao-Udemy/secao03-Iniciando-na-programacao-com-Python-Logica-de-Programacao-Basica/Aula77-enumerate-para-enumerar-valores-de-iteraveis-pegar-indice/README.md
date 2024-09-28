# Aula 77 - enumerate para enumerar valores de iteráveis (pegar índices):
Vamos enumerar!! (No sentido matemático?? kkkkkkkk)

No caso, dada uma lista não vazia, temos uma função chamado enumerate que enumera todos os índices da lista.

Em outras palavras, é como uma sequência que exibe os seus índices donde cada elemento está definido

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

No caso, pelo enumerate, o formato em que será exibido o indice e o elemento definido nesse índice estará no formato de tupla.
