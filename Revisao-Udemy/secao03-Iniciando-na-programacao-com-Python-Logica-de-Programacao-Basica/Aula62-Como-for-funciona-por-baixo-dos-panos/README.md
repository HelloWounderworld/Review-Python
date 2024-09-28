# Aula 62 - Como o for funciona por baixo dos panos? (next, iter, iterável e iterador):
Vamos entender o que acontece por baixo dos panos quando usamos o for.

Bom, foi feito, até agora, uma explicação bem breve sobre o que é iterável, que é algo que ele te entrega uma de cada vez. Claro, essa explicação é algo bem superficial para finalidades didáticas em pegar a noção de como ela funciona.

Agora, indo um pouco mais à fundo disso, o iterável, em Python, ele é advinda da chamada de um método com o nome '__iter__'. No caso, a definição de um método aqui é o mesmo que já foi visto em JavaScript, ou seja, é uma função que é definido dentro de um objeto. Bom, onde eu quero chegar com isso?

No caso, vamos ver o uso desse método

    texto = 'Leonardo'.__iter__()

Quando damos esse comando aqui executando o método, será chamado um iterador. No caso, ao printarmos essa variável, em vez de ser chamado o valor que foi definido dentro dela, será chamado o seguinte

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

O que será retornado

    <str_iterator object at 0x7ff397ef5c70>

No caso, ele está dizendo que foi chamado o iterador do str, 'str_iterador', que está dentro de um objeto e que ela está guardada na memória do seu computador com o endereço '0x7ff397ef5c70'.

Mas aí vem a pergunta. Toda vez que eu precisar chamar o método iterador, eu preciso fazer como foi feito na variável acima?

A resposta é não, pois existe um método pronto para isso chamado iter(), donde, dentro dela, reside esse método __iter__

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

    iteratador = iter(texto)  # iterator
    print(iteratador)

No caso, o que o print da variável iteratador irá nos retornar, será o mesmo do print para a variável texto.

Mas aí, qual é o motivo de estarmos discutindo isso? Seria pelo fato de que dentro dos métodos que existem para string, visto que string é um objeto, temos um método chamado next

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)

    iteratador = iter(texto)  # iterator
    print(iteratador)
    print(iteratador.__next__())
    print(iteratador.__next__())
    print(iteratador.__next__())
    print(iteratador.__next__())
    print('--------------')

No caso, esse método nos entrega o próximo valor como podemos ver no que é retornado pelo terminal

    <str_iterator object at 0x7f56840a9c70>
    <str_iterator object at 0x7f56840a9c70>
    L
    e
    o
    n
    --------------

Daí, se chamarmos o método __next__ várias vezes ao ponto de acabar a quantidade iterável de um objeto, será retornado o seguinte erro

    Traceback (most recent call last):
    File "/home/leonardo/Documentos/estudos/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula62-Como-for-funciona-por-baixo-dos-panos/aula62.py", line 21, in <module>
        print(iteratador.__next__())
    StopIteration

No caso, assim como temos o iter para o método __iter__, temos o next para o método __next__. E o quê isso significa? Podemos usar ela em while para vermos que ela tem a mesma funcionalidade

    texto = 'Leonardo'.__iter__()  # iterável
    print(texto)
    print('--------------')
    iteratador = iter(texto)  # iterator
    print(iteratador)
    print('--------------')
    while True:
        print(next(iteratador))

Vimos que, por se tratar de um loop inifinito em uma iteração finita, o next irá mostrar o mesmo erro na tela do bash.

Aí, uma forma de resolvermos isso seria usando o try e except dentro do while

    while True:
        try:
            letra = next(iteratador)
            print(letra)
        except StopIteration:
            break

Bom, o while acima, simula exatamente o que é feito pelo for por baixo dos panos e como ela funciona. No caso, temos o iterável, e nela aplicamos o iterador junto com o next e visto que não tem como mais iterar, StopIteration, então saímos do laço, como foi feito pelo except StopIteration acima. No caso, o for é um kit da funcionalidade acima, sem a necessidade de ter que criar cada passo na unha.
