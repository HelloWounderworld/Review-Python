# Aula 64 - Decoradores com parâmetros:
Vamos abordar com mais profundidade sobre funções decoradoras, syntax sugar, com técnicas mais avançadas.

Antes de comerçarmos a abordagem, vamos considerar o seguinte código

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    @decoradora
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)
    print(dez_mais_cinco)

No caso, o código acima, não tem muita novidade. Está sendo usado syntax sugar, @decoradora, para conseguirmos apontar as funções decoradores para as funções que queremos decorar, soma, e, por fim, usar.

No caso, o que queremos aprender aqui. Seria da uma forma de conseguirmos colocar parâmetros para as funções decoradoras. Bom, indo por partes, note que, no momento em que apontamos a função decoradora para alguma função que queremos decorar, ela já consta, ao compilarmos o código da seguinte forma 

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    @decoradora
    def soma(x, y):
        return x + y

Quando executamos somente esse trecho do código, conseguimos ver que o fato de ocorrer o apontamento, @decoradora, sobre a função que queremos decorar, soma, será exibido somente o print, Decoradora 1, donde mostra que a função soma, foi decorado, ou seja, ela foi retornado na forma com nome da função interna (inner function) definida, aninhada, dentro da função decoradora. Ou seja, a função "soma" -> func -> aninhada. É como se eu trocasse a função soma para a aninhada, de forma a nos permitir em definir se queremos fazer mais coisas ou não dentro da função aninhada.

Agora, para entendermos mais ainda a lógica de programação que está por trás dessa função decoradora, seria compilando o seguinte trecho do código

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    @decoradora
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)

No caso, vamos conseguir ver que, pelo fato de termos definido a variável e dentro dela chamar a função deocrada "soma", já ocorreu o processo definido dentro da função aninhada, visto que será printado, Aninhado, junto com o print Decoradora 1. Ou seja, significa que a função decorado, soma, foi executado, trocando de nome para a função aninhado, e foi retornado o seu resultado que está guardado pela variável "dez_mais_cinco", cujo o resultado seria exibido pelo print(dez_mais_cinco)

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    @decoradora
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)
    print(dez_mais_cinco)

Claro, se colocarmos, por exemplo, "res + 20" no "return res" irá retornar os dois valores que foram somados pela função decorada, soma, mais "20"

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res + 20
        return aninhada

    @decoradora
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)
    print(dez_mais_cinco)

Blz, mas onde está o assunto principal dessa seção, que é passar parâmetros para a função decoradora? Até agora, só entendemos a lógica de programação de como funciona a função decoradora quando se é apontado de forma básica.

Bom, a resposta para isso, seria que no momento em que realizarmos o apontamento, se fizermos o seguinte

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res + 20
        return aninhada

    @decoradora()
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)
    print(dez_mais_cinco)

Ou seja, colocamos "@decoradora()" em vez de "@decoradora". No caso, se colocarmos esse parênteses no apontamento, a lógica de programação mudará muito. O formato acima, sem passar nenhum parâmetro dentro de "@decoradora()" não irá funcionar.

Para entendermos melhor essa mudança, vamos tentar passar um parâmetro para a função decoradora da seguinte forma mais arcaia, mas que manterá o código funcionando

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    def arcaico(a, b, c):
        return decoradora

    @arcaico(1, 2, 3)
    def soma(x, y):
        return x + y

    dez_mais_cinco = soma(10, 5)
    print(dez_mais_cinco)

Vamos ver que no formato acima, o código irá voltar a funcionar exatamente como função decoradora, mas, desta vez, conseguindo passar algum parâmetro.

Bom, a forma arcaica que mostramos acima, meio que, na verdade, é exatamente assim que se faz para conseguirmos passar o parâmetro para as funções decoradas. Para deixarmos isso mais claro, bastaríamos realizar o seguinte

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    def arcaico(a, b, c):
        print(a, b, c)
        return decoradora

    @arcaico(1, 2, 3)
    def soma(x, y):
        return x + y

Ao executarmos o trecho do código acima, vamos ver que, irá exibir o print "1 2 3" e "Decoradora 1". Ou seja, que aconteceu aqui foi que o apontamento "@arcaico(1, 2, 3)", considerou os parâmetros que foi passado nele primeiro e, em seguida, decoramos a função "soma" pela função "decoradora", ou seja, é o momento em que criamos uma nova função aninhada recebendo como parâmetro a função "soma", pelo "func".

Basicamente, o que está acontecendo aqui é a mesma coisa que está acontecendo com a seguinte forma de execução

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    multiplica = decoradora(lambda x, y: x * y)

    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)

Ou seja, conseguimos já deixar definidos como será as tratativas para os parâmetros x e y, caso for passado algum valor que permita realizar a tal tratativa definida.

Ou seja, temos aqui duas formas de apontamento de funções decoradora, uma usando o lambda e outra usando a syntax sugar

    # Decoradores com parametros
    def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    @decoradora
    def soma(x ,y):
        return x + y

    multiplica = decoradora(lambda x, y: x * y)

    dez_mais_cinco = soma (10, 5)
    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)
    print(dez_mais_cinco)

No caso, a forma expressa acima, nos deixará mais claro que, de fato, a função "decoradora" é uma fábrica de funções, que bastando ser apontada para as funções que queremos decorar, ela irá fabricar uma nova função.

Agora, visto que podemos fabricar as funções, podemos, também, fabricar decoradores. Ou seja, podemos criar uma função de fabrica de decoradores da seguinte forma

    # Decoradores com parametros
    def fabrica_de_funcoes(func):
        print('Fabrica de funcoes 1')

        def aninhada(*args, **kwargs):
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada

    def fabrica_de_decoradores(a, b, c):
        retrun fabrica_de_funcoes

    @fabrica_de_decoradores(1, 2, 3)
    def soma(x ,y):
        return x + y

    multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

    dez_mais_cinco = soma (10, 5)
    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)
    print(dez_mais_cinco)

Bom, o formato acima, é uma forma de conseguirmos fabricar decoradores. Porém, não é uma forma usual.

Se prestarmos atenção, temos a fabrica_de_decoradores, que é o nosso primeiro escopo, em seguida, fabrica_de_funcoes, que é o nosso segundo escopo, e, por último, aninhada, que é o terceiro escopo. Ou seja, estamos trabalhando aqui com três escopos. Donde, não é necessário separarmos da forma acima. Podemos organizar, de forma didática, os três escopos da seguinte forma

    # Decoradores com parametros
    def fabrica_de_decoradores(a=None, b=None, c=None):
        def fabrica_de_funcoes(func):
            print('Fabrica de funcoes 1')

            def aninhada(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                return res
            return aninhada
        return fabrica_de_funcoes

    @fabrica_de_decoradores(1, 2, 3)
    def soma(x ,y):
        return x + y

    multiplica = fabrica_de_funcoes(lambda x, y: x * y)

    dez_mais_cinco = soma (10, 5)
    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)
    print(dez_mais_cinco)

Em linguagens matemáticas, pensa que a fábrica de decoradores é literalmente função iterada, aquelas funções que tem ordem de considerar os argumentos passados dentro dela, "f(x)(y)" donde "f: X -> Z" e "f(x): Y -> W", donde "x -> f(x)" e "y -> f(x)(y)".
