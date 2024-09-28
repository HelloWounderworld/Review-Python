# Aula 73 - map, partial, GeneratorType e esgotamento de Iterators:
Vamos aprender sobre três funções que sempre estão juntos: map, filter e reduce.

Nessa aula, iremos ver sobre o map.

Como começo, colocar o seguinte código

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

Daí, vamos chamar a função "print_iter" que definimos acima

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    print_iter(produtos)

Bom, nada de surpresa, pois apenas listamos o que foi computado dentro da lista produtos.

Se quisermos apenas expandir o dicionário, podemos usar o list comprehension, como já chegamos a aprender

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    novos_produtos = [
        {**p} for p in produtos
    ]

    print_iter(produtos)
    print_iter(novos_produtos)

Bom, até então, nada mudou. No caso, se quisermos alterar o valor dos preços, podemos apenas realizar o seguinte

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    novos_produtos = [
        {**p, 'preco': 123} for p in produtos
    ]

    print_iter(produtos)
    print_iter(novos_produtos)

No caso, alteramos o preco dos produtos, todas elas, no valor de 123.

No caso, podemos otimizar esse processo definindo uma função

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    novos_produtos = [
        {**p, 
            'preco': aumentar_porcentagem(p['preco'], 1.1)} 
        for p in produtos
    ]

    print_iter(produtos)
    print_iter(novos_produtos)

Existe um método em Python, dentro do módulo functools, chamado partial, cuja a funcionalidade dela é igual ao clousure. Basicamente, o método partial é um método que recebe uma função e um dos parâmetros que vai na função para depois, quando passado o último parâmetro a função é executado... Lembra do que estudamos sobre clousure passando os parâmetros? Sim, basicamente, existe o método partial que faz isso.

    from functools import partial

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    novos_produtos = [
        {**p, 
            'preco': aumentar_dez_porcento(p['preco'])} 
        for p in produtos
    ]

    print_iter(produtos)
    print_iter(novos_produtos)

É literalmente o que se faz em uma função clousure que dá para passar os parâmetros.

Assim, finalmente, podemos falar sobre map, que é um método nativo do Python.

    from functools import partial

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = map(
        muda_preco_de_produto,
        produtos
    )

    print_iter(produtos)
    print_iter(novos_produtos)

Para usar o map, basicamente, ela precisa de uma outra função. Donde, essa outra função será o que irá determinar a tarefa que vc quer realizar. No caso, do exemplo acima, vemos que o map, dentro dela, chamamos a função "muda_preco_de_produto" e o map iterou aplicando essa função para cada elemento da lista produtos.

No caso, podemos ver que se dermos um print simples sobre a lista "novos_produtos", podemos ver que ela irá nos retornar um objeto de uma classe e não a lista. Além disso, podemos analisar se o map ele é um iterável e/ou iterador.

    from functools import partial

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = map(
        muda_preco_de_produto,
        produtos
    )

    print_iter(produtos)
    print_iter(novos_produtos)

    print(novos_produtos)
    print(hasattr(novos_produtos, '__iter__')) #iterável
    print(hasattr(novos_produtos, '__next__')) #iterador

Ao rodarmos o código acima, conseguimos ver que ela é iterável e um iterador. Além disso, podemos ver se ela é um generator tbm. No caso, bastaria usar o método GeneratorType que está dentro do módulo types

    from functools import partial
    from types import GeneratorType

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = map(
        muda_preco_de_produto,
        produtos
    )

    print_iter(produtos)
    print_iter(novos_produtos)

    print(novos_produtos)
    print(hasattr(novos_produtos, '__iter__')) #iterável
    print(hasattr(novos_produtos, '__next__')) #iterador
    print(isinstance(novos_produtos, GeneratorType))

Vamos ver que irá retornar um "False", o que indica que ela o map não é um generator.

Um outr detalhe interessante, seria que se tentarmos printar usando o list, print(list(novos_produtos)), vamos ver que a lista estará vazia

    from functools import partial
    from types import GeneratorType

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = map(
        muda_preco_de_produto,
        produtos
    )

    print_iter(produtos)
    print_iter(novos_produtos)

    print(novos_produtos)
    print(hasattr(novos_produtos, '__iter__')) #iterável
    print(hasattr(novos_produtos, '__next__')) #iterador
    print(isinstance(novos_produtos, GeneratorType))
    print(list(novos_produtos))

No caso, isso se deve pelo fato de que o iterador ele é esgotado. Ou seja, uma vez usado um iterator os dados não são mais armazenados. Então, se quisermos continuar usando a mesma lista que foi modificada para outras finalidades tbm, bastaria realizar o seguinte

    from functools import partial
    from types import GeneratorType

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = list(map(
        muda_preco_de_produto,
        produtos
    ))

    print_iter(produtos)
    print_iter(novos_produtos)

    print(novos_produtos)
    print(hasattr(novos_produtos, '__iter__')) #iterável
    print(hasattr(novos_produtos, '__next__')) #iterador
    print(isinstance(novos_produtos, GeneratorType))
    print(list(novos_produtos))

Ou seja, usar o map dentro do método list do Python. Assim, podemos ficar reutilizando a nova lista onde for necessário.

Bom, entendido o conceito de map, claro que, dentro dela, podemos usar outras funções, como a função lambda

    from functools import partial
    from types import GeneratorType

    def print_iter(iterator):
        print(*list(iterator), sep='\n')
        print()

    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90}
    ]

    def aumentar_porcentagem(valor, porcentagem):
        return round(valor * porcentagem, 2)

    aumentar_dez_porcento = partial(
        aumentar_porcentagem,
        porcentagem=1.1
    )

    def muda_preco_de_produto(produto):
        return {
            **produto,
            'preco': aumentar_dez_porcento(
                produto['preco']
            )
        }

    novos_produtos = list(map(
        muda_preco_de_produto,
        produtos
    ))

    print_iter(produtos)
    print_iter(novos_produtos)

    print(novos_produtos)
    print(hasattr(novos_produtos, '__iter__')) #iterável
    print(hasattr(novos_produtos, '__next__')) #iterador
    print(isinstance(novos_produtos, GeneratorType))
    print(list(novos_produtos))

    print(
        list(
            map(
                lambda x: x*3
                [1, 2, 3, 4]
            )
        )
    )

No caso, a função lambda acima serve para triplicar os valores dentro da lista [1, 2, 3, 4].
