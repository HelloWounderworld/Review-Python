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
Vamos abordar mais sobre escopo.

Bom, existem dois tipos de escopo, global e local:

- Escopo global: É o escopo onde todo o código é alcançavel.

- Escopo local: É o escopo onde apenas nomes do mesmo local podem ser alcançados.

Bom, um exemplo legal, que mostra a ideia de que as ordem de priorização vai de escopo local em direção ao escopo externo está na seguinte função

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            x = 11
            y = 2
            print(x,y)
        outra_funcao()
    
    escopo()

Ao executarmos a função acima, será printado, pelo print(x,y), o valor "11 2". Mas, agora, se comentarmos o "x = 11", qual valor de "x" será considerado?

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            #x = 11
            y = 2
            print(x,y)
        outra_funcao()
    
    escopo()

Será considerado o valor do "x" mais próximo que temos, que é o "x = 10", então será printado "10 2". O mesmo, vale se comentarmos "x = 10" com "x = 11" comentado, será considerado "x" mais próximo que temos que é o "x = 1". Esse comportamento se parece muito com a teoria de categoria quando vc consegue concluir as propriedades de uma categoria considerando apenas a sua sub-categoria. No caso, visto essa ideia em questão, se fizermos um experimento análogo com "y", no sentido de em vez de definirmos os "y"'s externamento, executamos print(y) fora do escopo onde o "y" está definido?

    x = 1

    def escopo():
        x = 10
        def outra_funcao():
            #x = 11
            y = 2
            print(x,y)
        outra_funcao()
        print(y)
    
    print(y)
    escopo()

No caso, como a prioridade da ordem é de dentro para fora, então o print(y) executado fora do escopo de onde o "y" está definido nos retornará um erro dizendo que não temos a variável "y" definido.

Leitura:

    https://phylos.net/2021-06-01/python-escopos-e-namespaces
    https://www.interviewcake.com/concept/java/call-stack#:~:text=The%20call%20stack%20is%20what,dice%20and%20printed%20the%20sum.

## Aula 07 - Retorno de valores das funções (return):
O retorno das funções, sempre que executada, ela retorna um determinado valor. Por padrão, as funções executadas retornam o "None", como podemos ver abaixo

    variavel = print("Leonardo")
    print(variavel)

No caso, a função "print" foi criado, pelo desenvolvedores python, para que ele, sempre que chamado, exibisse a msg que foi colocado dentro dela, não importa se foi tentado atribuir ela dentro de uma variável. O mesmo vale quando definimos uma função personalizado usando "def"

    def soma(x,y):
        print(x+y)

    variavel = soma(1,2)
    print(variavel)

Mas, agora, suponhamos que tal valor exibido pelo "x+y" queremos que tal valor seja atribuído para à variável "random". No caso, para isso, teremos que utilizar o "return" como segue

    def soma(x,y):
        return x+y

    random = soma(1,2)
    print(random)

Ou seja, a sintaxe "return", como o nome disse, ele retorna algum valor. E isso só pode ser executado dentro da função e que é uma sintaxe que serve para parar a execução de uma função. Ou seja, podemos criar uma função, donde combinado com condicionais, exista um conjunto de return. Quando acionado o return dentro de uma função, mesmo havendo outros códigos posteriores, ela não será mais executada. A função para exatamente nela.

## Aula 08 - (Parte 1) e (Parte 2) *args para quantidade de argumentos não nomeados variáveis:
Agora, uma pergunta. Note que, a função print() podemos colocar quantos argumentos finitos que quisermos que ela é exibida no console ao ser executada

    print(1)
    print(1,2,3)
    print(1,2,3,4,5,6,7)

Entretanto, em uma função personalizada, como soma(x,y), temos um limite de quantidade de argumentos que podemos colocar, donde, excedido isso, não será possível compilar a função

    def soma(x,y):
        return x + y

Mas aí, vem a pergunta, existe alguma forma de conseguirmos dinamizar isso para as funções personalizadas como no print()?

A resposta é sim. Vamos usar a sintaxe "*args", como podemos ver no exemplo abaixo

    x, y, *resto = 1, 2, 3, 4, 5, 6, 7
    print(x,y,resto)

Podemos realizar isso em funções personalizada tbm, como segue

    def soma(*args):
        print(args, type(args))

    soma(1,2,3,4,5,6,7)

Vamos ver que o "print(args)" devolve os argumentos que passamos em soma(1,2,3,4,5,6,7) na forma de tupla. Claro que podemos alterar essa tupla para uma lista como segue

    def soma(*args):
        args = list(args)
        print(args, type(args))

    soma(1,2,3,4,5,6,7)

Mas, a finalidade nossa aqui dessa função é realizarmos a soma dos valores que foram passados no argumento

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    print(soma(1,2,3,4,5,6,7))

Além disso, em vez de passarmos os argumentos uma por uma, poderíamos criar uma variável que carrega todos os argumentos queremos passar em uma função

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    random = 1,2,3,4,5,6,7
    print(soma(random))

Ops... Creio que não funcinou, pois foi mostrado a seguinte msg, que vc está mandando uma tupla e o "*args" ela forma uma tupla no conjunto de argumentos. Mas, então, qual a forma correta de guardarmos um conjunto de argumentos em uma variável e passar isso em uma função? Bom, bastaríamos colocar um asterisco na variável que carrega o argumento

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    random = 1,2,3,4,5,6,7
    print(soma(*random))

No caso, o que foi feito acima, é um ato de desempacotamento, como foi feito no exemplo do "x, y, *resto".

## Aula 10 - Exercícios com funções + Solução (prepare-se para pausar):
Bora praticar! Segue o enunciado

Primeiro enunciado

    # Exercícios com funções

    # Crie uma função que multiplica todos os argumentos
    # não nomeados recebidos
    # Retorne o total para uma variável e mostre o valor
    # da variável.

Segundo enunciado

    # Crie uma função fala se um número é par ou ímpar.
    # Retorne se o número é par ou ímpar.

## Aula 11 - Higher Order Functions - Funções de primeira classe:
Vamos entender sobre funções de primeira classe. Basicamente, a definição de funções de primeira classe significa que, assim como outros dados em Python, as funções em Python, também, podem ser tratadas como um dado.

    def saudacao(msg):
        return msg

    print(saudacao('Bom dia!'))

No caso, como a definição acima se aplica, pegando a função, saudacao, como exemplo, podemos realizar a seguinte tratativa nela como se fosse um dado mesmo

    def saudacao(msg):
        return msg

    saudacao_2 = saudacao
    random = saudacao_2('Boa noite!!!')
    print(random)
    print(saudacao('Bom dia!'))

Ou seja, note que, na variável "saudacao_2" estou atribuindo à ela "saudacao" que é o nome da função e, em seguida, usando a variável "saudacao_2" como se fosse uma função colocando um argumento 'Boa notie!!!'.

Nessa brincadeira, podemos definir uma função que decide ou não executar alguma outra função, como segue

    def saudacao(msg):
        return msg

    def executa(funcao):
        return funcao()

    saudacao_2 = saudacao
    random = executa(saudacao_2)
    print(random)

Entretanto, do jeito como está acima dará erro, pois na função "saudacao" ela exige que tenha algum argumento e na chamada acima não considera nenhum tipo de argumento. Para resolvermos isso, seria necessário colocar "*arg" como mais um argumento da função "executa"

    def saudacao(msg):
        return msg

    def executa(funcao, *arg):
        return funcao(*arg)

    saudacao_2 = saudacao
    random = executa(saudacao_2, 'Boa tarde!')
    print(random)

Claro, no lugar de "*arg" poderia ser um parâmetro simples, mas o *arg ela serve mais para podemos conseguir flexibilizar mais a quantidade de argumentos, caso, por ventura, eu acabe colocando mais parâmetros dentro da função saudacao

    def saudacao(msg, nome):
        return f'{msg}, {nome}'

    def executa(funcao, *arg):
        return funcao(*arg)

    saudacao_3 = saudacao
    random = executa(saudacao_3, 'Boa tarde', 'Leonardo')
    print(random)

## Aula 12 - Termos técnicos: Higher Order Functions e First-Class Functions:
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

- Higher Order Functions - Funções que podem receber e/ou retornar outras funções

- First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.

## Aula 13 - Closure e funções que retornam outras funções:
O Closure, no caso, ela é a definição do que vimos de funções de primeira classe nas aulas anteriores, quando definimos a função "executa". Ou seja, é uma função que retorna outras funcções.

Vamos abordar o assunto com mais profundidade explorando o que mais de interessante podemos conseguir obter desse conceito

    def criar_saudacao(saudacao, nome):
        return f'{saudacao}, {nome}!'

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

Bom, o formato da função acima, ainda não é uma clousure. Mas, basicamente, já podemos ver que ela retorna a saudação que queremos fazer de forma correta. Agora, começando a implementar o clousure, que é criar uma funçõa que executa outra função, podemos realizar a seguinte modificação da função acima

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar()

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

No caso, se executarmos o script acima, vamos ver que tudo continua ocorrendo de forma correta. Porém, mesmo assim, ainda não é definitivamente uma clousure, pois, lembrando novamente, clousure ela nos dá mais flexibilidade de executar as funções nos momentos que queremos que ela seja executada ou não. A função acima, uma vez acionada, ela será executada e feito o devido retorno, f'{saudacao}, {nome}!'. Porém, temos uma forma de conseguirmos evitar que isso ocorra e de conseguirmos atribuir às variáveis "s1" e "s2" somente as funções saudar() prontas para serem executadas, mas não executando-as

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s2)

Ao rodarmos o script acima, vamos ver que os dois prints retornam a memória da função saudar (o que indica que as informações estão guardadas na memória), que são diferentes entre "s1" e "s2", mas não o que de fato essa função, saudar(), retorna que é a saudação. Ou seja, isso significa que as duas variáveis "s1" e "s2" passam a serem funções que vc tem a liberdade de definir o momento em que ela será executada

    def criar_saudacao(saudacao, nome):
        def saudar():
            return f'{saudacao}, {nome}!'
        return saudar

    s1 = cria_saudacao('Bom dia', 'Leonardo')
    s2 = cria_saudacao('Boa noite', 'Leonardo')
    print(s1)
    print(s1())

    print(s2)
    print(s2())

Basicamente, isso é o clousure. Ou seja, vc não executa a função, mas as informações dos argumentos que vc passou estão guardadas na memória, e vc terá acessao só no momento em que vc executa, fechando os parênteses (close, por issoclosure) para, aí sim, acessar as informações que ficam guaradadas na memória do computador.

Aciona o Breakpoint para verificar isso passo a passo e ver como funciona e ver se está de acordo com o que foi abordado acima!

Bom, a clousure, praticamente, é o que define o paradigma de uma programação funcional.

    https://www.programiz.com/python-programming/closure
    https://www.learnpython.org/en/Closures

## Aula 14 e 15 - Exercício com funções e Solução do exercício com funções:
Bora praticar! Seguir o enunciado

    # Exercícios
    # Crie funções que duplicam, triplicam e quadruplicam
    # o número recebido como parâmetro.

## Aula 16 - Introdução ao tipo de dados dict - Dicionários em Python:
Vamos introduzir ao conceito de o dicionários.

Dicionários são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "indice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc...

No caso, os dicionários, assim como as listas, são mutáveis.

Vamos pegar o seguinte exemplo de dicionário

    pessoa = {
        'nome': 'Leonardo Takashi',
        'sobrenome': 'Teramatsu',
        'idade': 26,
        'altura': 1.8,
        'endereços': [
            {'rua': 'tal tal', 'número': 123},
            {'rua': 'outra rua', 'número': 321},
        ]
    }
    print(pessoa, type(pessoa))

Existe, sim, uma outra forma de escrever um dicionário como acima, usando a sintaxe "dict()" da seguinte forma

    dict(nome='Leonardo Takashi', sobrenome='Teramatsu')

Entretanto, a forma mais usada é na forma de chave acima "{}".

Para acessar os elementos que foram definidas dentro de uma chave, bastaria realizar o seguinte.

    pessoa['nome de algum elemento que foi definido']
    print(pessoa['nome'])
    print(pessoa['sobrenome'])
    print(pessoa['idade'])
    print(pessoa['altura'])

Podemos, também, iterar um dicionário como se fosse lista. No caso, a diferença é que nessa itearação será pego as chaves e não o valores de cada chave

    for chave in pessoa:
        print(chave)

## Aula 17 - Manipulando chaves e valores em dicionários em Python:
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

## Aula 18 à 20 - (Parte 1 e 2) Métodos úteis nos dicionários Python (dict):
Vamos explorar os métodos usuais na linguagem Python.

Logo, são elas

- len: Conta a quantidade de chaves ou elementos existentes dentro de um dicionário e lista, respectivamente.
    
    Mais pela frente, vamos aprender a montar uma classe usando o Python que é o momento em que entramos no conceito da programação orientada à objetos. No caso, por curiosidade, iremos mostrar as duas formas de usarmos tais métodos que é uma classe

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.__len__())
        print(len(pessoa))

    Lembramos, um detalhe importante de um dicionário, é que ele, mesmo não sendo definitivamente, ele é como um conjunto, ou seja, vc poderia definir várias chaves iguais

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu1',
            'sobrenome': 'Teramatsu2',
            'sobrenome': 'Teramatsu3'
        }

        print(pessoa['sobrenome'])

    No caso, acima, no print, será exibido o último valor que foi definido para a chave "sobrenome".

    Além disso, ao analisarmos o comprimento desse dicionário, usando o "len", será exibido um valor "2". Como havíamos dito que esse dicionário, mesmo não sendo definitivamente um conjunto, mas ele se comporta como uma, em um conjunto vc poderia colocar infinitos elementos repetidos dentro dela que, ainda sim, será assimilado que existe um elemento desse dentro dela, o que difere, por exemplo, com a lista.

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu1',
            'sobrenome': 'Teramatsu2',
            'sobrenome': 'Teramatsu3'
        }

        print(pessoa['sobrenome'])
        print(pessoa.__len__())
        print(len(pessoa))

- keys: Permite que iteremos um dicionário via chave e não pelos valores definidos em cada chave.

    O método "keys" ele retorna as chaves que são definidos dentro de um dicionários. No caso, o seu uso se dá como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.keys())

    No caso, ele retorna um dict_keys com uma lista dentro dela. No caso, claro, podemos sim acessar os valores das chaves dentro dela, mas não diretamente. Precisamos converter-las como seguinte

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.keys())
        print(tuple(pessoa.keys()))
        print(list(pessoa.keys()))

    Que é o famoso processo de coersão.

- values: Permite que iteremos um dicionário via os valores que são definidos para cada chave.

    Agora, para entender o uso desse método vamos primeiro iterar o dicionário

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        for chave in pessoa:
            print(chave)
        
        for chave in pessoa.keys():
            print(chave)

    Em ambos os for's, será retornado as chaves que foram definidos dentro do dicionário "pessoa".

    Agora, o values, entra dentro desse cenário, para mostrarmos que erla irá retornar os valores do que as chaves como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        for chave in pessoa:
            print(chave)
        
        for chave in pessoa.keys():
            print(chave)

        print(pessoa.values())
        print(tuple(pessoa.values()))
        print(list(pessoa.values()))

        for chave in pessoa.values():
            print(chave)

    No caso, podemos se utilizar do método values como o keys, donde a única diferença é que, em vez de chaves, ele retornará os valores.

