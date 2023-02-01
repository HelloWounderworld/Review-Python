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


## Aula 08 - Tipo int e float (números) - Introdução aos tipos de dados:

## Aula 09 - Tipo bool (boolean) - Introdução aos tipos de dados:

## Aula 10 - Coerção de tipos (convertendo um tipo para outro):