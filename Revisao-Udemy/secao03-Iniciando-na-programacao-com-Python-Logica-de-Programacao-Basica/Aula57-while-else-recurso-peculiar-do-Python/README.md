# Aula 57 - while / else (recurso peculiar do Python):
Bom, vamos entender sobre um recurso bem específico do python, que é o while else.

A priori, não será nenhum problema da pessoa não fazer muito uso desse recurso, pois é um tipo bem pouco utilizado mesmo. Mas, como estamos em uma revisão e aprofundamento dessa linguagem, vale passarmos o conceito por desencargo de consciência

    """ while/else """
    string = 'Valor qualquer'

    i = 0
    while i < len(string):
        letra = string[i]

        if letra == ' ':
            break

        print(letra)
        i += 1
    else:
        print('Não encontrei um espaço na string.')
    print('Fora do while.')

Ela funciona da seguinte forma. Assim, como tem else para if, em várias outras funções em python ela tem o else junto, como while/else e for/else. Daí, ela funcoina quando o laço termina e vc quer devolver algum valor e o else, assim como foi visto nos estudos das condicionais, é o oposto da condição considerada no if, e o mesmo serve para o while.

No caso, um ponto importante que precisamos deixar claro aqui, é que o else, combinado com o while, ela não é executado visto que dentro do laço foi passado em algum break.