- items: Permite que iteremos via chave e o valor correspondente.

    O uso do método "items", também, é similar ao uso dos outros dois métodos acima, "keys" e "values". No caso, ela irá nos retornar tanto a chave quanto o valor na forma de tuplas em pares

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.items())
        print(tuple(pessoa.items()))
        print(list(pessoa.items()))

        for item in pessoa.items():
            print(item)

        for chave, valor in pessoa.items():
            print(chave, valor)

- setdefault: adiciona o valor caso não exista a chave.

    Esse método, basicamente, ele serve para conseguir definir a chave, caso no momento da consulta, a tal chave não estiver definida. Como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        pessoa.setdefault('idade', 26)
        print(pessoa['idade'])

        pessoa.setdefault('nome', 'Alan')
        print(pessoa['nome'])

    Esse método "setdefault", por padrão, caso vc não coloque nenhum valor na suposta chave que será atribuído, ela irá atribuir o None. E a tal chave que vc está tentando atribuir já existir, não irá realizar nada.

- copy: retorna uma cópia rasa (shallow copy).

    Bom, o método "copy" do Python, ele realiza uma cópia raza de um dicionário/lista. O que quer dizer isso?

    Antes de responder essa pergunta, vamos lembrar o seguinte

        dic1 = {
            'd1': 1,
            'd2': 2
        }

        dic2 = dic1

        dic2['d1'] = 1000
        print(dic1)

    A forma como realizamos a atribuição acima, quem lembra do conceito, ela estará definindo duas variáveis que está apontando para um mesmo objeto. Logo, ao realizar alguma alteração em uma chave do dic2, essa alteração irá surtir para o dic1 também.

    Agora, ao usarmos o método "copy", como segue

        dic1 = {
            'd1': 1,
            'd2': 2
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        print(dic1)
        print(dic2)
        print(dic3)

    Vamos ver que a tal alteração que realizamos na chave "d1" no "dic3" não surtiu ao "dic1", como ocorre no caso do "dic2". Bom, nesse caso, podemos dizer que realizamos uma cópia do dicionário "dic1". Porém, essa cópia é rasa. Em que sentido? Para valores imutáveis, ocorrerá uma cópia, de modo independente. Porém, para valores mutáveis como lista, dicionário, etc... Essa cópia não ocorre. Ou seja, como podemos ver no exemplo abaixo

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic3['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)

    Conseguimos ver que, para a lista definido dentro do dic1, a alteração que realizamos no dic3, do primeiro índice da lista da chave "d3", essa mudança surtiu para o "dic1" também, o mesmo para "dic2".

    Bom, o que eu suspeito desse método "copy" ser razo, seria por conta do processamento que demoraria muito ao realizar alguma cópia de algum valor mutável, então, para que ela seja rápido, que seja feito um apontamento para dois objetos iguais, usando do conceito de categoria.

    Agora, para que seja possível realizar uma cópia total (Deep Copy), o Python ele tem um módulo para isso. No caso, bastaria importar tal módulo

        import copy

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic3['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)

    Agora, mesmo importanto o módulo "copy", haverá momentos em que queremos usar ainda a cópia raza, para isso bastaria usar "copy.copy('dicionário/lista')".

        import copy

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = copy.copy(dic1)
        dic4 = copy.deepcopy(dic1)

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic4['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)
        print(dic4)

- get: obtém uma chave.

    Bom, já usamos o "get" aqui, no caso, ela tem como finalidade em conseguir verificar se alguma chave existe ou não e retornar um None, por padrão, caso a tal chave não exista ou o valor atribuído à chave, caso ela exista.

        p1 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p1.get('nome'))
        print(p1.get('idade'))
        print(p1.get('idade', 'Não tem a chave idade'))

- pop: Apaga um item com a chave especificada (del).

    Já o "pop" ele funciona como o "del" e temos mais uma funcionalidade, como complemento, que é exibir o valor da chave que está sendo excluído

        p2 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        name = p2.pop('nome')
        print(name)
        print(p2)

    Além de pop, temos, também, o método "popitem()", donde ela remove a última chave e exibe, na forma de tupla, a chave e o seu valor que está sendo eliminado

        p3 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        ultima_chave = p3.popitem()
        print(ultima_chave)
        print(p3)

- update: Atualiza um dicionário com o outro.

    Já o update, seria quando quisermos passar um conjunto de chaves de forma mais prática

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

    No caso, a forma acima, depois que passarmos as chaves que queremos que vá dentro do p4, o update ela inclui.

    Como não obstante, podemos, também, atualizar, no sentido de modificar, os valores das chaves já existentes como segue

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

        p4.update({
            'nome': 'Alan'
        })

        print(p4)

        p4.update({
            'sobrenome': 'Turing',
            'cidade': 'London'
        })

        print(p4)

    Uma outra maneira mais prática de utilizar o método update, seria, em vez de usar "{}", é atribuindo diretamente a chave e o valor

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

        p4.update({
            'nome': 'Alan'
        })

        print(p4)

        p4.update({
            'sobrenome': 'Turing',
            'cidade': 'London'
        })

        print(p4)

        p4.update(job='Mathematician', college='Cambridge')

        print(p4)

    Podemos realizar a tal atribuição usando tuplas tbm

        tupla = ('invention', 'Turing Machine')
        p4.update(tupla)
        print(p4)

    Claro, se quisermos passar várias tuplas, precisamos colocar pares de tupla (chave, valor) dentro de uma tupla

        ((chave1, valor1), (chave2, valor2), ...)

    Da mesma maneira serve para lista tbm.

## Aula 21 e 22 - Exercício e Solução - sistema de perguntas e respostas com Python:
Seguir o exercício.

## Aula 23 - Introdução ao tipo set em Python (conjuntos):
Vamos aprender sobre set aqui. Bom, basicamente, o set aqui a lógica dela é literalmente eoria dos conjuntos que aprendemos em ensino médio. O leitor poderá pegar qualquer livro sobre teoria de conjuntos. Eu, particularmente, recomendo dois livros em ambas nos seus primeiros capítulos:

- Curso de Analise Vol.1 - Elon Lages Lima 

- Curso de analise real - Cassio Neri e Marcos Cabral

Lembrando que, ambos os livros, o leitor não precisa ler ela inteirinho para entender a seção de conjuntos. Bastaria entender teoria a teoria de conjuntos logo na primeira seção.

Para quem quiser um livro muito mais punk aprendendo desde os primórdios de Fundamentos da Teoria de Conjuntos, recomendamos o livro

- Set Theory, The third Milennium Edition, Revised and Expanded - Thomas Jech

Lembrando, esse último livro é beeeem mais trabalhoso de se ler e de resolver os exercícios.

Pois bem, vamos abordar sobre "set" e o seu uso. Bom, basicamente, para criar um set começamos assim

    s1 = set()

Bom, o set, ele parece um dicionário, mas não tem chave e valor. Eu acho mais fácil de entender de forma inversa. Entender primeiro o set em seguida entender dicionário e, por fim, listas e tuplas, pois querendo ou não, na matemática, tudo se resume em conjuntos e relações, quando a pessoa começa a estudar desde o axioma de Zermelo Fraenkel and Choice. Pois assim, o leitor conseguirá perceber que dicionários, listas e tuplas, estão todas elas apoiadas sobre conceitos de conjuntos e funções, como uma forma de consequência.

Bom, como em conjuntos, o set, ele não tem uma ordem. Logo, podemos colocar um iterável dentro do set como segue, e veremos que ela não necessariamente exibe em ordem alfabética

    s1 = set('Leonardo')
    print(s1, type(s1))

Ou seja, já vimos que se colocarmos uma string dentro do set, ela irá iterar o nome "Leonardo". Mas, então, como podemos colocar o elemento "Leonardo" detro desse conjunto sem iterar as letras desse nome? Bastaria realizar o seguinte

    s2 = {'Leonardo'}
    print(s2, type(s2))

Ou seja, usando as chaves "{}".

## Aula 24 - Peculiaridades do tipo mutável set em Python:
Vamos ver mais algumas peculiaridades do tipo mutável set em Python.

No caso, os set's:

- Não aceitam valores mutáveis;

- Seus valores serão sempre únicos;

- não tem índexes;

- não garantem ordem;

- são iteráveis (for, in, not in)

Além de serem eficientes de removerem valores duplicados, por serem conjuntos em sua própria definição. Como podemos ver no exemplo abaixo

    s3 = {1, 1, 1, 1, 2, 3, 3, 3, 3, 3}
    print(s3)

Note que, no exemplo acima, temos o número "1" e "3" repetidos. Enttretanto, ao darmos o print desse conjunto, vemos que é exibido somente 1, 2 e 3.

Podemos converter listas e tuplas em um conjunto tbm da seguinte forma

    l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
    t1 = (1, 1, 1, 1, 2, 3, 3, 3, 3, 3)

    s4 = set(l1)
    s5 = set(t1)

    print(s4)
    print(s5)

E de conjunto, podemos converte em lista e tuplas tbm, como segue

    l1 = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3]
    t1 = (1, 1, 1, 1, 2, 3, 3, 3, 3, 3)

    s4 = set(l1)
    s5 = set(t1)

    print(s4)
    print(s5)

    l2 = list(s4)
    t2 = tuple(s5)
    
    print(l2)
    print(t2)

Bom, isso é um método bem eficiente para vc conseguir remover valores repetidos de uma lista do que usar outros recursos de iteração.

Agora, para reforçar de não pudermos colocar algum valor mutável dentro do set, vale ver o seguinte exemplo

    s6 = {1,2,3,[123]}

Se vc compilar o código acima, será retornando um erro dizendo que não podemos colocar uma lista dentro de um conjunto, o mesmo vale para dicionário. Entretanto, podemos colocar uma tupla, pois a tupla é um valor imutável.

    s7 = {1,2,3,(123,)}

Agora, podemos colocar um conjunto dentro de um conjunto? Dica: Axioma do Zermelo Freankel kkkkkkk

Bom, outra vantagem de usar o set para realizar alguma iteração, seria pela sua eficiência que é um pouco acima do que das listas, dicionários e tuplas.

Além disso, podemos usar as linguagens de conferência de pertencimento sobre o set como é feito em conjunto, o "in" e "not in".

    s7 = {1,2,3,(123,)}
    print(3 in s7)
    print(4 in s7)
    print(5 not in s7)

## Aula 25 - Métodos úteis do tipo set em Python:
Vamos aprender os métodos mais usuais para essa sintaxe "set".

São elas as mais usadas para "set()":

- add:

    No caso, como o nome já disse, essa sintaxe "set()" serve para adicionar elementos dentro de um "set()", como segue

        s9 = set()
        s9.add('Leonardo')
        s9.add(1)
        print(s9)

    Lembrando que esse método ela não admite em adicionar vários valores, mas, sim, apenas um valor por vez.

- update:

    O update, a sua forma de uso, é muito parecido com o que vimos para o dicionário. No caso, podemos usar esse update para conseguirmos adicionar um conjunto de elementos dentro do set, como segue

        s10 = set()
        s10.update('Hello')
        s10.update(('Hello'))
        print(s10)

    Por quê que estou mostrando duas formas de adicionar, via update, o "Hello"? No caso, a primeira forma, sem a tupla, é o mesmo que eu estar passando "set('Hello')" que isso irá realizar uma iteração, ou seja, irá considerar como elemento dentro do "set" cada caractere. Já, se quisermos que a palavra "Hello" se torne elemento dentro do "set" será necessário usar o "()" para conseguirmos passar ela como elemento, assim, como um conjunto de outros iteráveis.

        s10.update(('Hello', 1, 2, 3, 4, 5, 'Teramatsu'))

- discard:

    O discard serve para remover um elemento dentro do "set" passando diretamente o valor imutável que vc queira eliminar dentro dele

        s10.discard('Hello')
        print(s10)

- clear:

    Já o "clear" ela serve para podermos limpar o "set" que já tem os elementos

        s10.clear()
        print(s10)

Link para verificar os outros métodos existentes para a sintaxe "set":

    https://docs.python.org/2/library/sets.html
    https://www.programiz.com/python-programming/methods/set

## Aula 26 - Operadores importantes para o tipo set (conjuntos):
Bom, vamos aprender sobre os operadores existentes no "set".

Vale lembrar que tais operadores são, definitivamente, as operações usuais de conjuntos que temos na matemática.

São elas, as mais usuais

- Une | - União:

    Para união de conjuntos, usamos o caractere "|" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s13 = s11 | s12

- intersecção & (intersection):

    Para a intersecção de conjuntos, usamos o caractere "&" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s14 = s11 & s12

- diferença - complemento:

    Para o complemento de conjunto, usamos o caractere "-" como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s15 = s11 - s12

- diferença simétrica ^ - Itens que não estão em ambos - Complemento da união:

    Esse aqui é uma espécie de complemento da intersecção. Em outras palavras, ao detalharmos o que é representado pelo "^" que é a diferença simétrica de conjuntos, considerando A e B, os conjuntos, seria "(A-B)|(B-A)". Como segue

        s11 = {1,2,3}
        s12 = {2,3,4}

        s17 = s11 ^ s12
        s18 = (s11 - s12) | (s12 - s11)
        
        print(s17)
        print(s18)


## Aula 27 - Exemplo de uso do tipo set:
Irei te mostrar um exemplo de uso de set que é uma forma de uso corriqueiro.

Quando você quer verificar a existência de algum elemento se ele já existiu ou não. No caso, verificamos a existência de uma pertinência como segue

    letras = set()
    while True:
        letra = input('Digite: ')
        letras.add(letra.lower())

        if 'l' in letras:
            print('Tu encontrou a letra')
            break

        print(letras)

Ou seja, o set em si ele costuma ser mais eficiente do que outros tipos de objetos por não ter algum índice nela fincado. No caso, ela acaba sendo mais rápido para procurar algo.

## Aula 28 e 29 - Exercício/Solução - Encontre o primeiro duplicado considerando a segunda ocorrência:
Seguir o enunciado do exercício.

    """
    Exercício
    Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
    Requisitos:
        A ordem do número duplicado é considerada a partir da segunda
        ocorrência do número, ou seja, o número duplicado em si.
        Exemplo:
            [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
            [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
        Se não encontrar duplicados na lista, retorne -1
    """
    lista_de_listas_de_inteiros = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
        [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
        [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
        [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
        [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
        [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
        [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
        [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
        [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
        [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]

## Aula 30 - Introdução à função lambda + list.sort e sorted:
Vamos aprender sobre função lambda em Python.

No caso, a função lambda é uma função anônima de uma linha. No caso, sempre que montamos uma função lambda, toda a relação deverá estar contida em uma única linha.

    lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
    lista.sort(reverse=True)
    sorted(lista)

No caso, a funçã, usado acima, é uma função de ordenação, mas não é um função lambda. No caso, acima, é um exemplo simples de ordenação, visto que temos os números inteiros sendo usado nela. Agora, imagina se quisermos realizar uma espécie de ordenação numa lista de bibliotecas como seguite

    lista = [
        {'nome': 'Luiz', 'sobrenome': 'miranda'},
        {'nome': 'Maria', 'sobrenome': 'Oliveira'},
        {'nome': 'Daniel', 'sobrenome': 'Silva'},
        {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
        {'nome': 'Aline', 'sobrenome': 'Souza'},
    ]

No caso, não iremos conseguir usar o sort() como acima, pois aqui temos dicionarios entre dicionários, donde não há uma ordem entre objetos para conseguirmos realizar a tal ordenação que tanto queremos. Uma das maneiras, que podemos usar o sort() para conseguirmos realizar alguma ordenação de forma mais flexível, no sentido de definirmos os parâmetros que queremos considerar para realizar a ordenação seria usando o "key" dentro do sorte e nela passar alguma função que considera algum indice dentro da ordenação.

    def ordena(item):
        print('Objeto a ser ordenado: ', item)
        return item['nome']

    lista.sort(key=ordena)
    print(lista)

No caso, o que está acontecendo acima, seria que usamos a função ordena dentro do sort(). Ou seja, conseguimos definir por qual parâmetro consideramos paramos realizarmos a tal ordenação, 'nome'.

Lembrando que o Python, ele utiliza a tabela unicode para considerar a ordenação de qualquer caracteres. No nosso caso, o unicode é o utf8.

Entretanto, até agora, não abordamos função lambda. Vamos, agora, finalmente, usar uma função lambda para mostrarmos como isso ficaria mais flexivel do que o formato acima para conseguirmos realizar a devida ordenacação

    lista.sort(key=lambda item: item['nome'])

No caso, acima é definitivamente a função lambda. Note que, a versão da função lambda acima, é o último exemplo que mostramos de ordenação usando "key" de forma enxuta.

Podemos realizar a mesma ordenação aplicando a função lambda dentro da função sorted tbm, como segue

    sorted(lista, key=lambda item: item['nome'])

No caso, a ordenação acima é reversa.

## Aula 31 - Funções lambda complexas (para entendimento):
Bom, vamos ver como podemos verificar que tais funções podem ou não serem convertidos em uma função lambda.

Segue as funções seguintes

    def executa(funcao, *args):
        return funcao(*args)

    def soma(x,y):
        return x + y

    def cria_multiplicador(multiplicador):
        def multiplica(numero):
            return numero * multiplicador
        return multiplica
    
    print(executa(cria_multiplicador(soma(1,3)), 10))

Vamos, agora, aprender a converter as funções acima em funções lambdas.

- Primeiro, vamos converter a função soma em função lambda

        print(
            executa(
                lambda x,y: x+y,
                9, 3
            ),
            executa(soma, 9,3),
            soma(9,3)
        )

    Note que, a forma acima, retornará o que precisamos.

    Uma outra forma mais eficiente de realizarmos essa soma para mais e mais parâmetros seria da seguinte forma

        print(
            executa(
                lambda *args: sum(args),
                1,2,3,4,5,6,7
            )
        )

    Neste caso, estou usando a função "sum" para conseguirmos  realizar as devidas somas.

- Agora, vamos converter a função cria_multiplicador em uma função lambda:

    No caso, essa função, como ela executa uma outra função que está definida dentro dela, ficaria um pouco mais complicado realizar a devida execução

        duplica = executa(
                lambda x: lambda y: x*y,
                19
            )

        print(duplica(3))

    No caso, como a função criar_multiplicador ela serve para retornar alguma uma outra função, então na variável duplica precisamos criar uma função lambda e dentro dessa função lambda retornar outra função lambda onde essa função lambda de dentro ela retorna a multiplicação dos parâmetros da primeira função lambda e da segunda, que está definida dentro da primeira. E o duplica, finalmente, executa a segunda função lambda, visto que colocamos o segundo parâmetro para conseguirmos realizar a multplicação.

    Entretanto, notamos que a função lambda acima ficou muito complexo. No caso, a dica é não usar dessa forma. Claro, não significa que seria tranquilo, mas não é recomendável à esse nível que tornaria o código difícil para realizar a leitura.

Obs: É considerado como uma má prática a seguinte forma de função lambda

    funcao = lambda parametro: parametro

## Aula 32 - Empacotamento e desempacotamento de dicionários + *args e **kwargs:
Nessa aula, vamos aprender sobre empacotamento e desempacotamento de dicionários.

No caso, o que é empacotamento e desempacotamento de dicionários? Seria o seguinte

    a, b = 1, 2
    a, b = b, a
    print(a, b)

Note que, no caso, acima realizamos esse processo em valores imutáveis. Mas a mesma analogia é aplicado para dicionários como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa
    print(a, b)

No caso, na forma acima, o print retornará as chaves do dicionário pessoa.

Mas, podemos definir de uma forma que retorne os valores definidos nas chaves como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa.values()
    print(a, b)

Ou, podemos desempacotar na forma de itens tbm como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa.items()
    print(a, b)

Podemos, tbm, realizar um desempacotamento interno como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    (a1, a2), b = pessoa.items()
    print(a1, a2)
    print(b)

Podemos usar essa mesma lógica e aplicar na iteração

    for chave, valor in pessoa.items():
        print(chave, valor)

Agora, se quisermos unir dois dicionários como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    dados_pessoa = {
        'idade': 26,
        'altura': 1.84
    }

    print(pessoa, dados_pessoa)

Bom, uma alternativa que temos para realizar a união dos dois dicionários, seria criando um terceiro dicionários e dentro dela extrair os dois dicionários

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    dados_pessoa = {
        'idade': 26,
        'altura': 1.84
    }

    pessoa_completa = {**pessoa, **dados_pessoa}

    print(pessoa, dados_pessoa)
    print(pessoa_completa)

Uma outra alternativa seria usando o kwargs, que é conhecido como "keyword arguments". Daí, podemos utilizar dessa funcionalidade da seguinte forma

    def mostro_argumentos_nomeados(*args, **kwargs):
        print(kwargs)

    mostro_argumentos_nomeados(nome='Leonardo', qlq=1236)

Note que, no print dentro dessa função, ao passarmos os parâmetros da forma costumeira de definir os elementos dentro do dicionario, devolverá um dicionário.

A parte legal disso, seria que isso nos permitirá iterar num for da seguinte forma

    def mostro_argumentos_nomeados(*args, **kwargs):
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(nome='Leonardo', qlq=1236)

No caso, a função acima reconhece os argumentos não nomeados tbm. No caso, podemos passar os parâmetros como seguinte tbm

    def mostro_argumentos_nomeados(*args, **kwargs):
        print('Não nomeados: ', args)
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(1, 2, 3, nome='Leonardo', qlq=1236)

No caso, podemos, também, passar como argumento dentro dessa função um dicionário desempacotado como seguinte

    def mostro_argumentos_nomeados(*args, **kwargs):
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(**pessoa_completa)

Bom, por vias didáticos, a função mostro_argumentos_nomeados, definido acima, ela serve tanto para valores não nomeados quanto para nomeados, respectivamente, *args e **kwargs.

## Aula 33 - Introdução à List comprehension em Python:
Vamos aprender a mexer com list Comprehension.

Basicamente, o List comprehesion é uma forma rápida de criar listas a partir de iteráveis. Segue o exemplo

    print(list(range(10)))

No caso, acima, será criado uma lista de conjunto [10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. No caso, o exemplo acima, é só uma motivação, pois não usamos nada de lista até então. Agora, segue o seguinte exemplo, que seria a abordagem do contexto

    lista = []

    for i in range(10):
        lista.append(i)

    print(lista)

No caso, a forma acima nos permite mais flexibilidade para inclusão de alguma lógica para conseguirmos manipular a forma que queremos criar uma lista por iteração. Porém, podemos realizar isso de forma mais fácil, em vez de gastar mais linhas de código, que, agora sim, estamos entrando no assunto principal

    lista = [i for i in range(10)]
    print(lista)

No caso, o formato é mais ou menos assim

    [(valor que vc quer colocar) for i in range(n) (que será colocado n vezes)]

Ou seja, no lugar de "i" poderia ser tbm

    lista = [1 for i in range(10)]

Daí, será colocado o número 1 dez vezes.

E claro, podemos colocar uma lógica dentro dessa iteração rápida tbm. O que diversifica as alternativas de formas para monstar uma lista, como segue

    lista = [i * 2 for i in range(10)]
    print(lista)

Conseguimos, também, realizar uma operação ternária dentro disso para termos mais controle do que será ou não colocado dentro da lista.

## Aula 34 - Mapeamento de dados em list comprehension (map):
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

## Aula 35 - Filtro de dados em list comprehension (filter):
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

## Aula 36 - List comprehension com mais de um for:
Uma outra coisa legal de list comprehension em python é que podemos usar iterações dentro de iterações. Ou seja, quantos for que quisermos.

Suponhamos o seguinte cenário

    lista = []

    for x in range(3):
        for y in range(3):
            lista.append((x,y))

Bom, vamos tentar realizar o cenário acima usando list comprehension. No caso, ficaria da seguinte forma

    lista2 = [(x,y) for x in range(3) for y in range(3)]

Lembrando, que no list comprehension, o que fica no lado esquerdo do for é o que será incluído dentro da lista.

Essa mesma forma de iteração podemos realizar da seguinte forma tbm

    lista3 = [
        [x for y in range(3)]
        for x in range(3)
    ]

Em outras palavras, a interpretação disso seria, para cada índice x itero o x dentro da lista, que fica dentro da lista, três vezes pelo índice y.

Bom, o legal disso é que podemos usar para criação de matrizes de forma rápida para aplicações de conceitos de álgebra linear, Análise no Rn e Probabilidade e Estatística.

## Aula 37 - Mais detalhes sobre list comprehension:
Eu criei um vídeo gratuito falando muito mais sobre list comprehension tirando como base as dúvidas desse curso. Veja em 

    https://youtu.be/1YbTDczvqco

Professor Luiz Otávio!

## Aula 38 - Dictionary Comprehension e Set Comprehension:
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

## Aula 39 - isinstace() - para saber se objeto é de determinado tipo:
Bom, como usamos na última aula, o isinstance() ela serve para checar se um valor é de um determinado tipo.

Considere a seguinte lista

    lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Leonardo'}]

Claro, em programação não é uma boa prática vc receber esse tipo de lista que tem muita coisa misturada. Porém, nos problemas do dia a dia em uma empresa isso é muito comum de acontecer e acaba sendo necessário desenvolver um código que trate tais valores.

Agora, vamos usar o isinstance iterando esse for

    for item in lista:
        print(item, isinstance(item, set))

Bom, podemos, claro, combinar com as condicionais if usando o isinstance

    for item in lista:
        if isinstance(item, set):
            item.add(5)
            print(item, isinstance(item, set))

No caso, esse uso nos permite realizar diferentes tipos de tratativas conforme o tipo que o elemento dentro da lista está sendo representado.

O legal do VSCode, agora é algo típico desse IDE, podemos ver que dentro da condicional do if acima, realizamos o item.add(5). A parte curiosa disso é que quando realizamos o "item." ele exibe todos os métodos que lhe é possível utilizar para o set. Ou seja, o VSCode foi inteligente o suficiente para reconhecer que dentro daquela condicional, o item que estou tratando é um conjunto. Da mesma forma que podemos realizar isso para outros tipos de dados. Algo que nas outras IDE's não é possível realizar.

Bom, isso é um indício que hoje em dia a programação está mais fácil graças aos editores de textos. (Só espero que um dia ainda criem uma linguagem de programação única que serve para tudo, em vez de existir tantas linguagens de programação... Assim, o programador se preocuparia em focar somente nos conceitos matemáticos para conseguir criar algum código robusto. Da mesma forma que facilita para um matemático que queria trabalhar com a computação tbm...)

    for item in lista:
        if isinstance(item, set):
            item.add(5)
            print(item, isinstance(item, set))

        elif isinstance(item, str):
            item = item.upper()
            print(item, isinstance(item, str))

        elif isinstance(item, (int, float)):
            item+=1
            print(item, isinstance(item, (int, float)))

        else:
            print('OUTRO')

## Aula 40 - Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis:
Vamos ver mais sobre os valores Falsy e Truthy.

Bom, o falsy e thuthy, podemos usar sobre os valores mutáveis e imutáveis, donde temos como padrão os tipos de valores que são considerados falsos ou outros como verdadeiros. Já vimos sobre isso nas aulas anteriores sobre os valores mutáveis e imutáveis. Recomendamos que o leitor revise tais aulas caso ficou alguma dúvida.

    lista = []
    dicionario = {}
    conjunto = set()
    tupla = ()
    string = ''
    inteito = 0
    flutuante = 0.0
    nada = None
    falso = False
    intervalo = range(0)


    def falsy(valor):
        return 'falsy'if not valor else 'truthy'


    print(f'TESTE', falsy('TESTE'))
    print(f'{lista=}', falsy(lista))
    print(f'{dicionario=}', falsy(dicionario))
    print(f'{conjunto=}', falsy(conjunto))
    print(f'{tupla=}', falsy(tupla))
    print(f'{string=}', falsy(string))
    print(f'{inteito=}', falsy(inteito))
    print(f'{flutuante=}', falsy(flutuante))
    print(f'{nada=}', falsy(nada))
    print(f'{falso=}', falsy(falso))
    print(f'{intervalo=}', falsy(intervalo))

## Aula 41 - dir, hasattr e getattr em Python:
Uma das coisas mais corriqueiras que temos na programação tbm, seria em checar se existe algum determinado tipo de valor dentro de um objeto.

Bom, isso, muitas vezes, acaba sendo útil para conseguirmos debugar algum código. O que é frenquete de ser usado tbm, é o breakpoint onde a pessoa para o código bem no momento em que ela precisa e em seguida escolha a opção debbuger console e nela digitamos o nome da variável para mostrar o que seria exibido nela e tbm usar o dir(nome da variável) para mostrar que tipo de atributos existem para esse objeto. Ou seja, uma das formas de conseguirmos debugar o código é usando o "dir" e verificar se existe o método dentro dela tbm

    string = 'Leonardo'
    print(string)

Aciona o breakpoint e vai no consule debbuger e nela digita "dir(string)" para verificar se existe o método que vc quer dentro dela.

Ou podemos, também, usar o "hasattr" para verificar se um determinado tipo de atributo existe dentro de um objeto que estamos analisando

    string = 'Leonardo'

    if hasattr(string, 'upper'):
        print('Existe upper aqui')
        print(string.upper())

No caso, acima, estamos checando se o objeto "string" que está com o valor "Leonardo", nela tem um método chamado "upper" ou não.

Podemos, também, dinamizar isso. Ou seja, o nome do método poderia estar numa variável

    string = 'Leonardo'
    metodo = 'upper'

    if hasattr(string, metodo):
        print('Existe upper')
        print(string.upper())

Além disso, caso o nome do método esteja em forma de string numa variável e feito a checagem pelo hasattr, vc queira usar ela, aí temos o getattr para isso. Ou seja, vc poderá usar o método que está dinamizado sem precisar chamar ela via o próprio objeto

    tring = 'Leonardo'
    metodo = 'upper'

    if hasattr(string, metodo):
        print('Existe upper')
        print(getattr(string, metodo)())

    else:
        print('O método não existe', metodo)

## Aula 42 - Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores):
Bom, nas seções anteiores já tínhamos abordado sobre coisas iteráveis e o que seria os iteradores.

No caso, a diferença gritante entre iterável e iteradores, seria que o iterável tem a responsabilidade de deter os valores sequencialmente e a única responsabilidade o iteradores seria te entregar um valor por vez.

    iterable = ['Eu', 'Tenho', '__iter__']
    iterator = iterable.__iter__() # tem __iter__ e __next__

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

No caso, o iterator ele te devolve os valores sucessores. Sem se importar em qual posição o valor atual se encontra.

Podemos ver acima, nos três prints, conforme chamamos o "next(iterator)" ele devolve o próximo da lista iterable.

Lembrando, iterator só se usa sobre objetos iteráveis!

O livro em que o professor Luiz Otávio viu sobre esse conceito pela primeira vez foi no

- Padrões de Projetos, Soluções reutilizáveis de software orientado a objetos

Não se preocupe que teremos uma seção inteirinha somente desse livro nessa revisão.

Link para leitura

    https://www.geeksforgeeks.org/python-difference-iterable-iterator/
    https://byjus.com/gate/difference-between-iterable-and-iterator-in-python/
    https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration

## Aula 43 - Generator expression, Iterables e Iterators em Python:
Vamos aprender sobre generator. No caso, esse generator é algo antigo que já existia no JavaScript, porém no Python foi implementado de forma recente.

Basicamente, o generator são funções que sabem pausar em determinada ocasião.

Todo generator é um iterator, mas não vale a recíproca.

Vamos mostrar um exemplo básico para melhorar a sua compreensão

    generator = [n for n in range(10)]

    print(generator)

Bom, pegamos um iterável simples acima só para exibição. Mas, agora, imagina se a variável "generator" acima tiver 10000 range e tiver que exibir isso tudo de uma vez. Isso, com certeza, tornaria a exibição caótica. No caso, o generator ele serve para vc conseguir determinar o momento para pausar.

Qual é a vantagem disso?

Bom, suponhamos que vc tenha que lidar com uma quantidade de dados exuberante e dela vc precisa tirar somente alguns dados. No caso, seria muito ineficiente se vc tiver que tratar toda hora todos os dados para conseguirmos filtrar somente aqueles dados que precisamos. No caso, o generator, ele facilita isso de forma a otimizar o processo sem a necessidade de ter que passar para todos os dados, mas, sim, selecionando somente aquelas que precisamos.

Para isso, do exemplo acima, bastaria mudar a lista para "()" como segue

    generator = (n for n in range(10000))

    print(generator)

Daí, no print será exibido um generator expression, do tipo

    <generator object <genexpr> at 0x7fac0339ec80>

Diferentemente de darmos o print sobre a forma

    generator = [n for n in range(10000)]
    
    print(generator)

Que será exibido uma quantidade exuberante de dados.

Vamos importar o módulo "sys" para mostrarmos o tamanho dos dados de cada tipo

    import sys

    lista = [n for n in range(10000)]
    generator = (n for n in range(10000))

    print(sys.getsizeof(lista))
    print(sys.getsizeof(generator))

Ao rodarmos o código acima, conseguimos ver que o tamanho da lista e do generator há uma deferença bem evidente.

Ou seja, o que isso singifica?

Significa que, enquanto na variável "lista" que, de fato, é uma lista quando criado uma lista via list comprehension, isso já estaria sendo guardado na memória da máquina, com o generator não será guardado. Podemos mudar o tamanho do range para lista e generator e isso ficará evidente, pois enquanto a lista irá aumentar de memória, o generator continuará na mesma quantidade.

Qual a vontagem disso?

Basicamente, otimiza o consumo da memória de modo que o generator, pelo fato dele não guardar nada na memória, ele fica no estado de espera para que vc solicite algum dado que esteja guardado sobre ele.

Assim, podemos realizar a busca de forma otimizada como segue

    import sys

    generator = (n for n in range(10000))

    print(sys.getsizeof(generator))
    print(generator)

    print(next(generator))
    print(next(generator))
    print(next(generator))

Note que, acima, no print que usa o método next, está sendo feito direitinho a busca necessária dos valores que foram iterados.

Agora, podemos usar o for para conseguirmos realizar a devida busca necessária de forma otimizada, entendido a natureza do generator

    import sys

    generator = (n for n in range(10000))

    print(sys.getsizeof(generator))
    print(generator)

    for n in generator:
        print(n)

Vimos que foi feito uma iteração em escala enorme que foi exibido pelo terminal correto? Bom, isso está preenchendo a memória conforme a quantidade de iterações que ocorreu, o que é diferente da situação que temos um iterável [n for n in range(10000)] pronto, pois isso indica que esses 10mil valores já estará guardado na memória, o que não é otimista do ponto de vista de uso de espaço da memória.

Ok, falei das vantagens de se usar um generator. Mas e as desvantagens?

Bom, o generator ele é um iterável, mas nela não se aplica os métodos e técnicas que temos de uma lista. Ou seja, não podemos saber o tamanho dela, no caso não dá para usar o len, muito menos não podemos consultar o valor pelo índice, etc... Tudo isso, só pelo fato dele não estar na memória, como uma lista estaria. Portanto, só é possível consultar os valores próximos uma por uma e iterar ela com o for de modo que vc consiga realizar uma busca mais eficiente

    print(len(generator))
    print(generator[50])

Os dois prints acima dará um erro. Assim, como outros métodos que se aplica para uma lista dará o mesmo erro, pois não está na memória.

Fonte para leitura

    https://www.geeksforgeeks.org/difference-between-iterator-vs-generator/
    https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

## Aula 44 - Introdução às Generator functions em Python:
Bom, agora, vamos explorar mais ainda dos recursos úteis que temos para o Generator.

Vamos começar por montar uma função

    def generator(n=0):
        return 1

    gen = generator(n=0)
    print(gen)

Esse aqui é só para começar para ver que a função retorna "1" mesmo. Até aqui, não estamos abordarndo de forma eficiente a natureza principal da função generator, que é a sua propriedade de conseguir pausar.

Agora, sim, vamos desenvolver um algoritmo que usar muito bem da natureza do generator. Segue o seguinte código

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen)

No caso, note que, acima mudamos o return para yield. O que essa sintaxe tem de funcionalidade?

Ela retorna o valor "1", só que na variável "gen" que executamos a função generator, esse valor "1" retornado não está guardado na memória. Como podemos ver no print, em vez dela devolver um valor "1", ela devolve generator expression, como do seguinte tipo

    <generator object generator at 0x7fcd9b45cc80>

Isso, novamente, evidencia que não está guardado na memória o valor retornado, mas, sim, ela está esperando ser chamado como podemos ver se fizermos o seguinte

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen)
    print(next(gen))

No print que usa o método "next" ela retorna o valor "1", como de se esperar, e é o momento em que irá consumir um espaço na memória tbm.

Como dizemos quando começamos a abordar sobre generator. Todo generator é um iterável tbm, então, obviamente, podemos usar o seguinte método iter tbm

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))

Acrescentamos tbm que depois do yield podemos usar o return tbm. Mas aí como esse return irá funcionar visto que já foi retornado algo, mesmo que não esteja na memória? Bom, o return ela servirá para mostrar que não há mais valor e ela será exibida em uma funcionalidade chamada raise

    def generator(n=0):
        yield 1
        return 'ACABAOU'

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))
    print(next(gen))

No caso, ao executarmos o código acima, vamos conseguir ver que na segunda vez que é chamado o next, como não tem mais nenhum valor depois do "1" que foi retornado, então no terminal será exibido uma mensagem "StopIteration" exibindo o valor do return, que neste caso é o "ACABOU".

Ou seja, o return, ela serve para defitivamente parar a função, pois, depois do yield, pode existir mais e mais yields que visto que, pelo next ou por alguma iteração for, foi batido um tal valor retornado pelo yield, a função generator, irá continuar com a leitura da linha sucessiva dentro dela

    def generator(n=0):
        yield 1
        print('Continuando......')
        yield 2

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))
    print(next(gen))

No caso, forma como está acima, no segundo next será exibido o valor "2", pois quando foi executado o primeiro next, foi pausado a função generator na linha onde está "yield 1", e quando usamos o next pela segunda vez, dentro da função "generator", ela dará a continuidade a partir do ponto em que foi pausado, "yiel 1", adiante, então virá o print('Continuando.....') e em seguida o segundo yield, "yield 2".

Isso irá continuar até que o próximo next não retorne nada, caso vc não use o return, pois aí, por padrão, as funções def elas retornam um None.

Bom, entendido o conceito e visto a sua funcionalidade do ponto de vista manual, usando o next, vamos agora dinamizar isso usando o for. Assim, conseguimos montar o seguinte código para função generator para considerar escalas de valores maiores

    def generator(n=0):
        yield 1
        print('Continuando......')
        yield 2

    gen = generator(n=0)
    for n in gen:
        print(n)

Note que, na forma dinâmica acima, usando o for, quando o for exibiu tudo o que pode ser exibido pelo generator, não foi exibido a mensagem "StopIteration". Ela simplesmente parou a exibição no "2" ou se tiver algum print ou qualquer outra coisa em seguida, menos o return, irá parar nela.

Agora, vamos melhorar a qualidade do código generator, como prometido, para escala maior

    def generator(n=0, maximum=100000):
        while True:
            yield n

            n += 1

            if n > maximum:
                return

    gen = generator()
    gen1 = generator(n=5, maximum=200)
    for n in gen:
        print(n)

Bom, note que, agora, a função generator, por padrão temos duas variáveis padrões definidas nela, e que o yield está dentor de um laço infinito while, cujo o laço irá parar somente quando ocorrer o return, ou seja, entendo dentro da condicional.

## Aula 45 - yield from em generator functions:
Podemos, também, usar o yield from em funções generators. O que é isso?

Basicamente, o yield from ela importa o processo de uma outra função generator para uma outra função.

Exemplo, suponhamos as duas seguintes funções

    def gen1():
        yield 1
        yield 2
        yield 3

    def gen2():
        yield 4
        yield 5
        yield 6

Bom, note que, a função gen2 é uma continuação da função gen1. Daí, existem situações em que depois que ocorrer um processo numa determinada função eu quero que o processo seja continuado numa outra função. Para isso que serve o yield from, que bastaria usar da seguinte forma

    def gen1():
        yield 1
        yield 2
        yield 3

    def gen2():
        yield from gen1()
        yield 4
        yield 5
        yield 6

    gen = gen2()

    for numero in gen:
        print(numero)

Daí, será exibido todos os números de 1 até 6.

Bom, com isso podemos fazer coisas bem mais interessantes. Recomendo o leitor tentar entender a lógica de programação que está no código do arquivo aula45.py.

## Aula 46 e 47 - (Parte 1 e 2) try e except para tratar exceções:
Bom, essa parte, a lógica é muito similar ao try/catch que se ensina na linguagem JavaScript.

Ela serve para conseguir tratarmos uma exceção.

Assim, temo como sintaxe disso os seguinte try, except, else e finally. No caso, a combinação é válida da seguinte forma try/except, try/finally, mas não tem try/else. Então em que momento se usa o else? Vamos abordar isso ao longo do curso.

    try:
        ...
    except:
        ...

ou

    try:
        ...
    finally:
        ...

Bom, como uma boa prática, é recomendável que nunca deixe de acontecer algum erro silencioso. Na forma, como está acima para except

    try:
        ...
    except:
        ...

Vc está criando, propositalmente, um erro silencioso. Claro, a forma acima só foi para mostrar as combinações possíveis, mas que fique bem claro que na prática não se deve colocar algum erro silecioso, no geral.

Agora, vamos ver o seguinte exemplo 

    a = 18
    b = 0
    c = a / b

Bom, ao definirmos a variável acima, se tentarmos executar o código, teremos um erro, pois não está definido matematicamente, dentro do conjunto que estamos trabalhando, a divisão por zero. Logo, ao tentarmos rodar o código acima, não será possível pois isso irá induzir à um erro.

Agora, vamos utilizar do cenário acima para conseguirmos explorar sobre o uso de try/exception. No caso, obviamente, em cenários usuais, tais divisões acima, estariam sendo utilizados de forma dinâmica, onde o cliente que irá colocar algum valor para conseguirmos tratar. No caso, pensando nisso, vamos colocar o seguinte

    a = 18
    b = 0

    try:
        c = a / b
    except:
        print('Deu ruim!')

    print('CONTINUAR')

Ao rodarmos o código acima, as duas mensagens 'Deu ruim' e 'CONTINUAR' serão exibidos pois, como podemos ler literalmente, foi feito uma tentativa de divisão, mas isso não deu certo, então acabou entrando na exceção e dentro da exceção foi feito o que foi definido, print, então saímos do código e seguimos para o print('CONTINUAR').

Bom, como podemos ver, a funcionalidade é igualzinho ao try/catch do JavaScript para tratamento de exceções ou impedimento de que a aplicação não pare no meio do processo. Advinha, então, o que o finally faz? kkkkkkk Bom, bastaria dar uma lembrada, para quem estudou JavaScript, mas vamos abordar isso ao longo da aula.

Voltando para o try/except, a forma como foi codado acima, mesmo que sirva para entender como é o tipo de uso, a forma acima ainda assim, está dentro dos conjuntos de más práticas, pois a msg que utilizei acima "Deu ruim" torna ainda o erro silecioso. Mesmo que eu tenha colocado alguma msg do tipo 'Não se pode dividir por zero', ainda sim, continuará sendo uma má prática, pois qualquer tipo de outro erro que acontecer, a msg exibida será o aviso de não dividir por zero. Ou seja, o erro continua sendo silecioso, como segue

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except:
        print('Dividiu por zero.')

    print('CONTINUA')

No caso, o formato acima deixa ainda mais nítido em que momento o código dentro do try para e vai para o except, o print('Linha 2') não será exibido.

Agora, falseando um outro tipo de erro, seria colocando o seguinte

    try:
        a = 18
        # b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except:
        print('Dividiu por zero.')

    print('CONTINUA')

Agora, nesse cenário, como a variável b está comentado, cairá em um outro tipo de erro. Bastaria rodar só o código

    a = 18
    # b = 0
    c = a / b

para conseguirmos ver que tipo de erro será exibido.

Ou seja, se tivessemos um try/except da forma como estamos acima, mesmo exibindo a msg 'Dividiu por zero.' dificilmente iremos saber que tipo de erro, realmente, está ocorrendo para ter acontecido algo do tipo acima.

No caso, em resumo, sempre precisamos ter em mente que é necessário exibir direito que tipo de erro está sendo tratado na exception. Como?

Bom, basicamente, temos várias formas. Primeiro, de forma clássica, vamos mostrar o jeito mais arcaico, que é definindo o tipo de erro uma por uma. Ao rodarmos o código 

    a = 18
    b = 0
    c = a / b

pelo terminal, será exibido o tipo de erro. Em Python, as exceções são classes, então o tipo de erro que é exibido pelo terminal, no caso acima, "ZeroDivisionError" é uma classe, então uma das formas de tratarmos o excetp seria literalmente chamar esse tipo de classe nela como segue

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')

    print('CONTINUA')

Obs: Todas as nomenclaturas de uma classe é escrito em Pascal Case. Ou seja, sempre que inicia algum nome ela começa, primeiro, com letra maiúscula.

Note que, com o código acima, iremos conseguir tratar o erro caso ocorra alguma divisão por zero. Além disso, se ocorrer algum outro erro, esse erro será exibido pelo terminal, claro parando toda a aplicação, que é o que queremos evitar a priori, pensando no cenário em que tiver algum usuário utilizando a aplicação, como no caso abaixo

    try:
        a = 18
        # b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')

    print('CONTINUA')

Ou seja, o tipo de erro já não é mais a divisão por zero. Então, não irá cair dentro da except e isso irá parar de rodar o código, sem exibir 'CONTINUA'. Daí, o que precisaria ser feito? Claro, criar uma outra except colocando nela o erro que foi capturado

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')

    print('CONTINUA')

Aí vem a seguinte pergunta. Devo sempre ficar caçando uma por uma os possíveis erros para gradualmente tornar o sistema muito mais completo?

A resposta para isso é, depende. Pois existem cenários em que a contagem dos tipos de erros é evidente e existem cenários que não. Ok, mas e se acontecer o segundo cenário? Para esse caso, existe uma forma de tratar o erro, mas que eu não gosto muito, que seria chamando a classe de erro mais superior de todas que é Exception

    try:
        a = 18
        b = 0
        print('Linha 1')
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Eu, particularmente, detesto esse tipo de classe, pois, querendo ou não, torna, de certa forma, silencioso o tipo de erro. Pois, a classe Exception, ela é a classe de nível mais acima de todas as outras classes de erros existente. Serve para conseguir tratar qualquer tipo de erro, mas, muitas vezes, não deixando claro a natureza desse erro.

Bom, a moral da história, é que o try/except, dentro do except, não podemos dinamizar de forma que quando venha algum erro desconhecido, seja possível que o sistema trate ela de forma eficiente. Ou seja, esse exception existe mais para conseguir facilitar que o usuário continue utilizando a aplicação, enquanto que, em paralelo, o desenvolvedor consiga realizar o reparo ou investigação do problema para conseguir incluir, possivelmente, mais uma except e nela definir algum tratamento mais eficiente, depois que toma o devido conhecido do erro, que antes era desconhecido.

Bom, vamos explorar os seguintes erros tbm

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Acima, temos dois tipos de erros. A primeiroa é de tipagem, pois a variável "b" é imuável e estamos tentando acessar algum índice dentro dela comoc se fosse lista e a outra é um erro de tipagem, no print('Linha 1'), pois estamos tentando acessar o índice que não existe dentro dessa string. Bom, se rodarmos cada um dos códigos de forma isolado, vamos ter os seguinte erros TypeError e IndexError.

No caso, bastaria colocar mais dois except, como uma boa prática. Mas desta vez, vamos colocar duas de uma vez, que não é uma boa prática, mas de forma proposital, para conseguirmos mostrar uma coisa interessante

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError):
        print('TypeError + IndexError')
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Note que, no except (TypeError, IndexError):, não sabemos que tipo de erro está acontecendo, mas sabemos que é certeza uma das duas. Para isso, existe uma froma de conseguirmos exibir isso que seria usando o alias "as" das seguinte forma

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError:
        print('Dividiu por zero.')
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError) as error:
        print('TypeError + IndexError')
        print('Mensagem:', error)
        print('Nome do erro:', error.__class__.__name__)
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

No caso, a forma acima, irá exibir que tipo de erro ocorreu na mensagem e qual foi o nome do erro, que seria o nome da classe. Tornando assim, mais evidente o tipo de erro que aconteceu. O mesmo podemos realizar para except que tem somente uma classe de erro, como seguinte

    try:
        a = 18
        b = 0
        print(b[0])
        print('Linha 1'[1000000])
        c = a / b
        print('Linha 2')
    except ZeroDivisionError as e:
        print('Dividiu por zero.')
        print('Mensagem:', e)
        print('Nome do erro:', e.__class__.__name__)
    except NameError:
        print('Alguma variável não está definido')
    except (TypeError, IndexError) as error:
        print('TypeError + IndexError')
        print('Mensagem:', error)
        print('Nome do erro:', error.__class__.__name__)
    except Exception:
        print('Erro desconhecido')

    print('CONTINUA')

Tornando assim, mais evidente o tipo de erro.

## Aula 48 - try, except, else e finally + Built-in Exceptions:
O que vc pode querer fazer com o try/except e que mesmo que tenha passado no try e expcet, que a aplicação ela não pare. No caso, que de alguma forma o sistema continue em funcionamento sem que ela pare. Para isso, seria necessário colocar uma outra funcionalidade junto com o try/except, que é o finally

    try:
        ...
    except:
        ...
    finally:
        ...

Acima, basicamente, está a estrutura padrão de uso. No caso, finally ela sempre será executado mesmo que tenha ocorrido algum erro ou que a aplicação tenha dado certo. No caso, o uso eficaz desse método é sempre colocar alguma conclusão do processo que, independente do que resultar, que tal processo ocorra no final.

    try:
        print('ABRIR ARQUIVO')
        8/0
    except ZeroDivisionError:
        print('DIVIDIU ZERO')
    finally:
        print('FECHAR ARQUIVO')

Uma outra alternativa de um uso conjunto com o finally, seria usando o else. Nesse caso, vc não irá precisar colocar alguma condicional dentro do finally de caso o processo tenha dado certo. No lugar disso, podemos usar o else

    try:
        print('ABRIR ARQUIVO')
        # 8/0 # Comenta e descomenta para verificar que quando dá certo ela entra no else e quando não dá, ela não entra no else.
    except ZeroDivisionError:
        print('DIVIDIU ZERO')
    else:
        print('NÃO DEU ERRO')
    finally:
        print('FECHAR ARQUIVO')

Claro, mesmo assim o finally ela é um passo que irá com toda certeza ser passado nela. Bom, nesse caso fica a dúvido do que o else ela tem de utilidade. No caso, o else ela serve mais para conseguir colocar algum processo posterior ao processo que deu certo, pois antes de o processo ser finalizado, vc queira colocar algum tipo de condição ou efetuar algo.

Seguir o link para leitura:

    https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

## Aula 49 - raise - lançando exceções (erros):
Bom, agora que estamos em um nível intermediário para avançado, vamos verificar os tratamentos de erros.

Uma das características que compõe um bom programador é que eles gostam de erros, no ramo tecnológico, quanto mais erros vc sabe tratar melhor seria a qualidade de funcionamento do teu programa, donde essa qualidade é um grande diferencial no ramo da tecnologia.

Vamos, agora, simular um tipo de erro para melhorar. Muitas vezes, precisamos que um determinado erro seja lançado para melhorar e, por fim, encontrar algum meio de tratamento. Para isso, vamos aprender a usar a funcionalidade "raise" que serve, exatamente, para lançar algum erro. No caso, vamos verificar o seguinte

    def divide(x, y):
        return x / y

    print(divide(8, 0))

Claro que sabemos a divisão acima dará um erro. Mas a finalidade que queremos é que esse erro seja lançado.

Bom, para isso vamos realizar o uso do try/except dentro da função divide

    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return x

    print(divide(8, 0))

Bom, no caso, o exemplo acima, ela serve para realizar alguma tratativa da divisão pelo zero, que foi retornar o número do numerador da divisão. Só que, queremos que tal erro seja lançado. Para isso que usamos o raise

    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise

    print(divide(8, 0))

No caso, o raise ela relança o erro que ocorreu. Entretanto, a condição acima é redundante com o caso de simplesmente retornar na função "divisao" o valor "x / y" feito a tal divisão errônea. A nossa finalidade é que usemos o raise para realizar alguma tratativa util, como no caso seguinte

    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError('Você está tentando dividir por zero!')

        return x / y

    print(divide(8, 0))

Note que, ao executarmos o código acima, agora, a msg de erro clássico "division by zero" mudou para pela msg que escrevi dentro da classe ZeroDivisionError. Basicamente, o que eu fiz acima é criar o meu próprio erro.

Agora, como uma via de uma boa prática, vamos precisar realizar o seguinte. Em uma função, sempre seria uma boa colocar de funcionalidade somente o que queremos que aquela função realize. Por exemplo, a função que criamos "divide" seria de boa prática colocar dentro dessa função a funcionalidade de divisão, somente. Entretanto, na forma como está a função "divide" no último exemplo, ela está sendo colocado a funcionalidade de tratativa do erro. O ideal é que essa tratativa esteja separado e que ela seja chamado dentro dessa função. No caso, algo do seguinte tipo

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def divide(x, y):
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, 0))

