# Aula 16 - Introdução ao tipo de dados dict - Dicionários em Python:
Vamos introduzir ao conceito de o dicionários.

Dicionários são estruturas de dados do tipo par de "chave" e "valor".

Chaves podem ser consideradas como o "indice" que vimos na lista e podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc...

No caso, os dicionários, assim como as listas, são mutáveis.

Vamos pegar o seguinte exemplo de dicionário

    pessoa = {
        'nome': 'Leonardo Takashi',
        'sobrenome': 'Teramatsu',
        'idade': 26,
        'altura': 1.8,
        'endereços': [
            {'rua': 'tal tal', 'número': 123},
            {'rua': 'outra rua', 'número': 321},
        ]
    }
    print(pessoa, type(pessoa))

Existe, sim, uma outra forma de escrever um dicionário como acima, usando a sintaxe "dict()" da seguinte forma

    dict(nome='Leonardo Takashi', sobrenome='Teramatsu')

Entretanto, a forma mais usada é na forma de chave acima "{}".

Para acessar os elementos que foram definidas dentro de uma chave, bastaria realizar o seguinte.

    pessoa['nome de algum elemento que foi definido']
    print(pessoa['nome'])
    print(pessoa['sobrenome'])
    print(pessoa['idade'])
    print(pessoa['altura'])

Podemos, também, iterar um dicionário como se fosse lista. No caso, a diferença é que nessa itearação será pego as chaves e não o valores de cada chave

    for chave in pessoa:
        print(chave)