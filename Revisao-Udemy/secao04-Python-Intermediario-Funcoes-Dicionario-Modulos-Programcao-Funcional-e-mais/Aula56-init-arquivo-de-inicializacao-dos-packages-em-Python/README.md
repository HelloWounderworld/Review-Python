# Aula 56 - __init__.py é um arquivo de inicialização dos packages em Python:
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
