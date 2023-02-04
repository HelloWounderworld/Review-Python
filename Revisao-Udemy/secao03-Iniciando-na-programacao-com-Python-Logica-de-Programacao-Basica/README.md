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


## Aula 15 - Concatenação (+) e repetição (*) com operadores aritméticos:

## Aula 16 - Precedência entre os operadores aritméticos:

## Aula 17 - Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis:

## Aula 18 - Solução exercício de programação - Cálculo do IMC:

## Aula 19 - Uma introdução às f-strings (formatação de strings):

## Aula 20 - Formatação de strings com o método format:

## Aula 21 - Usando a função input para coletar dados do usuário:

## Aula 22 - Introdução aos blocos de código + if / elif / else (condicionais):

## Aula 23 - if, elif e else: entendendo o fluxo do interpretador em condicionais:

## Aula 24 - O Debugger do VS Code e o interpretador do Python lendo os códigos:

## Aula 25 - Operadores relacionais (de comparação) em Python:

## Aula 26 - Exercício de programação com if e comparação:

## Aula 27 - Solução - Exercício de programação com if e comparação:

## Aula 28 - Operador Lógico "and":

## Aula 29 - Operador Lógico "or":

## Aula 30 - Operador lógico "not":

## Aula 31 - Operadores in e not in:

## Aula 32 - Interpolação de string com % em Python:

## Aula 33 - Formatação de strings com f-strings:

## Aula 34 - Fatiamento de strings e a função len:

## Aula 35 - Exercício: teste seu conhecimento até aqui:

## Aula 36 - Solução - Exercício: teste seu conhecimento até aqui:

## Aula 37 - Introdução ao try e except para capturar erros (exceptions):

## Aula 38 - Parte 1: Variáveis, constantes e complexidade de código:

## Aula 39 - Parte 2: Variáveis, constantes e complexidade de código:

## Aula 40 - id - A identidade do valor que está na memória:

## Aula 41 - Flags, is, is not e None:

## Aula 42 - Exercícios - Enunciados:

## Aula 43 - Solução 1 dos Exercícios - Enunciados:

## Aula 44 - Solução 2 dos Exercícios - Enunciados:

## Aula 45 - Solução 3 dos Exercícios - Enunciados:

## Aula 46 - Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string:

## Aula 47 - while e break - Estrutura de repetição (Parte 1):

## Aula 48 - while - Condição em detalhes:

## Aula 49 - Operadores de atribuição com operadores aritméticos:

## Aula 50 - while + continue - pulando alguma repetição:

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
