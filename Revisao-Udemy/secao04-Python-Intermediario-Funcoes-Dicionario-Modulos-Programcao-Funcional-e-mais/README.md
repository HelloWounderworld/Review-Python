# Seção 4 - Python Intermediário - Funções, Dicionários, Módulos, Programação Funcional e +

## Aula 01 - O que vamos aprender nessa seção intermediária?:
Se vc chegou até aqui firme e forte, pode se considerar um nível um pouco acima do intermediário na linguagem Python!

Recomendamos que vc faça uma revisão do que vc aprendeu da seção anterior, pois daqui em diante, irei omitir certas tecnicalidades, esperando que a pessoa já entenda a msg por trás dessa omissão.

## Aula 02 - Introdução às funções Python - def define uma função:
Vamos aprender a definir funções em Python.

Até agora, temos uma função que já usamos várias vezes na linguagem Python, que é o print

    print('Varias')

isso é uma função no Python. Mas, uma coisa que não vimos até agora é a forma como criamos a função em Python.

Para criarmos uma função em Python, temos que utilizar a sintaxe "def". Por exemplo, se quisermos definir uma função print, com "P" maiúsculo, podemos

    def Print():
        print('Varias')

No caso, a função def, ela pode receber alguma parâmetro/argumento dentro dos parênteses

    def Print(a, b, c):

Além disso, como padrão, as funções Python elas retornam None, quando vc não usar nenhuma espécie de return para retornar algum valor.

Para executar a função depois de definida ela, terá que chamar pelo nome acrescentado pelo parênteses.

    def Print():
        print('Varias')

    Print()

Quando uma função têm parâmetros, por padrão, quando vc executar-las, precisa atribuir algum valor conforme à quantidade de parâmetros que estão sendo definidos

    def imprimir(a, b, c):
        print('Varias1')
        print('Varias2')
        print('Varias3')
        print('Varias4')

    imprimir() #Isso aqui não vai executar a função, pois essa função exige parâmetros.
    imprimir(1, 2, 3)

Obviamente, se uma função exige algum argumento, significa que podemos usa-la dentro dessa função

    def imprimir(a, b, c):
        print(a, b, c)

    imprimir() #Isso aqui não vai executar a função, pois essa função exige parâmetros.
    imprimir(1, 2, 3)

Assim, como podemos definir outras formas de função como segue

    def saudacao(nome):
        print(f'Olá {nome}!')

    saudacao('Me dá aqui Eduardo!!')
    saudacao('Leonardo')

Mas, sempre que definirmos alguma função com parâmetro é necessário que seja colocado algum parâmetro? A resposta para isso é não, pois na própria função em que definimos o parâmetro, podemos deixar um parâmetro padrão definido para caso não coloquemos algum parâmetro ao executarmos a função

    def saudacao(nome='Mumei'):
        print(f'Olá {nome}!')

    saudacao('Me dá aqui Eduardo!!')
    saudacao('Leonardo')
    saudacao()

## Aula 03 - Argumentos nomeados e argumentos posicionais (não nomeados) em funções:
Vamos falar de argumentos nomeados e não nomeados em Python. Bom, a idiea é bem simples, os nomeados tem nome e os não nomeados, não tem nome. E o argumento não nomeado é chamado de argumento posicional.

No caso, pegamos um exemplo

    def soma(x, y):
        #Definicao 
        print(x+y)

    # Não nomeado
    soma(1,2)
    soma(2,1)

    # Nomeado
    soma(x=1, y=2)
    soma(y=2, x=1)

Como podemos ver no exemplo acima, os argumentos nomeados são, quando estou executando alguma função que tenha parâmetros, eu tenho a alternativa de passar somente os valores ou tenho a alternativa de passar os valores junto com os parâmetros como acima, soma(y=2, x=1) ou soma(x=1, y=2). Independente de se os valores que foram passados junto com os argumentos estiveram em ordem ou não como foi definido nos parâmetros da função soma, os valores serão definidos para os respectivos parâmetros nomeados.

