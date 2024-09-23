# Aula 06 - Escopo da classe e de métodos da classe:
Aqui está uma classe em Python que ilustra o conceito de escopo de classe e métodos de classe, explicando como os atributos e métodos são acessados e modificados:

    class Veiculo:
        # Atributo de classe (compartilhado por todas as instâncias)
        numero_de_rodas = 4

        def __init__(self, marca, modelo):
            # Atributos de instância (específicos para cada instância)
            self.marca = marca
            self.modelo = modelo

        def mostrar_detalhes(self):
            # Método de instância que acessa tanto atributos de instância quanto de classe
            return f"{self.marca} {self.modelo} tem {Veiculo.numero_de_rodas} rodas."

        @classmethod
        def mudar_numero_de_rodas(cls, novas_rodas):
            # Método de classe que modifica um atributo de classe
            cls.numero_de_rodas = novas_rodas

    # Criando instâncias da classe Veiculo
    carro1 = Veiculo("Toyota", "Corolla")
    carro2 = Veiculo("Honda", "Civic")

    # Acessando método de instância
    print(carro1.mostrar_detalhes())  # Toyota Corolla tem 4 rodas.

    # Modificando o atributo de classe usando método de classe
    Veiculo.mudar_numero_de_rodas(6)

    # Acessando o método de instância novamente para ver o efeito da mudança
    print(carro1.mostrar_detalhes())  # Toyota Corolla tem 6 rodas.
    print(carro2.mostrar_detalhes())  # Honda Civic tem 6 rodas.


Explicação:

- Atributos de Classe: numero_de_rodas é um atributo de classe, o que significa que ele é compartilhado por todas as instâncias da classe. Qualquer modificação neste atributo afetará todas as instâncias.

- Atributos de Instância: marca e modelo são atributos de instância, definidos dentro do método __init__. Eles são específicos para cada instância criada.

- Métodos de Instância: mostrar_detalhes é um método de instância que pode acessar atributos de instância usando self e atributos de classe diretamente pelo nome da classe.

- Métodos de Classe: mudar_numero_de_rodas é um método de classe, indicado pelo decorador @classmethod. Ele modifica o atributo de classe numero_de_rodas. Métodos de classe recebem cls como o primeiro parâmetro, que se refere à própria classe, não a uma instância específica.

Este exemplo demonstra como os atributos e métodos funcionam dentro do escopo de uma classe em Python, mostrando a interação entre atributos de classe e de instância e como eles podem ser manipulados.

Bom, como podemos ver, as classes tambem possuem escopos, assim como, os metodos internos dessas classes tambem, possuem escopos.

Ou seja, isso significa que eu nao poderia fazer algo do seguinte tipo

    class Animal:
        nome = 'Leao'
    
    print(nome)

Porem, podemos pegar a tal variavel definida dentro dessa classe, sem a necessidade de instancia-la

    class Animal:
        nome = 'Leao'
    
    print(Animal.nome)

Bom, agora, se definirmos algo do seguinte tipo

    class Animal:
        # nome = 'Leao'

        def __init__(self, nome):
            self.nome = nome

    # print(nome)
    print(Animal.nome)

No caso, depois dessam, nao iremos conseguir mais rodar a variavel "nome", pois agora, ela se tornou um atributo para instancia. No caso, precisaria instanciar a classe como o seguinte

    class Animal:
        # nome = 'Leao'

        def __init__(self, nome):
            self.nome = nome

    # print(nome)
    # print(Animal.nome)
    leao = Animal(nome='Leao')
    print(leao.nome)

Porem, como dissemos acima, se definirmos alguma variavel dentro desse def, como ela tem o seu proprio escopo interno, nao vamos conseguir acessa-lo por fora.

    class Animal:
        # nome = 'Leao'
        # print(variavel)

        def __init__(self, nome):
            self.nome = nome

            # variavel = "Valor"
            # print(variavel)

        def acao(self):
            # print(variavel)
            ...

    # print(nome)
    # print(Animal.nome)
    leao = Animal(nome='Leao')
    print(leao.nome)
    # print(variavel)
    # print(leao.acao())

Ou seja, ao tentarmos acessar "variavel" por fora do metodo "def", nao sera possivel.

Porem, o "self", como ela se refere ao escopo da classe, conseguimos, sim, acessar pelo outros metodos como seguinte

    class Animal:
        # nome = 'Leao'
        # print(variavel)

        def __init__(self, nome):
            self.nome = nome

            # variavel = "Valor"
            # print(variavel)

        def acao(self):
            # print(variavel)
            return f'{self.nome} esta executando uma acao'

    # print(nome)
    # print(Animal.nome)
    leao = Animal(nome='Leao')
    print(leao.nome)
    # print(variavel)
    print(leao.acao())

Da mesma forma que, se eu definir um parametro dentro de um novo metodo dentro da classe, Animal, ao executar tal metodo, se nao passar algum valor, sera retornado um erro

    class Animal:
        # nome = 'Leao'
        # print(variavel)

        def __init__(self, nome):
            self.nome = nome

            # variavel = "Valor"
            # print(variavel)

        def acao(self):
            # print(variavel)
            return f'{self.nome} esta executando uma acao'
        
        def comendo(self, alimento):
            # print(variavel)
            return f'{self.nome} esta comendo {alimento}'

    # print(nome)
    # print(Animal.nome)
    leao = Animal(nome='Leao')
    print(leao.nome)
    # print(variavel)
    print(leao.acao())
    # leao.acao()
    print(leao.comendo('Carne'))
    print(leao.comendo())

Da mesma forma que utilizamos o self para atributos, podemos utilizar para os metodos que foram definidos dentro de uma classe, como seguinte

    class Animal:
        # nome = 'Leao'
        # print(variavel)

        def __init__(self, nome):
            self.nome = nome

            # variavel = "Valor"
            # print(variavel)

        def acao(self):
            # print(variavel)
            return f'{self.nome} esta executando uma acao'
        
        def comendo(self, alimento):
            # print(variavel)
            return f'{self.nome} esta comendo {alimento}'
        
        def executar(self, *args, **kwargs):
            return self.comendo(*args, **kwargs)

    # print(nome)
    # print(Animal.nome)
    leao = Animal(nome='Leao')
    print(leao.nome)
    # print(variavel)
    print(leao.acao())
    # leao.acao()
    # print(leao.comendo('Carne'))
    print(leao.executar('Carne'))
    # print(leao.comendo())

Note que, o metodo executar, ela esta cumprindo o papel de executar outros metodos dentro da classe, Animal. Ou seja, usando o self, podemos executar um metodo dentro de uma classe no outro metodo que foi criado dentro da mesma classe.

Bom, resumindo, uma variavel dentro do escopo de um metodo dentro da classe, nao pode ser chamado por fora, a nao ser que ela esteja sendo atribuido pelo "self" no init. Assim como, o metodo definido dentro de uma classe pode ser executado por outro metodo definido dentro da mesma classe utilizando o "self". Ou seja, o "self" ela indica o escopo dentro da classe.