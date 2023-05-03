# Seção 3 - Iniciando na programação com Python (Lógica de Programação básica):

## Aula 01 - O que vamos aprender? Devo seguir essa seção?:
Vou revisar python!

## Aula 02 - Me ajude a produzir conteúdo gratuito:
Eu acredito que a educação deva ser gratuita, mas NINGUÉM valoriza conteúdo gratuito. Eu gostaria que você me ajudasse a mudar isso. Você pode começar me seguindo, curtindo, comentando e interagindo com o meu conteúdo gratuito na redes sociais.

YouTube: https://www.youtube.com/otaviomiranda

TikTok: https://www.tiktok.com/@otaviomirandabr

Instagram: https://www.instagram.com/otaviomirandabr/

Twitter: https://twitter.com/otaviomirandabr

Discord

Com a intenção de conectar os alunos, criamos um servidor no discord 

    https://discord.gg/67PyPrXhwz.

A ideia é simplesmente conectar alunos, fazer networking, trocar informações e coisas relacionadas.

Para tirar dúvidas com o instrutor, você ainda deve usar o sistema de perguntas e respostas da Udemy, visto que o grupo é voltado para relações entre alunos somente.

Veja todos os meus cursos em: 

    https://www.otaviomiranda.com.br/2017/meus-cursos/

Atenção: só para ficar claro, eu (Luiz Otávio) não participo ativamente dessa comunidade (ou quase nenhuma outra rede social).

Seguem ele pessoal!!

## Aula 03 - Criando meu primeiro módulo Python (*.py):
O formato da extensão python é .py

## Aula 04 - O interpretador do Python + comentários de código:
Vamos aprender a fazer comentário no arquivo python!

No caso, no arquivo aula03-04-05.py, a forma para realizarmos um comentário seria por três tipos

    # - Permite fazer comentário em uma linha, apenas

    """ """ - Permite fazer comentário em um conjunto de linhas

    ''' ''' - Permite fazer comentário em um conjunto de linha

Donde, a sua aplicação ficaria

    """
    DocString
    E escrever o que eu
    quiser
    asdfasdfd
    """

    ''' Usar para escrever suas notas '''
    print(123)  # Na frente

Agora, a forma para conseguirmos exibir alguma msg pelo terminal, usaremos o print, como podemos ver no código acima. Ao rodarmos o arquivo, vamos conseguir exibir a msg acima no terminal. Mas, lembre-se, o print ele funciona para ser exibido as coisas na tela.

## Aula 05 - Docstrings como comentários:
Mais sobre comentário, a forma de utilizar o """ """ e ''' '''.

No caso, as aspas, ", ele se comporta como comentário, mas temos que deixar claro que ele não é um comentário, pois o interpretador do python ele irá ler isso. No caso, a forma de comentar usando as aspas, é conhecido como DocString.

Agora, o aspas simples, tbm, serve para comentar, que também é uma DocString.

No caso, o DocString, ele pode ser usado como uma forma de anotar e, como será lido pelo interpretador python, ele ficará guardado na memória, diferente de comentar por # que será ignorado.

## Aula 06 - A função print:
Vamos conhecer melhor sobre a função print.

A função print é usada para exibir algo na tela. Como podemos ver no arquivo aula06.py dessa aula

    print(12, 34)

Quando queremos colocar mais de um argumento, separamos ela por vírgula e, além disso, para print feito em cada linha vc verá que será pulado as linhas que são exibidas pelo terminal tbm

    print(12, 34)
    print(56, 78)

Podemos definir a forma como separamos tbm. No caso, no print(12, 34), pelo fato de vc estar dividindo por vírgula, ocorre que o espaço se torna um separador natural. Mas, podemos definir um tipo de separador tbm usando o recurso chamado sep

    print(12, 34, sep='-')
    print(56, 78, sep="*")

No caso, o sep acima vc consegue definir com qual caractere vc quer que ocorra a separação entre 12 e 34 (assim como para 56 e 78). No caso, note que, o separardor, sep, ele aceita tanto aspas simples quanto dupla. Além disso, se por acaso fizermos sep="", ou seja, uma string vazio, isso indicará que estamos juntando os caracteres que queremos, na verdade, separar

    print(12, 34, sep='-')
    print(12, 34, sep='')
    print(56, 78, sep="*")

Podemos, também, colocar uma espécie de quebra de linha manual, usando  end, por exemplo

    print(12, 34, sep='-', end='\r\n')
    print(12, 34, sep='', end='\n')
    print(56, 78, sep="*", end='\n')

Nesse contexto, não irá acontecer nada, mesmo usando o end, visto a funcionalidade do print, como padrão. Mas existem cenários em que é neceesário ocorrer uma quebra de linha. Para certifcar que, de fato, o end, usando o \r e \n, serve para quebra de linha, coloquemos um outro tipo de caractere como

    print(12, 34, sep='-', end='##')
    print(56, 78, sep="*", end='\n')

Note que, no terminal não ocorreu a quebra de linha e nela foi mesclado o caracteres ##, poderia ser qualquer outro caractere para fazer o mesmo efeito.

Sempre que usarmos a função print, a declaração é toda em minúscula, ou seja, não é possível fazer Print().

## Aula 07 - Tipo str (string) - Introdução aos tipos de dados:
Vamos introduzir aos tipos de dados.

Vamos primeiro entender o que é a linguagem de programação Python.

Assim como o JavaScript, Python ela é uma linguagem de programação de tipagem dinâmica. O que difere com o JavaScript, é que, enquanto o Python essa tipagem dinâmica é forte, o JavaScript ela é de uma tipagemdinâmica fraca.

    https://www.treinaweb.com.br/blog/quais-as-diferencas-entre-tipagens-estatica-ou-dinamica-e-forte-ou-fraca

    https://pt.stackoverflow.com/questions/21508/qual-a-diferen%C3%A7a-entre-uma-linguagem-de-programa%C3%A7%C3%A3o-est%C3%A1tica-e-din%C3%A2mica

    https://medium.com/@alissoncs_/diferen%C3%A7as-entre-tipagens-est%C3%A1tica-din%C3%A2mica-fraca-e-forte-755e08d82caa

O que significa que uma linguagem de programação ser de tipagem dinâmica, significa que a linguagem em si já sabe que tipo de linguagem de programação está sendo passada para ela. No caso do Python, quando colocamos 

    print(1234)

O conteúdo de dentro, 1234, da função print, o python já conhece. O que difere, por exemplo, da linguagem de programação de tipagem estática, pois nela, sempre que vc colcoar algum valor, vc precisa declarar se ela é um number, string, boolean, etc...

Agora, nessa aula, objetivo é falar sobre strings. 

No caso, o que são strings?

Strings são textos que estão dentro de aspas, pode ser simples ou dupla, tanto faz.

    # Strings - Textos que vão dentro de aspas, pode ser simples ou duplas
    print('Hello WounderWordl!')
    print("Hello WounderWordl!")

A mesma lógica de aspas que eu estudei em JavaScript, aqui funciona tbm

    # Strings - Textos que vão dentro de aspas, pode ser simples ou duplas
    print('Hello WounderWordl!')
    print("Hello WounderWordl!")
    print("Hello 'WounderWordl!'")
    print('Hello "WounderWordl!"')
    print("Hello \"WounderWordl!\"")
    print('Hello \'WounderWordl!\'')

Quando rodamos o código acima, no terminal não conseguimos ver se foi usado o escape, \, ou não. Mas existe uma forma de vc conseguir exibir isso no terminal tbm

    print(r"Hello \"WounderWordl!\"")
    print(r'Hello \'WounderWordl!\'')

No caso, segundo o criador do python, esse "r" que usamos para poder exibir os escapes ele é usado muito para expressões regulares.

Uma outra coisa que precisa-se saber bem seria sobre quando vc cria uma documentação usando """ """ ou ''' ''', os DocStrings. Eles são strings tbm.

## Aula 08 - Tipo int e float (números) - Introdução aos tipos de dados:
Vamos entender melhor sobre o dado number, em python.

No caso, temos dois tipos, int e float.

- int - Número inteiro: O tipo int representa qualquer número positivo ou negativo. int sem sinal é considerado positivo.

- float - Número com ponto flutuante: O tipo float representa qualquer número positivo ou negativo com ponto flutuante. O float sem sinal é considerado positivo.

Para conferirmos se um dado número é um tipo int ou float, usamos o type

- type - A classe type mostra o tipo que o Python inferiou ao valor.

Como prova disso, no arquivo aula08.py temos o seguinte

    # Tipo int
    print(11)
    print(-11)
    print(0)

    # Tipo float
    print(1.1)
    print(10.11)
    print(0.0)
    print(-1.5)

    # Função type
    print(type(1))
    print(type(1.0))
    print(type(0))
    print(type(0.0))

Obs: Tudo em python é um objeto, então quando rodamos a classe type, não é estranho, no terminal, ter retornado o valor <class bla bla>, pois as classes são os que manipulam os objetos.

## Aula 09 - Tipo bool (boolean) - Introdução aos tipos de dados:
Vamos conhecer os booleanos.

Como foi visto na revisão do JavaScript, aqui não muda muita coisa tbm.

Os booleanos são tipos de dados que são usados para declarar alguma validade de uma sentença ou não se dividindo em True e False. Geralmente, usamos muito em operações condicionais, if, donde dentro do operador avaliamos alguma sentença ou em outros casos somente validamos alguma execução ou não. Ou seja, assim como em JavaScript, aqui em python, não precisamos muitas vezes usar diretamente true ou false, mas, de forma implícita, tais dados booleanos estarão trabalhando por baixo dos panos quando usamos os operadores lógicos tbm.

    # Tipo de dado bool (boolean)
    # Ao questionar algo em um programa,
    # só existem duas respostas possíveis:
    # sim (True) ou não (False).
    # Existem vários operadores para "questionar".
    # Dentre eles o ==, que é um operador lógico que
    # questiona se um valor é igual a outro
    print(10 == 10)  # Sim => True (Verdadeiro)
    print(10 == 11)  # Não => False (Falso)
    print(type(True))
    print(type(False))
    print(type(10 == 10))
    print(type(10 == 11))

