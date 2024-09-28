# Aula 33 - Introdução à List comprehension em Python:
Vamos aprender a mexer com list Comprehension.

Basicamente, o List comprehesion é uma forma rápida de criar listas a partir de iteráveis. Segue o exemplo

    print(list(range(10)))

No caso, acima, será criado uma lista de conjunto [10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. No caso, o exemplo acima, é só uma motivação, pois não usamos nada de lista até então. Agora, segue o seguinte exemplo, que seria a abordagem do contexto

    lista = []

    for i in range(10):
        lista.append(i)

    print(lista)

No caso, a forma acima nos permite mais flexibilidade para inclusão de alguma lógica para conseguirmos manipular a forma que queremos criar uma lista por iteração. Porém, podemos realizar isso de forma mais fácil, em vez de gastar mais linhas de código, que, agora sim, estamos entrando no assunto principal

    lista = [i for i in range(10)]
    print(lista)

No caso, o formato é mais ou menos assim

    [(valor que vc quer colocar) for i in range(n) (que será colocado n vezes)]

Ou seja, no lugar de "i" poderia ser tbm

    lista = [1 for i in range(10)]

Daí, será colocado o número 1 dez vezes.

E claro, podemos colocar uma lógica dentro dessa iteração rápida tbm. O que diversifica as alternativas de formas para monstar uma lista, como segue

    lista = [i * 2 for i in range(10)]
    print(lista)

Conseguimos, também, realizar uma operação ternária dentro disso para termos mais controle do que será ou não colocado dentro da lista.
