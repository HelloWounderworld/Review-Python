# Aula 37 - Introdução ao try e except para capturar erros (exceptions):
Vamos ver sobre try e except.

Basicamente, o try, como o nome já disse, é tentar executar uma ação e ver o que acontece depois disso. Em JavaScript, por exemplo, isso está muito presente quando é usado o try, catch e finally. E a funcionalidade é algo parecido para python com as sintaxes try e except.

No caso, vamos apenas mostrar uma introdução desses conceitos

    """
    Introdução ao try/except
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar
    """

    print(1234)
    print(456)
    # int('a')
    # float('a')

Note que, o int e o float usado, no exemplo acima, ao descomentarmos elas e simularmos, vamos conseguir ver que será exbido uma msg de erro pelo terminal.

Agora, nesse exemplo de baixo, podemos ver o caso em que o operador * ele funciona como uma espécie de repetição, caso for string, e de múltiplicação, caso for um number

    numero = input('Vou dobrar o número que vc digitar: ')
    numero_float = float(numero)

    print(f'O dobre de {numero} é {numero * 2}')
    print(f'O dobre de {numero} é {numero_float * 2}')
    print(f'O dobre de {numero} é {numero_float * 2:.0f}')
    print(f'O dobre de {numero} é {numero_float * 2:.2f}')

Usamos um método aqui, tbm, para verificar se o que foi colocado dentro do input são apenas números ou não, cujo método se chama isdigit()

    numero_str = input('Vou dobrar o número que vc digitar: ')
    print(numero_str.isdigit())

    numero_float = float(numero_str)

    print(f'O dobre de {numero_str} é {numero_str * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')

Bom, esse método nos permite usar nas condicionais para conferir se os dados estão ou não certos

    numero_str = input('Vou dobrar o número que vc digitar: ')
    # print(numero_str.isdigit())

    if numero_str.isdigit():
        numero_float = float(numero_str)
        print(f'O dobre de {numero_str} é {numero_str * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
    else:
        print('Isso não é um número')

Bom, até agora, nada de try/catch, pois mostramos outras formas de driblar essas sintaxes. Porém, podemo usar nesses casos tbm

    numero_str = input('Vou dobrar o número que vc digitar: ')
    # print(numero_str.isdigit())

    try:
        # ...
        print('STR: ', numero_str)
        numero_float = float(numero_str)
        print('FLOAT: ', numero_float)
        print(f'O dobre de {numero_str} é {numero_str * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.0f}')
        print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
    except:
        # ...
        print('Isso não é um número')

No código acima, vc vai ver que se colocarmos no input algo que não seja número, ou um mix de números com outros caractéres, ocorrerá um erro no numero_float e isso irá fazer com que do try seja direcionado imediatamente no except.

Mas aí entra na seguinte pergunta. Se tem meios para driblar usando as condicionais em vez de try/catch, então por quê temos que usa-las?

Bom, aí entra na questão de entender das limitações das condicionais. Por exemplo, existem casos em que há uma excessão em que a condicional não consegue dar conta ou considerar, mesmo que a lógica aplicada para tais regra de negócio estejam certos. Existem casos em que isso não consegue cobrir todas as possibilidades que um algoritmo atende das exigências humanas. Daí, entra em papel a importância de uso do try/catch.

Ou seja, basicamente, a ideia e que se vc verificar uma situacao em que seja necessario testar algo, mas que nao da para computar todas as possibilidades, o uso do try/cath acaba sendo essencial. O uso da condicional, apenas, se usa em situacoes em que vc verifica se uma determinada regra de negocio ou ate mesmo as possibilidades estao todas computaveis para serem analisadas e que basta que uma delas sejam satisfeitas, isso em uma situacao mais controlada.
