# Aula 70 - count é um iterador sem fim (itertools):
Vamos mostrar um contador infinito em Python, que se chama "count" que é um método dentro do módulo itertools.

Basicamente, o "count" ele é um contador infinito e um iterador sem fim.

Vamos, por começar, a importar tal método

    from itertools import count

    c1 = count()

    print(next(c1))
    print(next(c1))

Vamos conseguir ver que irá retornar 0 e 1.

Bom, se vc lembra de algumas longas aulas anteriores, existem formas de conferir se um determinado método ele é um iterador e iterável

    from itertools import count

    c1 = count()

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

Coisa que, no r1 = range(10), podemos ver que não é true em todos

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

Ou seja, conseguimos ver que o "range" ele é um iterável, mas não é o iterador.

Agora, lembrando que o método "count()" é um iterável infinito, então se usarmos o "for" de forma imprecisa, irá entrar num loop infinito, o que vc deverá tomar cuidado

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    for i in c1:
        if i >= 100:
            break

        print(i)

Perceba que a contagem do for acima está começando pelo 2, pois já foi feito a iteração pelo next nos dois prints acima.

Bom, se o seu computador não for muito possante, isso poderia travar o seu computador se não colocarmos algum break dentro do for iterando o count(), visto que esse método é um iterador/contador infinito.

Diferentemente de range, que sempre que usamos ele, precisamos definir um fim para ele

    from itertools import count

    c1 = count()
    r1 = range(10)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    for i in c1:
        if i >= 100:
            break

        print(i)
    print()
    for j in range(100):
        print(j)

Bom, visto que no range, também, é possível definir o início tbm. O mesmo vale para o count

    from itertools import count

    c1 = count(10)
    r1 = range(10, 100)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    print('count')
    for i in c1:
        if i >= 100:
            break

        print(i)
    print()
    print('range')
    for j in r1:
        print(j)

Da mesma forma que conseguimos definir os steps no range, no sentido de iterar apenas os múltiplos de número $`n`$, sendo $`n\in\mathbb{N}`$.

Da mesma forma que podemos definir direito para quem começa ou qual será o step

    from itertools import count

    c1 = count(10)
    c2 = count(step=5, start=10)
    r1 = range(10, 100)

    print(next(c1))
    print(next(c1))

    print('c1', hasattr(c1, '__iter__'))
    print('c1', hasattr(c1, '__next__'))

    print('r1', hasattr(r1, '__iter__'))
    print('r1', hasattr(r1, '__next__'))

    print('count')
    for i in c1:
        if i >= 100:
            break

        print(i)

    for k in c2:
        if k >= 100:
            break

        print(k)
    print()
    print('range')
    for j in r1:
        print(j)
