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

## Aula 06 - (Parte 2) Escopo de funções e módulos em Python + global:

## Aula 07 - Retorno de valores das funções (return):

## Aula 08 - (Parte 1) *args para quantidade de argumentos não nomeados variáveis:

## Aula 09 - (Parte 2) *args para quantidade de argumentos não nomeados variáveis:

## Aula 10 - Exercícios com funções + Solução (prepare-se para pausar):

## Aula 11 - Higher Order Functions - Funções de primeira classe: