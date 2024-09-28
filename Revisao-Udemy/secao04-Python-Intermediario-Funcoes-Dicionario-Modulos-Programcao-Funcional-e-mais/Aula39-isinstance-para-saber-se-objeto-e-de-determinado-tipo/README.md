# Aula 39 - isinstace() - para saber se objeto é de determinado tipo:
Bom, como usamos na última aula, o isinstance() ela serve para checar se um valor é de um determinado tipo.

Considere a seguinte lista

    lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Leonardo'}]

Claro, em programação não é uma boa prática vc receber esse tipo de lista que tem muita coisa misturada. Porém, nos problemas do dia a dia em uma empresa isso é muito comum de acontecer e acaba sendo necessário desenvolver um código que trate tais valores.

Agora, vamos usar o isinstance iterando esse for

    for item in lista:
        print(item, isinstance(item, set))

Bom, podemos, claro, combinar com as condicionais if usando o isinstance

    for item in lista:
        if isinstance(item, set):
            item.add(5)
            print(item, isinstance(item, set))

No caso, esse uso nos permite realizar diferentes tipos de tratativas conforme o tipo que o elemento dentro da lista está sendo representado.

O legal do VSCode, agora é algo típico desse IDE, podemos ver que dentro da condicional do if acima, realizamos o item.add(5). A parte curiosa disso é que quando realizamos o "item." ele exibe todos os métodos que lhe é possível utilizar para o set. Ou seja, o VSCode foi inteligente o suficiente para reconhecer que dentro daquela condicional, o item que estou tratando é um conjunto. Da mesma forma que podemos realizar isso para outros tipos de dados. Algo que nas outras IDE's não é possível realizar.

Bom, isso é um indício que hoje em dia a programação está mais fácil graças aos editores de textos. (Só espero que um dia ainda criem uma linguagem de programação única que serve para tudo, em vez de existir tantas linguagens de programação... Assim, o programador se preocuparia em focar somente nos conceitos matemáticos para conseguir criar algum código robusto. Da mesma forma que facilita para um matemático que queria trabalhar com a computação tbm...)

    for item in lista:
        if isinstance(item, set):
            item.add(5)
            print(item, isinstance(item, set))

        elif isinstance(item, str):
            item = item.upper()
            print(item, isinstance(item, str))

        elif isinstance(item, (int, float)):
            item+=1
            print(item, isinstance(item, (int, float)))

        else:
            print('OUTRO')
