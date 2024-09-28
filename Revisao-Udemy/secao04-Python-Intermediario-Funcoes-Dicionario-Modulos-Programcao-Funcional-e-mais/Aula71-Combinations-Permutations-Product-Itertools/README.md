# Aula 71 - Combinations, Permutations e Product - Itertools:
Vamos ver como utilizar as ferramentas matemáticas de contagem básica que aprendemos no ensino médio.

Bom, eu tenho várias referências de livros que a pessoa poderia aprender sobre Análise Combinatória, que é um ramo extremamente importante da matemática, principalmente, quando se trata de aplicar tais conhecimentos no mundo da programação, donde, a grosso modo, é aplicado muito conceito de matemática discreta. Pois bem, deixarei como referência dois livros uma da SBM, Sociedade Brasileira Matemática em que o IMPA, o maior instituto de pesquisa em matemática do Brasil, costuma fazer parceria para publicar os livros de mais diversos pesquisadores extremamente influentes da matemática Brasileira e outra, um livro que eu achei interessante e que encontrei por um acaso:

- Análise Combinatória e Probabilidade com as soluções dos exercícios - Augusto César Morgado, João Bosco Pitombeira de Carvalho, Paulo Cezar Pinto Carvalho, Pedro Fernandez.

- Fundamentos Matemáticos para a Ciência da Computação, Matemática Discreta e suas Aplicações, Sétima Edição - Judith L. Gersting - Capítulo 4.

Bom, por começo, considere as seguintes listas

    pessoas = [
        'João', 'Joana', 'Luiz', 'Letícia'
    ]
    camisetas = [
        ['preta', 'branca']
    ]

- Combinação:

    Daí, suponhamos que queiramos verificar quantas combinações diferentes podemos realizar na lista "pessoas" com grupo de 2. Lembrando, se tratando de combinações, a ordem não importa. Ou seja, consideramos ('João', 'Joana') = ('Joana', 'João'). Não é um produto cartesiano que veirifica as permutações.

    No caso, entendido a finalidade do que queremos, já existe um módulo na linguagem Python que possibilita realizar a tal combinação sem a necessidade de termos que criar algum algoritmo à respeito (se bem que eu recomendo, pelo menos, uma vez na vida a pessoa ter tal experiência). Então, seguimos da seguinte forma

        from itertools import combinations

        pessoas = [
            'João', 'Joana', 'Luiz', 'Letícia'
        ]
        camisetas = [
            ['preta', 'branca']
        ]

        print(combinations(pessoas, 2))
        print(list(combinations(pessoas, 2)))
        print(*list(combinations(pessoas, 2)),sep='\n')

    Importante dizer que o método "combinations" é um iterador, então vamos precisar usar alguma iteração para podermos exibir todas as combinações que pode ser feita ou usar o método "list" para exibir logo em lista mesmo.

    Bom, para facilitar mais ainda a visualização vamos criar uma função, de forma que não tenhamos necessidade de ter que ficar toda hora chamando o método "combinations"

        from itertools import combinations

        def print_iter(lista, num):
            print(*list(combinations(lista, num)), sep='\n')
            print()

        pessoas = [
            'João', 'Joana', 'Luiz', 'Letícia'
        ]
        camisetas = [
            ['preta', 'branca']
        ]

        print_iter(pessoas, 0)
        print_iter(pessoas, 1)
        print_iter(pessoas, 2)
        print_iter(pessoas, 3)
        print_iter(pessoas, 4)
        print_iter(pessoas, 5)

    Note que, para a combinação de 5 pessoas, como não é possível ser feito, simplesmente, foi retornado um null.

- Permutação:

    Vamos, agora, verificar sobre as permutações. No caso, a permutação, desta vez, considera sim o conceito de pares ordenados, ('João', 'Joana') $'\diff'$ ('Joana', 'João'). No caso, vamos importar o método "permutations" e nela colocarmos a ordem

        from itertools import combinations, permutations

        def print_iter(lista, nume):
            print(*list(combinations(lista, nume)), sep='\n')
            print()

        def print_permu(lista, nume):
            print(*list(permutations(lista, nume)), sep='\n')
            print()

        pessoas = [
            'João', 'Joana', 'Luiz', 'Letícia'
        ]
        camisetas = [
            ['preta', 'branca']
        ]

        print_iter(pessoas, 0)
        print_iter(pessoas, 1)
        print_iter(pessoas, 2)
        print_iter(pessoas, 3)
        print_iter(pessoas, 4)
        print_iter(pessoas, 5)

        print_permu(pessoas, 0)
        print_permu(pessoas, 1)
        print_permu(pessoas, 2)
        print_permu(pessoas, 3)
        print_permu(pessoas, 4)
        print_permu(pessoas, 5)

- Produto:

    O produto seria em econtrar várias formas de combinações. A definição segue do produto cartesiano. No caso, vamos colocar mais uma lista dentro da lista "camisetas"

        from itertools import combinations, permutations, product

        def print_iter(lista, nume):
            print(*list(combinations(lista, nume)), sep='\n')
            print()

        def print_permu(lista, nume):
            print(*list(permutations(lista, nume)), sep='\n')
            print()

        def print_prod(lista):
            print(*list(product(*lista)), sep='\n')
            print()

        pessoas = [
            'João', 'Joana', 'Luiz', 'Letícia'
        ]
        camisetas = [
            ['preta', 'branca'],
            ['p', 'm', 'g'],
            ['masculino', 'feminino', 'unisex'],
            ['algodão', 'poliester']
        ]

        print_iter(pessoas, 0)
        print_iter(pessoas, 1)
        print_iter(pessoas, 2)
        print_iter(pessoas, 3)
        print_iter(pessoas, 4)
        print_iter(pessoas, 5)

        print_permu(pessoas, 0)
        print_permu(pessoas, 1)
        print_permu(pessoas, 2)
        print_permu(pessoas, 3)
        print_permu(pessoas, 4)
        print_permu(pessoas, 5)

        print_prod(camisetas)

    Ou seja, conforme vai aumentando o número de sub-listas dentro da lista camisetas, o número de combinações vai aumentando exponencialmente.
