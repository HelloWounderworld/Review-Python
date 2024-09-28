# Aula 84 - Desempacotamento em chamadas de funções:
Vamos abordar sobre o assunto de desempacotamento em Python e de suas funções tbm.

Vimos que a termos a seguinte situação

    lista1 = ['Maria', 'Helena', 'Eduarda']
    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
    
    a1, b1, c1 = lista1
    a2, b2, c2 = lista2
    print(a1, c1)
    print(a2, c2)

Ao rodarmos o código acima, será retornado um erro para o print(a2, c2), visto que a lista2, ela está com mais elementos do que computado por a2, b2 e c2.

    Traceback (most recent call last):
    File "/home/leonardo/Documentos/estudos-programacao/Review-Python/Revisao-Udemy/secao03-Iniciando-na-programacao-com-Python-Logica-de-Programacao-Basica/Aula84-Desempacotamento-em-chamadas-de-funcoes/aula84.py", line 9, in <module>
        a2, b2, c2 = lista2
    ValueError: too many values to unpack (expected 3)

O erro que será exibido está acima.

Para corrigirmos esse erro, teremos que usar um asterisco com undeerline, que indica o resto, caso não usado

    lista1 = ['Maria', 'Helena', 'Eduarda']
    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
    
    a1, b1, c1 = lista1
    a2, b2, c2, *_ = lista2
    print(a1, c1)
    print(a2, c2)

Porém, assim, não ficaria o mesmo que o print(a1, c1), ou seja, que printa a Maria e a Eduarda. No caso, o que seria necessário para conseguirmos realizar isso para o print(a2, c2)? Bastaríamos usar o resto, *_, no meio deles

    lista1 = ['Maria', 'Helena', 'Eduarda']
    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
    
    a1, b1, c1 = lista1
    a2, b2, *_, c2 = lista2
    print(a1, c1)
    print(a2, c2)

Isso irá nos retornar o mesmo que está no print(a1, c1).

Com a mesma analogia, podemos pegar o penúltimo elemento tbm, como seguinte

    lista1 = ['Maria', 'Helena', 'Eduarda']
    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

    a1, b1, c1 = lista1
    a2, b2, *_, c2 = lista2
    a3, b3, *_, c3, d3 = lista2
    print(a1, c1)
    print(a2, c2)
    print(a3, c3, d3)

Bom, não era isso o que iríamos abordar no assunto dessa aula. Porém, fica como um reforço sobre tuplas para vcs.

O assunto em questão é sobre desempacotamento em chamadas de funções.

Agora, suponhamos que queremos iterar uma lista. A forma comum de realizarmos isso é usando o for

    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

    for nome in lista2:
        print(nome)

    for nome in lista2:
        print(nome, end=' ') # Caso vc quer que ele exiba em uma linha, ele tira o \n, quebra de linha

    for nome in lista2:
        print(nome, sep=' ') # Caso vc quiser que seja exibido sem o separador

    for nome in lista2:
        print(nome, end=' ', sep=' ') # Caso vc quiser que seja exibido em uma lista e sem o separador

Caso eu queira realizar o mesmo que no for que usamos o print(nome, end=' ', sep=' ') de maneira bem mais resumida, bastaria realizar o seguinte

    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']

    for nome in lista2:
        print(nome)

    for nome in lista2:
        print(nome, end=' ') # Caso vc quer que ele exiba em uma linha, ele tira o \n, quebra de linha

    for nome in lista2:
        print(nome, sep=' ') # Caso vc quiser que seja exibido sem o separador

    for nome in lista2:
        print(nome, end=' ', sep=' ') # Caso vc quiser que seja exibido em uma lista e sem o separador

    print(*lista2)

O mesmo é possível realizar para outros tipos de valores

    string = 'ABCD'
    lista2 = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
    tupla = 'Python', 'é', 'legal'

    print(*lista2)
    print(*string)
    print(*tupla)

Mas qual a parte legal disso? Seria que para lista mais complexas, podemos, usando isso, melhorar a sua visualização pelo terminal ou console.

    salas = [
        # 0        1
        ['Maria', 'Helena', ],  # 0
        # 0
        ['Elaine', ],  # 1
        # 0       1       2
        ['Luiz', 'João', 'Eduarda', ],  # 2
    ]

    print(salas)
    print(*salas)
    print(*salas, end='\n')
    print(*salas, sep='\n')

No caso, isso que vimos, usando o print, é o desempacotamento em funções.

Claro, podemos realizar a mesma coisa sem o uso de print, no caso, com a chamada de outras funções e isso será abordado ao longo das aulas.
