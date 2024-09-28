# Aula 20 - Formatação de strings com o método format:
Bom uma outra forma de formatar algo é utilizando o método format.

Lembra do que foi dito sobre tudo em python? Claro, tudo em python é um objeto. Logo, isso significa que para cada tipo de objeto em python, existem aquelas que se dispõe de métodos para serem aplicados para aquele objeto. No caso, em uma string, por exemplo, ao pegarmos uma string e concaternarmos com um ponto nela vc verá que terá inúmeros métodos disponíveis para ela

    formato = ''. // esse "." depois da string vazia, ao fizermos isso no arquivo .py, será mostrado os métodos que está disponível para ela.

No caso, um desses métodos que vamos utilizar é o método format

    a = 'A'
    b = 'B'
    c = 1.1
    formato = 'a={} b={} c={}'.format(a, b, c)

    print(formato)

No caso, quando aplicarmos o método format e dentro dela coloarmos as variáveis que definimos antes "a, b, c" bastaríamos chamar elas com as chaves "{}" dentro das strings que será chamado em ordem de esquerda para a direita, na ordem em que foi colocado as variaveis.

Podemos, também, definir isso, 'a={} b={} c={}', como uma variável e realizar as mesmas coisas que não terá nenhum problema

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'a={} b={} c={}'
    formato = string.format(a, b, c)

    print(formato)

Dentro dessas chaves que serão retornados cada coisa que foi atribuído para as variáveis a, b e c, podemos realizar as mesmas formatações que fizemos para f-strings

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'a={} b={} c={:.2f}'
    formato = string.format(a, b, c)

    print(formato)

Ou seja, podemos definir as quantidades de casas decimais que podem ser exibidas ou arredondadas.

Vimos que quando chamávamos apenas as chaves a ordem de exibição dos valores das variáveis, estavam de acordo com a ordem em que cada variável foi chamada no parâmetro. Mas podemos alterar essa ordem. E para isso, bastaria colocar índices em cada chave

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'a={0} b={1} c={2:.2f}'
    formato = string.format(a, b, c)

    print(formato)

Agora, mesmo chamando, por exemplo, a chave com o índice "{1}" antes de "a={0}", o que será exibido dentro dessa chave com o índice "{1}" será o valor atribuído na variável "b"

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'b={1} a={0} c={2:.2f}'
    formato = string.format(a, b, c)

    print(formato)

Podemos, também, chamar a variável quantas vezes quisermos com o índice definido

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'b={1} a={0} a={0} a={0} a={0} a={0} c={2:.2f}'
    formato = string.format(a, b, c)

    print(formato)

Algo que não era possível com a chave sem o índice de quando excedia da quantidade de variáveis que havía sido definido.

Agora, podemos, também, definir cada parâmetro dentro do format como uma variável. Isso permitirá que caso vc necessite de mudar a variável dentro do parâmetro, mas sem alterar o nome daquela variável que vc já chamou dentro da chave, será possível te dando mais flexibilidade

    a = 'A'
    b = 'B'
    c = 1.1
    string = 'b={nome2} a={nome1} a={nome1} a={nome1} a={nome1} a={nome1} c={nome3:.2f}'
    formato = string.format(
        nome1=a, 
        nome2=b,
        nome3=c
    )

    print(formato)

No caso, se vc quiser, por exemplo, mudar o valor do nome1, sem necessidade de alterar a posição da chamada dela dentro da string, não será necessário.
