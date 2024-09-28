# Aula 80 - Imprecisão dos números de ponto flutuante + round e decimal.Decimal:
O problema dos números de ponto flutuante é similar ao que estudei em JavaScript.

No caso, vale dar uma revisada no conceito e se quiser aprofundar mais ainda no probelma, seguir os links abaixo de leitura

    https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    https://docs.python.org/pt-br/3/tutorial/floatingpoint.html

Bom, existem várias formas de arrumarmos o problema de arredondamento

    number_1 = 0.1
    number_2 = 0.7
    number_3 = number_1 + number_2
    print(number_3)
    print(f'{number_3:.2f}')
    print(round(number_3, 2))
    print('-------------------')

Agora, uma outra forma mais assetiva de resolvermos esse problema de arredondamento, é importando um módulo chamado decimal

    import decimal

    numero_1 = decimal.Decimal('0.1')
    numero_2 = decimal.Decimal('0.7')
    numero_3 = numero_1 + numero_2
    print(numero_3)
    print(f'{numero_3:.2f}')
    print(round(numero_3, 2))
    print('-------------------')
