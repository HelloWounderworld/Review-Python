# Aula 32 - Empacotamento e desempacotamento de dicionários + *args e **kwargs:
Nessa aula, vamos aprender sobre empacotamento e desempacotamento de dicionários.

- args- *args permite passar um número variável de argumentos posicionais para uma função. - Dentro da função, args é acessado como uma tupla.

- kwargs- **kwargs permite passar um número variável de argumentos de palavra-chave (nomeados) para uma função.- Dentro da função, kwargs é acessado como um dicionário.

Combinando args e kwargsVocê pode usar ambos em uma função para aceitar qualquer combinação de argumentos posicionais e nomeados.

No caso, o que é empacotamento e desempacotamento de dicionários? Seria o seguinte

    a, b = 1, 2
    a, b = b, a
    print(a, b)

Note que, no caso, acima realizamos esse processo em valores imutáveis. Mas a mesma analogia é aplicado para dicionários como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa
    print(a, b)

No caso, na forma acima, o print retornará as chaves do dicionário pessoa.

Mas, podemos definir de uma forma que retorne os valores definidos nas chaves como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa.values()
    print(a, b)

Ou, podemos desempacotar na forma de itens tbm como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    a, b = pessoa.items()
    print(a, b)

Podemos, tbm, realizar um desempacotamento interno como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    (a1, a2), b = pessoa.items()
    print(a1, a2)
    print(b)

Podemos usar essa mesma lógica e aplicar na iteração

    for chave, valor in pessoa.items():
        print(chave, valor)

Agora, se quisermos unir dois dicionários como seguinte

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    dados_pessoa = {
        'idade': 26,
        'altura': 1.84
    }

    print(pessoa, dados_pessoa)

Bom, uma alternativa que temos para realizar a união dos dois dicionários, seria criando um terceiro dicionários e dentro dela extrair os dois dicionários

    pessoa = {
        'nome': 'Leonardo',
        'sobrenome': 'Hayashi'
    }

    dados_pessoa = {
        'idade': 26,
        'altura': 1.84
    }

    pessoa_completa = {**pessoa, **dados_pessoa}

    print(pessoa, dados_pessoa)
    print(pessoa_completa)

Uma outra alternativa seria usando o kwargs, que é conhecido como "keyword arguments". Daí, podemos utilizar dessa funcionalidade da seguinte forma

    def mostro_argumentos_nomeados(*args, **kwargs):
        print(kwargs)

    mostro_argumentos_nomeados(nome='Leonardo', qlq=1236)

Note que, no print dentro dessa função, ao passarmos os parâmetros da forma costumeira de definir os elementos dentro do dicionario, devolverá um dicionário.

A parte legal disso, seria que isso nos permitirá iterar num for da seguinte forma

    def mostro_argumentos_nomeados(*args, **kwargs):
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(nome='Leonardo', qlq=1236)

No caso, a função acima reconhece os argumentos não nomeados tbm. No caso, podemos passar os parâmetros como seguinte tbm

    def mostro_argumentos_nomeados(*args, **kwargs):
        print('Não nomeados: ', args)
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(1, 2, 3, nome='Leonardo', qlq=1236)

No caso, podemos, também, passar como argumento dentro dessa função um dicionário desempacotado como seguinte

    def mostro_argumentos_nomeados(*args, **kwargs):
        for chave, valor in kwargs.items():
            print(chave, valor)

    mostro_argumentos_nomeados(**pessoa_completa)

Bom, por vias didáticos, a função mostro_argumentos_nomeados, definido acima, ela serve tanto para valores não nomeados quanto para nomeados, respectivamente, *args e **kwargs.