Obs: Se uma função tiver uma quantidade maior ou igual à três de parâmetros, caso vc nomear algum parâmetro que esteja entre os valores, menos do final, os valores adiantes precisam serem nomeados.

    def soma2(x, y, z):
        print(f'{x=} y={y} {z=}', '|', 'x+y+z= ', x+y+z)

    soma2(1,2,z=3)
    soma2(1,y=2,3) # isso vai dar errado
    soma2(1,y=2,z=3)

## Aula 04 - Valores padrão para parâmetros em funções Python + NoneType e None:
Já vimos um pouco sobre definir um valor padrão para os parâmetros das funções, caso nenhum valor, ao executar a função, não seja enviado.

Mas, vamos abordar mais um pouco sobreesse assunto para mostrar mais algumas peculiaridades.

No caso, vamos ver o seguinte exemplo

    def soma(x, y):
        print(x+y)

    soma(1,2)
    soma(3,5)
    soma(100,200)

Feito as execuções acima, vamos supor, agora, que queiramos refatorar o código. Ou seja, vou colocar mais um parâmetro nela. No caso, o "z"

    def soma(x, y, z):
        print(x+y+z)

    soma(1,2)
    soma(3,5)
    soma(100,200)

Do jeito como está acima, não vamos conseguir executar a função, estará faltando algum parâmetro.

Para resolver esse problema, podemos deixar definido um valor padrão para o parâmetro z, caso nenhum valor para z seja atribuído ao executar a tal função.

    def soma(x, y, z=0):
        print(x+y+z)

    soma(1,2)
    soma(3,5)
    soma(100,200)

Porém, a solução acima tem um problema. Pois, temos um valor padrão definido para o "z", porém esse valor padrão, 0, é considerado False na linguagem Python. Se por acaso eu quiser utilizar algum if/else e simplesmente colocar "if z", mesmo com o "z" tendo algum valor definido como 0, nunca irá cair dentro desse if

    def soma(x, y, z=0):
        if z:
            print(f'{x=} {y=} {z=}', x+y+z)
        else:
            print(f'{x=} {y=}', x+y)

    soma(1,2)
    soma(3,5)
    soma(100,200)
    soma(7,9,0)

A execução soma(7,9,0) nunca irá exibir o valor.

No caso, para solucionar isso, podemos usar o None definido no parâmetro "z" e daí no if colocquemos "if z is not None:"

    def soma(x, y, z=None):
        if z is not None:
            print(f'{x=} {y=} {z=}', x+y+z)
        else:
            print(f'{x=} {y=}', x+y)

    soma(1,2)
    soma(3,5)
    soma(100,200)
    soma(7,9,0)
    soma(y=9,z=0,x=7)

Assim, conseguimos contornar a situação do valor padrão "z" ser um false.

Obs: Se eu tiver uma quantidade de parâmetros maior ou igual à 2, se eu definir algum valor padrão para o parâmetro que não esteja na última posição do argumento de uma função, então os parâmetros adiante até o último precisa estar com algum valor padrão definido.

## Aula 05 - (Parte 1) Escopo de funções e módulos em Python + global:
Vamos abordar sobre escopo de funções e módulos da linguagem Python.

Basicamente, como foi visto no curso de JavaScript, o escopo é até onde um determinado função ou variável ela tem como influência nas suas ações. Na linguagem Python, esse conceito ainda continua o mesmo.

Exemplo, vamos ver a seguinte função abaixo

    def escopo():
        x = 1
        print(x)
    escopo()

Bom, lembra do que foi dito insistentemente até agora? Os códigos são executados de esquerda para à direita sendo lida de cima para baixo. No caso, o exemplo acima, não está acontecendo isso necessariamente, pois a execução padrão é feita primeira e no meio do processo ela volta a realizar a leitura novamente, pois estou executando a função "escopo()" depois de definido a tal função. No caso, depende da localidade onde é chamado.