Isso nos permite melhorar a qualidade da leitura do código, de forma que ela fica mais didática, e tbm na sua organização. De forma que cada função fique mais independente da outra, pois a forma acima facilita em considerar e desconsiderar algumas funcionalidades sem a necessidade de refatorar grandes quantidades de linha.

Da mesma forma serve para conseguirmos criar a tratativa para outros tipos de erros, pois imagina a pessoa passa, dentro do argumento da função, alguma String? No caso, para esse cenário segue o seguinte

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def divide(x, y):
        if not isinstance(x, (float, int)):
            raise TypeError(
                f'{x} deve ser int ou float.'
            )

        if not isinstance(y, (float, int)):
            raise TypeError(
                f'{y} deve ser int ou float.'
            )
        
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, '0'))

Assim, passando o zero como uma string, na função "divide" acima ela irá retornar uma mensagem de erro dizendo que o "'0'" deveria ser um int ou float.

Claro, como uma boa prática do clean code, vamos colocar essa condicional que colocamos dentro da função divide para uma função fora

    def divisao_por_zero_indefinido(denominador):
        if denominador == 0:
            raise ZeroDivisionError('Não pode dividir pelo zero!')

    def deve_ser_int_ou_float(n):
        tipo_n = type(n)
        if not isinstance(n, (float, int)):
            raise TypeError(
                f'"{n}" deve ser int ou float. '
                f'"{tipo_n.__name__}" enviado.'
            )
        return True

    def divide(x, y):
        deve_ser_int_ou_float(x)
        deve_ser_int_ou_float(y)
        
        divisao_por_zero_indefinido(y)
        return x / y

    print(divide(8, '0'))

