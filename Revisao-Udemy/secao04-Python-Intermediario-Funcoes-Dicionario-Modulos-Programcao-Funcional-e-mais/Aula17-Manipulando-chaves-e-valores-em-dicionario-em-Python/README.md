# Aula 17 - Manipulando chaves e valores em dicionários em Python:
Vamos aprender a manipular mais ainda sobre chaves, a fim de entendermos melhor sobre o conceito de dicionário.

No caso, na aula anterior, vimos um caso estático. Logo, iremos, agora, abordar o dicionario no seu uso dinâmico. Então, começamos a definir um dicionario vazio

    pessoa = {}

Assim, suponhamos que depois de definido essa variável ocorreram inúmeros processos à frente e, no meio delas, tivemos que realizar algumas modificações dentro desse dicionário, inicialmente vazia. No caso, para conseguirmos criar um elemento dentro desse dicionário e atribuirmos algum valor dentro desse dicioário, precisamos realizar o seguinte

    pessoa['nome'] = 'Leonardo TT'

Conseguimos acessar o elemento definido desse dicionario de forma usual como vimos na última aula

    print(pessoa)
    print(pessoa['nome'])

Além disso, se tentarmos acessar algum elemento inexistente dentro desse dicionario, será exibido um erro.

Bom, a lógica é bastante similar à lista, quando tentamos acessar um índice não definido dentro dela

    lista = []

    print(lista[0])

O código acima exibirá um erro.

Os elementos que definimos no dicionários chamam-se chaves. Elas podem ser definidas manualmente, como fizemos até agora, porém podemos definí-la de forma dinâmica, usando a iteração "for"

    pessoa = {}
    chave = 'nome'

    pessoa[chave] = 'Leonardo TT'

    #print(pessoa['nome'])
    print(pessoa[chave])

Bom, acima, ainda, não usamos a iteração "for", porém já a sua forma de uso está sendo dinâmico, pois ao alteramos o valor de string da variável "chave" para algum outro valor a compilação acima não irá gerar algum erro

    pessoa = {}
    chave = 'nome_completo'

    pessoa[chave] = 'Leonardo TT'

    #print(pessoa['nome'])
    print(pessoa[chave])

Não irá gerar nenhum erro acima, pois estamos usando a variável "chave" para conseguirmos consultar as chaves que foram definidas dentro do dicionário e esse processo por si só já é um processo dinâmico.

Podemos, também, apagar alguma chave que definimos dentro de um dicionário. Bastaria usar a sintaxe "del" da seguinte forma

    pessoa = {}
    chave = 'nome_completo'

    pessoa[chave] = 'Leonardo TT'
    pessoa['sobrenome'] = 'Turing'

    #print(pessoa['nome'])
    print(pessoa)
    print(pessoa[chave])

    del pessoa['sobrenome']

    print(pessoa)
    print(pessoa[chave])

Bom, mudando a variável "chave" acima de "nome_completo" para "nome" e, suponhamos que, até então, o acesso à essa chave estava sendo feito de modo manual e, não, dinâmico, como seguinte

    pessoa = {}
    chave = 'nome'

    pessoa[chave] = 'Leonardo TT'
    pessoa['sobrenome'] = 'Turing'

    print(pessoa['nome_completo'])
    
    print('Aqui não vai executar')

No caso, na parte do código, print('Aqui não vai executar'), não será executado. Isso porque, quando eu estiver tentando acessar algum elemento inexistente dentro do dicionário "pessoa", o processo ele para. Claramente, isso é um cenário ruim dentro de um código, pois existem inúmeras situações em que não queremos que o código ele, simplesmente, pare no meio do processo e dê continuidade até o final, pelo menos. A solução para esses cenários nas outras linguagens de programação seria usar o "try/catch", pois nem o "if" escapa disso

    pessoa = {}
    chave = 'nome'

    pessoa[chave] = 'Leonardo TT'
    pessoa['sobrenome'] = 'Turing'

    if pessoa['nome_completo']:
        print('Existe')
    
    print('Aqui não vai executar')

Entretanto, na linguagem Python, não existe "try/catch". Logo, para conseguirmos contornar esse tipo de problema de modo que o código continue sendo compilado, mesmo que aconteça algum erro no meio do processo, seria em usarmos o seguinte ".get()" como segue

    pessoa = {}
    chave = 'nome'

    pessoa[chave] = 'Leonardo TT'
    pessoa['sobrenome'] = 'Turing'

    if pessoa.get('nome_completo'):
        print('Existe')
    
    print('Aqui não vai executar')

Com o uso do ".get()", mesmo que a chave que estamos procurando não exista dentro do dicionário, ele não para o processo de compilação no meio processo. No caso, esse método ".get()" que estamos usando, quando ele vê que a chave não existe, por padrão, ele retorna "None", cujo o booleano é "False" em Python. Claro, podemos sim definir o que devolver caso a chave procurada não se encontra

    pessoa = {}
    chave = 'nome'

    pessoa[chave] = 'Leonardo TT'
    pessoa['sobrenome'] = 'Turing'

    print(pessoa.get('nome_completo', 'Não existe'))

    if pessoa.get('nome_completo'):
        print('Existe')
    
    print('Aqui não vai executar')