Agora, abordando a ideia de escopo. No caso, vimos que a variável "x" acima, foi definido dentro da função "escopo". No caso, essa variável ela tem influência apenas dentro dessa função. Como prova disso, se tentarmos acessar a tal variável fora da função o código dá um erro

    def escopo():
        x = 1
        print(x)
    escopo()
    print(x)

Retornando pelo terminal que a variável "x" não está definida. Ou seja, esse "x" ela está definida somente dentro do escopo da função, e não fora dela.

Bom, uma forma de contornar esse problema seria definindo um valor "x" fora da função.

    x = 1
    def escopo():
        x = 1
        print(x)
    escopo()
    print(x)

Na situação acima, vem a seguinte pergunta. tanto o print que está fora da função e quanto o que está dentro da função escopo, ambos vão captar a variável externo? A resposta é sim!

Ou seja, no formato que está cima, se removermos a variável "x = 1" que está definio dentro da função, mesmo assim, o print que está residido nela, irá conseguir exibir o valor do "x" que está fora da função.

    x = 1
    def escopo():
        print(x)
    escopo()
    print(x)

Isso, novamente, tem haver com o escopo tbm. Ou seja, para a variável "x" que está definido fora do escopo da função "escopo", ela tem mais influência, até para as execuções internas das funções que estão sendo definido dentro desse escopo global onde a variável "x" está sendo definido.

Detalhe importante. Esse "x", ele precisa estar definido antes dessa função "escopo". Pois, se definirmos depois em que essa função foi definida e executada, não irá funcionar

    def escopo():
        print(x)
    escopo()
    x = 1

O formato acima, irá retornar um erro dizendo que o "x" não está definido.

Lembrando que na abordagem do escopo acima, definirmos as variáveis fora da função para usar dentro de uma função, é uma má prática e isso pode quebrar o seu código.

Vamos mostrar um outro exemplo que torna muito claro que, mesmo conseguindo acessar as variáveis do escopo externo, não podemos acessar as variáveis que estão definidos dentro dos escopos internos

    x = 1
    def escopo():
        def outra_funcao():
            y = 2
            print(x, y)
        outra_funcao()
        print(x)
    
    escopo()

No caso, o que está acontecendo acima, seria uma função definida dentro de uma outra função, e externamente, não conseguimos acessar a função, outra_funcao", definido dentro da função, escopo. No caso, para que consigamos executar a tal função, outra_funcao, precisamos que essa função seja executada dentro da função, escopo, pois fora dela é impossível ser acessado. A mesma lógica se aplica à variável "y" que está defindo dentro da função, outra_funcao.

Agora, outra abordagem interessante. No exemplo em que mostramos a variável "x" que está definido tanto fora quanto interno, precisamos deixar claro que esses dois "x" são diferentes. Ou seja, uma é um "x" que está definido no escopo global e outra é um "x" que está definido no escopo local. E a ordem de consideração será sempre de dentro para fora.

    x = 1
    def escopo():
        x = 10
        def outra_funcao():
            y = 2
            print(x, y)
        outra_funcao()
        print(x)
    
    print(x)
    escopo()

No caso, o que está acontecendo aqui é o seguinte. Os dois prints que estão sendo executados dentro das funções escopo e outra_funcao, ela considera a variável "x" que foi definido localmente, ou seja, "x = 10". Já o print que está sendo executado fora da função escopo, considera o "x" que foi definido globalmente, ou seja, "x = 1".

Agora, se executarmos o print depois de ter executado a função "escopo()"? Qual valor de "x" será executado?

    x = 1
    def escopo():
        x = 10
        def outra_funcao():
            y = 2
            print(x, y)
        outra_funcao()
        print(x)
    
    print(x)
    escopo()
    print(x)

A resposta é, continua sendo o "x" do escopo global.

Basicamente, como na teoria de categoria que explica o coneito de orientação ao objeto, as prioridades sempre serão de dentro para fora.