Bom, o legal do raise é que vc consegue criar as suas próprias excessões de erros para ter mais flexibilidade de tratamento. Isso computaria mais e mais possibilidades de erros para informar de forma didática ao usuário.

## Aula 50 - Módulos - import, from, as e *:
Nessa aula vamos aprender a fazer de várias maneiras o importe de módulos padrão.

No caso, isso, em outras palavras, indica que a linguagem Python, uma vez instalado essa linguagem na sua máquina, ela já carrega consigo muitos, mas muitos, módulos padrões para utilizar. Não é que nem no JavaScript ou Java, donde por meio de node_modules e grails/gradle, respectivamente, seria necessário para possibilitar em baixar as dependências para, finalmente, vc conseguir utilizá-la.

Ou seja, o Python, em si, já carrega uma quantidade imensa de módulos que nos livra, na maioria das vezes, da necessidade de ter que baixar alguma dependência por fora ou até mesmo importar algo customizado externamente.

    https://docs.python.org/3/py-modindex.html

Bom, a forma de importar os módulos, é muito parecido com os frameworks como ReactJS ou VueJS Você pode importar uma parte do módulo ou o módulo inteiro.

- Importando o módulo inteiro:

    Por exemplo, a forma para importar o módulo inteiro, seria apenas jogando o nome do módulo, como segue

        import sys

    E se vc quiser usar algo do sys, os métodos que estão salvo dentro desse módulo, acessamos elas que nem a forma como acessamos os objetos

        import sys

        sys.exit()
        print('Hello WounderWorld!)

    a função "exit()" acima, por exemplo, serve para sair do programa. No caso, se vermos o print não será executado.

    No caso, como importamos o módulo inteiro, sempre que formos utilizar os métodos definidos dentro desse módulo, precisamos utilizar o name space, sys, com um ponto, ., em seguida para conseguirmos acessar aos métodos que estão salvos dentro desse módulo.

        import sys

        print(sys.platform)

    o método "platform" serve para tu mostrar o kernel do sistema operacional da máquina que vc está rodando. No meu caso, como estou usando o Windows 10, as vezes eu estou pelo Linux Ubuntu 20.04, será, então, mostrado o seguinte

        win32

    Esse método serve para vc saber em qual sistema operacional vc está.

    A vantagem de acessarmos o método via name space, é que se definirmos alguma variável que tenha o mesmo nome do método, isso não irá dar problemas

        import sys

        platform = 'A minha'
        print(sys.platform)
        print(platform)

    A única desvantagem disso é que o nome ficaria muito grande. Entretanto, ela se enquadra dentro das boas práticas para evitar problemas no seu sistema.

    Outra coisa que devemos tomar cuidados ao importarmos o módulo inteiro, é a sobrescrição desse módulo

        import sys

        sys = 'alguma coisa'
        print(sys.)

    Você verá que, por ela estar sobrescrito, não irá ser exibido os métodos desse módulo.

    Podemos também, importar o módulo inteiro, se a pessoa ver que o nome está muito longe, usando algum alias

        import sys as s

        sys = 'alguma coisa'
        print(s.platform)

    Daí, como no alias, o sys está apelidado como "s", então mesmo que definimos a variável sys e nela atribuirmos algum valor, percebemos que isso não irá afetar o módulo.

- Importanto diretamente os métodos dentro do módulo:

    Agora, vamos mostrar uma forma de importar diretamente dos módulos apenas alguns métodos. Para isso, teríamos que usar o "from"

        from sys import exit, platform

    Donde estou dizendo literalmente "De (from) módulo(sys) importe(import) métodos(exit, platform)". Agora, podemos usar esses métodos de forma direta

        from sys import exit, platform

        print(platform)
        exit()

    Sem a necessidade de usarmos o name space para conseguirmos chamar os métodos.

    Já a desvantagem disso, é que se definirmos alguma variável com o mesmo nome "platform", por exemplo, estaremos sobrescrevendo esse método

        from sys import exit, platform

        platform = 'A minha'
        print(platform)
        exit()

    Ou seja, nessa forma de uso, vamos ter que tomar cuidado para não sobrescrevermos os métodos.

    Aqui, também, podemos apelidar os nomes dos método assim como apelidamos o nome do módulo inteiro como fizemos antes, usando o alias

        from sys import exit as ex, platform as pt

        platform = 'A minha'
        exit = 'Sair'
        print(pt)
        print(platform)
        print(exit)
        ex()

    No caso, a forma acima vai nos permitir, mesmo sobrescrevendo originalmente os nomes dos métodos, como elas foram apelidadas, então ainda estarão funcionando.

OBS: Sempre que formos apelidar algo, precisamos tomar cuidado na legibilidade do código, pois dependendo do apelido que vc atribuir para o módulo ou método, isso poderia dificultar na leitura do código.

- Má prática: Importanto tudo

    Agora, algo que se enquadra totalmente dentro do escopo da má prática seria importanto tudo

        from sys import *

        print(platform)
        exit()

    A forma acima, nos libera de importar todos os métodos do módulo. Porém isso é muito ruim, pois, dependendo do método que estivermos usando ela poderá ser sobrescrito sem sabermos disso, o que colabora na dificuldade de conseguirmos encontrar algum erro no código. 
    
    Além disso, se tivermos um conjunto de módulos que estão importados da forma acima, acaba dificultando em entender qual método está vindo de qual módulo.

    Logo, o recomendável, é que sempre que formos importar algum método diretamente do módulo, que seja feito de forma seletiva.

Link para leitura

    https://stackoverflow.com/questions/2386714/why-is-import-bad

## Aula 51 - Modularização - Entendendo os seus próprios módulos e sys.path no Python:
Vamos abordar sobre a modularização do código. Ou seja, vamos criar um módulo próprio personalizado, independente dos módulos que já existem na linguagem Python.

Basicamente, a modiularização é uma forma de organizar cada classe ou código em um arquivo, em vez de colocar todos os códigos em um único arquivo. Em outras palavras, seria o seguinte. Em qualquer sistema conseguimos realizar um esboço topológico da arquitetura desse sistema. Ou seja, vc consegue esboçar a arquitetura do sistema de forma simples e que bastaria entender o esboço simples para entender a funcionalidade do sistema inteiro. Só que esse esboço simples ela poderia estar em duas formas, uma inteiramente em um único arquivo, donde, dentro dela, esteja separado de forma didática ou não cada funcionalidade, o que é considerado de muita má prática, ou que cada funcionalidade esteja feita em cada arquivos e simplesmente a funcionalidade do sistema inteiro esteja sendo feito com base das relações entre tais arquivos.

Portanto, a ideia da modularização seria a segunda alternativa. Em outras palavras, vc organiza melhor as funcionalidades em cada arquivo de forma que fique mais fácil de compreender como o sistema inteiro funciona e que isso ajuda na manutenção e desenvolvimento da mesma.

Agora, vamos para a aplicação do coceito teórico acima. No Python, em qualquer caso, sempre, o primeiro módulo que é executado é o "__main__", podemos verificar isso chamando a classe "__name__" para identificar qual módulo está em funcionamento

    print('Este modulo, dentro do aula51.py, se chama ', __name__)

No caso, que tenha em mente que sempre o primeiro módulo que é executado pelo Python é o "__main__".

Agora, vamos tentar importar um outro módulo que é criado por vc ou parte dela. Uma coisa que sempre precisamos tomar cuidado seria no nome do módulo que vc queira colocar, pois isso correria o risco de colcarmos o nome de um módulo já existente no Python, o que ocorreria o problema de sobrescrição.

Vamos começar por uma importação simples onde o arquivo se encontra no mesmo nível do arquivo da aula51.py. No caso, criamos um arquivo "aula_51.py" e nela colocamos o seguinte

    print('Este modulo, dentro do aula_51.py, se chama ', __name__)

No caso, nos nomes dos módulos não podemos colocar espaços ou caracteres especiais como acentos, etc... Sempre elas precisam estar juntas com underscore em letras minúsculas.

Agora, voltando para o arquivo aula51.py, ao executarmos esse módulo, vamos ver que, será exibido o print dentro do arquivo aula51.py, primeiro, e, em seguida, a do arquivo aula_51.py. E o que o "__name__" vai exibir nos dois casos será diferente.

Além disso, vale ressaltar que o Python, no processo de importação de módulo, ela não é possível realizar busca dos arquivos externos a não ser que vc não especifique direito as paths para chegar até no arquivo desejado. Para isso, podemos ver isso usando o método path que tem dentro do módulo sys. Vamos importar no arquivo aula51.py o módulo sys e darmos o print no método dela

    import sys

    import aula_51

    print('Este modulo, dentro do aula51.py, se chama ', __name__)
    print(sys.path)
    print(*sys.path, sep='\n') # para melhorar a visualizacao

Note que, o "sys.path" ela mostra o caminho que foi feito para ser executado o "__name__" .

Da mesma forma, dentro do sys.path podemos incluir, por append(), uma path externa donde nessa path, na pasta final que estará sendo indicado, vc estará dizendo que existe um módulo Python que pode ser importado. Vc poderá testar na sua máquina como seguinte

    try:
        import sys
        sys.path.append('/Users/ltakashi/Documents/') # path que tenho dentro da minha maquina
    except ModuleNotFoundError:
        ...

    import helloWounderWorld

    import aula_51

    print('Este modulo, dentro do aula51.py, se chama ', __name__)
    print(*sys.path, sep='\n')

No caso, no sys.path acima eu adicionei uma path e dentro da pasta final dessa path criei um arquivo "helloWounderWorld.py" e dentro dela coloquei

    print('Hello WounderWorld!!!')

Indicando qual módulo python existente dentro da pasta "Documents" estou querendo importar.

Bom, não é comum realizarmos uma manipulação do tipo para trabalharmos. O comum é termos um arquivo python e ao redor dela, em níveis mais baixo dela ocorrer as alterações necessárias para conseguirmos trabalhar.

Link para leitura

    https://www.geeksforgeeks.org/sys-path-in-python/
    https://acervolima.com/sys-path-em-python/

## Aula 52 - Como importar coisas do seu próprio módulo (ponto de vista do __main__):
Lembrando, novamente, os níveis dos arquivos tem que estarem iguais ou abaixo do "__main__"!!! Se não, ficaria mais complicado conseguirmos montar toda a arquitetura do sistema!!

Vamos aprender a importar coisas do seu próprio módulo. Algo análogo de como foi feito nos módulos que foram importados ou métodos que importamos diretamente a partir dos módulos nativos que já vem com a linguagem Python.

Bom, já vimos na última aula, se importarmos o módulo inteiro, tudo que tiver dentro desse módulo será importado. Agora se vai ser ou não executado já é outra história. Vamos criar uma pasta "code-class-52" e dentro dela criamos o arquivo "aula52.py" que será o nosso arquivo principal, __main__, e no mesmo nível de arquivo dele criamos módulo "aula52_m.py".

No arquivo, aula52.py, colocamos o seguinte

    import aula52_m

    print('Este módulo, aula52.py, se chama: ', __name__)

E no arquivo, aula52_m.py, colocamos o seguinte

    print('Este módulo, aula52_m, se chama: ', __name__)

Bom, ao rodarmos o arquivo, aula52.py, vimos que até aqui nada de novidade. Vimos que o print que está dentro do módulo, aula52_m.py, já é executado no momento em que executamos o arquivo, aula52.py.

Agora, no arquivo, aula52_m.py, vamos criar uma variável

    print('Este módulo, aula52_m, se chama: ', __name__)

    variavel_modulo = 'Leonardo'

Se rodarmos o arquivo, aula52.py, vamos ver só o print que está no arquivo, aula52_m.py. Como vamos acessar essa variável? 

A resposta é da mesma forma como acessamos os métodos dos módulos nativos do Python. Ou seja, acessamos da seguinte forma, no arquivo, aula52.py

    import aula52_m

    print('Este módulo, aula52.py, se chama: ', __name__)
    print(aula52_m) # Uma forma de saber de qual path esse módulo está vindo
    print(aula52_m.variavel_modulo)

Agora, da mesma forma que vimos nos módulos nativos do Python, temos uma forma de importamos somente os métodos ou variáveis definidas dentro daquele módulo da seguinte forma, no arquivo, aula52.py

    import aula52_m
    from aula52_m import variavel_modulo

    print('Este módulo, aula52.py, se chama: ', __name__)
    print(aula52_m) # Uma forma de saber de qual path esse módulo está vindo
    print(aula52_m.variavel_modulo)
    print(variavel_modulo)

Da mesma forma que se definimos os métodos, funções que ficam dentro de um objeto/módulo, a forma como vamos usa-las é o mesmo que vimos nos módulos nativos que Python. No caso, no arquivo, aula52_m.py, colocamos 

    print('Este módulo, aula52_m, se chama: ', __name__)

    variavel_modulo = 'Leonardo'

    def soma(x, y):
        return x + y

E assim no arquivo, aula52.py, temos

    import aula52_m
    from aula52_m import soma, variavel_modulo

    print('Este módulo, aula52.py, se chama: ', __name__)
    #print(aula52_m)
    print(aula52_m.variavel_modulo)
    print(variavel_modulo)
    print(aula52_m.soma(2, 3))
    print(soma(3, 4))

Claro que, assim como vimos para os módulos nativos, conseguimos apelidar os módulos personalizados que importamos, no arquivo, aula52.py

## Aula 53 - Recarregando módulos, importlib e singleton:
Vamos aprender a recarregar os módulos aqui.

Vamos criar uma pasta "code-class-53" e dentro dela iremos criar dois arquivos "aula53.py" e "aula53_m.py". Daí, vamos realizar a importação do módulo, aula53_m.py, como fizemos nas últimas duas aulas anteriores para o módulo principal, aula53.py.

Por começo, no módulo, aula53_m.py, colocamos

    print(123)

Até agora nada de novo. Em seguida, vamos colocar no módulo, aula53_m.py, a seguinte variável

    variavel = 'Leonardo'

Agora, no módulo, aula53.py, vamos tentar realizar o seguinte

    import aula53_m

    print(aula53_m.variavel)

    for i in range(10):
        import aula53_m

    print('Fim')

Note que, o print que está dentro do módulo, aula53_m.py, não está sendo exibido nas dez interações do for. O for, por exemplo, ela está sim iterando, bastaria dar um print no índice "i" que está percorrendo de 0 à 9.

Isso porque a importação de módulos elas são um tipo singleton. O que é isso?

Basicamente, o singleton é algo que a existência dela seja única naquele programa. Em outras palavras, quando importamos algum módulo, essa importação fica guardado na memória do processador de modo que vc não precisa importar novamente sempre que for necessário realizar o uso dela. Isso entra dentro do padrão de eficiência para economizar espaço na memória.

Entretanto, existem cenários em que vc precisa recarregar alguns módulos já importados. Não é algo muito comum, porém, em raras ocasiões é necessário realizar o recarregamento do módulo. Para isso, usamos um outro módulo para possibilitar esse recarregamento que seria o importlib. No caso, no arquivo, aula53.py, importamos o módulo

    import importlib

    import aula53_m

    print(aula53_m.variavel)

    for i in range(10):
        importlib.reload(aula53_m)

    print('Fim')

No caso, a cada chamada desse reload dentro do módulo importlib, iremos recarregar o módulo aula53_m.py.

Bom, qual a necessidade disso? Para entendermos isso, vamos ativar no terminal o modo iterativo em Python. Ou seja, pelo terminal, vai até a pasta code-class-53, e nela joga o seguinte comando

    python -i aula53.py

Vamos ver que nela irá o arquivo e ficará no modo interactive Python. Feito isso, no módulo, aula53_m.py, realizamos a seguinte alteração

    variavel = 'Leonardo 1'

Daí, no modo interactive Python ainda ativo, em ">>>" jogamos o seguinte comando

    aula53_m.variavel

Será exibido o antigo valor

    Leonardo

E não o atual.

Para isso que serve o reload do método importlib, pois ela irá recarregar o módulo, aula53_m.py, de modo que vc irá conseguir verificar a alteração feita nela. Joga de novo, no '>>>', o comando

    importlib.reload(aula53_m)

Em seguida, acessamos a variável de novo, '>>> aula53_m.py'. Verá que a alteração feita no módulo, aula53_m.py, agora está sendo considerado.

Para sair do modo interactive Python, basta colocar o comando 'quit()'.

Bom, precisa fazer tudo isso só para recarregar o módulo? Não!

No caso, a cada mudança que eu realizar no módulo, aula53_m.py, se eu recompilar novamente o módulo, aula53.py, seja ela pelo terminal ou diretamente no arquivo ou numa aplicação, refresh page, conseguimos considerar as alterações que ocorreram no outro módulo.

Bom, a moral da história é que vc tem que entender que os módulos Pythons são recarregados uma única vez, o que define a natureza de coisas que são chamados singletons em programação!

Link para leitura:

    https://refactoring.guru/pt-br/design-patterns/singleton/python/example
    https://docs.python.org/3/library/importlib.html
    https://realpython.com/lessons/reloading-module/
    https://stackoverflow.com/questions/18500283/how-do-you-reload-a-module-in-python-version-3-3-2

## Aula 54 - Introdução aos packages (pacotes) em Python:
Bom, até agora, criamos vários módulos e realizamos os devidos estudos acima dele.

Mas, agora, vamos introduzir o conceito de pacotes (packages) que seria o caso de uma pasta que carrega varios módulos.

Para isso, vamos criar o arquivo principal, aula54.py, e no mesmo nível desse arquivo vamos criar uma pasta chamado "aula54_p" e dentro dessa pasta vamos criar um arquivo com o nome "modulo.py".

Agora, no arquivo principal/raiz, aula54.py, vamos importar o módulo que está dentro do pacote, aula54_p. Para isso, vamos colocar o seguinte

    import aula54_p.modulo

Agora, no módulo, modulo.py, nela definimos o seguinte

    def soma_do_modulo(x, y):
        return x + y

Bom, agora, para conseguirmos usar dos recursos definidos dentro do módulo, modulo, é a mesma coisa como vimos nas aulas anteriores, no arquivo, aula54.py, colocamos

    import aula54_p.modulo

    print(aula54_p.modulo.soma_do_modulo(2, 3))

Daí, podemos verificar que estamos usando o método que definimos dentro do módulo, modulo.

Para mais detalhes de como está relacionado e qual arquivo é o main, vamos colocar o seguinte

    from sys import path

    import aula54_p.modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))

