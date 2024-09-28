# Aula 38 - Dictionary Comprehension e Set Comprehension:
Bom, como podemos imaginar, se existe list comprehension, então existe sim dictionary comprehension e set comprehension e vamos abordar sobre tais conteúdos nessa aula.

- Dictionary Comprehension:

    Vamos considerar o seguinte dicionário

        produto = {
            'nome': 'Caneta Azul',
            'preco': 2.5,
            'categoria': 'Escritório'
        }

    Como se aplica o conceito de comprehension dentro do dicionário? Bom, a lógica é a mesma que foi abordado para list comprehension.

    Logo, fazemos o seguinte, lembra que para o dicionário podemos fazer um for que pega tanto a chave quanto o valor dessa chave?

        novos_produtos = {
            chave: valor
            for chave, valor in produto.items()
        }

        p(novos_produtos)

    Importamos o módulo pprint.

    Bom, a mesma coisa podemos realizar para criar uma nova tupla

        tupla_produto = (
            (chave, produto)
            for chave, produto in produto.items()
        )

        p(tuple(tupla_produto))

    Claro, que se temos como fazer o dictionary comprehension, podemos, também, realizar os devidos mapeamentos e filtros. Por exemplo, se quisermos fazer com que todos os valores de strings sejam maiúculas, como no meio dos valores existe float, então precisaríamos colocar alguma condicional para possibilitar isso

        novos_produtos = {
            chave: valor.upper()
            if isinstance(valor, str) else valor
            for chave, valor in produto.items()
        }

        p(novos_produtos)

    Lembrando que o par if/else para mapeamento é necessário.

    No uso so isinstance() acima, podemos colocar uma condição em forma de tupla para ter mais possibilidades de análise booleana, pois viraria uma lógica de "ou". São elas

        novos_produtos = {
            chave: valor
            if isinstance(valor, (int, float)) else valor.upper()
            for chave, valor in produto.items()
        }

        p(novos_produtos)

    Podemos, também, como previsto, realizar filtros acima disso para selecionarmos os tipos de valores que podemos colocar dentro do dicionário

        novos_produtos = {
            chave: valor
            if isinstance(valor, (int, float)) else valor.upper()
            for chave, valor in produto.items()
            if chave == 'categoria'
        }

        p(novos_produtos)

    Lembrando que, em filtros, usamos somente o if, não podemos usar else.

    Claro que, visto list comprehension e dictionary comprehension, podemos misturar tbm. Ou seja, a partir de um dicionário criar um list comprehension e vice-versa.

        lista = [
            ('nome', 'Leonardo'),
            ('altura', 1.84),
            ('profissao', 'Engenheiro de Sistema'),
            ('formacao', 'Matemática pura')
        ]

        dc = {
            chave: valor
            for chave, valor in lista
        }

        p(dc)

    Claro, a forma acima nos permite customizar a criação da lista.

    Caso queira realizar a criação do dicionário acima sem realizar nenhuma personalização, então bastaria realizar o seguinte

        p(dict(lista))

- Set Comprehension:

    Aqui é bem mais simples do que dictionary e list comprehension. No caso, bastaria realizar o seguinte

        s1 = {i for i in range(10)}
        p(s1)
        p(set(range(10)))

    Claro, considerando as características de um conjunto.

Seguir o link para estudo com mais profundidade

    https://pyneng.readthedocs.io/en/latest/book/08_python_basic_examples/x_comprehensions.html
    https://towardsdatascience.com/the-use-of-list-dictionary-and-set-comprehensions-to-shorten-your-code-66e6dfeaae13
