# Aula 63 - Decoradores em Python (@syntax_sugar):
Bom, visto que aprendemos funções decoradoras, vamos precisar aprender sobre decoradores.

Bom, vamos continuar com o mesmo código da última aula

    # Funções decoradoras e decoradores
    # Decorar = Adicionar / Remover/ Restringir / Alterar
    # Funções decoradoras são funções que decoram outras funções
    # Decoradores são usados para fazer o Python
    # usar as funções decoradoras em outras funções.

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro('123')
    print(invertida)

No caso, iremos aplicar os conceitos de decoradores em cima desse código. Mas, claro, antes de tudo, o que são decoradores?

Decoradores em Python são conhecidos como Syntax Sugar (Açúcar Sintático). Em outras palavras, os decoradores em Python são recursos que facilitam a utilização das funções decoradoras em python!

Como iremos usar esse Syntax Sugar? No caso, no código abaixo

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    inverte_string_checando_parametro = criar_funcao(inverte_string)
    invertida = inverte_string_checando_parametro('123')
    print(invertida)

vemos que estamos precisando definir uma variável "inverte_string_checando_parametro" para conseguirmos guardar a função decoradora "criar_funcao" para que, finalmente, ela seja usada pela função "inverte_string". No caso, o Syntax Sugar irá tirar esse trabalho. Ou seja, em vez de criar tais variáveis, vamos conseguir apontar para o "inverte_string" considerar o uso da função "criar_funcao", sem a necessidade de criarmos essa variável, da seguinte forma

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    @criar_funcao
    def inverte_string(string):
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    invertida = inverte_string('123')
    print(invertida)

Note que, não tivemos o trabalho de ter que criar uma variável "inverte_string_checando_parametro" e usarmos a função decoradora "criar_funcao" para, dentro dela, colocarmos como argumento a função "inverte_string" que é o momento que decora essa função, para, por fim, por via da outra variável, invertida, conseguirmos ver o que foi executado dentro dela, por via do print. No caso, o syntax sugar ajuda a tirar esse trabalho de forma a conseguirmos apontar simplesmente qual função vamos querer que a nossa função decoradora decore.

Ou seja, bastaria escolher qual função vc quer que ela seja decorado pela função decoradora e colocar a sintaxe "@nome_da_funcao_decoradora" em cima da função que vc queira decorar para que, no uso dela, vc precise chamar somente o nome da função que foi decorado.

Outra questão curiosa é o seguinte

    def criar_funcao(func):
        def interno(*args, **kwargs):
            print('Vou te decorar!')
            for arg in args:
                is_string(arg)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora você foi decorado!')
            return resultado
        return interno

    @criar_funcao
    def inverte_string(string):
        print(f'{inverte_string.__name__}')
        return string[::-1]

    def is_string(param):
        if not isinstance(param, str):
            raise TypeError('param deve ser uma string')

    invertida = inverte_string('123')
    print(invertida)

Ao colocarmos o print "print(f'{inverte_string.__name__}')" dentro da função "inverte_string", vamos ver que o que é retornado é o nome "interno", que é o nome da função que é definida dentro da função decoradora "criar_funcao". Ou seja, o nome não é da função que foi decorada, "inverte_string". Agora, se eu comento a sintaxe "@criar_funcao", o nome da função decorada, volta a ser "inverte_string".

Bom, essa parte é o básico de uma função decorador. Na próxima aula iremos um uso mais avançado sobre funções decoradores.

Links para leituras

    https://pythonacademy.com.br/blog/domine-decorators-em-python

    https://www.geeksforgeeks.org/decorators-in-python/

    https://pt.stackoverflow.com/questions/23628/como-funcionam-decoradores-em-python#:~:text=Uma%20fun%C3%A7%C3%A3o%20em%20Python%20%C3%A9,par%C3%A2metro%20e%20retorna%20uma%20fun%C3%A7%C3%A3o.

    https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
