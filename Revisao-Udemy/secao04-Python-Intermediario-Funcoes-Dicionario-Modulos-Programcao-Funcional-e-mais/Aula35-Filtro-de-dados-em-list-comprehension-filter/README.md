# Aula 35 - Filtro de dados em list comprehension (filter):
Vamos, agora, aprender a fazer a list comprehension usando o filtro.

Mas, antes de abordamos o assunto, vamos melhorar a nossa forma de exibição importando um módulo chamado "pprint", pretty print. Da seguinte forma

    import pprint

No caso, o uso desse módulo, dentro dela, tem um método chamado "pprint()" donde nos permite exibir o que queremos, como um print() usual. Porém, a vantagem é que conseguimos customizar a exibição da seguinte forma

    import pprint

    pprint.pprint(novos_produtos, sort_dicts=False, width=40)

Ou seja, podemos definir vários parâmetros que podem ser ou não ser consideradoso para conseguir realizar a devida exibição. Porém, como podemos perceber, ficar toda hora chamadno esse método com tamanho parâmetros toda hora em cada linha ficaria feio visualmente, o código. Logo, seria conveniente definirmos uma função onde, dentro dela, iremos definir a forma de exibição para sempre que quisermos exibir algo, bastando chamar a tal função que, dentro dela, estará definido todos os parâmetros de exibição que precisamos

    import pprint

    def p(v):
        pprint.pprint(v, sort_dicts=False, width=40)

Agora, vamos partir para a abordagem do filtro em list comprehension. No caso, vamos criar um list comprehension simples primeiro

    lista = [n for n in range(10)]
    p(lista)

Daí, vamos conseguir realizar o filtro usando o if, no caso, essa condicional virá depois do for, pois é uma condicional que definirá se um determinado elemento será incluído na lista ou não

    lista = [ n for n in range(10) if n < 5]
    p(lista)

Note que, só foi incluído os elementos que satisfez a condicional acima. No caso, isso é uma forma de realizar o filtro. Agora, vamos misturar, com o filtro e o mapeamento, ou seja, as condicionais antes do for e depois do for

    produtos = [
        {'nome': 'p1', 'preco': 20, },
        {'nome': 'p2', 'preco': 10, },
        {'nome': 'p3', 'preco': 30, },
    ]

    novos_produtos = [
        {**produto, 'preco': produto['preco']}
        if produto['preco'] > 20 else {**produto}
        for produto in produtos
        if produto['preco'] > 10
    ]

    p(novos_produtos)

No caso, a interpretação acima, do if depois do for, é inclua o produto dentro da lista, se o preço dele for acima do 10.

Bom, como podemos ver a lógica condicional tanto do mapeamento quanto do filtro acima, não está tão legal. Obviamente, caso realizarmos o uso delas iremos colocar uma lógica mais conveniente. Porém, o importante aqui é entender a diferença entre o conceito de mapeamento e filtro. Enquanto que o mapeamento ela serve para vc colocar as condicionais sem selecionar o que será ou não incluso na lista, de modo que, sempre no final o tamanho da lista seja o mesmo que a quantidade de iterações realizadas por for, o filtro vc usa as condicionais e que não necessariamente, no final, o tamanho da lista esteja no mesmo tamanho que a quantidade de iterações que foi feito pelo for. Claro, podemos combinar os dois, como podemos ver acima, mas recomendamos o leitor entender direitinho o conceito de mapeamento e filtro para manusear as condicionais de forma mais flexível e que faça sentido.