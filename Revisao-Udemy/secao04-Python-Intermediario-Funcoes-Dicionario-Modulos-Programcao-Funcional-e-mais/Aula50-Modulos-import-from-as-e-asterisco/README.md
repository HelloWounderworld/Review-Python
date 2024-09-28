# Aula 50 - Módulos - import, from, as e *:
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