Ficaria mais fácil para mim entender que o booleano é uma espécie que atua como álgebra. Ou seja, não existe mais ou menos ou aproximado, mas sim ou é ou não é. Daria para axiomatizar toda a álgebra de grupos, aneis e corpos e teoria de Galois dentro disso. Um dos projetos meus é criar esse axioma em forma de classe para depois verificar em que área no mundo teria a aplicabilidade. O mesmo vale para a álgebra linear!

## Aula 10 - Coerção de tipos (convertendo um tipo para outro):
Vamos ver o que é conversão de tipos e coerção.

No caso, type convertion, typecasting, coercion é o ato de converter um tipo em outro tipos imutáveis e primitivos: str, int, float, bool

Em python, com a estrutura de programação com tipagem dinâmica forte, ele permite que vc define algum valor sem necessidade de declarar o mesmo, como foi visto antes. O mesmo vale para operações, donde vc consegue realizar operações aritméticas sem a necessidade de declar o ato. No caso, em especial, o operador "+" ele tem uma estrutura de polimorfismo aqui, ou seja, ela está definida tanto para operações aritméticas com números quanto para operações de concatenação e tais ações, tbm, vc não precisaria declarar

    print(1 + 1)
    print('a' + 'b')

Obs: Diferentemente de JavaScript, no python se vc fizar a operação do tipo 

    print('a' + 1)

Ele não será válido, pois no JavaScript essa operação ele interpreta que valor number seria uma string para concatenar com a outra string. Em python, isso gera um erro

    Traceback (most recent call last):
    File "/home/leonardo/Documentos/estudos/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula10-Coercao-de-tipos-convertendo-um-tipo-para-outro/aula10.py", line 8, in <module>
        print('a' + 1)
    TypeError: can only concatenate str (not "int") to str

Ou seja, isso é tipicamente característica de uma linguagem de programação de tipagem dinâmica forte, diferentemente de JavaScript, que é de tipagem dinâmica fraca.

No caso, a forma como eu interpreto isso é que Python ele é como se fosse um cara muito rígido com as definições matemáticas sem abuso de notações, equanto que o JavaScript, ele não é tão rígido, ao ponto de permitir algumas operações com abuso de notação.

Existem funções em Python que ele converte um tipo de dado para outro quando isso é permissível, visto que o Python é uma linguagem dinâmica de tipagem forte.

    print('1', type('1'))
    print(int('1'), type(int('1')))

No caso, acima vemos que estamos convertendo uma string, mas com caractere 1 que é um número, para um inteiro. Visto que a classe type está verificando o seu tipo e, como prova disso, no terminal podemos ver que o primeiro print ele retorna um tipo string e o segundo um tipo int, de inteiro. Porém, note que, isso só foi possível visto que o dado primitivo que está como string ele era permissível de ser alterado para um número inteiro, pois o seguinte caso não seria possível realizar o mesmo processo que fizemos acima

    print('a', type('a'))
    print(int('a'), type(int('a')))

Um outro detalhe importante que precisamos saber seria quando realizamos as operações entre dois números, sendo um int e outro um float

    print(1.0 + 1)

O que vc acha que o python iria retornar nesse caso? 

A resposta é que quando vc realiza alguma operação matemática com int e um float, será devolvido um float, isso faz sentido, visto que os floats são números que permitem a existência de números flutuantes.

O mesmo uso que fizemos acima para a função int, vale para o float.

Algumas coisas, podemos converter para um booleano tbm.

Uma curiosidade seria o seguinte

    print(bool(''))
    print(bool(' '))

    print(bool({}))
    print(bool({ 'Estado': 'SP'}))

    print(bool([]))
    print(bool([1]))

No código acima, estamos usando a função bool para uma string vazia e um bool para uma string com um espaço, da mesma forma para outros dois objetos, um bool para objeto vazio e outro que conste algum elemento. O que vc acha que será devolvido?

Outra função que temos de conversão é o str, ou seja, ela converte em uma string

    print(str(11) + 'b')
    print(str({}))
    print(str([]))
    print(str(True))
    print(str(False))

Podemos ver acima que a função str consegue converter um monte valores em uma string, bastaria ver o que está sendo retornado pelo terminal.

## Aula 11 - Introdução às variáveis em Python:
Vamos ver sobre variáveis em Python.

As variáveis são usada para salvar algo na memória do computador.

PEP8: inicie variáveis com letras minúsculas, pode usar números e underline.

Basicamente, o PEP8 ele é um guia de estilo de código python.

    https://peps.python.org/pep-0008/

O sinal de "=" é um operador de atribuição. Ele é usado para atribuir um valor a um nome (variável)

    nome_completo = 'Leonardo Takashi Teramatsu'
    soma_dois_mais_dois = 2 + 3
    int_um = bool('1')
    nome_variavel1 = 'Hello WounderWorld!'
    print(int_um, type(int_um))
    print(nome_completo, soma_dois_mais_dois)
    print(nome_variavel1)

Bom, a ideia de variáveis aqui é o mesmo para JavaScript, no sentido de funcionalidade. Ou seja, usamos as variáveis para podermos utilizar a mesma em vários outros lugares e quando é necessário realizar alguma alteração de dado, não precisamos ficar alterando manulamente uma por uma, bastaria alterar pela variável, que tal alteração irá se perpetuar de forma uniforme. A diferença da forma como declaramos as variáveis aqui em python com a do JavaScript, é que em JavaScript precisaria declarar uma sintaxe let e const, já aqui em Python nada disso é necessário, contanto que esteja de acordo com as regras do PEP8.

Uma boa prática para definir uma variável é definir o nome dela que seja descritivo para um dado que será colocado nessa variável.

## Aula 12 - Exercício com variáveis e tipos de dados:
Vamos aprender a manipular as variaveis.

## Aula 13 - Solução - exercício com variáveis e tipos de dados:
A solução o exercício basta conferir no arquivo aula12-13.py.

## Aula 14 - Introdução aos operadores aritméticos (matemática):
Vamos aprender sobre os operadores aritiméticos em Python.

Basicamente, os operadores, são os mesmos do que foi visto em JavaScript.

O único operador que não temos em JavaScript, mas temos em Python é a divisão por inteiro.

São elas

- Adição/concatenação: +

- Subtração: -

- Multiplicação: *

- Divisão: /

- Divisao Inteira: //

- Exponenciação: **

- Modulo / Resto da divisão: %

Bom, aqui não tem tanto segredo, as funcionalidades são os mesmos que tem em JavaScript.

Obs: Toma muito cuidado de usar o operador da exponenciação. Pois se ele explodir muito rápido, isso pode dar um erro, pois o Python não consegue suportar a computação de um número muito grande.

## Aula 15 - Concatenação (+) e repetição (*) com operadores aritméticos:
Vamos entender um pouco mais dos operadores "+" e "*", as suas peculiaridades.

No caso, o operador "+", ele serve para concatenação, além da adição usual com números. Além disso, em Python, quando usamos esse operador para uma string com um número, diferentemente de Python, isso irá gerar um erro, devido à linguagem de programação Python ser de tipagem dinâmica forte.

Agora, temos um outro operador que tem as suas peculiaridades, que é o "*". Podemos usar esse operador tanto para multiplicar números quanto para pedirmos que um dado string ele se repita.

    a_dez_vezes = 'A' * 10
    tres_vezes_leonardo = 3 * 'Leonardo'
    print(a_dez_vezes)
    print(tres_vezes_leonardo)

## Aula 16 - Precedência entre os operadores aritméticos:
Vamos ver sobre as precedência entre os operadores aritméticos.

No caso, a ordem de precedência é o seguinte

    # 1. () - Entre parênteses
    # 2. ** - Exponenciação
    # 3. * / // % - Multiplicação, divisão, divisão por inteiro, módulo
    # 4. + - - Soma e subtração.

Bom, no caso, se tivermos dois ou três operadores que tenha a mesma precedência? Como seria a ordem de execução? 

Nesse sentido é o mesmo que no JavaScript, de direita para esquerda.

## Aula 17 - Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis:
Vamos praticar os operadore aritméticos que revisamos até agora para fixarmos o conceito.

## Aula 18 - Solução exercício de programação - Cálculo do IMC:
Basta veriricar o arquivo aula17-18.py.

## Aula 19 - Uma introdução às f-strings (formatação de strings):
Vamos aprender o básico sobre a formatação de strings.

No caso, suponhamos que tenhamos uma frase que queiramos jogar tudo em uma variável. Claro, o usual nessa hora seria usar uma string para tal finalidade. Mas podemos usar a formatação de strings que ela permite não somente manter o formato string, mas permite implementar algumas variáveis dentro dela

    linha_1 = f'{nome} tem {altura:.2f} de altura,'
    linha_2 = f'pesa {peso} quilos e seu imc é'
    linha_3 = f'{imc:.2f}'

    print(linha_1)
    print(linha_2)
    print(linha_3)

Ou seja, o f-strings ela é uma espécie de crase do JavaScript, onde podemos chamar  as outras variáveis que definimos dentro dela e retornar, pelo terminal, em uma forma de string.

Bom, isso foi uma brevíssima introdução sobre f-strings.

## Aula 20 - Formatação de strings com o método format:
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

## Aula 21 - Usando a função input para coletar dados do usuário:
Vamos ver um pouco mais sobre a função input.

O input ele é uma função do python donde vc pode coletar dados do usuário que estiver usando o seu programa.

No caso, no arquivo aula21.py temos o seguinte código

    nome = input('Qual o seu nome? ')
    print(f'O seu nome é {nome}')
    print(f'O seu nome é {nome=}')

Basicamente, quando vc rodar o código acima, pelo terminal será exibido a msg de pergunta "Qual o seu nome?", como definido dentro da função input e em seguinte, com o f-strings, conseguimos exibir essa msg.