Bom, ao rodarmos o arquivo, notamos que o print(*path, sep='\n') ela irá mostrar todos as paths reconhecendo se tem ou não algum módulo python definido nela.

Da mesma forma, podemos importar o método diretamente dentro do módulo que definimos

    from sys import path

    import aula54_p.modulo
    from aula54_p.modulo import soma_do_modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))

Conseguimos, também, apelidar usando alias, "as".

Agora, uma outra curiosidade que temos, é importar somente o módulo inteiro dentro de um pacote. No caso, para isso realizamos o seguinte

    from sys import path

    import aula54_p.modulo
    from aula54_p import modulo
    from aula54_p.modulo import soma_do_modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))
    print(modulo.soma_do_modulo(4, 5))

No caso, no "from aula54_p import modulo", vc está conseguindo importar o módulo inteiro, modulo. E a forma de usarmos os métodos definidos dentro desse módulo, modulo, é usando o name space.

Bom, daí temos outras formas de importar que é similar ao que vimos nas três últimas aulas.

    from sys import path

    import aula54_p.modulo
    from aula54_p import modulo
    from aula54_p.modulo import soma_do_modulo
    from aula54_p.modulo import *

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))
    print(modulo.soma_do_modulo(4, 5))

Onde, vimos que a forma de importar "from aula54_p.modulo import *" é considerada de má prática. Porém, no cenário em que estamos, que temos liberdade de criar um pacote e módulo personalizado, caso importamos por essa prática considerada ruim, conseguimos selecionar os tipos de recursos que podem ser importados usando a sintaxe "__all__". No caso, no módulo, modulo, colocamos o seguinte

    __all__ = [
        'variavel'
    ]

    print('Este modulo, modulo.py, tem o nome: ', __name__)

    variavel = 'Leonardo'

    def soma_do_modulo(x, y):
        return x + y

