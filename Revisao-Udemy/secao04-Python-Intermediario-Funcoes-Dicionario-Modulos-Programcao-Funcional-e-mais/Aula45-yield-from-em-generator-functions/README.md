# Aula 45 - yield from em generator functions:
Podemos, também, usar o yield from em funções generators. O que é isso?

Basicamente, o yield from ela importa o processo de uma outra função generator para uma outra função.

Exemplo, suponhamos as duas seguintes funções

    def gen1():
        yield 1
        yield 2
        yield 3

    def gen2():
        yield 4
        yield 5
        yield 6

Bom, note que, a função gen2 é uma continuação da função gen1. Daí, existem situações em que depois que ocorrer um processo numa determinada função eu quero que o processo seja continuado numa outra função. Para isso que serve o yield from, que bastaria usar da seguinte forma

    def gen1():
        yield 1
        yield 2
        yield 3

    def gen2():
        yield from gen1()
        yield 4
        yield 5
        yield 6

    gen = gen2()

    for numero in gen:
        print(numero)

Daí, será exibido todos os números de 1 até 6.

Bom, com isso podemos fazer coisas bem mais interessantes. Recomendo o leitor tentar entender a lógica de programação que está no código do arquivo aula45.py.