Além disso, no código acima, temos um truque de conseguirmos exibir não somente o conteúdo que foi colocado dentro input mas o seu tipo tbm, donde é exibido "{nome=}".

O mesmo podemos fazer os inputs para números tbm. Só que com um detalhe é que o input ele envia uma string. Logo, seria necessário alterar o input para um tipo número

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    int_numero_1 = int(numero_1)
    int_numero_2 = int(numero_2)

    print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

Obs: Como uma boa prática, recomendamos que o programador não faça a seguinte forma de conversão achando que isso seria um corta caminho

    numero_1 = int(input('Digite um número: '))

Pode parecer que de fato é um corta caminho, mas o problema é que isso pode gerar uma confusão de quando seria necessário procurar onde está dando erro no código. Pois muitas vezes dificulta o que o usuário colocou dentro do input para checar a validade ou não.

## Aula 22 - Introdução aos blocos de código + if / elif / else (condicionais):
Vamos ver sobre bloco de código começando com as condicionais if, elif e else.

No caso, bloco em python, por hora, vc poderia entender como uma espécie de instrução para uma determinada ação. Ou seja, ela é uma lista de sequências de passos que será executado avaliando um determinado valor de entrada.

Geralmente, a criação de tal instrução em outras linguagens orientada à objetos, como JavaScript, são feitas usando-se uma chave "{}". Já o Python, ele não precisa de chave.

   entrada = input('Você quer "entrar" ou "sair"? ')

    if entrada == 'entrar':
        print('Você entrou no sistema')
    elif entrada == 'sair':
        print('Você saiu do sistema')
    else:
        print('Você não digitou nem entrar e nem sair.')

    print('Fora dos blocos')

Note que, o bloco como está acima, vc digitando algo e, consequentemente, mesmo devolvendo algo, note que, as linhas de código fora do bloco posteriores continuam em funcionamento?

Bom, aqui a analogia é a mesma que no JavaScript, donde vc poderia usar o return caso vc queira que naquele escopo, seja finalizada até alí.

Bom, vismo que a ideia principal de montar um bloco em python é que ele seja feita via identação. Ou seja, quando vc cria uma instrução, tudo o que vem depois dele que esteja espaçado por um tab estará sendo executado dentro dele.

## Aula 23 - if, elif e else: entendendo o fluxo do interpretador em condicionais:
Vamos entender mais ainda sobre blocos.

Lembra quando foi dito sobre a identação?

Pois bem, no caso, como podemos ver 

    condicao = True

    if condicao:
        print('Este é o codigo do if')
        
    print('Fora do if')

Vemos que quando rodamos o código acima, o print('Fora do if'), será exibido, pois ele está no mesmo nível de alinhamento com a condicional if em que foi utilizado.

    condicao = True

    if condicao:
        print('Este é o codigo do if')
    else:
        print('Este é o codigo do else')
    if 10 == 10:
        print('Outro if')
        
    print('Fora do if')

Aqui estamos deixando claro que se quisermos usar o else ou elif, necessariamente precisa da existência do if e mesmo criando um bloco com as condicionais, nada impede de criar um outro if depois delas tbm.

Existe casos em que mesmo que entre na condição vc não pensou em algum código nela ainda. No caso, vc poderia usar o pass

    condicao = False

    if condicao:
        print('Este é o codigo do if')
    elif 3 == 3:
        pass
    else:
        print('Este é o codigo do else')
    if 10 == 10:
        print('Outro if')
        
    print('Fora do if')

Basicamente, o bloco de condicionais, a forma como ela funciona, é o mesmo que a do JavaScript. Em um único bloco, vc poderia ter muita, mas muita, condicionais para ser avaliado. Mas bastou que uma delas seja satisfeita, então irá sair do bloco inteiro em seguida.

## Aula 24 - O Debugger do VS Code e o interpretador do Python lendo os códigos:
Vamos aprender a usar o Debugger do VSCode que permite vc conseguir conferir que tipo de erro está acontecendo.

No VSCode temos um recurso chamado Run and Debbug, na aba onde está exibindo os recursos é o desenho com um play e um inseto colado nela. No caso, podemos usar esse Run and Debugger para podermos corrigir os erros de códigos que vc tem.

Podemos, também, usar um recurso chamado BreakPoint para conseguirmos ver exatamente no ponto onde vc queria que parasse durante a compilação do código.

## Aula 25 - Operadores relacionais (de comparação) em Python:
Vamos ver sobre os operações relacionais de comparação em Python.

São elas

    """
    Operadores de comparação (relacionais)
    OP      Significado         Exemplo (True)
    >       maior               2 > 1
    >=      maior ou igual      2 >= 2
    <       menor               1 < 2
    <=      menor ou igual      2 <= 2
    ==      igual               'a' == 'a'
    !=      diferente           'a' != 'b'
    """

Bom, em conceitos matemáticos mais à fundo, os operadores que conseguimos definir, todas elas são uma relação. A princípio, tudo na matemática podemos representar por funções que é uma relação. No caso, isso não muda tbm para os operadores de comparação que é uma relação.

    maior = 2 > 1
    maior_ou_igual = 2 >= 2
    menor = 1 < 2
    menor_ou_igual = 2 <= 2
    igual = 'a' == 'a'
    diferente = 'a' != 'b'
    print(maior)
    print(maior_ou_igual)
    print(menor)
    print(menor_ou_igual)
    print(igual)
    print(diferente)

Em vez de usar vários prints, se quiser usar de modo interativo podemos jogar no terminal o seguinte comando

    python -i aula25.py

Que é o shell interativo do python.

## Aula 26 - Exercício de programação com if e comparação:
O exercício é para vc realizar uma comparação.

## Aula 27 - Solução - Exercício de programação com if e comparação:
Deixarei o código que o professor desenvolveu. A minha estará no arquivo aula26.py.

## Aula 28 - Operador Lógico "and":
Bom, vamos ver sobre uma das lógicas proposicional, o 'e/and'.

Quem conhece muito bem sobre teoria dos conjuntos a lógia aplicada nela é a mesma. Como é o meu caso irei usar essa aula só para ver quais são as sintaxes para eu poder aplicar a teoria

    # Operadores lógicos
    # and (e), or (ou) e not (não)
    # and - Todas as condições precisam ser verdadeiras.
    # Se qualquer valor for considerado falso, a expressão inteira avaliada naquele valor será considerada falso
    # São considerado falso:
    # 0 0.0 '' False
    # Também existe o tipo None que é usado para representar um não valor.
    entrada = input('[E]ntrar [S]air: ')
    senha_digitada = input('Senha: ')

    senha_permitida = '123456'

    if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar')
    else:
        print('Sair')

No caso, a sintaxe usada para representarmos o operador and é o próprio nome "and".

No caso, assim como em JavaScript, em Python, também, temos a avaliação de curto circuito

    # Avaliação de curto circuito
    print(bool(0))
    print(bool(0.0))
    print(bool(''))
    print(True and False and True)
    print(True and 0 and True)
    print('' and True and True)
    print(True and True and 0.0)

No caso, a ideia do curto circuito em python é a mesma que no JavaScript.

## Aula 29 - Operador Lógico "or":
A avaliação do curto circuito em python é o mesmo que o JavaScript.

## Aula 30 - Operador lógico "not":
Na matemática é conhecido como uma negação de uma sentença.

Ou seja, negar um não seria sim, assim como negar um sim seria um não. No caso, aqui o not não muda nada, visto que a sintaxe para isso é o 'not'

    not True => False

    not False => True

Nas demonstrações matemáticas isso aparece muito nas demonstrações por contra-positiva.

## Aula 31 - Operadores in e not in:
O operador acima é literalmente o operador que confere a condição de pertinência ou não de um dado elemento sobre um conjunto.

    # Operadores in e not in
    # Strings são iteráveis
    #  0 1 2 3 4 5
    #  O t á v i o
    # -6-5-4-3-2-1
    # nome = 'Otávio'
    # print(nome[2])
    # print(nome[-4])
    # print('vio' in nome)
    # print('zero' in nome)
    # print(10 * '-')
    # print('vio' not in nome)
    # print('zero' not in nome)

    nome = input('Digite seu nome: ')
    encontrar = input('Digite o que deseja encontrar: ')

    if encontrar in nome:
        print(f'{encontrar} está em {nome}')
    else:
        print(f'{encontrar} não está em {nome}')

No caso, a forma como é conferida usando esses dois operadores in e not in, é por meio de iteração.

## Aula 32 - Interpolação de string com % em Python:
Vamos ver sobre a interpolação de string com % em Python.

Basicamente, a interpolação é o mesmo que realizamos com o format antes, só que por via de uma sintaxe diferente

    """
    Interpolação básica de strings
    s - strings
    d e i - int
    f - float
    x e X - Hexadecimal (ABCDEF0123456789)
    """
    nome = 'Leonardo'
    preco = 1000.95897643
    # em % expressando a variável, se tiver somente uma variável
    # não precisa colocar () para especificar cada uma
    variavel1 = 'Meu nome é %s' %nome
    # variavel = '%s, o preco total foi R$ %f' %(nome, preco)
    variavel = '%s, o preco total foi R$ %.2f' %(nome, preco)
    print(variavel)
    print(variavel1)

No caso, é uma outra forma de conseguirmos colocar os valores das variáveis dentro de uma string.

O Hexadecimal é o mesmo uso

    print('O hexadecialm de %d é %x' %(15,15))
    print('O hexadecialm de %d é %04x' %(15,15))
    print('O hexadecialm de %d é %04x' %(1500,1500))
    print('O hexadecialm de %d é %08x' %(1500,1500))

## Aula 33 - Formatação de strings com f-strings:
Vamos ver formatação de strings com f-strings.

Bom, o f-strings já foi visto antes o seu uso e já aplicamos algumas vezes nos estudos daqui. Porém vamos ver algo um pouco mais à fundo disso

    """
    Formatação básica de strings
    s - string
    d - int
    f - float
    .<número de dígitos>f
    x ou X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda
    < - Direita
    ^ - Centro
    = - Força o número a aparecer antes dos zeros
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a 
    """
    variavel = 'ABC'
    print(f'{variavel}')