Ao colocarmos, dentro da lista __all__, a variavel, na forma de importação, from aula54_p.modulo import *, o "tudo" que conseguimos importar desse módulo será considerado somente as que estejam dentro dessa lista "__all__".

Bom, claro que, se comentarmos a lista "__all__" inteirinha, vamos cuspir todo o recurso para a fora dessa lista e conseguiremos usar dentro da forma de importação de má prática, from aula54_p.modulo import *.

Link para leitura:

    https://realpython.com/python-modules-packages/

## Aula 55 - O ponto de vista do __main__ pode te confundir em módulos e pacotes Python:
Bom, nas últimas 4 aulas, vire e mexe estávamos insistindo de que sempre, mas sempre, o primeiro arquivo que é executado é o __main__, que é o arquivo que estará no nível mais alto e o primeiro que será sempre executado. Basta criarmos um arquivo aula55.py, que será o nosso arquivo main, e então colocarmos nela

    print(__name__)

Agora, vamos criar uma pasta "aula55_p" e dentro dela criamos dois arquivos "modulo.py" e "modulo_b.py".

Mas, primeiro, para entendermos melhor sobre o ponto de vista de "__main__". Ao analisarmos o sys.path do main sempre ela é mostrado de onde ela está sendo chamado. Mas existe uma outra forma de analisarmos isso tbm, que é usando o Python path. Basta jogar no terminal no diretório em que está o arquivo aula55.py, o comando

    python --help

