# Aula 65 - Ordem de aplicação dos decoradores:
Falta comentarmos sobre a ordem de aplicação dos decoradores.

No caso, podemos utilizar mais de um decorador numa função. Disso, nos permite definir a ordem de execução de tais decoradores.

Vamos partir do seguinte código, que é da última aula

    # Decoradores com parametros
    def fabrica_de_decoradores(a=None, b=None, c=None):
        def fabrica_de_funcoes(func):
            print('Fabrica de funcoes 1')

            def aninhada(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                return res
            return aninhada
        return fabrica_de_funcoes

    @fabrica_de_decoradores(1, 2, 3)
    def soma(x ,y):
        return x + y

    multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)

    dez_mais_cinco = soma (10, 5)
    dez_vezes_cinco = multiplica(10, 5)
    print(dez_vezes_cinco)
    print(dez_mais_cinco)

No caso, vamos mudar os nomes primeiro

    # Decoradores com parametros
    def parametros_decorador(nome):
        def decorador(func):
            print('Decorador: ', nome)

            def sua_nova_funcao(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                final = f'{res} {nome}'
                return final
            return sua_nova_funcao
        return decorador

    @parametros_decorador(nome='Segundo')
    @parametros_decorador(nome='Primeiro')
    def soma(x ,y):
        return x + y

    dez_mais_cinco = soma (10, 5)
    print(dez_mais_cinco)

Ao executarmos o trecho acima, iremos conseguir ver que, no print, será exibido de forma crescente de primeiro para segundo, mesmo que a ordem esteja o inverso acima. Além disso, como prova de que podemos fabricar várias funções decoradoras, elas ficam guardadas dentro da fábrica, se não não seria possível realizar o processo de concatenação como é exibido "15 Primeiro Segundo".

    # Decoradores com parametros
    def parametros_decorador(nome):
        def decorador(func):
            print('Decorador: ', nome)

            def sua_nova_funcao(*args, **kwargs):
                print('Aninhado')
                res = func(*args, **kwargs)
                final = f'{res} {nome}'
                return final
            return sua_nova_funcao
        return decorador

    @parametros_decorador(nome='5')
    @parametros_decorador(nome='4')
    @parametros_decorador(nome='3')
    @parametros_decorador(nome='2')
    @parametros_decorador(nome='1')
    def soma(x ,y):
        return x + y

    dez_mais_cinco = soma (10, 5)
    print(dez_mais_cinco)

A ordem é inversa. Será exibido "15 1 2 3 4 5".