Agora, suponhamos que queremos colocar mais caracteres de espaço para esquerda. No caso, o f-strings ele faz isso

    print(f'{variavel: >10}.')
    print(f'{variavel: <10}.')

Donde é análogo para espaço para direita.

           ABC.
    ABC       .

Basicamente, é o que está sendo devolvido. No caso, a contagem funciona assim

           3210  
           ABC.

e o restante de 4 até 9 para preencher o restante de 10 caractéres.

Mas, mais especificamente, isso que estamos fazendo é uma forma de colocarmos mais caractéres no lado esquerdo ou direito.

Temos uma forma de colocar o caractére no centro tbm

    print(f'{variavel: ^10}.')

No caso, será retornado o seguinte

       ABC    .

Temos tbm, para exibir alguns números, a forma seguinte

    print(f'{1000.4873648123746:.1f}')
    print(f'{1000.4873648123746:,.1f}')
    print(f'{-1000.4873648123746:,.1f}')
    print(f'{1000.4873648123746:-,.1f}')
    print(f'{1000.4873648123746:+,.1f}')
    print(f'{1000.4873648123746:0>+10,.1f}')
    print(f'{1000.4873648123746:0=+10,.1f}')

Donde, será o retornado o seguinte

    1000.5
    1,000.5
    -1,000.5
    1,000.5
    +1,000.5
    00+1,000.5
    +001,000.5

E temos tbm o hexadecimal como foi visto antes

    print(f'O hexadecimal de 1500 é {1500:08X}')

Além disso, temos a possibilidade tbm de usarmos para exibir os seus métodos

    print(f'{variavel!r}')

Para mais detalhes seguir a documentação

    https://realpython.com/python-f-strings/#:~:text=Also%20called%20%E2%80%9Cformatted%20string%20literals,the%20__format__%20protocol.

## Aula 34 - Fatiamento de strings e a função len:
Vamos ver fatiamento de strings e função len.

No caso, o fatiamento de strings é tratar elas como um array para conseguirmos realizar algumas manipulações

    """
    Fatiamento de strings
    012345678
    Olá mundo
    -987654321
    Fatiamento [i:f:p] [::]
    Obs.: a função len retorna a qtd 
    de caracteres da str
    """
    variavel = 'Olá mundo'
    print(variavel[5])

Acessando a leta "u" dessa string.

Podemos acessar o mesmo elemento usando o número negativo tbm

    print(variavel[-4])

Além disso, podemos fazer o fatiamento

    print(variavel[4:])

No caso, aqui ele indica que quero pegar o pedaço da string que começa do "m" e vai até o fim.

Assim, podemos tbm colocar o final onde queremos que seja pego

    print(variavel[4:7])

No caso, colocamos o pedaço até onde queremos pegar, mas nesse caso aqui será omitido o índice 7. Ou seja, será pego até o índice 6.

O mesmo podemos fazer de trá para frente. No caso, se quisermos pegar uma fatia a partir de um ponto e tudo o que vier antes dele podemos fazer o seguinte

    print(variavel[:5])

Percebe-se que aqui, o índice 5 foi omitido e foi pego do índice 4 para trás. Da mesma forma, podemos fazer para os números tbm

    print(variavel[-8:-2])

No caso, note que, aqui mesmo sendo número negativo a regra de range continua funcionando. No caso, o "-2" ele indica o caractere "d", mas ela foi omitido ao pegar o pedaço da fatia.

Podemos, tbm, saber a quantidade de caractere que está presente numa string usando o len

    print(len('aaaaaaaaa'))
    print(len(variavel))

No caso, aqui fica evidente que de fato é contado idependente se um dado caractere apareceu mais de uma vez, ela é contado mesmo assim indexando um novo índice nela. Seria uma função em que vai dos naturais e algumas quantidades de índices de naturais vão até um mesmo caratere de palavras.

Ainda faltou falar de passos no fatiamento

    print(variavel[0:len(variavel):1])

Aqui o terceiro parâmetro, onde está o '1', indica os passos em que ele vai pulando os caractéres para ser exibido no final. No caso, o '1' aqui não vai mudar nada porque ele não estará pulando nada. Creio que com o próximo exemplo ficaria mais evidente

    print(variavel[0:len(variavel):2])

No caso, o print acima retorna o seguinte

    Oámno

Visto que a string original é 'Olá mundo'.

Podemos usar, nessa bricadeira, o número negativo tbm

    print(variavel[0:len(variavel):-1])
    print(variavel[0:len(variavel):-2])

Nisso, o que irá acontecer é que em vez de contar os passos de esquerda para direita, é contado de direita para à esquerda. Entretanto, ao usarmos o número negativo, os outros números tbm precisam serem negativos. Como prova disso, os dois prints acima não será retornado nada. O certo teria que ser

    print(variavel[-1:-10:-1])
    print(variavel[-1:-10:-2])

Agora, sim, será retornado as strings invertidas

    odnum álO
    onmáO

Podemos fazer o mesmo para o print(variavel[-1:-10:-1]) da seguinte forma abaixo

    print(variavel[::-1])

Como nesse caso aqui que foi invertido a string.

## Aula 35 - Exercício: teste seu conhecimento até aqui e Aula 36 - Solução - Exercício: teste seu conhecimento até aqui:
Vamos fazer um teste para fixar melhor os conteúdos que foi estudados até agora

No caso, essa seria as exigências

    """
    Exercício
    Peça ao usuário para digitar seu nome
    Peça ao usuário para digitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade: 
        exiba "Desculpe, você deixou campos vazios."
    """

Bom, basta codar para exercitar.

## Aula 37 - Introdução ao try e except para capturar erros (exceptions):
Vamos ver sobre try e except.

Basicamente, o try, como o nome já disse, é tentar executar uma ação e ver o que acontece depois disso. Em JavaScript, por exemplo, isso está muito presente quando é usado o try, catch e finally. E a funcionalidade é algo parecido para python com as sintaxes try e except.

No caso, vamos apenas mostrar uma introdução desses conceitos

    """
    Introdução ao try/except
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar
    """

    print(1234)
    print(456)
    # int('a')
    # float('a')

Note que, o int e o float usado, no exemplo acima, ao descomentarmos elas e simularmos, vamos conseguir ver que será exbido uma msg de erro pelo terminal.

Agora, nesse exemplo de baixo, podemos ver o caso em que o operador * ele funciona como uma espécie de repetição, caso for string, e de múltiplicação, caso for um number

    numero = input('Vou dobrar o número que vc digitar: ')
    numero_float = float(numero)

    print(f'O dobre de {numero} é {numero * 2}')
    print(f'O dobre de {numero} é {numero_float * 2}')
    print(f'O dobre de {numero} é {numero_float * 2:.0f}')
    print(f'O dobre de {numero} é {numero_float * 2:.2f}')

Usamos um método aqui, tbm, para verificar se o que foi colocado dentro do input são apenas números ou não, cujo método se chama isdigit()

    numero_str = input('Vou dobrar o número que vc digitar: ')
    print(numero_str.isdigit())

    numero_float = float(numero_str)

    print(f'O dobre de {numero_str} é {numero_str * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')

