# Aula 75 - Introdução ao empacotamento e desempacotamento:
No caso, vamos ver sobre atribuição via desestruturação (conhecido como empacotamento e desempacotamento) para lista em Python.

No caso, será a minha revisão sobre atribuição via desestruturação.

No caso, a lógica é a mesma do que estudei em JavaScript

    nomes = ['Maria', 'Helena', 'Luiz']

    nome1, nome2, nome3 = nomes

    print(nome1)
    print(nome2)
    print(nome3)

Agora, da mesma forma em JavaScript, as quantidades de variáveis tem que ser equivalentes com a quantidade de elementos que tem dentro da lista.

Além disso, se quisermos definir somente uma variável usando a atribuição via desestruturação, a prática é análoga do que vimos em JavaScript

    nome1, *resto = nomes
    print(nome1)
    print(resto)

Ou seja, a única coisa que diferencia com o JavaScript está na sintaxe.

Com relação ao resto, existe uma boa prática entre os desenvolvedores que indicam que o resto que tiver na lista não irei usar. Para isso, usamos o underline

    # nome1, *resto = nomes
    nome1, *_ = nomes
    print(nome1)
    # print(resto)
    print(_)

O mesmo serve para variáveis, usando atribuição via desestruturação, de que não vamos querer usar

    # nome1, *resto = nomes
    # nome1, *_ = nomes
    _, nome2, *_ = nomes
    # print(nome1)
    print(nome2)
    # print(resto)
    print(_)
