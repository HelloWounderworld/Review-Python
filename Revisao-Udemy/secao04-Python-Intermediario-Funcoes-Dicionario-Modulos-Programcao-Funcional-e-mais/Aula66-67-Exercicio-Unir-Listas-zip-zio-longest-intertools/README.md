# Aula 66 e 67 - Exercício e Solução - Unir listas + zip e zip_longest do intertools:
Seguir o enunciado

    # Exercício - Unir listas
    # Crie uma função zipper (como o zipper de roupas)
    # O trabalho dessa função será unir duas
    # listas na ordem.
    # Use todos os valores da menor lista.
    # Ex.:
    # ['Salvador', 'Ubatuba', 'Belo Horizonte']
    # ['BA', 'SP', 'MG', 'RJ']
    # Resultado
    # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

Vamos aprender, tbm, sobre o módulo itertools donde iremos aprender os métodos zip e zip_longest.

Primeiro, irei colocar a forma como o professor solucionou o problema

    def zipper(lista1, lista2):
        intervalo_maximo = min(len(lista1), len(lista2))
        return [
            (lista1[i], lista2[i]) for i in range(intervalo_maximo)
        ]

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zipper(l1, l2))

Bom, existe um método nativo do python que já realiza criações sem a necessidade de criarmos uma função da forma como temos acima. Esse método se chama "zip"

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zip(l1, l2))
    print(list(zip(l1, l2)))

Temos, também, um módulo do Python que se chama itertools e dentro dela um método chamado "zip_longest", donde ele faz a mesma coisa que o zip com uma única diferença. Em vez de pegar a menor lista, que nem o zip, ele pega a maior lista.

    from itertools import zip_longest

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zip(l1, l2))
    print(list(zip(l1, l2)))
    print(zip_longest(l1, l2))
    print(list(zip_longest(l1, l2)))
