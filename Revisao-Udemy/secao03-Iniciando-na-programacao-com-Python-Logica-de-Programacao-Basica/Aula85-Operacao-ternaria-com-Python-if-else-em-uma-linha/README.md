# Aula 85 - Operação ternária com Python (if e else de uma linha):
A Operação ternária nas linguagens de programação são bem famosas. Basicamente, estamos fazendo if-else em uma única linha.

    print('Valor' if True else 'Outro valor')
    print('Valor' if False else 'Outro valor')

    condicao = 10 == 10
    variavel = 'Valor' if condicao else 'Outro valor'
    print(variavel)

No caso, a única diferença é que nas outras linguagens a sintaxe para expressar essa lógica ternária é por "? :".

Com a operação ternária podemos realizar, mesmo que não seja o recomendável, uma concatenação de lógica

    'Valor' if True else 'Valor2' if True else 'Valor3' if True ...
