# Aula 18 à 20 - (Parte 1 e 2) Métodos úteis nos dicionários Python (dict):
Vamos explorar os métodos usuais na linguagem Python.

Logo, são elas

- len: Conta a quantidade de chaves ou elementos existentes dentro de um dicionário e lista, respectivamente.
    
    Mais pela frente, vamos aprender a montar uma classe usando o Python que é o momento em que entramos no conceito da programação orientada à objetos. No caso, por curiosidade, iremos mostrar as duas formas de usarmos tais métodos que é uma classe

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.__len__())
        print(len(pessoa))

    Lembramos, um detalhe importante de um dicionário, é que ele, mesmo não sendo definitivamente, ele é como um conjunto, ou seja, vc poderia definir várias chaves iguais

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu1',
            'sobrenome': 'Teramatsu2',
            'sobrenome': 'Teramatsu3'
        }

        print(pessoa['sobrenome'])

    No caso, acima, no print, será exibido o último valor que foi definido para a chave "sobrenome".

    Além disso, ao analisarmos o comprimento desse dicionário, usando o "len", será exibido um valor "2". Como havíamos dito que esse dicionário, mesmo não sendo definitivamente um conjunto, mas ele se comporta como uma, em um conjunto vc poderia colocar infinitos elementos repetidos dentro dela que, ainda sim, será assimilado que existe um elemento desse dentro dela, o que difere, por exemplo, com a lista.

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu1',
            'sobrenome': 'Teramatsu2',
            'sobrenome': 'Teramatsu3'
        }

        print(pessoa['sobrenome'])
        print(pessoa.__len__())
        print(len(pessoa))

- keys: Permite que iteremos um dicionário via chave e não pelos valores definidos em cada chave.

    O método "keys" ele retorna as chaves que são definidos dentro de um dicionários. No caso, o seu uso se dá como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.keys())

    No caso, ele retorna um dict_keys com uma lista dentro dela. No caso, claro, podemos sim acessar os valores das chaves dentro dela, mas não diretamente. Precisamos converter-las como seguinte

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.keys())
        print(tuple(pessoa.keys()))
        print(list(pessoa.keys()))

    Que é o famoso processo de coersão.

- values: Permite que iteremos um dicionário via os valores que são definidos para cada chave.

    Agora, para entender o uso desse método vamos primeiro iterar o dicionário

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        for chave in pessoa:
            print(chave)
        
        for chave in pessoa.keys():
            print(chave)

    Em ambos os for's, será retornado as chaves que foram definidos dentro do dicionário "pessoa".

    Agora, o values, entra dentro desse cenário, para mostrarmos que erla irá retornar os valores do que as chaves como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        for chave in pessoa:
            print(chave)
        
        for chave in pessoa.keys():
            print(chave)

        print(pessoa.values())
        print(tuple(pessoa.values()))
        print(list(pessoa.values()))

        for chave in pessoa.values():
            print(chave)

    No caso, podemos se utilizar do método values como o keys, donde a única diferença é que, em vez de chaves, ele retornará os valores.

- items: Permite que iteremos via chave e o valor correspondente.

    O uso do método "items", também, é similar ao uso dos outros dois métodos acima, "keys" e "values". No caso, ela irá nos retornar tanto a chave quanto o valor na forma de tuplas em pares

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(pessoa.items())
        print(tuple(pessoa.items()))
        print(list(pessoa.items()))

        for item in pessoa.items():
            print(item)

        for chave, valor in pessoa.items():
            print(chave, valor)

- setdefault: adiciona o valor caso não exista a chave.

    Esse método, basicamente, ele serve para conseguir definir a chave, caso no momento da consulta, a tal chave não estiver definida. Como segue

        pessoa = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        pessoa.setdefault('idade', 26)
        print(pessoa['idade'])

        pessoa.setdefault('nome', 'Alan')
        print(pessoa['nome'])

    Esse método "setdefault", por padrão, caso vc não coloque nenhum valor na suposta chave que será atribuído, ela irá atribuir o None. E a tal chave que vc está tentando atribuir já existir, não irá realizar nada.