Nela vc procura pelo nome "PYTHONPATH" e estará explicando o que estará sendo usando para identificar a path. Estará escrito "sys.path".

Bom, um cenário usual dentro de um pacote, aula55_p, é que dentro dela tenha mais e mais módulos. É muito difícil ver um pacote com apenas um único módulo. No caso, no módulo, modulo_b.py, vamos definir uma função

    def fala_oi():
        print('Hello WounderWorld!')

E esse módulo, poderia ser chamado por um outro módulo, modulo.py. Bastaria importar da forma usual

    from modulo_b import fala_oi

Agora, ao chegarmos no arquivo main, aula55.py, se tentarmos importar o módulo, modulo.py, vamos ter o seguinte

    from aula55_p.modulo import fala_oi

    print(__name__)

Você verá que teremos a opção de importar o "fala_oi" que é a função definida no módulo, modulo_b.py.

Por hora, vamos definir uma função simples dentro do módulo, modulo.py

    def soma_do_modulo(x, y):
        return x + y

Vamos tentar importar essa função acima junto com o, from modulo_b import fala_oi, no arquivo main, aula55.py

    from aula55_p import soma_do_modulo

    print(__name__)

E dessa forma tentamos compilar o arquivo. Você verá que o mesmo erro irá acontecer de quando tentamos compilar na forma, from aula55_p.modulo import fala_oi

    ModuloNotFoundError: No module named 'modulo_b'

O motivo desse erro acontecer, seria por conta de que, quando tentamos importar pela forma, from aula55_p,modulo import soma_do_modulo, do ponto de vista do arquivo main, aula55.py, visto que o módulo, modulo.py, está importando um outro modulo do mesmo nível dele, o main tentará importar o outro módulo que está sendo importando pelo módulo que o main está importando. Ou seja, se dentro dos módulos existentes dentro desse pacote, existir algum modulo que importa um outro modulo do mesmo nível, mas do ponto de vista desse módulo que esteja dentro do pacote, ao tentarmos importar esse módulo dentro desse pacote do ponto de vista do main, o mesmo irá tentar importar até o módulo que está sendo importado pelo módulo que o main está importando.

Portanto, para evitar que tais erros aconteça, sempre que formos importar algo de um modulo para outro temos que considerar do ponto de vista do main, neste caso a aula55.py. Assim, no módulo, modulo.py, vamos ter que realizar a seguinte alteração

    from modulo_b import fala_oi -> 
    
Assim, ao compilarmos o main, aula55.py, aquele erro não irá ser mais exibido e conseguimos carregar todos os módulos.

Temos a opção de conseguirmos, no modulo.py, simplesmente colocar apenas o ponto, em vez do nome da pasta inteira

    from .modulo_b import fala_oi

Porém, para possibilitar isso, precisamos realizar uma alteração no setting.json do Python da seguinte forma

    "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.insertSpaces": false,
    "editor.formatOnSave": true
    // "editor.codeActionsOnSave": {
    //   "source.fixAll": true,

Entretanto, por hora, vamos deixar do jeito que está para melhor conseguirmos entender o conceito.

Link para leitura

    https://docs.python.org/pt-br/3/library/__main__.html
    https://docs.python.org/3/reference/import.html

## Aula 56 - __init__.py é um arquivo de inicialização dos packages em Python:
Até agora, estudamos sobre pacotes em python.

Vamos ver que tais pacotes criados podem, isoladamente, serem inicializados via ini em python.

Antes de fazermos isso, vamos inicialmente criar os devidos diretórios.

No caso, vamos usar "aula56.py" como main e criamos o pacote "aula56_p" e, dentro dela, criamos dois módulos "modulo.py" e "modulo_b.py". Criamos, dentro da pasta aula56_p, um outro arquivo, que este será o arquivo de inicialização, que terá o nome "__init__.py" (dunder init).

No módulo, modulo.py, colocamos o seguinte

    variavel = 'Alguma coisa'

    def soma_do_modulo(x, y):
        return x + y

    nova_variavel = 'OK'

No módulo, modulo_b.py, vamos colocar o seguinte

    def falar_oi():
        print('Hello Wounderworld!')

Agora, para o começo, dentro do main, aula56.py, vamos importar apenas o pacote

    import aula56_p

Daí, no arquivo de inicialização, __init__.py, nela iremos colocar o seguinte

    print(
        'Você importou ', __name__
    )

Ao compilarmos o arquivo main, aula56.py, vamos ver que o print do arquivo init será compilado.

No caso, o que podemos fazer no init?

Basicamente, qualquer coisa que executarmos dentro do init vai ficar disponível para o package. Ou seja, podemos usar desse arquivo para "enganar" o Python. Por exemplo, se eu definir uma função dentro do init da seguinte forma

    def dobra(x):
        return x * 2

No arquivo main podemos chamar essa função da seguinte forma

    import aula56_p

    print(aula56_p.dobra(3))

Ou seja, acabamos de usar do pacote, aula56_p, como se fosse um módulo, aqui que eu "engano" o Python.

Bom, e não para por aí. Usando dessa mesma lógica, dentro do init podemos disponibilizar os dois módulos da seguinte forma

    from aula56_p.modulo import variavel, nova_variavel, soma_do_modulo

Daí, agora, no aquivo main, conseguimos ver que podemos realizar a mesma coisa que fizemos antes, tratar o pacote, aula56_p, como se fosse um módulo para chamar tais métodos e variáveis definidas dentro do módulo, modulo.py

    import aula56_p

    # print(aula56_p.dobra(3))
    print(aula56_p.nova_variavel)
    print(aula56_p.variavel)
    print(aula56_p.soma_do_modulo(3,4))

Ou, se quisermos, conseguimos realizar a importação de um método em particular da forma usual, tratando o aula56_p como um módulo também

    from aula56_p import soma_do_modulo

    print(soma_do_modulo(2, 3))

Isso graças ao que configuramos no init.

Além disso, no init, havíamos feito a importação 

    from aula56_p.modulo import variavel, nova_variavel, soma_do_modulo

Podemos dizer que aqui é um dos pouquíssimos casos em que podemos realizar a importação que é considerada de má prática

    from aula56_p.modulo import *

O mesmo para o outro módulo, modulo_b.py.

Uma outra coisa interessante, seria em trocarmos os nomes simbólicos de forma dinâmica. No caso, ao olharmos na aula56.py e realizarmos a importação

    from aula56_p import falar_oi, soma_do_modulo

    print(soma_do_modulo(5, 6))
    falar_oi()

vemos que a função "falar_oi()" é uma função que é importado pelo modulo_b. Ao clicarmos no "falar_oi()" com o botão direito do mouse e escolhermos a opção "Rename Symbol" e nela colocarmos algum outro nome, vamos ver que esse nome está alterado até no módulo, modulo_b.py, sem a necessidade de realizarmos isso manualmente.

Link para leitura

    https://www.geeksforgeeks.org/dunder-magic-methods-python/
    https://mathspp.com/blog/pydonts/dunder-methods
    https://stackoverflow.com/questions/2386714/why-is-import-bad

## Aula 57 e 58 - Proposta de 3 exercícios em um e solução:
Seguir com o enunciado

    # copy, sorted, produtos.sort
    # Exercícios
    # Aumente os preços dos produtos a seguir em 10%
    # Gere novos_produtos por deep copy (cópia profunda)
    produtos = [
        {'nome': 'Produto 5', 'preco': 10.00},
        {'nome': 'Produto 1', 'preco': 22.32},
        {'nome': 'Produto 3', 'preco': 10.11},
        {'nome': 'Produto 2', 'preco': 105.87},
        {'nome': 'Produto 4', 'preco': 69.90},
    ]

    # Ordene os produtos por nome decrescente (do maior para menor)
    # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

    # Ordene os produtos por preco crescente (do menor para maior)
    # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

## Aula 59 e 60 - Exercício e Solução - Adiando execução de funções:
Seguir com o enunciado

    # Exercício - Adiando execução de 
    # Bom, temos as funções abaixo, mas se executarmos terá um problema
    # O que eu quero é que vc corrija esse problema de modo que
    # para a soma, sempre ocorrerá uma soma de 5
    # para a multiplicação, sempre ocorrerá a multiplicação de 10
    # Basicamente, o que está acontecendo aqui é que a função soma e mutiplica está se precipitando
    # antes mesmo de definir um valor para y.
    # Ou seja, o que eu quero que vc faça seria em aditar a executação, para ter tempo em definir o y
    # e, finalmente, conseguirmos executar.
    def soma(x, y):
        return x + y


    def multiplica(x, y):
        return x * y


    def criar_funcao(funcao, *args):
        return funcao(*args)


    soma_com_cinco = criar_funcao(soma, 5)
    multiplica_por_dez = criar_funcao(multiplica, 10)

Foi usado clousure para resolver esse problema.

## Aula 61 - Variáveis livres + nonlocal (locals, globals):
Vamos falar de variáveis livres e nonlocal.

- Variável livre:

    Vamos começar pela definição do que seria uma variável livre:

        Uma variável livre é uma variável referenciada em uma função, que não é nem uma variável local nem um argumento daquela função.

    Vamos pegar um exemplo padrão disso

        def fora():
            a = 1

            def dentro():
                return a
            return dentro
        
        print(fora())
        print(fora()())

    No caso, nma função "fora()" definido acima a variável livre é o "a" que está sendo definido dentro dessa função, pois ela não está sendo definido dentro do escopo da função "dentro()".

    Claro, podemos dinamizar essa variável livre

        def fora(x):
            a = x

            def dentro():
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    No caso, agora, a variável livre "a" está dinamizada, pois podemos colocar o valor que quisermos.

    Para conferirmos isso, podemos usar as funções nativas do python o "locals" e "globals"

        def fora(x):
            a = x

            def dentro():
                print(locals())
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Donde, o "locals()" ela confere, quais variáveis são locais.

    Além disso, para definitivamente, sabermos se, de fato, "a" é ou não uma variável livre, podemos usar o "__code__.co_freevars"

        def fora(x):
            a = x

            def dentro():
                print(locals())
                print(dentro.__code__.co_freevars)
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Podemos usar o "globals" para verificarmos quais são as variáveis globais

        print(globals())

        def fora(x):
            a = x

            def dentro():
                print(locals())
                print(dentro.__code__.co_freevars)
                return a
            return dentro
        
        dentro1 = fora(10)
        dentro2 = fora(20)

        print(dentro1())
        print(dentro2())

    Seguir link de leitura:

        https://www.codesansar.com/python-programming/local-global-free-variables-example.htm#:~:text=In%20Python%2C%20there%20exist%20another,is%20known%20as%20free%20variable.

        https://dunossauro.github.io/python-funcional/roteiros/08_closures_1_escopo.html

- nonlocal:

    Agora, visto que aprendemos o conceito de variável livre acima, suponhamos que queiramos realizar um processo iterativo usando a variável livre como seguinte

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))
    
    Bom, inicialmente, a função acima não tem nada de novidade, pois seja qual for o "valor_a_concatenar" que iremos colocar, vamos sempre retonar o valor final.

    Mas, agora, suponhamos que queremos realizar o seguinte

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                valor_final += valor_a_concatenar
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))

    No caso, a ideia é que ela irá retonar para cada print os respectivos strings concatenados. Porém, no formato como está acima, isso irá retornar um erro.

    O motivo disso, estaria por conta do escopo. Ou seja, a variável livre "valor_final" não é do escopo da função "interna". Podemos apenas ler o valor dessa variável livre, mas não podemos alterar ela. Por isso, para corrigirmos esse problema, precisamos falar para o Python de que essa variável livre, valor_final, não é do escopo da função "interna" e é aí que entra o uso da sintaxe "nonlocal"

        def concatenar(string_inicial):
            valor_final = string_inicial

            def interna(valor_a_concatenar):
                nonlocal valor_final
                valor_final += valor_a_concatenar
                return valor_final
            return interna

        c = concatenar('a')
        print(c('b'))
        print(c('c'))
        print(c('d'))

    O uso é muito parecido com a sintaxe "global" para dizer que uma variável é global.

    Link para leitura

        https://www.toppr.com/guides/python-guide/references/methods-and-functions/global-local-nonlocal-variables/python-global-local-and-nonlocal-variables-with-examples/#:~:text=In%20python%2C%20nonlocal%20variables%20refer,nor%20in%20the%20global%20scope.&text=Here%2C%20the%20inner()%20function%20is%20nested%20in%20nature.

        https://pt.stackoverflow.com/questions/250362/qual-a-diferen%C3%A7a-de-global-e-nonlocal-no-python

## Aula 62 - Funções decoradoras em geral:
Vamos aprender sobre funções decoradoras e decoradores.

Basicamente, funções decoradoras/decoradores, como o nome já disse, são funções que decora outras coisas. No caso, sempre que vc estiver utilizando essa função decoradora, vc estará recebendo essa coisa e decorando essa coisa e mudando o valor dela, ou não, ou nem retornando nada.

    Decorar = Adicionar / Remover/ Restringir / Alterar