Agora, se quisermos manipular uma variável que foi definido fora de uma função dentro dela, precisamos dizer que essa variável é global

    x = 1
    def escopo():
        global x
        x = 10
        def outra_funcao():
            y = 2
            print(x, y)
        outra_funcao()
        print(x)
    
    print(x)
    escopo()
    print(x)

No caso, o print(x) que está sendo executado depois do "escopo()" qual valor ele irá exibir? A resposta é o valor de "x = 10". Ou seja, ao dizer "global x" dentro da função, escopo, estamos dizendo que a variável "x" que será definido dentro do mesmo escopo da função adiante, ela será considerada uma variável global.

## Aula 06 - (Parte 2) Escopo de funções e módulos em Python + global:

## Aula 07 - Retorno de valores das funções (return):

## Aula 08 - (Parte 1) *args para quantidade de argumentos não nomeados variáveis:

## Aula 09 - (Parte 2) *args para quantidade de argumentos não nomeados variáveis:

## Aula 10 - Exercícios com funções + Solução (prepare-se para pausar):

## Aula 11 - Higher Order Functions - Funções de primeira classe:

## Aula 12 - Termos técnicos: Higher Order Functions e First-Class Functions:

## Aula 13 - Closure e funções que retornam outras funções:

## Aula 14 - Exercício com funções:

## Aula 15 - Solução do exercício com funções:

## Aula 16 - Introdução ao tipo de dados dict - Dicionários em Python:

## Aula 17 - Manipulando chaves e valores em dicionários em Python:

## Aula 18 - (Parte 1) Métodos úteis nos dicionários Python (dict):

## Aula 19 - Shallow Copy vs Deep Copy em dados mutáveis Python:

## Aula 20 - (Parte 2) Métodos úteis nos dicionários Python (dict):

## Aula 21 - Exercício - sistema de perguntas e respostas com Python:

## Aula 22 - Solução do Exercício - sistema de perguntas e respostas com Python:

## Aula 23 - Introdução ao tipo set em Python (conjuntos):

## Aula 24 - Peculiaridades do tipo mutável set em Python:

## Aula 25 - Métodos úteis do tipo set em Python:

## Aula 26 - Operadores importantes para o tipo set (conjuntos):

## Aula 27 - Exemplo de uso do tipo set:

## Aula 28 - Exercício - Encontre o primeiro duplicado considerando a segunda ocorrência:

## Aula 29 - Solução - Encontre o primeiro duplicado considerando a segunda ocorrência:

## Aula 30 - Introdução à função lambda + list.sort e sorted:

## Aula 31 - Funções lambda complexas (para entendimento):

## Aula 32 - Empacotamento e desempacotamento de dicionários + *args e **kwargs:

## Aula 33 - Introdução à List comprehension em Python:

## Aula 34 - Mapeamento de dados em list comprehension (map):

## Aula 35 - Filtro de dados em list comprehension (filter):

## Aula 36 - List comprehension com mais de um for:

## Aula 37 - Mais detalhes sobre list comprehension:

## Aula 38 - Dictionary Comprehension e Set Comprehension:

## Aula 39 - isinstace() - para saber se objeto é de determinado tipo:

## Aula 40 - Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis:

## Aula 41 - dir, hasattr e getattr em Python:

## Aula 42 - Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores):

## Aula 43 - Generator expression, Iterables e Iterators em Python:

## Aula 44 - Introdução às Generator functions em Python:

## Aula 45 - yield from em generator functions:

## Aula 46 - (Parte 1) try e except para tratar exceções:

## Aula 47 - (Parte 2) try e except para tratar exceções:

## Aula 48 - try, except, else e finally + Built-in Exceptions:

## Aula 49 - raise - lançando exceções (erros):

## Aula 50 - Módulos - import, from, as e *:

## Aula 51 - Modularização - Entendendo os seus próprios módulos e sys.path no Python:

## Aula 52 - Como importar coisas do seu próprio módulo (ponto de vista do __main__):