- copy: retorna uma cópia rasa (shallow copy).

    Bom, o método "copy" do Python, ele realiza uma cópia raza de um dicionário/lista. O que quer dizer isso?

    Antes de responder essa pergunta, vamos lembrar o seguinte

        dic1 = {
            'd1': 1,
            'd2': 2
        }

        dic2 = dic1

        dic2['d1'] = 1000
        print(dic1)

    A forma como realizamos a atribuição acima, quem lembra do conceito, ela estará definindo duas variáveis que está apontando para um mesmo objeto. Logo, ao realizar alguma alteração em uma chave do dic2, essa alteração irá surtir para o dic1 também.

    Agora, ao usarmos o método "copy", como segue

        dic1 = {
            'd1': 1,
            'd2': 2
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        print(dic1)
        print(dic2)
        print(dic3)

    Vamos ver que a tal alteração que realizamos na chave "d1" no "dic3" não surtiu ao "dic1", como ocorre no caso do "dic2". Bom, nesse caso, podemos dizer que realizamos uma cópia do dicionário "dic1". Porém, essa cópia é rasa. Em que sentido? Para valores imutáveis, ocorrerá uma cópia, de modo independente. Porém, para valores mutáveis como lista, dicionário, etc... Essa cópia não ocorre. Ou seja, como podemos ver no exemplo abaixo

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic3['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)

    Conseguimos ver que, para a lista definido dentro do dic1, a alteração que realizamos no dic3, do primeiro índice da lista da chave "d3", essa mudança surtiu para o "dic1" também, o mesmo para "dic2".

    Bom, o que eu suspeito desse método "copy" ser razo, seria por conta do processamento que demoraria muito ao realizar alguma cópia de algum valor mutável, então, para que ela seja rápido, que seja feito um apontamento para dois objetos iguais, usando do conceito de categoria.

    Agora, para que seja possível realizar uma cópia total (Deep Copy), o Python ele tem um módulo para isso. No caso, bastaria importar tal módulo

        import copy

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = dic1.copy()

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic3['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)

    Agora, mesmo importanto o módulo "copy", haverá momentos em que queremos usar ainda a cópia raza, para isso bastaria usar "copy.copy('dicionário/lista')".

        import copy

        dic1 = {
            'd1': 1,
            'd2': 2,
            'd3': [
                'Leo', 'Louco', 'Medo'
            ]
        }

        dic2 = dic1
        dic3 = copy.copy(dic1)
        dic4 = copy.deepcopy(dic1)

        dic2['d1'] = 1000
        dic3['d1'] = 2000
        dic4['d3'][0] = 'Turing'
        print(dic1)
        print(dic2)
        print(dic3)
        print(dic4)

- get: obtém uma chave.

    Bom, já usamos o "get" aqui, no caso, ela tem como finalidade em conseguir verificar se alguma chave existe ou não e retornar um None, por padrão, caso a tal chave não exista ou o valor atribuído à chave, caso ela exista.

        p1 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p1.get('nome'))
        print(p1.get('idade'))
        print(p1.get('idade', 'Não tem a chave idade'))

- pop: Apaga um item com a chave especificada (del).

    Já o "pop" ele funciona como o "del" e temos mais uma funcionalidade, como complemento, que é exibir o valor da chave que está sendo excluído

        p2 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        name = p2.pop('nome')
        print(name)
        print(p2)

    Além de pop, temos, também, o método "popitem()", donde ela remove a última chave e exibe, na forma de tupla, a chave e o seu valor que está sendo eliminado

        p3 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        ultima_chave = p3.popitem()
        print(ultima_chave)
        print(p3)

- update: Atualiza um dicionário com o outro.

    Já o update, seria quando quisermos passar um conjunto de chaves de forma mais prática

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

    No caso, a forma acima, depois que passarmos as chaves que queremos que vá dentro do p4, o update ela inclui.

    Como não obstante, podemos, também, atualizar, no sentido de modificar, os valores das chaves já existentes como segue

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

        p4.update({
            'nome': 'Alan'
        })

        print(p4)

        p4.update({
            'sobrenome': 'Turing',
            'cidade': 'London'
        })

        print(p4)

    Uma outra maneira mais prática de utilizar o método update, seria, em vez de usar "{}", é atribuindo diretamente a chave e o valor

        p4 = {
            'nome': 'Leonardo Takashi',
            'sobrenome': 'Teramatsu'
        }

        print(p4)

        p4.update({
            'idade': 26,
            'altura': 1.8
        })
        print(p4)

        p4.update({
            'nome': 'Alan'
        })

        print(p4)

        p4.update({
            'sobrenome': 'Turing',
            'cidade': 'London'
        })

        print(p4)

        p4.update(job='Mathematician', college='Cambridge')

        print(p4)

    Podemos realizar a tal atribuição usando tuplas tbm

        tupla = ('invention', 'Turing Machine')
        p4.update(tupla)
        print(p4)

    Claro, se quisermos passar várias tuplas, precisamos colocar pares de tupla (chave, valor) dentro de uma tupla

        ((chave1, valor1), (chave2, valor2), ...)

    Da mesma maneira serve para lista tbm.