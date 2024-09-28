# Aula 61 - range + for para usar intervalos de números:
Vamos ver sobre o range usado no for.

Lembrando que o range ele não depende do for assim como o for não depende do range para o seu uso.

No caso, o range ele nos permite definir o intervalo de iteração do for

    """
    For + Range
    range -> range(start, stop, step)
    """

No caso, como descrito acima, no range podemos definir o start, stop e o step, respectivamente, o começo, o alcance e os passos. No caso, o começo e o alcance seria definitivamente o intervalo em que iremos compilar seguindo a regra do conjunto dos números naturais de [n] = {0, 1, 2, ..., n-2, n-1}, visto que definimos range(0, n) ou range(n), para n um natural. E o step serve para definir os passos em que vc quer que a iteração pule.

Segue um exemplo simples do uso do range no for

    for i in range(10):
        print(i)
    print('----------------------')
    for i in range(0,10):
        print(i)
    print('----------------------')
    for i in range(5,10):
        print(i)
    print('----------------------')

Um exemplo usando o step

    numeros = range(0, 100, 8)

    for numero in numeros:
        print(numero)

Bom, assim como vimos em JavaScript, em python, usando o step, podemos usar números negativos tbm. No caso, se quisermos usar o step negativo, vamos precisar que os pontos de partidas e finais sejam negativos tbm

    for i in range(0,-10, -2):
        print(i)
