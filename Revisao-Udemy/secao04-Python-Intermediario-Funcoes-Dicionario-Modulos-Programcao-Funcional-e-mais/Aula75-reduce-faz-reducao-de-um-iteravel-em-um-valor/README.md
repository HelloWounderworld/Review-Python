# Aula 75 - reduce - faz a redução de um iterável em um valor:
Basicamente, o reduce, ela serve para realizar uma redução de um valor em um único valor.

Bom, o método reduce ela não é um método nativo do Python. Ela é um método do módulo functools. 

Por começo vamos realizar o seguinte

    from functools import reduce

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

Agora, para entendermos o conceito do reduce, vamos fazer o seguinte. Iremos mostrar um exemplo que não usa o reduce mas que serve para entender a tal ferramenta

    from functools import reduce

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    total = 0
    for p in produtos:
        total += p['preco']

    print(total)

Bom, no exemplo acima, usamos o for para acumular o total de somas dos produtos. Um tipo de função que criamos acima usando o "for" se chama acumulador. Basicamente, a função reduce precisa tbm de um acumulador para conseguirmos realizar o uso dela. Uma forma acima, podemos reduzir tbm usando o método "sum"

    from functools import reduce

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    print(sum(p['preco'] for p in produtos))

Bom, com o reduce temos que realizar o seguinte

    from functools import reduce

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    def funcao_do_reduce(acumulador, produto):
        print(acumulador)
        print(produto)
        print()
        return 1

    total = reduce(
        funcao_do_reduce,
        produtos,
        0
    )

No caso, dentro do reduce(funcao, lista, valor_inicial), vc coloca tais parâmetros e a forma de execução se parece com o filter e map. Podemos usar o método reduce sem o valor_inicial, mas não recomendamos realizar tal tipo de uso. Se usarmos, na situação acima, o método reduce sem o parâmetro "valor_inicial", será considerado como valor inicial o objeto inteiro.

No exemplo do uso do reduce acima, basicamente, ao rodarmos o código, vamos ver que o que está sendo retornado, "return 1", indica o valor do acumulador. Podemos ver que no início, o print(acumulador), retorna 0, mas, depois, adiante, ela retorna 1. Ou seja, visto que o valor_inicial foi 0, ela está sendo inteligente o suficiente para conseguirmos considerar que o acumulador ela é da natureza numérica.

Visto que isso está acontecendo, agora, podemos realizar o acumulo da soma total dos precos

    from functools import reduce

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    def funcao_do_reduce(acumulador, produto):
        print(acumulador)
        print(produto)
        print()
        return acumulador + produto['preco']

    total = reduce(
        funcao_do_reduce,
        produtos,
        0
    )

    print('Total é', total)

Seguir link para leitura sobre map, filter e reduce

    https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce

    https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
