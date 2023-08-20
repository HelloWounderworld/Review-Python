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

Bom, o formato da função acima, ainda não é uma clousure. Mas, basicamente, já podemos ver que ela retorna a saudação que queremos fazer de forma correta. Agora, começando a implementar o clousure, que é criar uma funçõa que exeucta outra função, podemos realizar a seguinte modificação da função acima

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

- Une - União:

- intersecção & (intersection):

- diferença - complemento:

- diferença simétrica ^ - Itens que não estão em ambos - Complemento da união:

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

## Aula 53 - Recarregando módulos, importlib e singleton:

## Aula 54 - Introdução aos packages (pacotes) em Python:

## Aula 55 - O ponto de vista do __main__ pode te confundir em módulos e pacotes Python:

## Aula 56 - __init__.py é um arquivo de inicialização dos packages em Python:

## Aula 57 - Proposta de 3 exercícios em um:

## Aula 58 - Solução - Proposta de 3 exercícios em um:

## Aula 59 - Exercício - Adiando execução de funções:

## Aula 60 - Solução - Exercício - Adiando execução de funções:

## Aula 61 - Variáveis livres + nonlocal (locals, globals):

## Aula 62 - Funções decoradoras em geral:

## Aula 63 - Decoradores em Python (@syntax_sugar):

## Aula 64 - Decoradores com parâmetros:

## Aula 65 - Ordem de aplicação dos decoradores:

## Aula 66 - Exercício - Unir listas:

## Aula 67 - Solução do Exercício + zip e zip_longest do itertools:

## Aula 68 - Exercícios - somando duas listas:

## Aula 69 - Exercício solucionado - somando listas:

## Aula 70 - count é um iterador sem fim (itertools):

## Aula 71 - Combinations, Permutations e Product - Itertools:
