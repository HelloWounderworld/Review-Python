# Aula 05 - (Parte 1) Escopo de funções e módulos em Python + global:
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