Vamos começar com um exemplo básico

    def inverte_string(string):
        return string[::-1]

    invertida = inverte_string('Leonardo')
    print(invertida)

Lembre-se, em programação, uma boa prática fundamental no processo de compilação e eficiência está no quesito de obedecer a regra "Princípio de Responsabilidade Única (Single Responsability Principle - SRP)". Em outras palavras, se um determinado objeto está fazendo mais do que o necessário, então está errado. Você precisa dividir esse objeto de modo que separe cada finalidade para cada lugar, de forma organizada.

No caso, esse conceito um pouco avançado, como quero colocar isso aqui no exemplo que demos acima. No caso, suponhamos que no lugar de uma string colocamos uma numeração

    def inverte_string(string):
        return string[::-1]

    invertida = inverte_string(123)
    print(invertida)

Com certeza, isso iria resultar em um erro. Masl, então, como iremos tratar? Seguindo a definição do SRP, teríamos que criar mais uma função que trate, especificamente, esse problema, como seguinte

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print('Ok, agora você foi decorado!')
            return resultado
        return interno
    
    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro(123)
    print(invertida)

E é aqui, o momento que entra em jogo a prática da função decoradora. No caso, estamos decorando uma função via "criar_funcao".

O estudante poderia muito bem pensar o seguinte "Ué? Não bastava colocar um if dentro da função inverte_string? Qual é a finalidade de ter que usar uma função decoradora?"

Bom, a resposta para essa pergunta está que ela serviu, antes do passo de executar definitivamente a função, se todos os critérios estão satisfeitos, o que difere de realizar a tal conferencia dentro da execução da função. A vantagem disso, está em otimizar o processo sem a necessidade de ter que compilar uma função, visto que algumas hipóteses não está sendo satisfeitas.

Link para leitura:

    https://www.hashtagtreinamentos.com/decorators-no-python?gad=1&gclid=CjwKCAjwg4SpBhAKEiwAdyLwvAFakfQTcdMgNmUSBm-C9p2qBeA-S3SJLyGWaLH2Cv6wCXME1rBUWRoCV9EQAvD_BwE
    
    https://pt.stackoverflow.com/questions/23628/como-funcionam-decoradores-em-python

    https://www.datacamp.com/tutorial/decorators-python

    https://www.geeksforgeeks.org/decorators-in-python/

Link para leitura - SRP:

    https://www.freecodecamp.org/news/solid-principles-single-responsibility-principle-explained/#:~:text=The%20Single%20Responsibility%20Principle%20(SRP,only%20one%20reason%20to%20change%22.&text=The%20class%20above%20violates%20the%20single%20responsibility%20principle.

    https://en.wikipedia.org/wiki/Single-responsibility_principle

    https://www.devmedia.com.br/arquitetura-o-principio-da-responsabilidade-unica/18700#:~:text=O%20Mandamento%20do%20princ%C3%ADpio%20da,ela%20n%C3%A3o%20segue%20este%20princ%C3%ADpio.

## Aula 63 - Decoradores em Python (@syntax_sugar):
Bom, visto que aprendemos funções decoradoras, vamos precisar aprender sobre decoradores.

Bom, vamos continuar com o mesmo código da última aula

    # Funções decoradoras e decoradores
    # Decorar = Adicionar / Remover/ Restringir / Alterar
    # Funções decoradoras são funções que decoram outras funções
    # Decoradores são usados para fazer o Python
    # usar as funções decoradoras em outras funções.

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro('123')
    print(invertida)

No caso, iremos aplicar os conceitos de decoradores em cima desse código. Mas, claro, antes de tudo, o que são decoradores?

Decoradores em Python são conhecidos como Syntax Sugar (Açúcar Sintático). Em outras palavras, os decoradores em Python são recursos que facilitam a utilização das funções decoradoras em python!

Como iremos usar esse Syntax Sugar? No caso, no código abaixo

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro('123')
    print(invertida)

vemos que estamos precisando definir uma variável "inverte_string_checando_parametro" para conseguirmos guardar a função decoradora "criar_funcao" para que, finalmente, ela seja usada pela função "inverte_string". No caso, o Syntax Sugar irá tirar esse trabalho. Ou seja, em vez de criar tais variáveis, vamos conseguir apontar para o "inverte_string" considerar o uso da função "criar_funcao", sem a necessidade de criarmos essa variável, da seguinte forma

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    @criar_funcao
    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    invertida = inverte_string('123')
    print(invertida)

Note que, não tivemos o trabalho de ter que criar uma variável "inverte_string_checando_parametro" e usarmos a função decoradora "criar_funcao" para, dentro dela, colocarmos como argumento a função "inverte_string" que é o momento que decora essa função, para, por fim, por via da outra variável, invertida, conseguirmos ver o que foi executado dentro dela, por via do print. No caso, o syntax sugar ajuda a tirar esse trabalho de forma a conseguirmos apontar simplesmente qual função vamos querer que a nossa função decoradora decore.

Ou seja, bastaria escolher qual função vc quer que ela seja decorado pela função decoradora e colocar a sintaxe "@nome_da_funcao_decoradora" em cima da função que vc queira decorar para que, no uso dela, vc precise chamar somente o nome da função que foi decorado.

Outra questão curiosa é o seguinte

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    @criar_funcao
    def inverte_string(string):
        print(f'{inverte_string.__name__}')
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    invertida = inverte_string('123')
    print(invertida)

Ao colocarmos o print "print(f'{inverte_string.__name__}')" dentro da função "inverte_string", vamos ver que o que é retornado é o nome "interno", que é o nome da função que é definida dentro da função decoradora "criar_funcao". Ou seja, o nome não é da função que foi decorada, "inverte_string". Agora, se eu comento a sintaxe "@criar_funcao", o nome da função decorada, volta a ser "inverte_string".

Bom, essa parte é o básico de uma função decorador. Na próxima aula iremos um uso mais avançado sobre funções decoradores.

Links para leituras

    https://pythonacademy.com.br/blog/domine-decorators-em-python

    https://www.geeksforgeeks.org/decorators-in-python/

    https://pt.stackoverflow.com/questions/23628/como-funcionam-decoradores-em-python#:~:text=Uma%20fun%C3%A7%C3%A3o%20em%20Python%20%C3%A9,par%C3%A2metro%20e%20retorna%20uma%20fun%C3%A7%C3%A3o.

    https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1

## Aula 64 - Decoradores com parâmetros:
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

## Aula 65 - Ordem de aplicação dos decoradores:
Falta comentarmos sobre a ordem de aplicação dos decoradores.

No caso, podemos utilizar mais de um decorador numa função. Disso, nos permite definir a ordem de execução de tais decoradores.

Vamos partir do seguinte código, que é da última aula

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

    multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

    dez_mais_cinco = soma (10, 5)
    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)
    print(dez_mais_cinco)

No caso, vamos mudar os nomes primeiro

    # Decoradores com parametros
    def parametros_decorador(nome):
        def decorador(func):
            print('Decorador: ', nome)

            def sua_nova_funcao(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                final = f'{res} {nome}'
                return final
            return sua_nova_funcao
        return decorador

    @parametros_decorador(nome='Segundo')
    @parametros_decorador(nome='Primeiro')
    def soma(x ,y):
        return x + y

    dez_mais_cinco = soma (10, 5)
    print(dez_mais_cinco)

Ao executarmos o trecho acima, iremos conseguir ver que, no print, será exibido de forma crescente de primeiro para segundo, mesmo que a ordem esteja o inverso acima. Além disso, como prova de que podemos fabricar várias funções decoradoras, elas ficam guardadas dentro da fábrica, se não não seria possível realizar o processo de concatenação como é exibido "15 Primeiro Segundo".

    # Decoradores com parametros
    def parametros_decorador(nome):
        def decorador(func):
            print('Decorador: ', nome)

            def sua_nova_funcao(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                final = f'{res} {nome}'
                return final
            return sua_nova_funcao
        return decorador

    @parametros_decorador(nome='5')
    @parametros_decorador(nome='4')
    @parametros_decorador(nome='3')
    @parametros_decorador(nome='2')
    @parametros_decorador(nome='1')
    def soma(x ,y):
        return x + y

    dez_mais_cinco = soma (10, 5)
    print(dez_mais_cinco)

A ordem é inversa. Será exibido "15 1 2 3 4 5".

## Aula 66 e 67 - Exercício e Solução - Unir listas + zip e zip_longest do intertools:
Seguir o enunciado

    # Exercício - Unir listas
    # Crie uma função zipper (como o zipper de roupas)
    # O trabalho dessa função será unir duas
    # listas na ordem.
    # Use todos os valores da menor lista.
    # Ex.:
    # ['Salvador', 'Ubatuba', 'Belo Horizonte']
    # ['BA', 'SP', 'MG', 'RJ']
    # Resultado
    # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

Vamos aprender, tbm, sobre o módulo itertools donde iremos aprender os métodos zip e zip_longest.

Primeiro, irei colocar a forma como o professor solucionou o problema

    def zipper(lista1, lista2):
        intervalo_maximo = min(len(lista1), len(lista2))
        return [
            (lista1[i], lista2[i]) for i in range(intervalo_maximo)
        ]

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zipper(l1, l2))

Bom, existe um método nativo do python que já realiza criações sem a necessidade de criarmos uma função da forma como temos acima. Esse método se chama "zip"

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zip(l1, l2))
    print(list(zip(l1, l2)))

Temos, também, um módulo do Python que se chama itertools e dentro dela um método chamado "zip_longest", donde ele faz a mesma coisa que o zip com uma única diferença. Em vez de pegar a menor lista, que nem o zip, ele pega a maior lista.

    from itertools import zip_longest

    l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
    l2 = ['BA', 'SP', 'MG', 'RJ']
    print(zip(l1, l2))
    print(list(zip(l1, l2)))
    print(zip_longest(l1, l2))
    print(list(zip_longest(l1, l2)))

## Aula 68 e 69 - Exercícios e Solução - somando duas listas:
Seguir o enunciado

    """
    Considerando duas listas de inteiros ou floats (lista A e lista B)
    Some os valores nas listas retornando uma nova lista com os valores somados:
    Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
    menor.
    Exemplo:
    lista_a     = [1, 2, 3, 4, 5, 6, 7]
    lista_b     = [1, 2, 3, 4]
    =================== resultado
    lista_soma  = [2, 4, 6, 8]
    """
    lista_a = [10, 2, 3, 40, 5, 6, 7]
    lista_b = [1, 2, 3, 4]
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)

    # lista_soma = []
    # for i in range(len(lista_b)):
    #     lista_soma.append(lista_a[i] + lista_b[i])
    # print(lista_soma)

    # lista_soma = []
    # for i, _ in enumerate(lista_b):
    #     lista_soma.append(lista_a[i] + lista_b[i])
    # print(lista_soma)

No exercício anterior, fizemos a soma de duas listas usando várias soluções diferentes.

Uma delas foi usando zip para unir duas listas e utilizar list comprehension para fazer a conta:

    lista_a = [10, 2, 3, 4, 5]
    lista_b = [12, 2, 3, 6, 50, 60, 70]
    lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
    print(lista_soma)  # Saída: [22, 4, 6, 10, 55]

O problema é que zip só une as listas até o tamanho da menor lista (como proposto no exercício).

Uma outra possibilidade é usar zip_longest para capturar os valores da lista maior.

A ideia é a mesma, veja:

    from itertools import zip_longest
    
    lista_a = [10, 2, 3, 4, 5]
    lista_b = [12, 2, 3, 6, 50, 60, 70]
    lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
    print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.

## Aula 70 - count é um iterador sem fim (itertools):
Vamos mostrar um contador infinito em Python, que se chama "count" que é um método dentro do módulo itertools.

Basicamente, o "count" ele é um contador infinito e um iterador sem fim.

Vamos, por começar, a importar tal método

    from itertools import count

    c1 = count()

    print(next(c1))
    print(next(c1))

Vamos conseguir ver que irá retornar 0 e 1.

Bom, se vc lembra de algumas longas aulas anteriores, existem formas de conferir se um determinado método ele é um iterador e iterável

    from itertools import count

    c1 = count()

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

Coisa que, no r1 = range(10), podemos ver que não é true em todos

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

Ou seja, conseguimos ver que o "range" ele é um iterável, mas não é o iterador.

Agora, lembrando que o método "count()" é um iterável infinito, então se usarmos o "for" de forma imprecisa, irá entrar num loop infinito, o que vc deverá tomar cuidado

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    for i in c1:
        if i >= 100:
            break

        print(i)

Perceba que a contagem do for acima está começando pelo 2, pois já foi feito a iteração pelo next nos dois prints acima.

Bom, se o seu computador não for muito possante, isso poderia travar o seu computador se não colocarmos algum break dentro do for iterando o count(), visto que esse método é um iterador/contador infinito.

Diferentemente de range, que sempre que usamos ele, precisamos definir um fim para ele

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    for i in c1:
        if i >= 100:
            break

        print(i)
    print()
    for j in range(100):
        print(j)

Bom, visto que no range, também, é possível definir o início tbm. O mesmo vale para o count

    from itertools import count

    c1 = count(10)
    r1 = range(10, 100)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    print('count')
    for i in c1:
        if i >= 100:
            break

        print(i)
    print()
    print('range')
    for j in r1:
        print(j)

Da mesma forma que conseguimos definir os steps no range, no sentido de iterar apenas os múltiplos de número $`n`$, sendo $`n\in\mathbb{N}`$.

Da mesma forma que podemos definir direito para quem começa ou qual será o step

    from itertools import count

    c1 = count(10)
    c2 = count(step=5, start=10)
    r1 = range(10, 100)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    print('count')
    for i in c1:
        if i >= 100:
            break

        print(i)

    for k in c2:
        if k >= 100:
            break

        print(k)
    print()
    print('range')
    for j in r1:
        print(j)

## Aula 71 - Combinations, Permutations e Product - Itertools:
Vamos ver como utilizar as ferramentas matemáticas de contagem básica que aprendemos no ensino médio.

## Aula 72 - groupby - agrupando valores (itertools):

## Aula 73 - map, partial, GeneratorType e esgotamento de Iterators:

## Aula 74 - filter é um filtro funcional:

## Aula 75 - reduce - faz a redução de um iterável em um valor:

## Aula 76 - Funções recursivas, recursividade e Stack Overflow:

## Aula 77 - Limite de recursão e cuidados com funções recursivas:

## Aula 78 - O que são ambientes virtuais? (venv):

## Aula 79 - Como criar o seu ambiente virtual com venv:

## Aula 80 - Ativando e desativando o meu ambiente virtual venv:

## Aula 81 - pip - instalando pacotes e bibliotecas:

## Aula 82 - Criando e usando um requirements.txt:

## Aula 83 - Criando arquivos com Python + Context Manager with:

## Aula 84 - with open (context manager) e métodos úteis do TextIOWrapper:

## Aula 85 - Modos de abertura de arquivo e encoding com with open:
