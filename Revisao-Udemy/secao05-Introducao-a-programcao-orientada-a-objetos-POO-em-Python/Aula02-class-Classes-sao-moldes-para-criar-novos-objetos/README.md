# Aula 02 - class - Classes são moldes para criar novos objetos:
Classes sao moldes para criar novos objetos.

As classes geram novos objetos (instancias) que podem ter seus proprios atributos e metodos.

Os objetos gerados pela classe podem usar seus dados internos para realizar varias acoes.

Por convencao, usamos PascalCase para nomes de classes.

Um exemplo disso e uma string

    string = 'Leonardo'  # str
    print(string.upper())
    print(isinstance(string, str))

Basicamente, a variavel que criamos "string" acima e que atribuimos, de fato, uma string, conseguimos ver que nela existem varios metodos (upper(), capitalize(), count, etc...)

Bom, para criarmos uma classe de forma manual usamos a sintaxe "class" como seguinte

    class Pessoa:
        ...

Dentro dela, colocamos "...", mas o usual e que coloquemos metodos getter e setters, os atributos, como no Java, e nela colocamos o os metodos do que queremos que essa classe faca.

Uma vez criado uma classe, a maneira como a instanciamos seria da seguinte forma

    class Pessoa:
        ...

    p1 = Pessoa()

Diferente, nao? Em Java precisamos colocar o "new" antes da instanciacao de uma nova classe, mas em Python isso nao e necessario.

Bom, assim como no Java, aqui a logica nao muda muito, quando se trata de definirmos novos atributos. E a maneira como iremos acessa-las e da seguinte forma

    class Pessoa:
        ...

    p1 = Pessoa()
    p1.nome = "Leonardo" # Setter
    p1.sobrenome = "Teramatsu" # Setter
    print(p1.nome) # Getter
    print(p1.sobrenome) #Getter

Ou a forma mais rapida de atribuimos, seria

    class Pessoa:
        ...

    p1 = Pessoa("Leonardo", "Teramatsu")
    print(p1.nome) # Getter
    print(p1.sobrenome) #Getter

Claro, ao rodarmos os codigos acima, sera fornecido um erro, pois nao definimos nada dentro da classe Pessoa ainda.