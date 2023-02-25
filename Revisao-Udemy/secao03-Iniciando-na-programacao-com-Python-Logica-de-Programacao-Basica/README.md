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

## Aula 52 - Exercício guiado com while:

## Aula 53 - Solução do exercício guiado com while:

## Aula 54 - Exercício guiado - Calculadora - Parte 1:

## Aula 55 - Exercício guiado - Calculadora - Parte 2:

## Aula 56 - Exercício guiado - Calculadora - Parte 3:

## Aula 57 - while / else (recurso peculiar do Python):

## Aula 58 - while - Qual letra apareceu mais vezes na frase? (Iterando strings com while):

## Aula 59 - DEBUGGER: while - Qual letra apareceu mais vezes na frase?:

## Aula 60 - Introdução ao for / in - estrutura de repetição para coisas finitas:

## Aula 61 - range + for para usar intervalos de números:

## Aula 62 - Como o for funciona por baixo dos panos? (next, iter, iterável e iterador):

## Aula 63 - O que aprendemos com while também funciona no for (continue, break, else, etc):

## Aula 64 - Exercício - Jogo da palavra secreta:

## Aula 65 - Sobre exercícios - não saber é normal:

## Aula 66 - (Parte 1) Solução do exercício - Jogo da palavra secreta:

## Aula 67 - (Parte 2) Solução do exercício - Jogo da palavra secreta:

## Aula 68 - Tipo list - Introdução às listas mutáveis em Python:

## Aula 69 - Alterando uma lista com índices, del, append e pop (Tipo list):

## Aula 70 - Inserindo itens em qualquer índice da lista com insert (Tipo list):

## Aula 71 - Concatenando e estendendo listas em Python:

## Aula 72 - Cuidados com tipos de dados mutáveis - list e copy:

## Aula 73 - for in com tipo list:

## Aula 74 - Exercício - exiba os índices da lista (aula com solução):

## Aula 75 - Introdução ao empacotamento e desempacotamento:

## Aula 76 - Tipo tuple (tuplas):

## Aula 77 - enumerate para enumerar valores de iteráveis (pegar índices):

## Aula 78 - Exercício - crie uma lista de compras com listas:

## Aula 79 - Solução do exercício - crie uma lista de compras com listas (com try / except):

## Aula 80 - Imprecisão dos números de ponto flutuante + round e decimal.Decimal:

## Aula 81 - split, join e strip são métodos muito úteis da str:

## Aula 82 - Listas dentro de listas (iteráveis dentro de iteráveis):

## Aula 83 - Detalhes sobre o interpretador do Python:

## Aula 84 - Desempacotamento em chamadas de funções:

## Aula 85 - Operação ternária com Python (if e else de uma linha):

## Aula 86 - Exercício - Gerar o primeiro dígito de um CPF com Python:

## Aula 87 - Solução do exercício - Gerar o primeiro dígito de um CPF com Python:

## Aula 88 - Exercício - Gerar o segundo dígito de um CPF com Python:

## Aula 89 - Solução do exercício - Gerar o segundo dígito de um CPF com Python:

## Aula 90 - Possíveis problemas e soluções para nosso algoritmo do CPF:

## Aula 91 - Criando um gerador de CPFs com nosso algoritmo e Python:
