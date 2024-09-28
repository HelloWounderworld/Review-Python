# Aula 36 - List comprehension com mais de um for:
Uma outra coisa legal de list comprehension em python é que podemos usar iterações dentro de iterações. Ou seja, quantos for que quisermos.

Suponhamos o seguinte cenário

    lista = []

    for x in range(3):
        for y in range(3):
            lista.append((x,y))

Bom, vamos tentar realizar o cenário acima usando list comprehension. No caso, ficaria da seguinte forma

    lista2 = [(x,y) for x in range(3) for y in range(3)]

Lembrando, que no list comprehension, o que fica no lado esquerdo do for é o que será incluído dentro da lista.

Essa mesma forma de iteração podemos realizar da seguinte forma tbm

    lista3 = [
        [x for y in range(3)]
        for x in range(3)
    ]

Em outras palavras, a interpretação disso seria, para cada índice x itero o x dentro da lista, que fica dentro da lista, três vezes pelo índice y.

Bom, o legal disso é que podemos usar para criação de matrizes de forma rápida para aplicações de conceitos de álgebra linear, Análise no Rn e Probabilidade e Estatística.

# Aula 37 - Mais detalhes sobre list comprehension:
Eu criei um vídeo gratuito falando muito mais sobre list comprehension tirando como base as dúvidas desse curso. Veja em 

    https://youtu.be/1YbTDczvqco

Professor Luiz Otávio!