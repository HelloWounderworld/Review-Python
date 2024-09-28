# Aula 54 - Introdução aos packages (pacotes) em Python:
Bom, até agora, criamos vários módulos e realizamos os devidos estudos acima dele.

Mas, agora, vamos introduzir o conceito de pacotes (packages) que seria o caso de uma pasta que carrega varios módulos.

Para isso, vamos criar o arquivo principal, aula54.py, e no mesmo nível desse arquivo vamos criar uma pasta chamado "aula54_p" e dentro dessa pasta vamos criar um arquivo com o nome "modulo.py".

Agora, no arquivo principal/raiz, aula54.py, vamos importar o módulo que está dentro do pacote, aula54_p. Para isso, vamos colocar o seguinte

    import aula54_p.modulo

Agora, no módulo, modulo.py, nela definimos o seguinte

    def soma_do_modulo(x, y):
        return x + y

Bom, agora, para conseguirmos usar dos recursos definidos dentro do módulo, modulo, é a mesma coisa como vimos nas aulas anteriores, no arquivo, aula54.py, colocamos

    import aula54_p.modulo

    print(aula54_p.modulo.soma_do_modulo(2, 3))

Daí, podemos verificar que estamos usando o método que definimos dentro do módulo, modulo.

Para mais detalhes de como está relacionado e qual arquivo é o main, vamos colocar o seguinte

    from sys import path

    import aula54_p.modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))

Bom, ao rodarmos o arquivo, notamos que o print(*path, sep='\n') ela irá mostrar todos as paths reconhecendo se tem ou não algum módulo python definido nela.

Da mesma forma, podemos importar o método diretamente dentro do módulo que definimos

    from sys import path

    import aula54_p.modulo
    from aula54_p.modulo import soma_do_modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))

Conseguimos, também, apelidar usando alias, "as".

Agora, uma outra curiosidade que temos, é importar somente o módulo inteiro dentro de um pacote. No caso, para isso realizamos o seguinte

    from sys import path

    import aula54_p.modulo
    from aula54_p import modulo
    from aula54_p.modulo import soma_do_modulo

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))
    print(modulo.soma_do_modulo(4, 5))

No caso, no "from aula54_p import modulo", vc está conseguindo importar o módulo inteiro, modulo. E a forma de usarmos os métodos definidos dentro desse módulo, modulo, é usando o name space.

Bom, daí temos outras formas de importar que é similar ao que vimos nas três últimas aulas.

    from sys import path

    import aula54_p.modulo
    from aula54_p import modulo
    from aula54_p.modulo import soma_do_modulo
    from aula54_p.modulo import *

    print(__name__)
    print(*path, sep='\n')
    print(aula54_p.modulo.soma_do_modulo(2, 3))
    print(soma_do_modulo(3, 4))
    print(modulo.soma_do_modulo(4, 5))

Onde, vimos que a forma de importar "from aula54_p.modulo import *" é considerada de má prática. Porém, no cenário em que estamos, que temos liberdade de criar um pacote e módulo personalizado, caso importamos por essa prática considerada ruim, conseguimos selecionar os tipos de recursos que podem ser importados usando a sintaxe "__all__". No caso, no módulo, modulo, colocamos o seguinte

    __all__ = [
        'variavel'
    ]

    print('Este modulo, modulo.py, tem o nome: ', __name__)

    variavel = 'Leonardo'

    def soma_do_modulo(x, y):
        return x + y

Ao colocarmos, dentro da lista __all__, a variavel, na forma de importação, from aula54_p.modulo import *, o "tudo" que conseguimos importar desse módulo será considerado somente as que estejam dentro dessa lista "__all__".

Bom, claro que, se comentarmos a lista "__all__" inteirinha, vamos cuspir todo o recurso para a fora dessa lista e conseguiremos usar dentro da forma de importação de má prática, from aula54_p.modulo import *.

Link para leitura:

    https://realpython.com/python-modules-packages/
