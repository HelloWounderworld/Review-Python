# Aula 34 - Mapeamento de dados em list comprehension (map):
Vamos aprender sobre mapeamento de dados. No caso, esse conceito existe até na programação funcional sobre mapeamento de dados e até chegamos a usar isso aqui no curso algumas vezes. Porém, a abordagem do conceito em si iremos realizar agora. No caso, vamos usar um exemplo abaixo

    produtos = [
        {'nome': 'p1', 'preco': 20, },
        {'nome': 'p2', 'preco': 10, },
        {'nome': 'p3', 'preco': 30, },
    ]

No caso, a partir da lista "produtos" acima, vamos mapear os preços desses produtos para uma outra nova lista, modificado os preços como segue

    novos_produtos = [
        produto
        for produto in produtos
    ]

    print(novos_produtos)

Só para começar a verificando se está funcionando como queremos.

Bom, visto que está tudo certo, então vamos, agora, partir para customização dos valores dos preços. No caso, como iremos fazer isso? Como iremos mudar os preços desses produtos? Bom, para isso iremos criar um novo objeto dentro dessa iteração com os parâmetros idênticos aos que temos em cada objeto indexado dentro da lista produtos. Para isso, iremos utilizar um dos métodos de criação de um objeto para conseguirmos realizar a tal alteração de preço

    novos_produtos = [
        {}
        for produto in produtos
    ]
    print(*novos_produtos, sep='\n')

Bom, se rodarmos o código como está acima, vamos criar um dicionário vazio conforme a quantidade de iterações que será feito da lista produtos. É dentro desse dicionário que queremos colocar os parâmetros e realizar as devidas alterações dos preços dos produtos. Logo, para isso realizamos o seguinte

    novos_produtos = [
        {'nome': produto['nome'], 'preco': produto['preco']}
        for produto in produtos
    ]

    print(*novos_produtos, sep='\n')

Bom, com a forma acima, vamos literalmente, realizar uma cópia da lista "produtos". Podemos realizar esse mesmo processo apenas desempacotando o objeto produto dentro de cada lista

    novos_produtos = [
        {**produto}
        for produto in produtos
    ]

    print(novos_produtos)

Bom, vamos lembrar que esse método de desempacotamento acima, não permite que as mesmas chaves sejam repetidas. Logo, não teríamos problema em repetir a mesma chave e nela definir algum valor diferente

    novos_produtos = [
        {**produto, 'preco': produto['preco'] * 2}
        for produto in produtos
    ]

    print(novos_produtos)

Bom, agora, vamos deixar mais interessante ainda as coisas. No caso, uma das finalidades interessantes do list comprehension seria em conseguirmos colocar algumas condicionais dentro do processo de modo que facilite a customização de uma lista. No caso, iremos implementar isso dentro da criação dessa lista novos_produtos

    novos_produtos = [
        {**produto, 'preco': produto['preco'] * 1.05}
        if produto['preco'] > 20 else {**produto}
        for produto in produtos
    ]

    print(*novos_produtos, sep='\n')

No caso, vemos que usamos uma condição ternária acima.
