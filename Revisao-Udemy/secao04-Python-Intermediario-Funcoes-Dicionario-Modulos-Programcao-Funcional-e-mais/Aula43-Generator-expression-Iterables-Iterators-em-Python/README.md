# Aula 43 - Generator expression, Iterables e Iterators em Python:
Vamos aprender sobre generator. No caso, esse generator é algo antigo que já existia no JavaScript, porém no Python foi implementado de forma recente.

Basicamente, o generator são funções que sabem pausar em determinada ocasião.

Todo generator é um iterator, mas não vale a recíproca.

Vamos mostrar um exemplo básico para melhorar a sua compreensão

    generator = [n for n in range(10)]

    print(generator)

Bom, pegamos um iterável simples acima só para exibição. Mas, agora, imagina se a variável "generator" acima tiver 10000 range e tiver que exibir isso tudo de uma vez. Isso, com certeza, tornaria a exibição caótica. No caso, o generator ele serve para vc conseguir determinar o momento para pausar.

Qual é a vantagem disso?

Bom, suponhamos que vc tenha que lidar com uma quantidade de dados exuberante e dela vc precisa tirar somente alguns dados. No caso, seria muito ineficiente se vc tiver que tratar toda hora todos os dados para conseguirmos filtrar somente aqueles dados que precisamos. No caso, o generator, ele facilita isso de forma a otimizar o processo sem a necessidade de ter que passar para todos os dados, mas, sim, selecionando somente aquelas que precisamos.

Para isso, do exemplo acima, bastaria mudar a lista para "()" como segue

    generator = (n for n in range(10000))

    print(generator)

Daí, no print será exibido um generator expression, do tipo

    <generator object <genexpr> at 0x7fac0339ec80>

Diferentemente de darmos o print sobre a forma

    generator = [n for n in range(10000)]
    
    print(generator)

Que será exibido uma quantidade exuberante de dados.

Vamos importar o módulo "sys" para mostrarmos o tamanho dos dados de cada tipo

    import sys

    lista = [n for n in range(10000)]
    generator = (n for n in range(10000))

    print(sys.getsizeof(lista))
    print(sys.getsizeof(generator))

Ao rodarmos o código acima, conseguimos ver que o tamanho da lista e do generator há uma deferença bem evidente.

Ou seja, o que isso singifica?

Significa que, enquanto na variável "lista" que, de fato, é uma lista quando criado uma lista via list comprehension, isso já estaria sendo guardado na memória da máquina, com o generator não será guardado. Podemos mudar o tamanho do range para lista e generator e isso ficará evidente, pois enquanto a lista irá aumentar de memória, o generator continuará na mesma quantidade.

Qual a vontagem disso?

Basicamente, otimiza o consumo da memória de modo que o generator, pelo fato dele não guardar nada na memória, ele fica no estado de espera para que vc solicite algum dado que esteja guardado sobre ele.

Assim, podemos realizar a busca de forma otimizada como segue

    import sys

    generator = (n for n in range(10000))

    print(sys.getsizeof(generator))
    print(generator)

    print(next(generator))
    print(next(generator))
    print(next(generator))

Note que, acima, no print que usa o método next, está sendo feito direitinho a busca necessária dos valores que foram iterados.

Agora, podemos usar o for para conseguirmos realizar a devida busca necessária de forma otimizada, entendido a natureza do generator

    import sys

    generator = (n for n in range(10000))

    print(sys.getsizeof(generator))
    print(generator)

    for n in generator:
        print(n)

Vimos que foi feito uma iteração em escala enorme que foi exibido pelo terminal correto? Bom, isso está preenchendo a memória conforme a quantidade de iterações que ocorreu, o que é diferente da situação que temos um iterável [n for n in range(10000)] pronto, pois isso indica que esses 10mil valores já estará guardado na memória, o que não é otimista do ponto de vista de uso de espaço da memória.

Ok, falei das vantagens de se usar um generator. Mas e as desvantagens?

Bom, o generator ele é um iterável, mas nela não se aplica os métodos e técnicas que temos de uma lista. Ou seja, não podemos saber o tamanho dela, no caso não dá para usar o len, muito menos não podemos consultar o valor pelo índice, etc... Tudo isso, só pelo fato dele não estar na memória, como uma lista estaria. Portanto, só é possível consultar os valores próximos uma por uma e iterar ela com o for de modo que vc consiga realizar uma busca mais eficiente

    print(len(generator))
    print(generator[50])

Os dois prints acima dará um erro. Assim, como outros métodos que se aplica para uma lista dará o mesmo erro, pois não está na memória.

Fonte para leitura

    https://www.geeksforgeeks.org/difference-between-iterator-vs-generator/
    https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
