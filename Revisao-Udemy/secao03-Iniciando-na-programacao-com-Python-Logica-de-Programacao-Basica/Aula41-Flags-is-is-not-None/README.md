# Aula 41 - Flags, is, is not e None:
Vamos continuar da aula anterior.

Uma outra prática muito ruim seria criar uma variavel dentro de um bloco de código para que seja usado depois, fora dela

    condicao = False

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        print('Não faça algo')

    print(passou_no_if)

No caso, do exemplo acima é uma má prática disso. O motivo de ser uma má prática seria devido ao fato de que se tiver um caso em que uma dada condição não faça entrar no if, significa que essa variável nunca havia sido criado. E isso fará com que tenha alguma possibilidade de ter algum erro pela frente.

No caso, o que seria uma boa prática nisso?

Seria criar uma variável fora do bloco e só depois disso usar dentro do bloco. No caso, temos duas alternativas para corrigir essa má prática

    condicao = False

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        passou_no_if = None
        print('Não faça algo')

    print(passou_no_if)

Acima, é uma das formas de solucionar, porém de forma pior, pois nela estaríamos dependendo do else. Então, a melhor forma seria o seguinte

    condicao = True
    passou_no_if = None

    if condicao:
        passou_no_if = True
        print('Faça algo')
    else:
        print('Não faça algo')

    print(passou_no_if, passou_no_if is None)

No caso, foi declarado a variável antes de entrar no if e isso evitará futuros problemas de usar alguma variável não declarada.
