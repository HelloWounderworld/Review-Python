# Aula 31 - Funções lambda complexas (para entendimento):
Bom, vamos ver como podemos verificar que tais funções podem ou não serem convertidos em uma função lambda.

Segue as funções seguintes

    def executa(funcao, *args):
        return funcao(*args)

    def soma(x,y):
        return x + y

    def cria_multiplicador(multiplicador):
        def multiplica(numero):
            return numero * multiplicador
        return multiplica
    
    print(executa(cria_multiplicador(soma(1,3)), 10))

Vamos, agora, aprender a converter as funções acima em funções lambdas.

- Primeiro, vamos converter a função soma em função lambda

        print(
            executa(
                lambda x,y: x+y,
                9, 3
            ),
            executa(soma, 9,3),
            soma(9,3)
        )

    Note que, a forma acima, retornará o que precisamos.

    Uma outra forma mais eficiente de realizarmos essa soma para mais e mais parâmetros seria da seguinte forma

        print(
            executa(
                lambda *args: sum(args),
                1,2,3,4,5,6,7
            )
        )

    Neste caso, estou usando a função "sum" para conseguirmos  realizar as devidas somas.

- Agora, vamos converter a função cria_multiplicador em uma função lambda:

    No caso, essa função, como ela executa uma outra função que está definida dentro dela, ficaria um pouco mais complicado realizar a devida execução

        duplica = executa(
                lambda x: lambda y: x*y,
                19
            )

        print(duplica(3))

    No caso, como a função criar_multiplicador ela serve para retornar alguma uma outra função, então na variável duplica precisamos criar uma função lambda e dentro dessa função lambda retornar outra função lambda onde essa função lambda de dentro ela retorna a multiplicação dos parâmetros da primeira função lambda e da segunda, que está definida dentro da primeira. E o duplica, finalmente, executa a segunda função lambda, visto que colocamos o segundo parâmetro para conseguirmos realizar a multplicação.

    Entretanto, notamos que a função lambda acima ficou muito complexo. No caso, a dica é não usar dessa forma. Claro, não significa que seria tranquilo, mas não é recomendável à esse nível que tornaria o código difícil para realizar a leitura.

Obs: É considerado como uma má prática a seguinte forma de função lambda

    funcao = lambda parametro: parametro