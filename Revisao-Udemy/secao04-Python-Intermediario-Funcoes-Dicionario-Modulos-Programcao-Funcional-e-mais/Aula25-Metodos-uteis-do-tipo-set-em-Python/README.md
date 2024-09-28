# Aula 25 - Métodos úteis do tipo set em Python:
Vamos aprender os métodos mais usuais para essa sintaxe "set".

São elas as mais usadas para "set()":

- add:

    No caso, como o nome já disse, essa sintaxe "set()" serve para adicionar elementos dentro de um "set()", como segue

        s9 = set()
        s9.add('Leonardo')
        s9.add(1)
        print(s9)

    Lembrando que esse método ela não admite em adicionar vários valores, mas, sim, apenas um valor por vez.

- update:

    O update, a sua forma de uso, é muito parecido com o que vimos para o dicionário. No caso, podemos usar esse update para conseguirmos adicionar um conjunto de elementos dentro do set, como segue

        s10 = set()
        s10.update('Hello')
        s10.update(('Hello'))
        print(s10)

    Por quê que estou mostrando duas formas de adicionar, via update, o "Hello"? No caso, a primeira forma, sem a tupla, é o mesmo que eu estar passando "set('Hello')" que isso irá realizar uma iteração, ou seja, irá considerar como elemento dentro do "set" cada caractere. Já, se quisermos que a palavra "Hello" se torne elemento dentro do "set" será necessário usar o "()" para conseguirmos passar ela como elemento, assim, como um conjunto de outros iteráveis.

        s10.update(('Hello', 1, 2, 3, 4, 5, 'Teramatsu'))

- discard:

    O discard serve para remover um elemento dentro do "set" passando diretamente o valor imutável que vc queira eliminar dentro dele

        s10.discard('Hello')
        print(s10)

- clear:

    Já o "clear" ela serve para podermos limpar o "set" que já tem os elementos

        s10.clear()
        print(s10)

Link para verificar os outros métodos existentes para a sintaxe "set":

    https://docs.python.org/2/library/sets.html
    https://www.programiz.com/python-programming/methods/set