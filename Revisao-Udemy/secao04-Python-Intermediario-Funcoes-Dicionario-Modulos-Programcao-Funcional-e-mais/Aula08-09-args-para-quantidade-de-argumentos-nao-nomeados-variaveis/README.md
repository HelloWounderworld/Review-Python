# Aula 08 - (Parte 1) e (Parte 2) *args para quantidade de argumentos não nomeados variáveis:
- args- *args permite passar um número variável de argumentos posicionais para uma função. - Dentro da função, args é acessado como uma tupla

Agora, uma pergunta. Note que, a função print() podemos colocar quantos argumentos finitos que quisermos que ela é exibida no console ao ser executada

    print(1)
    print(1,2,3)
    print(1,2,3,4,5,6,7)

Entretanto, em uma função personalizada, como soma(x,y), temos um limite de quantidade de argumentos que podemos colocar, donde, excedido isso, não será possível compilar a função

    def soma(x,y):
        return x + y

Mas aí, vem a pergunta, existe alguma forma de conseguirmos dinamizar isso para as funções personalizadas como no print()?

A resposta é sim. Vamos usar a sintaxe "*args", como podemos ver no exemplo abaixo

    x, y, *resto = 1, 2, 3, 4, 5, 6, 7
    print(x,y,resto)

Podemos realizar isso em funções personalizada tbm, como segue

    def soma(*args):
        print(args, type(args))

    soma(1,2,3,4,5,6,7)

Vamos ver que o "print(args)" devolve os argumentos que passamos em soma(1,2,3,4,5,6,7) na forma de tupla. Claro que podemos alterar essa tupla para uma lista como segue

    def soma(*args):
        args = list(args)
        print(args, type(args))

    soma(1,2,3,4,5,6,7)

Mas, a finalidade nossa aqui dessa função é realizarmos a soma dos valores que foram passados no argumento

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    print(soma(1,2,3,4,5,6,7))

Além disso, em vez de passarmos os argumentos uma por uma, poderíamos criar uma variável que carrega todos os argumentos queremos passar em uma função

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    random = 1,2,3,4,5,6,7
    print(soma(random))

Ops... Creio que não funcinou, pois foi mostrado a seguinte msg, que vc está mandando uma tupla e o "*args" ela forma uma tupla no conjunto de argumentos. Mas, então, qual a forma correta de guardarmos um conjunto de argumentos em uma variável e passar isso em uma função? Bom, bastaríamos colocar um asterisco na variável que carrega o argumento

    def soma(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum

    random = 1,2,3,4,5,6,7
    print(soma(*random))

No caso, o que foi feito acima, é um ato de desempacotamento, como foi feito no exemplo do "x, y, *resto".