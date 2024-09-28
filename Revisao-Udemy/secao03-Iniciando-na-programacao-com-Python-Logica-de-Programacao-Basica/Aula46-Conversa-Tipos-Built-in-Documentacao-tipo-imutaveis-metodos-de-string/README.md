# Aula 46 - Conversa - tipos built-in, documentação, tipo imutáveis, métodos de string:
Vamos ver um pouco da documentação do python dos tipos que já bem imbutidos dentro dessa linguagem

    https://docs.python.org/pt-br/3/library/stdtypes.html

No caso, os que vamos ver são os tipos imutáveis. São elas:

    str, int, float, bool

No caso, por serem valores imutáveis, serve a mesma a lógica que eu vi nos estudos de JavaScript. No sentido de que se fizermos algo do tipo

    string = 'Leonardo Takashi Teramatsu'
    outra_variavel = string

Automaticamente fizemos uma cópia da variável string acima. O que difere com objetos.

Além disso, o fato de ser imutável, uma vez atribuída um valor não podemos mudar o valor interno dela

    string = 'Leonardo Takashi Teramatsu'
    string[3] = 'ABC'

Ou seja, o código acima retornará um erro.

No caso, a forma correta de mudar algum valor atribuído em uma variável é criando uma outra variável da mesma e realizar o seguinte

    string = 'Leonardo Takashi Teramatsu'
    outra_variavel = f'{string[:3]}ABC{string[4:]}'

Ou seja, usamos o format string para conseguirmos formatar o valor interno de uma string.

Além disso, as strings tem os seus métodos tbm, como, por exemplo, se quisermos realizar alguma personalização na string podemos usar o método capitalize

    string = 'leonardo takashi teramatsu'
    print(string.capitalize())

Assim como tem outras e muitos métodos para string, onde vc poderá consultar na documentação acima.