Bom, esse método nos permite usar nas condicionais para conferir se os dados estão ou não certos

    numero_str = input('Vou dobrar o número que vc digitar: ')
    # print(numero_str.isdigit())

    if numero_str.isdigit():
        numero_float = float(numero_str)
        print(f'O dobre de {numero_str} é {numero_str * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
    else:
        print('Isso não é um número')

Bom, até agora, nada de try/catch, pois mostramos outras formas de driblar essas sintaxes. Porém, podemo usar nesses casos tbm

    numero_str = input('Vou dobrar o número que vc digitar: ')
    # print(numero_str.isdigit())

    try:
        # ...
        print('STR: ', numero_str)
        numero_float = float(numero_str)
        print('FLOAT: ', numero_float)
        print(f'O dobre de {numero_str} é {numero_str * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
    except:
        # ...
        print('Isso não é um número')

No código acima, vc vai ver que se colocarmos no input algo que não seja número, ou um mix de números com outros caractéres, ocorrerá um erro no numero_float e isso irá fazer com que do try seja direcionado imediatamente no except.

Mas aí entra na seguinte pergunta. Se tem meios para driblar usando as condicionais em vez de try/catch, então por quê temos que usa-las?

Bom, aí entra na questão de entender das limitações das condicionais. Por exemplo, existem casos em que há uma excessão em que a condicional não consegue dar conta ou considerar, mesmo que a lógica aplicada para tais regra de negócio estejam certos. Existem casos em que isso não consegue cobrir todas as possibilidades um algoritmo atende das exigências humanas. Daí, entra em papel a importância de uso do try/catch.

## Aula 38 e 39 - Parte 1 e Parte 2: Variáveis, constantes e complexidade de código:
Vamos falar sobre a complexidade de códigos e algumas boas práticas.

Vamos analisar o seguinte código

    velocidade = 61  # velocidade atual do carro
    local_carro = 100  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

No caso, essa parte onde está sendo exibido duas formas de declarar as variáveis vamos avaliar se está sendo feito uma boa prática ou não.

Note que, as variáveis escritas em maiúsculas são os mesmos das que estão sendo declaradas em minúsculas.

No caso, lembremos que em python, diferentemente de JavaScript, não existe uma forma de declarar uma variável que seja constante. Ou seja, uma vez declarada ao longo do processo ela nunca poderá ser mudada. Ou seja, uma vez declarada as variáveis em maiúsculas, elas podem ser atribuídas outros valores novamente.

Bom, ciente desse fato, como vamos poder contornar a tal situação?

O que recomendamos é que se for algum valor que vc não queira que seja mudado o seu valor, que vc atribuia a sua variável de forma maiúscula, como podemos ver acima em RADAR_1, LOCAL_1 e RADAR_RANGE.

Agora, uma prática considerada ruim no âmbito de condicionais, seriam aquelas condicionais que tenha muita, mas muita, lógica booleana. No caso, em um único if vc coloca uma série de and e or. O que deixaria o seu código muito, mas muito, complexo. A princípio, isso seria uma má prática, pois tornaria a leitura do seu código muito difícil de interpretar para avaliar se uma dada condição permitiria entrar ou não naquele if.

Basicamente, a regra geral em programação, é que sejam escritos códigos que fácil interpretação. Algo que foge bem longe daqueles códigos que vc não entende nada o que está sendo escrito nos filmes de hackers.

Outra prática que é considerada ruim seria colocar códigos de blocos dentro de outros códigos de blocos. Novamente, isso entra n complexidade de código que tornaria-a muito, mas muito, complexo para a leitura e entendimento da mesma. O ideal é que vc saiba separar cada bloco em cada lugar separadamente ou até mesmo em funções para vc conseguir chamar em momentos quando é necessário.

Bom, a moral da história, seria que os códigos precisam ser, na medida do possível, o mais simples e possível e bem organizado.

Bom, ciente disso, vamos implementar as condicionais usando as variáveis dos códigos acima para colocar em prática o que seria um código de boa prática

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    if velocidade > RADAR_1:
        print('Velocidade carro passou do radar 1')
        
    if local_carro >= (LOCAL_1 + RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
            velocidade > RADAR_1:
        print('carro multado em radar 1')

Bom, note que, acima já está aparecendo uma má prática. Qual seria?

A resposta é que o comparativo velocidade > RADAR_1 já está sendo usado mais de uma vez nas condicioais.

Bom, como iremos corrigir isso?

Da seguinte forma

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    vel_carro_pass_radar_1 = velocidade > RADAR_1
    carro_multado_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

    if vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')
        
    if carro_multado_radar_1 and vel_carro_pass_radar_1:
        print('carro multado em radar 1')
    
Ou seja, as condicionais eu denotei elas como variáveis para colocar nos if's.  

    velocidade = 61  # velocidade atual do carro
    local_carro = 90  # local em que o carro está na estrada

    RADAR_1 = 60  # velocidade máxima do radar 1
    LOCAL_1 = 100  # local onde o radar 1 está
    RADAR_RANGE = 1  # A distância onde o radar pega

    vel_carro_pass_radar_1 = velocidade > RADAR_1
    carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

    if vel_carro_pass_radar_1:
        print('Velocidade carro passou do radar 1')
        
    if carro_passou_radar_1:
        print('Carro passou radar 1')
        
    if carro_multado_radar_1:
        print('carro multado em radar 1')

Aqui está a versão mais simplificada e munida de boas práticas.

## Aula 40 - id - A identidade do valor que está na memória:
No caso, sempre que criamos alguma variável e queremos verificar se tal variável está guardada na memória, podemos ver isso vasculhando um identificador único, id.

Toda variável e valores tem esse identificador único, donde pode ser expresso usando a função id()

    v1 = 'a'
    print(id(v1))
    print(id(1))

Daí, note que, se colocarmos duas variáveis com mesmos valores o identificadores serão os mesmos, pois estão apontando para o mesmo valor

    v1 = 'a'
    v2 = 'a'
    print(id(v1))
    print(id(v2))
    print(id(1))

## Aula 41 - Flags, is, is not e None:
Vamos continuar da aula anterior.

Uma outra prática muito ruim seria criar uma variavel dentro de um bloco de código para que seja usado depois, fora dela

    condicao = False

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        print('Não faça algo')

    print(passou_no_if)

No caso, do exemplo acima é uma má prática disso. O motivo de ser uma má prática seria devido ao fato de que se tiver um caso em que uma dada condição não faça entrar no if, significa que essa variável nunca havia sido criado. E isso fará com que tenha alguma possibilidade de ter algum erro pela frente.

No caso, o que seria uma boa prática nisso?

Seria criar uma variável fora do bloco e só depois disso usar dentro do bloco. No caso, temos duas alternativas para corrigir essa má prática

    condicao = False

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        passou_no_if = None
        print('Não faça algo')

    print(passou_no_if)

Acima, é uma das formas de solucionar, porém de forma pior, pois nela estaríamos dependendo do else. Então, a melhor forma seria o seguinte

    condicao = True
    passou_no_if = None

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        print('Não faça algo')

    print(passou_no_if, passou_no_if is None)

No caso, foi declarado a variável antes de entrar no if e isso evitará futuros problemas de usar alguma variável não declarada.

## Aula 42 - Exercícios - Enunciados:
Vamos ter três exercícios diferentes em uma só!

O enunciado dos três são os seguintes

    """
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
    """

    """
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
    descrito, exiba a saudação apropriada. Ex. 
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
    """

    """
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
    menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
    "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
    """

## Aula 43, 44 e 45 - Solução 1, 2 e 3 dos Exercícios - Enunciados:
Confere a sua resolução com respectivo resolução do professor.

## Aula 46 - Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string:
Vamos ver um pouco da documentação do python dos tipos que já bem imbutidos dentro dessa linguagem

    https://docs.python.org/pt-br/3/library/stdtypes.html

No caso, os que vemos ver são os tipos imutáveis. São elas:

    str, int, float, bool

No caso, por serem valores imutáveis, serve a mesma a lógica que eu vi nos estudos de JavaScript. No sentido de que se fizermos algo do tipo

    string = 'Leonardo Takashi Teramatsu'
    outra_variavel = string

Automaticamente fizemos uma cópia da variável string acima. O que difere com objetos.

Além disso, o fato de ser imutável, uma vez atribuída um valor não podemos mudar o valor interno dela

    string = 'Leonardo Takashi Teramatsu'
    string[3] = 'ABC'

Ou seja, o código acima retornará um erro.

No caso, a forma correta de mudar algum valor atribuído em uma variável é criando uma outra varável da mesma e realizar o seguinte

    string = 'Leonardo Takashi Teramatsu'
    outra_variavel = f'{string[:3]}ABC{string[4:]}'

Ou seja, usamos o format string para conseguirmos formatar o valor interno de uma string.

Além disso, as strings tem os seus métodos tbm, como, por exemplo, se quisermos realizar alguma personalização na string podemos usar o método capitalize

    string = 'leonardo takashi teramatsu'
    print(string.capitalize())

Assim como tem outras e muitos métodos para string, onde vc poderá consultar na documentação acima.

## Aula 47 - while e break - Estrutura de repetição (Parte 1):
Vamos começar a ver sobre repetições que temos em python.

No caso, vamos começar a ver a repetição pelo while.

Bom, a estrutura de repetição, while, aqui ela tem a mesma funcionalidade que foi vista em JavaScript. A única diferença é que aqui em Python o while tem somente uma, visto que em JavaScript temos dois tipos o while e do while. Então, como foi avisado, devemos tomar cuidado com condições que colocamos no while que pode gerar um looping infinito

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    condicao = True

    while condicao:
        nome = input('Qual o seu nome: ')
        print(f'Seu nome é {nome}')

        if nome == 'sair':
            break

    print('Acabou')

Importante lembrar que o break que estamos usando aqui, ela considera o laço mais próximo, nesse caso o único while que estamos usando. Assim, se tivermos um loop dentro de um outro loop, e usarmos o break para o loop dentro, ele irá sair apenas do loop dentro e o loop fora irá continuar ainda.

## Aula 48 - while - Condição em detalhes:
Vamos ver com mais detalhe a condição que colocamos dentro do while.

Vimos que além de usarmos diretamente os booleanos, podemos, por meio de várias formas de comparações, criarmos um boolenanos de forma implícitas e considerar esses booleanos na condição do while

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    contador = 0

    while contador <= 10:
        contador = contador + 1
        print(contador)

    print('Acabou')

Ou seja, assim como usamos inúmeras formas de booleanos de forma implícita em condicionais if's, podemos realizar o mesmo para o while.

## Aula 49 - Operadores de atribuição com operadores aritméticos:
Os operadores de atribuição aqui em python, tem a mesma lógica que foi visto em JavaScript.

No caso, só deixarei o esboço seguinte

    """
    Operadores de atribuição
    = += -= *= /= //= **= %=
    """
    contador = 10

    ###

    contador /= 5
    print(contador)

## Aula 50 - while + continue - pulando alguma repetição:
Bom, aqui o continue funciona da mesma forma como foi estudado em JavaScript, então não irei me aprofundar tanto.

No caso, o continue, em repetição, ela serve para vc pular alguns dados

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    contador = 0

    while contador <= 100:
        contador += 1

        if contador == 6:
            print('Não vou mostrar o 6.')
            continue

        if contador >= 10 and contador <= 27:
            print('Não vou mostrar o', contador)
            continue

        print(contador)

        if contador == 40:
            break


    print('Acabou')

Além disso, da mesma forma para break, o continue, quando ele é ativado, os códigos de linhas posteriores não serão rodados. O que significa que em um loop, ela irá simplesmente, continuar a iterar adiante. Por isso, teria que tomar muito cuidado onde colocar o continue e o break, para que vc não crie algum laço infinito ou que vc acabe deixando de rodar alguns códigos que são sempre necessários rodar.

Mas a vantagem de usar break e o continue, está no fato de que eles te dão condições para tornar a sua compilação muito mais performáticos.

## Aula 51 - while + while (laços internos):
Vamos continuar com o assunto do while, desta vez vendo while dentro de um while.

Bom, um bom exemplo que faz o uso de while dentro de um while seria para construir uma matriz, visto que ela precisa de linha e coluna. Isso em forma de lista é definitivamente uma lista dentro de uma lista.

Obs: Podemos criar matriz 3d nessa brincadeira tbm colocando mais listas dentro de listas.

Assim, para entendermos o uso do while dentro de while vamos usar a matriz como um exemplo disso. Primeiramente, indo passo a passo, vamos fazer o seguinte

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    qtd_linhas = 5

    linha = 1
    while linha <= qtd_linhas:

        print(linha)

        linha += 1


    print('Acabou')

Para certificarmos de que está funcionando.

Visto que ele está funcionando corretamente, vamos agora trabalhar na sua coluna

    qtd_linhas = 5
    qtd_colunas = 5

    linha = 1
    while linha <= qtd_linhas:
        
        # print(linha)
        coluna = 1
        matriz = ''
        while coluna <= qtd_colunas:
            matriz = matriz + f'{linha}{coluna} '
            # print(f'{linha=} {coluna=}')
            coluna += 1
        print(matriz)
        linha += 1


    print('Acabou')

Bom, basicamente, nessa brincadeira, já daría para brincarmos com as teorias de álgebra linear e realizar algumas simulações com elas.

## Aula 52 - Exercício guiado com while:
Vamos praticar um mini EP (exercício de programação) para fixar melhor o assunto nas nossas cabeças.

Assim, o exercício é o seguinte

    """
    Iterando strings com while
    """
    #       012345678910
    nome = 'Luiz Otávio'  # Iteráveis
    #      1110987654321
    tamanho_nome = len(nome)
    print(nome)
    print(tamanho_nome)
    print(nome[3])

    nova_string = ''
    nova_string += '*L*u*i*z* *O*t*á*v*i*o'

No caso, dado o nome, queremos que no final esse nome tenha asterisco antes de cada letra do nome.

## Aula 53 - Solução do exercício guiado com while:
Veja a solução do professor e compare com a sua resolução.

## Aula 54, 55 e 56 - Exercício guiado - Calculadora - Parte 1, 2 e 3:
Bom, essa aula está como exercício, mas é opcional.

No caso, se a pessoa se sentir preparado pode tentar fazer, mas, caso não sinta preparado, então vale um estudo acima disso.

Eu me sinto mais preparado, então eu irei considerar essa aula como EP.

    """ Calculadora com while """
    while True:
        print('nummmmm')
        #########
        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break

Vamos criar uma calculadora que roda infinitamente até que a pessoa opte por sair. O esquema acima é o esquema base de como começar.

Agora, vamos partir para o processo de criar a calculadora.

## Aula 57 - while / else (recurso peculiar do Python):
Bom, vamos entender sobre um recurso bem específico do python, que é o while else.

A priori, não será nenhum problema da pessoa não fazer muito uso desse recurso, pois é um tipo bem pouco utilizado mesmo. Mas, como estamos em uma revisão e aprofundamento dessa linguagem, vale passarmos o conceito por desencargo de consciência

    """ while/else """
    string = 'Valor qualquer'

    i = 0
    while i < len(string):
        letra = string[i]

        if letra == ' ':
            break

        print(letra)
        i += 1
    else:
        print('Não encontrei um espaço na string.')
    print('Fora do while.')

Ela funciona da seguinte forma. Assim, como tem else para if, em várias outras funções em python ela tem o else junto, como while/else e for/else. Daí, ela funcoina quando o laço termina e vc quer devolver algum valor e o else, assim como foi visto nos estudos das condicionais, é o oposto da condição considerada no if, e o mesmo serve para o while.

No caso, um ponto importante que precisamos deixar claro aqui, é que o else, combinado com o while, ela não é executado visto que dentro do laço foi passado em algum break.

## Aula 58 - while - Qual letra apareceu mais vezes na frase? (Iterando strings com while):
Essa aula é opcional considerar ela como uma aula ou como um exercício.

Irei considerar ela como um exercício. Daí, a tarefa é o seguinte.

Criar um código que itera uma string e conte dentro dela, a letra que mais apareceu e exiba ela com a quantidade total de aparição da mesma

    print(
        'A letra que apareceu mais vezes foi '
        f'"{letra_apareceu_mais_vezes}" que apareceu '
        f'{qtd_apareceu_mais_vezes}x'
    )

Bom, lembrando que a minha resolução eu utilizei while dentro de while. Mas podemos evitar de usar isso usando um método da string chamado .count() como é feito na solução do professor que substitui o while dentro do meu while que eu criei.

## Aula 59 - DEBUGGER: while - Qual letra apareceu mais vezes na frase?:
Essa aula foi mais para melhorar a leitura e interpretação do código.

## Aula 60 - Introdução ao for / in - estrutura de repetição para coisas finitas:
Vamos ver sobre for, que é uma das formas de iterações mais importantes que temos em Python.

O for ele é uma estrutura de repetição, assim como vimos em while. Entretanto, o que difere com o while é que, enquanto que no while vc tem mais controle sobre a forma como a estrutura de repete, em for vc não tem esse controle condicional. No caso, ele itera de forma finita o conteúdo na qual vc pediu para ele iterar

    senha_salva = '123456'
    senha_digitada = ''
    repeticoes = 0

    while senha_salva != senha_digitada:
        senha_digitada = input(f'Sua senha ({repeticoes}x): ')

        repeticoes += 1

    print(repeticoes)
    print('Aquele laço acima pode ter repetições infinitas')

Um exemplo de repetição pelo while acima

    texto = 'Python'

    novo_texto = ''
    for letra in texto:
        novo_texto += f'*{letra}'
        print(letra)
    print(novo_texto + '*')

Exemplo de repetição do for.

Bom, aí entra a pergunta. Qual das duas formas de iterações é boa?

A resposta, obviamente, é depende. Pois, por exemplo, existem situações em que o for ele acaba sendo incompatível para certas finalidades exigidas.

Um exemplo disso, seria para caso vc exigir uma repetição indeterminada, como no exemplo acima em que colocamos a senha e enquanto a senha não estiver certa o programa ela irá continuar a perguntar várias vezes até que vc forneça a senha correta. Percebe-se que nesse tipo de cenário, não há uma quantidade de repetições determinadas as serem realizadas. Assim como vimos outros tipo de exercícios que tivemos com o uso do while, onde vc coloca a condicional, literalmente, "True" e definimos uma função dentro de while que ela repita enquanto o programa não receber alguma resposta que indica em sair do laço pelo break, como no programa que te perguntava se deseja sair ou não do laço. Nessas situações, claramente, o laço for não é eficiente, pois o laço for ela é eficiente no uso de repetições com quantidade determinada e de forma bem direta sem muito trabalho que tínhamos para o while.

## Aula 61 - range + for para usar intervalos de números:
Vamos ver sobre o range usado no for.

Lembrando que o range ele não depende do for assim como o for não depende do range para o seu uso.

No caso, o range ele nos permite definir o intervalo de iteração do for

    """
    For + Range
    range -> range(start, stop, step)
    """

No caso, como descrito acima, no range podemos definir o start, stop e o step, respectivamente, o começo, o alcance e os passos. No caso, o começo e o alcance seria definitivamente o intervalo em que iremos compilar seguindo a regra do conjunto dos números naturais de [n] = {0, 1, 2, ..., n-2, n-1}, visto que definimos range(0, n) ou range(n), para n um natural. E o step serve para definir os passos em que vc quer que a iteração pule.

Segue um exemplo simples do uso do range no for

    for i in range(10):
        print(i)
    print('----------------------')
    for i in range(0,10):
        print(i)
    print('----------------------')
    for i in range(5,10):
        print(i)
    print('----------------------')

Um exemplo usando o step

    numeros = range(0, 100, 8)

    for numero in numeros:
        print(numero)

Bom, assim como vimos em JavaScript, em python, usando o step, podemos usar números negativos tbm. No caso, se quisermos usar o step negativo, vamos precisar que os pontos de partidas e finais sejam negativos tbm

    for i in range(0,-10, -2):
        print(i)

## Aula 62 - Como o for funciona por baixo dos panos? (next, iter, iterável e iterador):
Vamos entender o que acontece por baixo dos panos quando usamos o for.

Bom, foi feito, até agora, uma explicação bem breve sobre o que é iterável, que é algo que ele te entrega uma de cada vez. Claro, essa explicação é algo bem superficial para finalidades didáticas em pegar a noção de como ela funciona.

Agora, indo um pouco mais à fundo disso, o iterável, em Python, ele é advinda da chamada de um método com o nome '__iter__'. No caso, a definição de um método aqui é o mesmo que já foi visto em JavaScript, ou seja, é uma função que é definido dentro de um objeto. Bom, onde eu quero chegar com isso?

No caso, vamos ver o uso desse método

    texto = 'Leonardo'.__iter__()

Quando damos esse comando aqui executando o método, será chamado um iterador. No caso, ao printarmos essa variável, em vez de ser chamado o valor que foi definido dentro dela, será chamado o seguinte

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

O que será retornado

    <str_iterator object at 0x7ff397ef5c70>

No caso, ele está dizendo que foi chamado o iterador do str, 'str_iterador', que está dentro de um objeto e que ela está guardada na memória do seu computador com o endereço '0x7ff397ef5c70'.

Mas aí vem a pergunta. Toda vez que eu precisar chamar o método iterador, eu preciso fazer como foi feito na variável acima?

A resposta é não, pois existe um método pronto para isso chamado iter(), donde, dentro dela, reside esse método __iter__

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

    iteratador = iter(texto)  # iterator
    print(iteratador)

No caso, o que o print da variável iteratador irá nos retornar, será o mesmo do print para a variável texto.

Mas aí, qual é o motivo de estarmos discutindo isso? Seria pelo fato de que dentro dos métodos que existem para string, visto que string é um objeto, temos um método chamado next

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

    iteratador = iter(texto)  # iterator
    print(iteratador)
    print(iteratador.__next__())
    print(iteratador.__next__())
    print(iteratador.__next__())
    print(iteratador.__next__())
    print('--------------')

No caso, esse método nos entrega o próximo valor como podemos ver no que é retornado pelo terminal

    <str_iterator object at 0x7f56840a9c70>
    <str_iterator object at 0x7f56840a9c70>
    L
    e
    o
    n
    --------------

Daí, se chamarmos o método __next__ várias vezes ao ponto de acabar a quantidade iterável de um objeto, será retornado o seguinte erro

    Traceback (most recent call last):
    File "/home/leonardo/Documentos/estudos/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula62-Como-for-funciona-por-baixo-dos-panos/aula62.py", line 21, in <module>
        print(iteratador.__next__())
    StopIteration

No caso, assim como temos o iter para o método __iter__, temos o next para o método __next__. E o quê isso significa? Podemos usar ela em while para vermos que ela tem a mesma funcionalidade

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)
    print('--------------')
    iteratador = iter(texto)  # iterator
    print(iteratador)
    print('--------------')
    while True:
        print(next(iteratador))

Vimos que, por se tratar de um loop inifinito em uma iteração finita, o next irá mostrar o mesmo erro na tela do bash.

Aí, uma forma de resolvermos isso seria usando o try e except dentro do while

    while True:
        try:
            letra = next(iteratador)
            print(letra)
        except StopIteration:
            break

Bom, o while acima, simula exatamente o que é feito pelo for por baixo dos panos e como ela funciona. No caso, temos o iterável, e nela aplicamos o iterador junto com o next e visto que não tem como mais iterar, StopIteration, então saímos do laço, como foi feito pelo except StopIteration acima. No caso, o for é um kit da funcionalidade acima, sem a necessidade de ter que criar cada passo na unha.

## Aula 63 - O que aprendemos com while também funciona no for (continue, break, else, etc):
Vamos ver que os usos que fizemos de continue, break, else, etc... Para o while, funciona tudo para o for tbm.

No caso, segue um exemplo disso

    for i in range(10):
        if i == 2:
            print('i é 2, pulando...')
            continue

        if i == 8:
            print('i é 8, seu else não executará')
            break

        for j in range(1, 3):
            print(i, j)
    else:
        print('For completo com sucesso!')

Além disso, assim como foi visto o uso do break dentro do while que está de um outro while, o mesmo vale para o for

    for i in range(10):
        for j in range(10):
            if j == 2:
                print('Escopo interno', j)
                break
        print('Escopo externo', i)

Ou seja, ele funciona de uma forma de que o break ele quebra apenas o laço mais próximo dele.

## Aula 64 - Exercício - Jogo da palavra secreta:
Vamos fazer um EP para fortalecer mais sobre o assunto do for.

Aqui será o que é pedido para o problema

    """
    Faça um jogo para o usuário adivinhar qual
    a palavra secreta.
    - Você vai propor uma palavra secreta
    qualquer e vai dar a possibilidade para
    o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você 
    vai conferir se a letra digitada está
    na palavra secreta.
        - Se a letra digitada estiver na
        palavra secreta; exiba a letra;
        - Se a letra digitada não estiver
        na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu
    usuário.
    """

Tente, depois que resolvido o problema, deixar o meu código o mais enxuto possível!

## Aula 65 - Sobre exercícios - não saber é normal:
Lembre-se! O fato de surtir a vontade de aprender e vc estar aqui acompanhando isso já é um talento, até onde se sabe na definição da neurosciência! Pois, independente se a circunstância te obriga ou não, vc poderia ter optado por não fazer nada ou escolher outra coisa. Mas se vc se identificou, intencionalmente ou não, isso é um indício de que vc tem talento na área! O resto é persistência, vide a frase do Thomaz Edison

    Genialidade é 1% inspiração e 99% transpiração

## Aula 66 - (Parte 1) Solução do exercício - Jogo da palavra secreta:
Bom, compara com a solução do professor com o seu!

## Aula 67 - (Parte 2) Solução do exercício - Jogo da palavra secreta:
Bom, compara com a solução do professor com o seu!

## Aula 68 - Tipo list - Introdução às listas mutáveis em Python:
Vamos aprender sobre listas.

No caso, deixamos claro que as listas são muito, mas muito, usadas para vários trabalhos com linguagem Python.

Basicamente, a lista em python é o array que eu ví em JavaScript e, claro, possui inúmeras funcionalidades similares que eu ví em JavaScript, para python tbm.

Inclusive, vale dar uma revisão em JavaScript para lista para traçar um comparativo na lista em Python para ver o que são e o que não são similares de uso entre eles.

Até agora, vimos que o tipo de objeto que tem um comportamento muito similiar com a lista foram os strings. Bom, por quê estou falando isso? Basicamente, da mesma forma que conseguimos iterar o string conseguimos iterar uma lista.

## Aula 69 - Alterando uma lista com índices, del, append e pop (Tipo list):
Vamos ver os métodos que temos para as listas, as mais usadas.

Bom, eu já vi isso na minha faculdade, então essa aula será mais como uma revisão

    """
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append, insert, pop, del, clear, extend, +
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
    """
    #        0   1   2   3   4   5
    lista = [10, 20, 30, 40]
    # lista[2] = 300
    # del lista[2]
    # print(lista)
    # print(lista[2])
    lista.append(50)
    lista.pop()
    lista.append(60)
    lista.append(70)
    ultimo_valor = lista.pop(3)
    print(lista, 'Removido,', ultimo_valor)

Obs: Muito cuidado ao usar a função delete, del. Pois, dependendo do uso dele vc poderá deixar o processamento do seu código muito, mas muito, lento. Por exemplo, quando usamos o del para apagar qualquer elemento que não esteja no último, a lista que será exibida seria uma espécie de lista nova. Ou seja, quando uso esse del, praticamente é criado uma nova lista. Agora, suponhamos que usamos esse del para apagar o segundo elemento de uma lista que tenha 10 mil elementos? No caso, o processo estaria realizando uma criação de uma nova lista só para deslocar os outros 9998 elementos à um índice antecessor. Isso vai requer um consumo muito enorme do processamento da sua máquina e tornaria o código seu muito, mas muito, lento.

Na medida do possível, uma boa prática que podemos realizar com as listas é add e remover apenas os últimos elementos. Ou seja, usamos as funções del e insert somente quando a lista que estamos manipulando seja uma lista bem menor.

## Aula 70 - Inserindo itens em qualquer índice da lista com insert (Tipo list):
Vamos entender agora uma função que chamado insert que serve para inserir os elementos dentro de uma lista.

No caso, vamos revisar o seguinte

    """
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
    """
    #        0   1   2   3
    lista = [10, 20, 30, 40]
    lista.append('Luiz')
    nome = lista.pop()
    lista.append(1233)
    del lista[-1]
    # lista.clear()
    lista.insert(100, 5)
    print(lista[4])

## Aula 71 - Concatenando e estendendo listas em Python:
Vamos agora entender sobre concatenando e extensão de listas em Python.

Bom, a ideia é o mesmo como foi visto em JavaScript, no ponto de vista lógico.

Só irei mostrar as sintaxes de como realizar os processos

    """
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
    """
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    lista_c = lista_a + lista_b
    lista_a.extend(lista_b)
    print(lista_a)

## Aula 72 - Cuidados com tipos de dados mutáveis - list e copy:
Vamos ver alguns cuidados que precisamos tomar ao trabalharmos com os tipos de dados mutáveis.

A princípio a lógica é a mesma do que eu estudei em JavaScript, sobre a forma de copiar uma lista

    lista_a = [1, 2, 3]
    lista_b = lista_a

No caso, o formato acima não estará gerando uma cópia da lista. Ou seja, as duas variáveis estará apontando para a mesma memória.

Agora, a forma certa de realizar a tal cópia seria o seguinte

    """
    Cuidados com dados mutáveis
    = - copiado o valor (imutáveis)
    = - aponta para o mesmo valor na memória (mutável)
    """
    lista_a = ['Luiz', 'Maria', 1, True, 1.2]
    lista_b = lista_a.copy()
    print(lista_a)
    print(lista_b)
    print('--------------------')

    lista_a[0] = 'Qualquer coisa'
    print(lista_a)
    print(lista_b)
    print('--------------------')

## Aula 73 - for in com tipo list:
No caso, como foi dito em algumas aulas anteriores, podemos usar o for para iterar as listas

    """
    for in com listas
    """
    lista = ['Maria', 'Helena', 'Luiz']

    for nome in lista:
        print(nome, type(nome))

## Aula 74 - Exercício - exiba os índices da lista (aula com solução):
Nessa aula é opcional se o estudante vai querer considerar ela como exercício ou como uma aula.

Eu irei considerar como um exerício

    """
    Exercício
    Exiba os índices da lista
    0 Maria
    1 Helena
    2 Luiz
    """

## Aula 75 - Introdução ao empacotamento e desempacotamento:
No caso, vamos ver sobre atribuição via desestruturação (conhecido como empacotamento e desempacotamento) para lista em Python.

No caso, será a minha revisão sobre atribuição via desestruturação.

No caso, a lógica é a mesma do que estudei em JavaScript

    nomes = ['Maria', 'Helena', 'Luiz']

    nome1, nome2, nome3 = nomes

    print(nome1)
    print(nome2)
    print(nome3)

Agora, da mesma forma em JavaScript, as quantidades de variáveis tem que ser equivalentes com a quantidade de elementos que tem dentro da lista.

Além disso, se quisermos definir somente uma variável usando a atribuição via desestruturação, a prática é análoga do que vimos em JavaScript

    nome1, *resto = nomes
    print(nome1)
    print(resto)

Ou seja, a única coisa que diferencia com o JavaScript está na sintaxe.

Com relação ao resto, existe uma boa prática entre os desenvolvedores que indicam que o resto que tiver na lista não irei usar. Para isso, usamos o underline

    # nome1, *resto = nomes
    nome1, *_ = nomes
    print(nome1)
    # print(resto)
    print(_)

O mesmo serve para variáveis, usando atribuição via desestruturação, de que não vamos querer usar

    # nome1, *resto = nomes
    # nome1, *_ = nomes
    _, nome2, *_ = nomes
    # print(nome1)
    print(nome2)
    # print(resto)
    print(_)

## Aula 76 - Tipo tuple (tuplas):
Bom, como na aula anterior não discutimos muito bem sobre tuplas, vamos ver isso nessa aula.

No caso, a tupla a sua sintaxe se dá pelo ()

    nomes = ('Maria', 'Helena', 'Luiz')

Podemos definir uma tupla sem usar o (), tbm

    nomes = ('Maria', 'Helena', 'Luiz')

Ela é uma lista imutável.

Bom, tudo o que vc pode fazer numa lista, na qual não altere os elementos definidos dentro dela e/ou que modifique a quantidade da lista, vc pode fazer numa tupla.

Uma outra forma de criarmos uma tupla seria convertendo de uma lista

    nomes = ['Maria', 'Helena', 'Luiz']
    print(nomes)
    print('-----------------')
    nomes1 = tuple(nomes)
    nomes2 = list(nomes)
    print(nomes1[-1])
    print(nomes1)
    print('-----------------')
    print(nomes2[-1])
    print(nomes2)
    print('-----------------')

## Aula 77 - enumerate para enumerar valores de iteráveis (pegar índices):
Vamos enumerar!! (No sentido matemático?? kkkkkkkk)

No caso, dada uma lista não vazia, temos uma função chamado enumerate que enumera todos os índices da lista.

Em outras palavras, é como uma sequência que exibe os seus índices donde cada elemento está definido

    """
    enumerate - enumera iteráveis (índices)
    """
    # O enumerate faz algo do tipo de baixo numa lista
    # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
    lista = ['Maria', 'Helena', 'Luiz']
    lista.append('João')
    print(enumerate(lista))
    print(list(enumerate(lista)))
    # Podemos definir a partir de qual índice começará a ser enumerado.
    print(list(enumerate(lista, start=19)))
    print('-----------------------')
    # Curioso que quando colocamos o enumerate no for, não precisamos colocar o list para iterar
    for indice, nome in enumerate(lista):
        print(indice, nome, lista[indice])
    print('-----------------------')

    for item in enumerate(lista):
        print(item)
        indice, nome = item
        print(indice, nome)
    print('-----------------------')

    for tupla_enumerada in enumerate(lista):
        print('FOR da tupla:')
        for valor in tupla_enumerada:
            print(f'\t{valor}')
    print('-----------------------')

No caso, pelo enumerate, o formato em que será exibido o indice e o elemento definido nesse índice estará no formato de tupla.

## Aula 78 - Exercício - crie uma lista de compras com listas:
Vamos praticar listas!

Segue a sentença

    """
    Faça uma lista de comprar com listas
    O usuário deve ter a possibilidade de
    inserir, apagar e listar valores da sua lista
    Não permita que o programa quebre com 
    erros de índices inexistentes na lista.
    """

## Aula 79 - Solução do exercício - crie uma lista de compras com listas (com try / except):
Compare com a solução do professor!

## Aula 80 - Imprecisão dos números de ponto flutuante + round e decimal.Decimal:
O problema dos números de ponto flutuante é similar ao que estudei em JavaScript.

No caso, vale dar uma revisada no conceito e se quiser aprofundar mais ainda no probelma, seguir os links abaixo de leitura

    https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

Bom, existem várias formas de arrumarmos o problema de arredondamento

    number_1 = 0.1
    number_2 = 0.7
    number_3 = number_1 + number_2
    print(number_3)
    print(f'{number_3:.2f}')
    print(round(number_3, 2))
    print('-------------------')

Agora, uma outra forma mais assetiva de resolvermos esse problema de arredondamento, é importando um módulo chamado decimal

    import decimal

    numero_1 = decimal.Decimal('0.1')
    numero_2 = decimal.Decimal('0.7')
    numero_3 = numero_1 + numero_2
    print(numero_3)
    print(f'{numero_3:.2f}')
    print(round(numero_3, 2))
    print('-------------------')

## Aula 81 - split, join e strip são métodos muito úteis da str:
Vamos aprender a usar o split e join para lidar com lista e string.

Seguir os links de leitura abaixo sobre tais métodos

    https://www.geeksforgeeks.org/python-program-split-join-string/
    https://www.freecodecamp.org/news/python-string-split-and-join-methods-explained-with-examples/

Bom, por começo, vamos tentar manipular o seguinte string

    frase = 'Olha só que, coisa interessante'

No caso, o split, ele é um método que ajuda a dividir uma string de acordo com um tipo de caractere que vc pede para ele separar

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)
    print(lista_palavras)

Além disso, podemos usar o método strip, donde ela é o método que tira os espaços do início e o fim de uma frase

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        print(lista_palavras[i].strip())
        
    print(lista_palavras)

O strip, podemos optar por qual lado do espaço das frases que queremos eliminar, usand "r", de right, ou "l", de left

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        print(lista_palavras[i].strip())
        print(lista_palavras[i].rstrip())
        print(lista_palavras[i].lstrip())
        
    print(lista_palavras)

Podemos, nessa iteração, corrigir os elementos dentro da lista, tirado os espaços usando o strip

    frase = 'Olha só que, coisa interessante'
    # lista_palavras = frase.split()
    lista_palavras = frase.split(',')
    print(frase)

    for i, frase in enumerate(lista_palavras):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        lista_palavras[i] = lista_palavras[i].strip()
        
    print(lista_palavras)

Claro, o formato acima é de forma enxuta, mas dificulta a leitura do código. Em seu formato de boa prática ficaria o seguinte

    frase = '     Olha só que    , coisa interessante    '
    # lista_palavras = frase.split()
    lista_palavras_cruas = frase.split(',')
    print(frase)
    lista_palavras = []

    for i, frase in enumerate(lista_palavras_cruas):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        # lista_palavras[i] = lista_palavras[i].strip()
        lista_palavras.append(lista_palavras_cruas[i].strip())
        
    print(lista_palavras_cruas)
    print(lista_palavras)

Agora, o join, é um outro método de string e ela tem por finalidade unir as frases.

    frase = '     Olha só que    , coisa interessante    '
    # lista_palavras = frase.split()
    lista_palavras_cruas = frase.split(',')
    print(frase)
    lista_palavras = []

    for i, frase in enumerate(lista_palavras_cruas):
        # print(lista_palavras[i].strip())
        # print(lista_palavras[i].rstrip())
        # print(lista_palavras[i].lstrip())
        # lista_palavras[i] = lista_palavras[i].strip()
        lista_palavras.append(lista_palavras_cruas[i].strip())
        
    # print(lista_palavras_cruas)
    # print(lista_palavras)
    # frases_unidas = ''.join('abc')
    # frases_unidas = '-'.join('abc')
    # frases_unidas = '-'.join(lista_palavras)
    frases_unidas = ', '.join(lista_palavras)
    print(frases_unidas)

Nesse método, note que, precisamos passar algum parâmetro para ela para unir seja ela os caracteres de uma frase string ou seja ela os elementos de uma lista. Por exemplo, no join usado para 'frases_unidas = '-'.join('abc')', note que, ao rodarmos o códido printando-a, será retornado 'a-b-c'. Se for vazio, '', será retornado a mesma string que foi colocado no join. A mesma lógica vale para listas. Enquando que em uma string, cada caracteres que compõe uma string é vista como um elemento, na lista é a mesma coisa.

Obs: Até agora, somente a lista, string e tuples são iteráveis.

## Aula 82 - Listas dentro de listas (iteráveis dentro de iteráveis):
É mais para quem não entendeu direito o conceito. Visto que se vc mnaja de matriz, então acaba sendo mais fácil a sua compreensão.

Obs: lista dentro de lista, generalizando-a é iteráveis dentro de iteráveis, pois podemos fazer isso combinando entre lista, string e tuplas tbm.

## Aula 83 - Detalhes sobre o interpretador do Python:
São comandos que vc pode executar pelo terminal propriamente da linguagem python. Ou seja, é uma forma de linux shell mas para o python.

    """
    Interpretador do Python

    python mod.py (executa o mod) (Pode ser colocado a path dentro de "" onde se encontra o arquivo .py para executar a mesma)
    python -u (unbuffered)
    python -m mod (lib mod como script)
    python -c 'cmd' (comando)
    python -i mod.py (interativo com mod)

    The Zen of Python, por Tim Peters // é um poema explicando as boas práticas de código no python. Basta jogar no termianl "python -c 'import this'", ou vc pode até colocar dentro de um arquivo esse "import this" e rodar esse arquivo.

    Bonito é melhor que feio.
    Explícito é melhor que implícito.
    Simples é melhor que complexo.
    Complexo é melhor que complicado.
    Plano é melhor que aglomerado.
    Esparso é melhor que denso.
    Legibilidade conta.
    Casos especiais não são especiais o bastante para quebrar as regras.
    Embora a praticidade vença a pureza.
    Erros nunca devem passar silenciosamente.
    A menos que sejam explicitamente silenciados.
    Diante da ambiguidade, recuse a tentação de adivinhar.
    Deve haver um -- e só um -- modo óbvio para fazer algo.
    Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
    Agora é melhor que nunca.
    Embora nunca frequentemente seja melhor que *exatamente* agora.
    Se a implementação é difícil de explicar, é uma má ideia.
    Se a implementação é fácil de explicar, pode ser uma boa ideia.
    Namespaces são uma grande ideia -- vamos fazer mais dessas!
    """

Obs: Um detalhe que até agora não foi visto e que foi feito as aulas e exercícios de programas de forma natural, seria sobre o uso do ponto é vígula,;. No JavaScript, podemos ver que toda hora usamos esse caractere e até agora em python não ocorreu esse uso do caractere. Mas isso não significa que no python não tenha isso. Ou seja, tem sim. E vamos ver os momentos convenientes em que esse ponto e vígula seria necessário ser utilizado.

## Aula 84 - Desempacotamento em chamadas de funções:

## Aula 85 - Operação ternária com Python (if e else de uma linha):

## Aula 86 - Exercício - Gerar o primeiro dígito de um CPF com Python:

## Aula 87 - Solução do exercício - Gerar o primeiro dígito de um CPF com Python:

## Aula 88 - Exercício - Gerar o segundo dígito de um CPF com Python:

## Aula 89 - Solução do exercício - Gerar o segundo dígito de um CPF com Python:

## Aula 90 - Possíveis problemas e soluções para nosso algoritmo do CPF:

## Aula 91 - Criando um gerador de CPFs com nosso algoritmo e Python:
