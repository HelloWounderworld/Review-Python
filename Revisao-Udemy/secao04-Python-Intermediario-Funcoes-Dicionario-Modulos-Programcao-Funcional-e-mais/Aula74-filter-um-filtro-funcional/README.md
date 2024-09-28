# Aula 74 - filter é um filtro funcional:
Basicamente, o filter, ele serve para conseguirmos filtrar os produtos.

Por começo, vamos usar o seguinte

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()


    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    print_iter(produtos)

Vamos ilustrar um exemplo sem o filter para entendermos como ela terá um papel fundamental para o filtro

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()


    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    novos_produtos = [
        p for p in produtos
        if p['preco'] > 10
    ]

    print_iter(produtos)
    print(novos_produtos)

No exemplo acima, sem o uso do filter, usamos a condicional "if" para apenas listarmos os produtos com o preço estritamente maior que 10.

Agora, como faremos isso usando o filter? Basicamente, iremos realizar o seguinte

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()


    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    novos_produtos = filter(
        lambda p: p['preco'] > 10,
        produtos
    )

    print_iter(produtos)
    print_iter(novos_produtos)

Claro, no uso do filter acima, colocamos uma função lambda, mas podemos colocar outras funções como fizemos quando usamos o map.
