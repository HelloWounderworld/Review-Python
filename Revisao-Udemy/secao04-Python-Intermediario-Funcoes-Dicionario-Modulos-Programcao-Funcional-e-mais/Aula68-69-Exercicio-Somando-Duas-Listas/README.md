# Aula 68 e 69 - Exercícios e Solução - somando duas listas:
Seguir o enunciado

    """
    Considerando duas listas de inteiros ou floats (lista A e lista B)
    Some os valores nas listas retornando uma nova lista com os valores somados:
    Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
    menor.
    Exemplo:
    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
    =================== resultado
    lista_soma  = [2, 4, 6, 8]
    """
    lista_a = [10, 2, 3, 40, 5, 6, 7]
    lista_b = [1, 2, 3, 4]
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)

    # lista_soma = []
    # for i in range(len(lista_b)):
    #     lista_soma.append(lista_a[i] + lista_b[i])
    # print(lista_soma)

    # lista_soma = []
    # for i, _ in enumerate(lista_b):
    #     lista_soma.append(lista_a[i] + lista_b[i])
    # print(lista_soma)

No exercício anterior, fizemos a soma de duas listas usando várias soluções diferentes.

Uma delas foi usando zip para unir duas listas e utilizar list comprehension para fazer a conta:

    lista_a = [10, 2, 3, 4, 5]
    lista_b = [12, 2, 3, 6, 50, 60, 70]
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)  # Saída: [22, 4, 6, 10, 55]

O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

A ideia é a mesma, veja:

    from itertools import zip_longest
    
    lista_a = [10, 2, 3, 4, 5]
    lista_b = [12, 2, 3, 6, 50, 60, 70]
    lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
    print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.
