# Aula 88 - Problema dos parâmetros mutáveis em funções Python:
Vamos falar sobre os problemas de parâmetros mutáveis em Python.

Vimos nas aulas anteriores sobre os problema de cópia raza e cópia profunda de dados mutáveis em Python. Bom, recomendamos, caso vc não lembre direito do assunto, em fazer uma revisão leve, pois para vc entender o conceito desse assunto em questão será necessário esse conhecimento.

Por começo, vamos nos basear com funções para vc conseguir entender o que irá acontecer. Vamos definir o seguinte

    def adiciona_clientes(nome, lista=[]):
        lista.append(nome)
        return lista

    cliente1 = adiciona_clientes('Leonardo')
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

Bom, até agora, não vemos nenhum problema. Pois, na primeira chamada da função, foi adicionado o nome "Leonardo", sem passar nenhuma lista e, na segunda chamada da função, foi adicionado o nome "Joana" para ser incluída dentro da lista "cliente1" que foi criado na primeira vez que a função "adiciona_clientes" foi chamado. Pelo menos, é o que dá a entender, mas a resposta é não!

No caso, na primeira vez que chamamos a função "adiciona_clientes" e colocamos apenas o nome "Leonardo" sem colocar nenhuma lista, a lista que foi definida por padrão pela função "adiciona_clientes" foi usado. E na segunda vez que chamamos a função, mas, desta vez, colocando o nome "Joana" como primeiro parâmetro e a lista, que foi criada na primeira chamada, como segundo parâmetro, o que aconteceu foi que a lista que foi definida dentro da função, continua sendo usada. O que isso significa? Significa que o "cliente1" e a segunda vez que chamamos a função, ambas estão apontando ainda pela mesma lista, que é a lista que foi criado pela própria função.

Como prova disso, se tentarmos criar uma segunda lista

    def adiciona_clientes(nome, lista=[]):
        lista.append(nome)
        return lista

    cliente1 = adiciona_clientes('Leonardo')
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)

Ao executarmos o código acima, o nome "Helena", está sendo colocado dentro da lista, onde já estava incluso os dois nomes "Leonardo" e "Joana".

E não adianta jogar, novamente, passar como o segundo parâmetro o "cliente2" que só será acrescentado de novo mais um nome sobre os três nomes existentes, pois estão, ainda, apontando para o mesmo objeto

    def adiciona_clientes(nome, lista=[]):
        lista.append(nome)
        return lista

    cliente1 = adiciona_clientes('Leonardo')
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

Bom, estou falando sobre lista aqui, mas entenda que qualquer parâmetro multável irá acontecer a mesma coisa aqui.

Uma das formas de resolvermos esse problema seria em, simplesmente, colocar como parâmetro uma lista vazia

    def adiciona_clientes(nome, lista=[]):
        lista.append(nome)
        return lista

    lista1 = []
    cliente1 = adiciona_clientes('Leonardo', lista1)
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

Mas, claro, a boa prática, seria em não definir uma parâmetro mutável como padrão dentro de uma função e, no lugar dela, passar alguma valo imutável

    def adiciona_clientes(nome, lista=None):
        lista.append(nome)
        return lista

    lista1 = []
    cliente1 = adiciona_clientes('Leonardo', lista1)
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

Mas, claro, se, simplesmente, definirmos como "lista=None" como está na função acima, isso irá quebrar o nosso código quando tentarmos rodar o "cliente2". Nesse caso, podemos realizar o seguinte

    def adiciona_clientes(nome, lista=None):
        if lista is None:
            lista = []
        lista.append(nome)
        return lista

    lista1 = []
    cliente1 = adiciona_clientes('Leonardo', lista1)
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

Mas, blz, isso não é a mesma coisa que definirmos o parâmetro "lista=[]"?

A resposta é não!

O motivo disso, seria que, a diferença entre você definir um parâmetro multável com a forma que foi corrigida acima, seria que, na forma acima, sempre que eu não passar um segundo parâmetro, será criado uma nova lista, dessa forma, quebrando o apontamento para uma única lista, quando vc deixava definido como um parâmetro padrão. 

No caso, isso significa os seguinte

    def adiciona_clientes(nome, lista=None):
        if lista is None:
            lista = []
        lista.append(nome)
        return lista

    lista1 = []
    cliente1 = adiciona_clientes('Leonardo', lista1)
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

    cliente3 = adiciona_clientes('Milena')
    print(cliente3)
    adiciona_clientes('Rogerio', cliente3)
    print(cliente3)

Agora, vemos que, independentemente de colocarmos, na primeira chamada, uma lista vazia ou não, isso não causará o problema de apontamento para a mesma lista. Mas, sim, sempre será criado uma lista nova.

Claro, uma vez criado uma lista, podemos, por fora da função, manipula-las tbm

    def adiciona_clientes(nome, lista=None):
        if lista is None:
            lista = []
        lista.append(nome)
        return lista

    lista1 = []
    cliente1 = adiciona_clientes('Leonardo', lista1)
    print(cliente1)
    adiciona_clientes('Joana', cliente1)
    adiciona_clientes('Fernando', cliente1)
    cliente1.append('Edu')
    print(cliente1)

    cliente2 = adiciona_clientes('Helena')
    print(cliente2)
    adiciona_clientes('Maria', cliente2)
    print(cliente2)

    cliente3 = adiciona_clientes('Milena')
    print(cliente3)
    adiciona_clientes('Rogerio', cliente3)
    print(cliente3)

Bom, moral da história dessa aula!

Como uma boa prática, nunca, mas nunca, passe como valor padrão de um parâmetro, um valor mutável! Isso vale para qualquer valor mutável!
