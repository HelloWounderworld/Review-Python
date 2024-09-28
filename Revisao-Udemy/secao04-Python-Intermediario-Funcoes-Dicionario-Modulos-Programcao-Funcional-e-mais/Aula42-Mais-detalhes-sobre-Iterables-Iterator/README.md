# Aula 42 - Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores):
Bom, nas seções anteiores já tínhamos abordado sobre coisas iteráveis e o que seria os iteradores.

No caso, a diferença gritante entre iterável e iteradores, seria que o iterável tem a responsabilidade de deter os valores sequencialmente e a única responsabilidade o iteradores seria te entregar um valor por vez.

    iterable = ['Eu', 'Tenho', '__iter__']
    iterator = iterable.__iter__() # tem __iter__ e __next__

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

No caso, o iterator ele te devolve os valores sucessores. Sem se importar em qual posição o valor atual se encontra.

Podemos ver acima, nos três prints, conforme chamamos o "next(iterator)" ele devolve o próximo da lista iterable.

Lembrando, iterator só se usa sobre objetos iteráveis!

O livro em que o professor Luiz Otávio viu sobre esse conceito pela primeira vez foi no

- Padrões de Projetos, Soluções reutilizáveis de software orientado a objetos

Não se preocupe que teremos uma seção inteirinha somente desse livro nessa revisão.

Link para leitura

    https://www.geeksforgeeks.org/python-difference-iterable-iterator/
    https://byjus.com/gate/difference-between-iterable-and-iterator-in-python/
    https://stackoverflow.com/questions/9884132/what-are-iterator-iterable-and-iteration
