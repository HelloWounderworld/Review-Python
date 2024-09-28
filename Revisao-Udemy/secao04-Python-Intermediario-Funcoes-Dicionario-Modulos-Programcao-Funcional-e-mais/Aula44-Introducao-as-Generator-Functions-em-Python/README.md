# Aula 44 - Introdução às Generator functions em Python:
Bom, agora, vamos explorar mais ainda dos recursos úteis que temos para o Generator.

Vamos começar por montar uma função

    def generator(n=0):
        return 1

    gen = generator(n=0)
    print(gen)

Esse aqui é só para começar para ver que a função retorna "1" mesmo. Até aqui, não estamos abordarndo de forma eficiente a natureza principal da função generator, que é a sua propriedade de conseguir pausar.

Agora, sim, vamos desenvolver um algoritmo que usar muito bem da natureza do generator. Segue o seguinte código

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen)

No caso, note que, acima mudamos o return para yield. O que essa sintaxe tem de funcionalidade?

Ela retorna o valor "1", só que na variável "gen" que executamos a função generator, esse valor "1" retornado não está guardado na memória. Como podemos ver no print, em vez dela devolver um valor "1", ela devolve generator expression, como do seguinte tipo

    <generator object generator at 0x7fcd9b45cc80>

Isso, novamente, evidencia que não está guardado na memória o valor retornado, mas, sim, ela está esperando ser chamado como podemos ver se fizermos o seguinte

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen)
    print(next(gen))

No print que usa o método "next" ela retorna o valor "1", como de se esperar, e é o momento em que irá consumir um espaço na memória tbm.

Como dizemos quando começamos a abordar sobre generator. Todo generator é um iterável tbm, então, obviamente, podemos usar o seguinte método iter tbm

    def generator(n=0):
        yield 1

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))

Acrescentamos tbm que depois do yield podemos usar o return tbm. Mas aí como esse return irá funcionar visto que já foi retornado algo, mesmo que não esteja na memória? Bom, o return ela servirá para mostrar que não há mais valor e ela será exibida em uma funcionalidade chamada raise

    def generator(n=0):
        yield 1
        return 'ACABAOU'

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))
    print(next(gen))

No caso, ao executarmos o código acima, vamos conseguir ver que na segunda vez que é chamado o next, como não tem mais nenhum valor depois do "1" que foi retornado, então no terminal será exibido uma mensagem "StopIteration" exibindo o valor do return, que neste caso é o "ACABOU".

Ou seja, o return, ela serve para defitivamente parar a função, pois, depois do yield, pode existir mais e mais yields que visto que, pelo next ou por alguma iteração for, foi batido um tal valor retornado pelo yield, a função generator, irá continuar com a leitura da linha sucessiva dentro dela

    def generator(n=0):
        yield 1
        print('Continuando......')
        yield 2

    gen = generator(n=0)
    print(gen.__iter__())
    print(next(gen))
    print(next(gen))

No caso, forma como está acima, no segundo next será exibido o valor "2", pois quando foi executado o primeiro next, foi pausado a função generator na linha onde está "yield 1", e quando usamos o next pela segunda vez, dentro da função "generator", ela dará a continuidade a partir do ponto em que foi pausado, "yiel 1", adiante, então virá o print('Continuando.....') e em seguida o segundo yield, "yield 2".

Isso irá continuar até que o próximo next não retorne nada, caso vc não use o return, pois aí, por padrão, as funções def elas retornam um None.

Bom, entendido o conceito e visto a sua funcionalidade do ponto de vista manual, usando o next, vamos agora dinamizar isso usando o for. Assim, conseguimos montar o seguinte código para função generator para considerar escalas de valores maiores

    def generator(n=0):
        yield 1
        print('Continuando......')
        yield 2

    gen = generator(n=0)
    for n in gen:
        print(n)

Note que, na forma dinâmica acima, usando o for, quando o for exibiu tudo o que pode ser exibido pelo generator, não foi exibido a mensagem "StopIteration". Ela simplesmente parou a exibição no "2" ou se tiver algum print ou qualquer outra coisa em seguida, menos o return, irá parar nela.

Agora, vamos melhorar a qualidade do código generator, como prometido, para escala maior

    def generator(n=0, maximum=100000):
        while True:
            yield n

            n += 1

            if n > maximum:
                return

    gen = generator()
    gen1 = generator(n=5, maximum=200)
    for n in gen:
        print(n)

Bom, note que, agora, a função generator, por padrão temos duas variáveis padrões definidas nela, e que o yield está dentor de um laço infinito while, cujo o laço irá parar somente quando ocorrer o return, ou seja, entendo dentro da condicional.
