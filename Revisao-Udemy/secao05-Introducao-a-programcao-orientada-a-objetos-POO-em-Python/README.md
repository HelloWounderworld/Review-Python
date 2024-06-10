# Introdução à Programação Orientada a Objetos em Python - POO (Classes):

## Aula 01 - Introdução à seção e livros de referência:
Seguir as seguintes referências de livros:

- Php Programando com Orientação a Objetos

- Python Fluent

- Padrões de Projeto soluções reutilizáveis - GOF

- Patterns of Enterprise Application Architecture

## Aula 02 - class - Classes são moldes para criar novos objetos:
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

## Aula 03 -  Introdução ao método __init__ (inicializador de atributos):
Bom, entendido a ideia geral de como funciona uma classe, para quem ja sabe Java, viu que possui bastante analogia.

Agora, vamos partir para definir os atributos e permitir que tais atributos definidos sejam inicializados. Para isso, vamos precisar utilizar a sintaxe "__init__" da seguinte forma

    class Pessoa:
        def __init__(self, nome, sobrenome):
            self.nome = nome
            self.sobrenome = sobrenome

No caso, o "self" aqui e o tal do "this", para quem aprendeu Java ou JavaScript. Ou seja, ela representa o escopo local onde mostra tudo o que foi definido localmente, neste caso, da classe. Em outras palavras, o "self" ela referencia ao objeto que esta sendo criado.

Como podemos ver acima, ao utilizarmos a sintaxe "__init__", no primeiro parametro precisamos colocar o "self" e, em seguinte, os parametros dos atributos que queremos definir. Porem, no momento em que vc for instanciar a classe, Pessoa, vc nao precisa colocar nenhum valor que referencie ao "self". O Python, automaticamente, ele ja entende qual que tais valores sera referenciado pelo objeto usando o "self". Ou seja, da seguinte forma

    class Pessoa:
        def __init__(self, nome, sobrenome):
            self.nome = nome
            self.sobrenome = sobrenome

    p1 = Pessoa("Leonardo", "Teramatsu")
    print(p1.nome) # Getter
    print(p1.sobrenome) #Getter

Ou, tambem, vc poderia atribuir da seguinte forma

    class Pessoa:
        def __init__(self, nome, sobrenome):
            self.nome = nome
            self.sobrenome = sobrenome

    p1 = Pessoa()
    p1.nome = "Leonardo"
    p1.sobrenome = "Teramatsu"
    print(p1.nome) # Getter
    print(p1.sobrenome) #Getter

Podemos, tambem, utilizar o "__init__" independentemente dentro de uma classe, pois ela e um inicializador.

Lembre-se, o metodo init sempre, mas sempre, retorna "None"!!! Ao criarmos uma classe e definirmos o inicializador dentro dela, provavelmente, aparecera de forma automatica o seguinte 

    def __init__(self) -> None:
        pass

Basicamente, o Python esta dizendo literalmente que o init ela sempre retorna "None".

Se por acaso fizermos o seguinte o que poderia acontecer?

    class Carro:
        def __init__(self):
            self.nome = 'Fusca'

Bom, basicamente, o nome do que foi feito acima se chama "Hard coded" (Algo que foi escrito diretamente no codigo), ou seja, nao importa qual seja qualquer outra variavel com qualquer outro nome, no atributo "nome" sera sempre o que foi definido manualmente acima.

Bom, para evitarmos que ocorra o "hard coded", isso mostra o significado de ter que definirmos os parametros depois da self

    class Carro:
        def __init__(self, alguma_coisa='Sei la'):
            self.nome = alguma_coisa

    fusca = Carro()
    print(fusca.nome)

    celta = Carro()
    print(celta.nome)

Enfim, pontos importantes dessa aula foram

- __init__: serve para inicializar os atributos

- self: serve para referenciar o objeto local.

Link para leitura:

    https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python
    https://www.analyticsvidhya.com/blog/2024/02/all-about-init-in-python/#:~:text=The%20__init__%20method,necessary%20setup%20or%20initialization%20tasks.
    https://www.geeksforgeeks.org/__init__-in-python/
    https://www.shiksha.com/online-courses/articles/understanding-self-in-python/#:~:text=The%20use%20of%20%E2%80%9Cself%E2%80%9D%20in,and%20class%20variables%20or%20methods.

## Aula 04 - Métodos em instâncias de classes Python:
Agora, vamos criar metodos dentro das classes.

Nao ha muito segredo aqui, entao vale mais a pena vc verificar como se cria o metodo dentro de uma classe em Python na pratica

    class Carro:
        def __init__(self, nome):
            self.nome = nome
    
    fusca = Carro()
    fusca.nome = 'Fusca'

Bom, vamos partir para a criacao de um metodo. Vamos criar o metodo chamado "acelerar"

    class Carro:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
    
    fusca = Carro()
    fusca.nome = 'Fusca'

Detalhe importante. Colocamos o parametro "self" dentro do metodo tbm. Isso para referenciar ao objeto que esta sendo criado. Ou seja, quem eu quero acelerar? O fusca. Assim, como se eu instanciar uma nova classe, celta, de qual carro eu quero que ela seja acelerado? Do celta.

E isso, mesmo que dentro do metodo eu nao tenha passado nenhum outro parametro, para que a classe entenda que eu estou agindo sobre o objeto que foi criado o self e necessario sempre ser colocado como o primeiro parametro.

No caso, o metodo, como comeco ficaria o seguinte

    class Carro:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
            print(f'{self.nome} esta acelerando...')

    fusca = Carro('Fusca')
    print(fusca.nome)

    celta = Carro(nome='Celta')
    print(celta.nome)

Dai, para conseguirmos utilizar esse metodo, nao muda muito com o Java e JavaScript. Ou seja, usando o "." para conseguirmos chamar

    class Carro:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
            print(f'{self.nome} esta acelerando...')

    fusca = Carro('Fusca')
    print(fusca.nome)
    fusca.acelerar()

    celta = Carro(nome='Celta')
    print(celta.nome)
    celta.acelerar()

## Aula 05 - Entendendo self em classes Python:
Bom, vamos entender melhor sobre o self em classes Python.

Basicamente, o self ele e um this nas outras linguagens como Java e JavaScript.

O self, em classe Python, ele e um nome adotado como convencao, pois se quisermos, podemos colocar um outro nome como seguinte

    class Carro:
        def __init__(blablabla, nome):
            blablabla.nome = nome

        def acelerar(blablabla):
            print(f'{blablabla.nome} esta acelerando...')

E mesmo assim, como a classe Python, considera o primeiro parametro como self, o parametro "blablabla" funcionara como self

    class Carro:
        def __init__(blablabla, nome):
            blablabla.nome = nome

        def acelerar(blablabla):
            print(f'{blablabla.nome} esta acelerando...')

    fusca = Carro('Fusca')
    print(fusca.nome)
    # print(fusca.acelerar())
    fusca.acelerar()

    celta = Carro(nome='Celta')
    print(celta.nome)
    celta.acelerar()

E mais, todos os parametros selfs nao precisa ser o mesmo nome

    class Carro:
        def __init__(blablabla, nome):
            blablabla.nome = nome

        def acelerar(efg):
            print(f'{efg.nome} esta acelerando...')

    fusca = Carro('Fusca')
    print(fusca.nome)
    # print(fusca.acelerar())
    fusca.acelerar()

    celta = Carro(nome='Celta')
    print(celta.nome)
    celta.acelerar()

Mesmo assim, por ser o primeiro parametro, ela continua funcionando da mesma forma. Porem, a unica diferenca e que estariamos criando dois selfs diferentes dentro da classe acima, ao colocarmos o primeiro parametro de forma diferente.

Para entender melhor sobre self, primeiro entenda a classe da seguinte forma. A classe e como se fosse um molde de um cookie, tanto e que se fizermos algo como seguinte

    class Carro:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
            print(f'{self.nome} esta acelerando...')

    Carro.acelerar()

nao ira acontecer nada, pois no e o mesmo que eu esteja querendo degustar o cookie, mas em vez de degustar o resultado do que foi colocado o igrediente eu estarei tentando degustar o molde, pelo fato de fazer "Carro.acelerar()".

Ja, ao definirmos como o seguinte

    class Carro:
        def __init__(self, nome):
            self.nome = nome

        def acelerar(self):
            print(f'{self.nome} esta acelerando...')

    fusca = Carro('Fusca')
    print(fusca.nome)
    # print(fusca.acelerar())
    fusca.acelerar()

A variavel "fusca", pelo fato de eu ter instanciado a classe, Carro, ela sera o proprio cookie que foi criado a partir do molde, Carro. Ou seja, no momento em que eu estiver degustando dos sabores e das caracteristicas desse cookie, que sao os momentos em que eu estiver chamando algum metodo ou atributo que foi definido nela, eu estarei conseguindo degustar.

Assim, o self, ela entra exatamente para apontar ao que esta sendo degustado, que e o cookie. Neste caso, as variaveis "fusca" e "celta" que nelas foram instanciado tais classes, Carro.

Obs: Em teoria de categoria essa ideia e definido formalmente na linguagem matematica.

Link para leitura:

    https://www.shiksha.com/online-courses/articles/understanding-self-in-python/#:~:text=In%20Python%2C%20the%20term%20%E2%80%9Cself,as%20to%20create%20new%20members.
    https://www.geeksforgeeks.org/self-in-python-class/
    https://www.w3schools.com/python/gloss_python_self.asp
    https://awari.com.br/como-funciona-o-self-no-python-guia-completo-para-iniciantes/#:~:text=O%20self%20%C3%A9%20uma%20palavra,de%20programa%C3%A7%C3%A3o%2C%20como%20o%20Java.
    https://hub.asimov.academy/tutorial/entendendo-o-uso-do-self-em-python/#:~:text=usado%20em%20Python.-,O%20que%20%C3%A9%20o%20self%20%3F,a%20inst%C3%A2ncia%20de%20uma%20classe.

## Aula 06 - Escopo da classe e de métodos da classe:
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

## Aula 07 - Mantendo estados dentro da classe:
Bom, uma das caracteristicas muito legal de uma programacao orientada a objetos, seria que as suas instancias poderiam carregar os seus estados.

No caso, como podemos ver no exemplo

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            print(f'{self.nome} esta filmando...')
            self.filmando = True

    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    print(c1.filmando)
    print(c2.filmando)

Como podemos ver abaixo, no print(C1.filmando) e print(C2.filmando), podemos ver que e devolvido True e False, respectivamente. Ou seja, isso significa que o estado da instancia, filmando, foi guardado, depois que foi acionado o metodo, filmar, que muda o valor desse atributo de False para True e ela mantem mesmo depois disso.

Bom, podemos melhorar mais ainda a qualidade desse metodo para conseguirmos verificar se a camera ja esta no estado de gravacao

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    print(c1.filmando)
    print(c2.filmando)

Bom, como podemos ver, acima, testando ela, fica mais nitido ainda a caracteristica de que o estado de uma instancia estar sendo mantido.

Agora, vamos acrscentar mais um metodo, fotografar. Nela, podemos aproveitar algumas condicoes que foi criado no metodo, filmar

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

        def fotografar(self):
            if self.filmando:
                print(f'{self.nome} nao pode fotografar filmando...')
                return
            
            print(f'{self.nome} esta fotografando...')
            self.filmando = True
            
    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    c1.filmar()
    c1.fotografar()
    print(c1.filmando)
    print(c2.filmando)

Bom, claro, depois de feito o metodo acima, falta criar um outro metodo que desative o modo de filmagem, entao vamos precisar criar o seguinte metodo

    class Camera:
        def __init__(self, nome, filmando=False):
            self.nome = nome
            self.filmando = filmando

        def filmar(self):
            if self.filmando:
                print(f'{self.nome} ja esta filmando...')
                return

            print(f'{self.nome} esta filmando...')
            self.filmando = True

        def parar_filmar(self):
            if not self.filmando:
                print(f'{self.nome} nao esta filmando...')
                return

            print(f'{self.nome} esta parando de filmar...')
            self.filmando = False

        def fotografar(self):
            if self.filmando:
                print(f'{self.nome} nao pode fotografar filmando...')
                return
            
            print(f'{self.nome} esta fotografando...')
            self.filmando = True
            
    c1 = Camera('Canon')
    c2 = Camera('Sony')

    c1.filmar()
    c1.filmar()
    c1.fotografar()
    c1.parar_filmar()
    c1.fotografar()
    # print(c1.filmando)
    # print(c2.filmando)

Bom, como podemos ver, conseguimos criar a funcionalidade basica de uma camera atraves de uma classe.

## Aula 08 - Atributos de classe:
Vamos abordar mais ainda sobre o conceito de atributo de classe.

Atributos de classe em Python são variáveis que são definidas dentro de uma classe, mas fora de qualquer método. Esses atributos são compartilhados por todas as instâncias da classe, o que significa que eles têm o mesmo valor para cada instância, a menos que explicitamente alterados. Atributos de classe são úteis para armazenar propriedades que devem ser as mesmas para todas as instâncias de uma classe.

Bom, como podemos ver no nosso exemplo que criamos

    class Pessoa:
        atributo = 'valor'

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return 2024 - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

A classe, Pessoa, que foi criado, nela, conseguimos definir o atributo chamado 'atributo'. E no metodo, get_ano_nascimento, temos um hard coder, 2024. Para esse hard coder, podemos criar uma constante fora da classe como seguinte

    # Atributos e classe
    ANO_ATUAL = 2024

    class Pessoa:
        atributo = 'valor'

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return ANO_ATUAL - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Mas, tambem, como uma alternativa pratica, podemos criar um atributo desse tipo dentro da classe tbm

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Para acessarmos esse atributo, que esta valendo para todas as classes, existem duas formas:

- Primeira: Pessoa.ano_atual

- Segunda: self.ano_atual - Pode existir uma instancia, ano_atual, no init. Entao, para separarmos entre o que e atributo e instancia, melhor adotarmos a pratica acima para atributos, quando for acessar o seu valor.

A primeira forma de acessarmos o atributo, ano_atual, dentro da classe, esta entre as boas praticas. Ja a segunda ela e um pouco perigosa, pois, dependendo do caso, fica sujeito a alteracao no processo de instanciacao externo.

Como vimos na aula anterior, conseguimos acessar esse atributo dentro dessa classe sem a necessidade de instanciarmos a classe, Pessoa

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(Pessoa.ano_atual)
    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Porem, esse atributo que definimos dentro dessa classe, ela esta sujeita a alteracao, como seguinte

    # Atributos e classe
    # ANO_ATUAL = 2024

    class Pessoa:
        # atributo = 'valor'
        ano_atual = 2024

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade
        
    p1 = Pessoa('Joao', 35)
    p2 = Pessoa('Helena', 12)

    print(Pessoa.ano_atual)
    Pessoa.ano_atual = 1

    print(p1.get_ano_nascimento())
    print(p2.get_ano_nascimento())

Mas qual o motivo disso ter ocorrido? Bom, o motivo disso e porque ela e o atributo da classe. Ou seja, um atributo que esta atrelado ao molde em si. Entao, quando vc mudar o valor dela, essa mudanca surtira para todas as instancias efetudadas.

### Utilidades dos Atributos de Classe
1. Valores Constantes: Atributos de classe são frequentemente usados para definir constantes que são relevantes para todas as instâncias da classe.

2. Contadores ou Estatísticas: Eles podem ser usados para contar o número de instâncias de uma classe ou acumular valores que são relevantes em um nível de classe, como o total de todas as transações feitas em todas as instâncias de uma classe de conta bancária.

3. Configurações Padrão: Atributos de classe podem ser usados para definir valores padrão que são compartilhados por todas as instâncias, como configurações padrão em aplicativos.

4. Métodos de Fábrica: Eles podem ser usados em conjunto com métodos de classe para criar instâncias de uma maneira particular, baseada em parâmetros que são comuns a todas as instâncias.

5. Dados Compartilhados: Eles permitem que dados sejam compartilhados entre todas as instâncias de uma classe, o que pode ser útil para implementar certos padrões de design como Singleton.

### Exemplo de Atributo de Classe

    class Carro:
        numero_de_rodas = 4  # Atributo de classe

        def __init__(self, marca, modelo):
            self.marca = marca  # Atributo de instância
            self.modelo = modelo  # Atributo de instância

        def detalhes(self):
            return f"{self.marca} {self.modelo} tem {Carro.numero_de_rodas} rodas."

    # Acessando o atributo de classe diretamente pela classe
    print(Carro.numero_de_rodas)  # Saída: 4

    # Modificando o atributo de classe afeta todas as instâncias
    Carro.numero_de_rodas = 6
    carro1 = Carro("Toyota", "Corolla")
    carro2 = Carro("Honda", "Civic")

    print(carro1.detalhes())  # Saída: Toyota Corolla tem 6 rodas.
    print(carro2.detalhes())  # Saída: Honda Civic tem 6 rodas.

### Considerações
Alterar um atributo de classe afeta todas as instâncias que acessam esse atributo através da classe. No entanto, se uma instância sobrescreve esse atributo (por exemplo, self.numero_de_rodas = 5), essa mudança será local para a instância.

Atributos de classe são uma ferramenta poderosa para compartilhar dados e comportamentos entre todas as instâncias de uma classe, mas devem ser usados com cuidado para evitar comportamentos inesperados devido ao compartilhamento de estado.

## Aula 09 - __dict__ e vars para atributos de instância:
Em Python, __dict__ e a função vars() são usados para acessar o dicionário de atributos de um objeto. Eles são úteis para inspeção, serialização e manipulação dinâmica de atributos de objetos.

O __dict__ mantem um objeto do tipo mapping.

### Uso de __dict__:
Como podemos ver abaixo, conseguimos manipular os atributos que foram instanciados, desde mudar o seu valor e, ate mesmo, deletar

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

Porem, esses atributos elas estao armazenados em algum lugar antes, quando tinha algum valor. Entoa, onde esses valores estavam salvos?

Re: dentro do __dict__.

O __dict__ é um atributo especial que armazena todos os atributos de um objeto em forma de dicionário. Cada chave do dicionário é o nome de um atributo e cada valor é o valor correspondente do atributo.

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

Tome cuidado que o __dict__ ele e editavel. Ou seja, podemos fazer algo do seguinte tipo

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

    p.__dict__['outra'] = 'coisa'
    print(p.__dict__)

Bom, o legal disso seria que usando o __dict__ conseguimos salvar tais dados armazenados numa classe instanciada em forma de JSON. E tbm, recuperar esse JSON e criar novamente os objetos das classes, como por exemplo

    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p1.nome = 'Eita'
    print(p1.nome)

    del p1.nome
    print(p1.nome)

    p = Pessoa("João", 30)
    print(p.__dict__)

    p.__dict__['outra'] = 'coisa'
    print(p.__dict__)

    dados = {'nome': 'Helena', 'idade': 12}
    p1 = Pessoa(**dados)
    print(p1.__dict__)

Ou seja, desenpacotamento do dicionario.

Ou seja, podemos usar esse __dict__ para salvar dados ou retorna-los, via banco de dados que sera feito mais pela frente em MySQL. Claro, podemos realizar a mesma coisa para qualquer outro banco de dados nao relacional tbm.

### Uso de vars():
vars() é uma função integrada que retorna o __dict__ de um objeto. Se nenhum argumento for fornecido, vars() atuará como locals().

print(vars(p))

### Utilidades:
- 1. Inspeção de Objeto: __dict__ e vars() podem ser usados para inspecionar os atributos de um objeto em tempo de execução, o que é útil para debugging e logging.

- 2. Serialização: Facilitam a serialização de objetos para formatos como JSON, permitindo converter facilmente os atributos de um objeto em um dicionário antes de serializar.

- 3. Manipulação Dinâmica: Permitem a manipulação dinâmica de atributos. Por exemplo, você pode adicionar, modificar ou remover atributos de um objeto em tempo de execução.

- 4. Cópia de Atributos: Podem ser usados para copiar atributos de um objeto para outro dinamicamente.

- 5. Reflexão e Metaprogramação: São úteis em técnicas avançadas de programação onde o código precisa manipular informações sobre si mesmo.

### Considerações:
- __dict__ só está disponível em objetos que têm um dicionário de atributos, o que não inclui objetos criados a partir de classes definidas com __slots__ ou alguns tipos embutidos como listas e tuplas.

- vars() pode ser usado em qualquer objeto que suporte __dict__. Se o objeto não suportar __dict__, vars() lançará um TypeError.

Essas ferramentas são poderosas para manipulação dinâmica de objetos e introspecção em Python, facilitando a programação reflexiva e dinâmica.

## Aula 10 e 11 - Exercício e Solução - Salve sua classe em JSON + if __name__ == '__main__':
Na aula 87 da secao 04, foi ensinado o conceito de salvar e recuperar os dados em JSON.

Recomendo o estudante revisar o conceito e aplicar nessa aula.

Em Python, a variável especial __name__ é usada para determinar se um script está sendo executado como o programa principal ou está sendo importado como um módulo em outro script. O valor de __name__ é definido automaticamente pelo Python da seguinte forma:

- Se o script está sendo executado diretamente pelo Python (ou seja, não está sendo importado), __name__ é definido como '__main__'.

- Se o script está sendo importado de outro script, __name__ é definido como o nome do módulo sob o qual ele está sendo executado.

### Utilidades de __name__ == '__main__':
- 1. Controle de Execução: Permite que um script tenha partes que sejam executadas apenas quando o script é executado diretamente, e não quando é importado como um módulo. Isso é útil para testes ou quando o script também pode ser usado como um módulo.

- 2. Testes e Debugging: Facilita a escrita de código de teste no mesmo arquivo que o código principal, permitindo que os testes sejam executados apenas quando o arquivo é executado diretamente.

- 3. Organização do Código: Ajuda a manter o código limpo e organizado, separando a funcionalidade do módulo da lógica de execução.

Exemplo de Uso:

    def func():
        print("Função sendo executada")

    if __name__ == '__main__':
        print("Executando como o programa principal")
        func()

Usar __name__ == '__main__' é uma prática comum em Python para facilitar a reutilização de código e a escrita de scripts que são tanto executáveis quanto importáveis como módulos, sem alterar seu comportamento quando são importados.

### Cenarios para comparar:
Vamos considerar um cenário onde temos dois arquivos Python: main.py e module.py. O arquivo module.py contém uma função que queremos usar tanto diretamente quanto importada em outro script. Usaremos __name__ para controlar como o código é executado dependendo de como o script é chamado.

No arquivo, moduleAula1011.py

    def print_message():
        print("Esta função foi chamada de module.py")

    if __name__ == '__main__':
        print("module.py está sendo executado diretamente")
        print_message()
    else:
        print("module.py foi importado")

No arquivo, mainAula1011.py

    import module

    def main():
        print("Esta é a função main de main.py")
        module.print_message()

    if __name__ == '__main__':
        main()

#### Cenário 1: Executando module.py diretamente
Quando você executa module.py diretamente usando python module.py, a saída será:

    module.py está sendo executado diretamente
    Esta função foi chamada de module.py

Neste caso, __name__ em module.py é '__main__', então o bloco de código dentro do if __name__ == '__main__': é executado.

#### Cenário 2: Importando module.py de main.py
Quando você executa main.py diretamente usando python main.py, a saída será:

    module.py foi importado
    Esta é a função main de main.py
    Esta função foi chamada de module.py

Aqui, module.py é importado, então __name__ em module.py não é '__main__', mas sim 'module'. Isso significa que o bloco if __name__ == '__main__': em module.py não é executado, mas a função print_message() ainda é acessível e usada em main.py.

#### Conclusão
Este exemplo mostra claramente como __name__ ajuda a controlar o comportamento do script dependendo de ele ser o ponto de entrada principal ou ser importado como um módulo. Isso permite que o mesmo arquivo funcione tanto como um script independente quanto como um módulo reutilizável em outros scripts, sem interferir na lógica de outros programas que o importam.

## Aula 12 - Curiosidades sobre convenções de nomes:
Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

## Aula 13 - Métodos de classe (@classmethod) + factories methods (métodos fábrica):
Lembra quando discutimos sobre atributo de classe?

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

Para acessarmos esse atributo de classe, nao precisamos instanciar a classe Pessoa, bastaria acessar como se fosse um metodo

    print(Pessoa.ano)

Agora, para o metodo, metodo_de_classe, que criamos, nao funciona da mesma coisa. Ou seja, usando o seguinte

    Pessoa.metodo_de_classe()

Isso ira nos fornecer um erro... Pois, precisariamos passar algum argumento como self, que nesse caso, seria uma classe que foi instanciado

    Pessoa.metodo_de_classe(p1)

Porem, ao usarmos @classmethod, conseguimos criar um metodo dentro da classe, Pessoa, sem a necessidade de passarmos o 'self' como parametro, mas, sim, a propria classe, 'cls', e conseguimos chamar o metodo sem a necessidade de instanciarmos a classe

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

    Pessoa.metodo_de_classe(p1)
    Pessoa.metodo_de_classe_sem_self()

Mas, ai, qual a utilidade desse @classmethod??? Seria para fabricar metodos, factories methods. Ou seja, um metodo que cria um outro objeto de pessoa. Como podemos ver no exemplo seguinte

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

        @classmethod
        def criar_com_50_anos(cls, nome):
            return cls(nome, 50)

No exemplo acima, suponhamos que tenhamos um conjunto de pessoas que toda elas tenham 50 anos. Entao, o metodo, criar_com_50_anos, funciona para conseguirmos instanciar uma nova classe, mas com esse valor hard coder, 50. Nesse metodo, criar_com_50_anos, conseguimos ver que esta sendo retornado o cls, que e a propria classe, Pessoa, de forma oculta.

    class Pessoa:
        ano = 2024 # atributo de classe

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def metodo_de_classe(self):
            print('Howdy!')

        @classmethod
        def metodo_de_classe_sem_self(cls):
            print('Hello!')

        @classmethod
        def criar_com_50_anos(cls, nome):
            return cls(nome, 50)

    p2 = Pessoa.criar_com_50_anos('Miyami')
    print(p2.nome)
    print(p2.idade)

Ou seja, isso que e o factories methods, que e um metodo que cria novos objetos com alguma logica.

Lembrando que nao temos o self dentro desses @classmethod. Entao, vc nao conseguiria dizer 'self.nome' ou 'self.idade' em si. Ou seja, pensa @classmethod e como se fosse um molde ou uma extensao de molde de uma classe.

### @classmethod:
Em Python, o decorador @classmethod é usado para definir um método da classe que pode ser chamado diretamente na classe, sem a necessidade de criar uma instância dela. Este método recebe o primeiro parâmetro como cls, que representa a própria classe, ao invés de self, que representa uma instância da classe.

#### Utilidades de @classmethod:

- Acesso a Atributos de Classe: Permite modificar ou acessar variáveis que são específicas da classe, não de instâncias individuais.

- Fábrica de Instâncias (Factory Methods): Frequentemente usado para criar métodos de fábrica. Um método de fábrica é um método que retorna objetos da classe, mas não necessariamente usando o construtor diretamente.

Exemplo de Uso de @classmethod

    class Pessoa:
        especie = "Homo sapiens"

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        @classmethod
        def criar_bebe(cls, nome):
            return cls(nome, 0)

        @classmethod
        def mudar_especie(cls, nova_especie):
            cls.especie = nova_especie

No exemplo acima:

- criar_bebe é um método de fábrica que cria uma nova instância da classe Pessoa com idade 0.

- mudar_especie é um método que altera o atributo de classe especie.

#### Utilidades dos Factory Methods:
- 1. Simplificação da Criação de Instâncias: Podem oferecer uma maneira mais intuitiva ou simplificada de criar instâncias, especialmente quando a criação envolve lógica complexa.

- 2. Nomeação de Construtores Alternativos: Permitem que você tenha múltiplos "construtores" com nomes claros que podem inicializar a classe de maneiras diferentes.

- 3. Encapsulamento de Lógica de Instanciação: Encapsula a lógica de criação de instâncias dentro da classe, mantendo o código externo mais limpo e simples.

Exemplo de Factory Method

    class Carro:
        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        @classmethod
        def com_ano_modelo(cls, marca, modelo, ano):
            carro = cls(marca, modelo)
            carro.ano = ano
            return carro

No exemplo acima, com_ano_modelo é um factory method que não só cria uma instância de Carro, mas também adiciona um atributo adicional ano à instância.

Em resumo, @classmethod e factory methods são ferramentas poderosas em Python para gerenciar como as instâncias são criadas e como a lógica relacionada à classe é manipulada.

### O que nao tem em @classmethod que tem na forma comum de instanciar uma classe?
Suponha que temos uma classe Empregado que precisa de um método para criar um empregado a partir de uma string que contém o nome e o salário separados por hífen. Isso é um exemplo clássico de um factory method, onde a lógica de criação da instância é um pouco mais complexa do que apenas passar argumentos diretamente para o construtor.

    class Empregado:
        def __init__(self, nome, salario):
            self.nome = nome
            self.salario = salario

        @classmethod
        def de_string(cls, dados_str):
            nome, salario = dados_str.split('-')
            return cls(nome, float(salario))

    # Instanciação comum
    emp1 = Empregado("João", 5000.00)

    # Instanciação usando @classmethod
    emp2 = Empregado.de_string("Maria-7000.00")

    print(emp1.nome, emp1.salario)  # Saída: João 5000.0
    print(emp2.nome, emp2.salario)  # Saída: Maria 7000.0

A instanciação comum de uma classe é mais vantajosa quando a criação do objeto é direta e não requer lógica adicional para configurar o objeto. Isso é particularmente útil quando os valores necessários para criar um objeto são simples e podem ser passados diretamente para o construtor sem necessidade de pré-processamento ou configuração complexa.

#### Exemplo Prático: Classe Ponto
Considere uma classe Ponto que representa um ponto em um sistema de coordenadas bidimensional. A criação de um ponto é direta, onde apenas as coordenadas x e y são necessárias.

    class Ponto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f"Ponto({self.x}, {self.y})"

    # Instanciação comum
    p1 = Ponto(3, 4)
    p2 = Ponto(5, 6)

    print(p1)  # Saída: Ponto(3, 4)
    print(p2)  # Saída: Ponto(5, 6)

##### Vantagens da Instanciação Comum Neste Caso
- 1. Simplicidade: A criação de um objeto Ponto é muito simples e direta. Os valores de x e y são passados diretamente ao construtor sem necessidade de manipulação adicional.

- 2. Clareza: A instanciação comum torna o código fácil de entender. Quando você vê Ponto(3, 4), é imediatamente claro que um ponto está sendo criado com coordenadas x=3 e y=4.

- 3. Performance: Embora a diferença seja geralmente mínima, a instanciação comum evita o overhead adicional de processamento que pode acompanhar um método de classe que manipula dados antes de criar uma instância.

- 4. Menos Código: Não há necessidade de definir um método de classe adicional se a lógica de criação do objeto não exigir isso. Menos código significa menos manutenção e menor chance de bugs.

##### Contexto onde @classmethod seria menos útil
No caso da classe Ponto, um @classmethod seria menos útil a menos que houvesse uma necessidade específica de criar pontos de uma maneira não convencional que exigisse algum tipo de cálculo ou configuração especial antes da criação do objeto. Por exemplo, se precisássemos de um método para criar um ponto que sempre esteja a uma certa distância de outro ponto, poderíamos considerar um @classmethod. No entanto, para a criação básica de pontos, a instanciação comum é mais direta e adequada.

Este exemplo mostra como a instanciação comum pode ser a escolha ideal para situações em que a criação de objetos é direta e não envolve lógica complexa.

#### Diferenças entre @classmethod e Instanciação Comum
- 1. Flexibilidade na Criação: O método de_string permite uma forma alternativa de criar uma instância da classe Empregado, processando uma string para extrair os dados necessários. Isso não é possível com a instanciação comum, a menos que essa lógica seja colocada fora da classe.

- 2. Encapsulamento de Lógica Específica: O @classmethod encapsula a lógica de conversão de uma string para uma instância dentro da classe. Isso mantém o código que usa a classe Empregado mais limpo e focado, sem se preocupar com os detalhes de como os dados são processados.

- 3. Uso de cls em vez de self: O @classmethod usa cls para acessar a classe e criar uma instância. Isso significa que ele opera com a classe em si, não com uma instância da classe. Em contraste, métodos regulares que usam self operam em instâncias específicas da classe.

- 4. Herança e Polimorfismo: Se Empregado fosse uma classe base para outras classes, de_string ainda retornaria uma instância da classe que foi chamada, graças ao uso de cls. Isso é útil em situações de herança, onde subclasses podem querer herdar ou modificar o comportamento do factory method.

Este exemplo ilustra como @classmethod pode ser usado para adicionar métodos de criação alternativos que encapsulam lógica específica, proporcionando flexibilidade e mantendo o código organizado.

## Aula 14 - @staticmethod (métodos estáticos) são inúteis em Python =):
O decorador @staticmethod em Python é usado para definir um método dentro de uma classe que não opera sobre uma instância da classe nem modifica o estado da classe. Esse método não recebe o primeiro parâmetro automático self (referência à instância) ou cls (referência à classe), que são comuns em métodos de instância e métodos de classe, respectivamente.

### Utilidades do @staticmethod:
- 1. Organização de Código: Permite agrupar funções que têm relevância lógica com uma classe, mas que não precisam acessar ou modificar dados da instância ou da classe.

- 2. Reuso de Código: Facilita a reutilização de métodos, pois eles podem ser chamados tanto a partir da classe quanto de suas instâncias, sem a necessidade de criar um objeto.

- 3. Desacoplamento: Como os métodos estáticos não dependem do estado de uma instância ou da classe, eles promovem um menor acoplamento entre o comportamento do método e os dados da classe/instância.

Obs: Desacoplamento em programação é o processo de projetar sistemas de modo que os componentes individuais sejam o mais independentes possível uns dos outros. Isso significa que mudanças em um componente têm impacto mínimo ou nenhum sobre outros componentes. O desacoplamento facilita a manutenção, o teste, a atualização e a reutilização do código, tornando o sistema mais flexível e robusto. Ele é alcançado através de práticas como o uso de interfaces, injeção de dependências, e padrões de design que promovem a separação de preocupações. Lei de Demeter (Clean Code).

### Exemplo de Uso de @staticmethod:

    class Matematica:
        @staticmethod
        def somar(x, y):
            return x + y

    # Chamando o método estático
    resultado = Matematica.somar(5, 3)
    print(resultado)  # Saída: 8

Neste exemplo, somar é um método estático que realiza uma operação de soma. Ele pode ser chamado diretamente através da classe sem a necessidade de criar uma instância.

### Considerações:
- Quando Usar: Use @staticmethod quando precisar de uma função que não modifica nem acessa variáveis da classe ou instâncias, mas que logicamente pertence à classe.

- Limitações: Métodos estáticos não podem acessar ou modificar o estado da classe ou das instâncias, o que pode ser uma limitação se tal acesso for necessário.

Em resumo, @staticmethod é útil para funções utilitárias ou auxiliares que se relacionam com a classe, mas que operam de forma independente de qualquer estado específico da classe ou de suas instâncias.

### Razões pelas quais @staticmethod pode ser visto como menos útil:
- 1. Sem Acesso ao Estado: Métodos estáticos não podem acessar ou modificar o estado da classe ou das instâncias. Se a funcionalidade requer acesso a esses dados, @staticmethod não seria apropriado.

- 2. Desacoplamento Excessivo: Embora o desacoplamento seja geralmente uma vantagem, em alguns casos, pode-se argumentar que um método estático é tão desacoplado que poderia simplesmente ser uma função fora da classe, não havendo necessidade de estar dentro da classe.

- 3. Alternativas Disponíveis: Em muitos casos, @classmethod pode ser mais apropriado se você precisar de acesso ao estado da classe. @classmethod permite acessar e modificar o estado da classe, o que pode ser mais útil para métodos que devem operar com esses dados.

- 4. Coesão: A coesão refere-se a quão bem os componentes de um módulo (ou classe) estão relacionados. Métodos estáticos, ao não operarem sobre o estado da classe, podem levar a uma coesão mais baixa, pois eles não estão trabalhando diretamente com os dados ou comportamentos que definem a classe.

### Exemplo de onde o uso de @staticmethod torna a melhor escolha para o seu uso:
Um exemplo prático onde @staticmethod é a melhor escolha envolve uma classe que realiza cálculos ou operações que são logicamente relacionadas à classe, mas que não necessitam acessar ou modificar o estado da classe ou de suas instâncias. Um exemplo comum pode ser uma classe que lida com operações matemáticas.

Suponha que você tenha uma classe que fornece utilitários matemáticos, como calcular a área de diferentes formas geométricas. Estas são operações puras que não dependem de nenhum estado específico da classe ou de suas instâncias.

    class Matematica:
        @staticmethod
        def area_circulo(raio):
            return 3.14159 * raio * raio

        @staticmethod
        def area_retangulo(largura, altura):
            return largura * altura

    # Uso dos métodos estáticos
    print("Área do Círculo:", Matematica.area_circulo(5))
    print("Área do Retângulo:", Matematica.area_retangulo(4, 5))

Quando você está construindo uma base axiomática matemática ou qualquer tipo de funcionalidade que envolva cálculos ou operações puras que não dependem do estado de uma instância ou da classe em si, o uso de @staticmethod é frequentemente a melhor escolha. Isso se deve a várias razões:

- 1. Independência de Estado: Métodos estáticos não acessam ou modificam o estado da instância ou da classe, o que é ideal para funções matemáticas que dependem apenas dos argumentos fornecidos e seguem princípios axiomáticos ou teoremas.

- 2. Reutilização e Acesso Fácil: Você pode chamar um método estático diretamente na classe sem precisar criar uma instância. Isso é muito prático para funções matemáticas que você deseja acessar frequentemente de diferentes partes do seu programa.

- 3. Organização Lógica: Agrupar funções matemáticas relacionadas dentro de uma classe usando @staticmethod ajuda a manter o código organizado e logicamente estruturado. Isso facilita a manutenção e o entendimento do código, especialmente em contextos onde múltiplas operações matemáticas estão sendo utilizadas.

- 4. Coesão: Manter operações matemáticas como métodos estáticos em uma classe relevante (como uma classe Matematica ou Calculadora) mantém o código coeso e focado, com todas as operações relacionadas agrupadas em um único local.

Exemplo bem esdruxulo e informal de uma classe que define os axiomas dos numeros reais

    class NumerosReais:
        @staticmethod
        def adicionar(x, y):
            return x + y

        @staticmethod
        def subtrair(x, y):
            return x - y

        @staticmethod
        def multiplicar(x, y):
            return x * y

        @staticmethod
        def dividir(x, y):
            if y == 0:
                raise ValueError("Não é possível dividir por zero.")
            return x / y

    # Uso dos métodos estáticos
    print("Adição:", NumerosReais.adicionar(5, 3))
    print("Subtração:", NumerosReais.subtrair(5, 3))
    print("Multiplicação:", NumerosReais.multiplicar(5, 3))
    print("Divisão:", NumerosReais.dividir(5, 3))

Bom, em resumo, os melhores momentos em que se utiliza @staticmethod, seriam em situacoes em que voce esteja definindo, postulando ou axiomatixando algo como uma linha de partida independente. Ao lembrar de definicoes matematicas, axiomas, postulados fisicos, etc... Algo dessas naturezas, percebemos que elas nao dependem de nenhum outro conceito e a partir delas que se iniciam toda a construcao.

## Aula 15 - method vs @classmethod vs @staticmethod:
Bom, vamos resumir os tres conceitos que vimos ate agora.

- method: self, metodo de instancia - Qualquer metodo que eu definir dentro da classe que necessite utilizar o self sera um metodo de instancia.

- @classmethod: cls, metodo de classe - Eu nao tenho acesso ao self dentro desse metodo. Metodo de classe ele recebe a classe, cls. Note que, a forma como construimos a classe dentro desse metodo e o mesmo.

- @staticmethod: metodo (nao self, nao cls) - Nao tem acesso ao self e nem a classe, cls. E uma funcao, apenas.

## Aula 16 - @property - um getter no modo Pythônico:
Quem conhece Java, provavelmente, ira sacar rapidamente que tem haver com o getter e o setter.

Sim, os conceitos fundamentais de getters e setters em Python usando @property e em Java são os mesmos. Ambos são utilizados para encapsular o acesso aos dados de uma classe, permitindo que a classe controle como esses dados são acessados e modificados, e para incluir lógica de validação ou transformação dos dados quando necessário.

O decorador @property em Python é usado para criar propriedades em uma classe, permitindo que você controle o acesso aos atributos de uma classe de maneira mais sofisticada. Ele transforma um método de uma classe em um atributo "getter", que pode ser acessado como se fosse um atributo normal, mas na verdade é um método sendo executado.

Suponhamos o seguinte cenario da seguinte classe

    class Caneta:
        def __init__(self, cor):
            self.cor = cor

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

Bom, se, por acaso, o nome do atributo, self.cor, tiver que ser mudado, da forma que o atributo esta sendo requisitado acima, tornaria extremamente trabalhoso para mudar todos os nomes.

    self.cor -> self.tinta # agora tu vai ter que mudar todos os prints, caneta.cor para caneta.tinta

Basicamente, para evitarmos que isso ocorra, podemos utilizar @property para encapsularmos e, com isso, criar o um getter que devolve o atributo. Dai, a vantagem disso seria que se, por acaso, tiver a necessidade de mudar o nome de um atributo, self.cor, sera necessario que vc mude somente dentro das classes e tudo continuara normal.

Como uma regra pratica e sempre recomendavel que vc encapsule aquelas linguagens de programacao mais enraizado, de modo que torne as alteracoes e melhorias mais faceis. As linguagens de programacao de infra, classe, banco de dados, etc... sera sempre de boa pratica que elas estejam todas encapsuladas assim separando os codigos de regra de negocio com codigo de nivel raiz.

Como uma aplicacao do @property, seguimos com o seguinte melhoria abaixo na classe, Caneta

    class Caneta:
        def __init__(self, cor):
            self.cor = cor

        def get_cor(self):
            return self.cor

    caneta = Caneta('Azul')
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())
    print(caneta.get_cor())

Com a forma acima, conseguimos proteger o atributo "self.cor", podemos controlar a sua transparencia tbm usando private, protected, public, etc... Porem, so com o encapsulamento acima, conseguimos adicionar uma camada na protecao. Se bem que, em Python, a ideia de proteger um atributo nao e muito relevante.

Agora, sem o uso do @property, a forma de encapsulamento mostrada acima e um getter.

Vamos utilizar, agora, o @property para implementar o getter de uma forma mais sofisticada

    class Caneta:
        def __init__(self, cor):
            self.tinta = cor

        @property
        def cor(self):
            return 'QUALQUER COISA'

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

Note que, utilizando o @property, conseguimos criar um getter, sem a necessidade de, ao chamarmos o metodo, cor, da forma como se fosse um metodo, como foi feito antes, print(caneta.get_cor()). Ou seja, print(caneta.cor), estamos chamando o ".cor" como se fosse um atributo, mas, na verdade, ela e um metodo. No caso, o @property, nos permite que consigamos chamar tal metodo como se fosse um atributo.

No caso, isso cabe no mesmo cenario de se mudarmos o nome do atributo raiz que esta dentro da classe

    class Caneta:
        def __init__(self, cor):
            self.tinta = cor

        @property
        def cor(self):
            return self.tinta

    caneta = Caneta('Azul')
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)
    print(caneta.cor)

### Funcionalidades do @property:
- 1. Encapsulamento: Permite esconder a implementação interna de um atributo, expondo apenas uma interface através de getters e setters.

- 2. Validação de Dados: Permite adicionar lógica de validação ao definir um valor.

- 3. Cálculo Dinâmico: Permite que o valor de um atributo seja calculado dinamicamente, em vez de ser armazenado.

Seguir o seguinte exemplo

    class Circulo:
        def __init__(self, raio):
            self._raio = raio

        @property
        def raio(self):
            return self._raio

        @raio.setter
        def raio(self, valor):
            if valor < 0:
                raise ValueError("O raio não pode ser negativo")
            self._raio = valor

        @property
        def area(self):
            return 3.14159 * self._raio ** 2

    # Uso da classe
    circulo = Circulo(5)
    print(circulo.raio)  # Saída: 5
    print(circulo.area)  # Saída: 78.53975

    circulo.raio = 10
    print(circulo.raio)  # Saída: 10
    print(circulo.area)  # Saída: 314.159

    # Tentativa de definir um raio negativo
    try:
        circulo.raio = -5
    except ValueError as e:
        print(e)  # Saída: O raio não pode ser negativo

- @property é usado para definir o método raio como um getter para o atributo _raio.

- @raio.setter define um método para definir o valor do _raio, incluindo uma verificação para garantir que o raio não seja negativo.

- A propriedade area é um exemplo de cálculo dinâmico, onde a área do círculo é calculada sempre que é acessada, usando o valor atual do raio.

Este exemplo ilustra como @property pode ser usado para adicionar validação e cálculo dinâmico, melhorando a segurança e a flexibilidade do código.

### O que seria um codigo Pythonico?
O termo "Pythonic" refere-se a uma filosofia de programação em Python que enfatiza a legibilidade, a simplicidade e a clareza do código. Ser "Pythonic" não é apenas sobre escrever código que funcione, mas sobre escrever código que se alinha com os princípios de design da linguagem Python, tornando-o fácil de entender e manter. Aqui estão alguns aspectos centrais do que torna um código Pythonic:

#### Seguir o Zen de Python
O Zen de Python, acessível através do comando import this no interpretador Python, é uma coleção de 19 "afirmações" que capturam a filosofia da linguagem. Algumas das mais destacadas incluem:

- "Bonito é melhor que feio."

- "Explícito é melhor que implícito."

- "Simples é melhor que complexo."

- "Deve haver uma — e preferencialmente só uma — maneira óbvia de fazer algo."

#### Utilizar recursos específicos da linguagem
Python oferece várias construções e recursos que não são encontrados em outras linguagens, ou que são mais elegantes em Python. Usar esses recursos de maneira eficaz é considerado Pythonic. Exemplos incluem:

- Compreensões de lista, dicionário e conjunto.

- Geradores e iteradores.

- Decoradores.

- Uso de with para gerenciamento de contexto.

####  Escrever código legível e conciso
Python valoriza a legibilidade do código. Isso significa evitar linhas excessivamente longas, usar nomes de variáveis e funções descritivos, e evitar construções complicadas quando uma solução simples e direta está disponível.

#### Seguir as convenções de estilo PEP 8
PEP 8 é o guia de estilo para Python que oferece convenções sobre como formatar código Python. Isso inclui diretrizes sobre nomes de variáveis, tamanho de linha, uso de espaços em branco e muito mais. Seguir o PEP 8 ajuda a manter o código Python uniforme e legível.

#### Aproveitar as funcionalidades de alto nível
Python é uma linguagem de alto nível com muitas abstrações embutidas, como manipulação automática de memória (garbage collection), tipos de dados dinâmicos e uma extensa biblioteca padrão. Usar essas funcionalidades plenamente é parte de escrever código Pythonic.

#### Preferir a simplicidade e a elegância
Pythonic code often involves finding the most straightforward solution to a problem, which not only works but also minimizes future code maintenance.

#### Exemplo de código não Pythonic vs Pythonic
Não Pythonic:

    result = []
    for i in range(len(some_list)):
        if some_list[i] > 0:
            result.append(some_list[i] * 2)

Pythonic:

    result = [x * 2 for x in some_list if x > 0]

O exemplo Pythonic usa uma compreensão de lista, que é mais concisa, mais fácil de ler e mais "Pythonic".

Em resumo, escrever de maneira Pythonic significa adotar as convenções e filosofias da linguagem Python para produzir código que não apenas funcione bem, mas que também seja limpo, legível e eficiente.

## Aula 17 - @property + @setter - getter e setter no modo Pythônico:
O decorador @setter em Python é usado em conjunto com o decorador @property para criar um "setter" que permite definir o valor de um atributo com controle adicional. Essencialmente, ele permite encapsular a lógica de atribuição de valores a um atributo, adicionando validações ou operações adicionais durante esse processo.

Aqui esta um exemplo basico de como @setter e usado

    class Pessoa:
        def __init__(self, nome):
            self._nome = nome

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, valor):
            if not isinstance(valor, str):
                raise ValueError("O nome deve ser uma string")
            self._nome = valor

No exemplo acima:

- @property é usado para definir um método getter para o atributo nome.

- @nome.setter define o método setter correspondente que permite modificar o valor do atributo _nome. Antes de atribuir o valor, ele verifica se o valor é uma string. Se não for, ele levanta uma exceção ValueError.

Essa abordagem de usar @property com @setter é útil para:

- Validação de dados: Garantir que os dados estejam corretos antes de serem atribuídos a um atributo.

- Encapsulamento: Esconder a representação interna enquanto expõe uma interface para passar e receber valores, permitindo mudanças na implementação interna sem afetar os usuários da classe.

- Controle adicional: Executar código adicional durante a atribuição de valores, como limpeza de dados ou transformação.

## Aula 18 - Encapsulamento (modificadores de acesso: public, _protected, __private):
Antes de abordarmos os tres modificadores de acesso, vamos entender o conceito de Encapsulamento em programacao orientada a objetos.

### Encapsulamento:
Encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO). Ele se refere à prática de ocultar os detalhes internos ou a implementação de uma classe e expor apenas o que é necessário para o mundo externo através de uma interface bem definida. Isso ajuda a proteger os dados internos da classe contra acessos indevidos e modificações não autorizadas, além de permitir uma maneira controlada de interagir com os objetos.

#### Funcionalidades do Encapsulamento:
- 1. Ocultação de Dados: Encapsulamento permite que os detalhes internos de implementação de uma classe sejam ocultados. Isso inclui atributos e métodos que não são necessários para os usuários da classe. Apenas uma interface necessária é exposta, o que simplifica o uso da classe.

- 2. Controle de Acesso: Através do encapsulamento, você pode controlar quem pode acessar os dados da classe e como eles podem ser modificados. Isso é feito através de métodos acessores (getters) e modificadores (setters), e pelo uso de níveis de acesso como public, protected e private.

- 3. Redução de Acoplamento: Encapsulamento ajuda a reduzir o acoplamento entre as classes, o que significa que mudanças em uma classe não afetam significativamente outras partes do programa. Isso torna o sistema mais modular e fácil de modificar ou estender.

- 4. Manutenção e Evolução: Com o encapsulamento, é mais fácil gerenciar e evoluir o código, pois as mudanças em uma classe podem ser feitas com um impacto mínimo sobre as outras classes que a utilizam. Isso é especialmente útil em sistemas grandes e complexos.

#### Exemplo em Python:

    class ContaBancaria:
        def __init__(self, titular, saldo_inicial=0):
            self.titular = titular
            self.__saldo = saldo_inicial  # Atributo privado

        def depositar(self, valor):
            if valor > 0:
                self.__saldo += valor
                print(f"Depósito de {valor} realizado com sucesso.")
            else:
                print("Valor do depósito deve ser positivo.")

        def sacar(self, valor):
            if valor > 0 and valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de {valor} realizado com sucesso.")
            else:
                print("Saque inválido.")

        def get_saldo(self):
            return self.__saldo

- O atributo __saldo é privado, o que significa que ele não pode ser acessado diretamente fora da classe ContaBancaria.

- Métodos públicos depositar, sacar e get_saldo são fornecidos para permitir operações controladas sobre o saldo.

Encapsulamento, portanto, não só protege os dados dentro de uma classe, mas também define claramente como a classe deve ser usada, contribuindo para um design de software mais robusto e manutenível.

### Modificadores de Acesso em Python - Importante: PYTHON NAO TEM MODIFICADORES DE ACESSO! E TUDO CONVENCAO!!

Em Python, os conceitos de public, protected e private são usados para controlar o acesso aos atributos e métodos de uma classe, ajudando a implementar o encapsulamento. No entanto, diferentemente de outras linguagens como Java ou C++, Python não possui keywords específicas para definir explicitamente o nível de acesso. Em vez disso, ele usa convenções de nomenclatura para indicar como um atributo ou método deve ser tratado em termos de visibilidade e acessibilidade.

#### Public
Public: Atributos e métodos públicos podem ser acessados de qualquer lugar, dentro ou fora da classe. Em Python, todos os membros de uma classe são públicos por padrão.

    class Carro:
        def __init__(self, marca):
            self.marca = marca  # Atributo público

        def dirigir(self):
            print("Carro está sendo dirigido")

#### Protected
Protected: Atributos e métodos protegidos são destinados a ser usados por subclasses, indicando que devem ser acessados apenas dentro da própria classe e por instâncias de subclasses. Em Python, isso é indicado por um único sublinhado (_) antes do nome do membro.

      class Carro:
        def __init__(self, marca):
            self._marca = marca  # Atributo protegido

        def _dirigir_privado(self):
            print("Método protegido, uso interno ou em subclasses")

#### Private
Private: Atributos e métodos privados não devem ser acessados fora da classe. Eles são usados para evitar que o código externo interfira diretamente com as variáveis internas. Em Python, isso é indicado por dois sublinhados (__) antes do nome do membro.

    class Carro:
        def __init__(self, marca):
            self.__marca = marca  # Atributo privado

        def __dirigir_privado(self):
            print("Método privado, acesso restrito à própria classe")

### Considerações
Em Python, o encapsulamento é mais uma convenção do que uma imposição estrita. Por exemplo, membros privados (com __) são apenas renomeados internamente com um nome da classe prefixado (ex: _Carro__marca), mas ainda podem ser acessados diretamente se realmente necessário, embora isso seja considerado uma má prática.

A ideia é que "somos todos adultos aqui", e os programadores são responsáveis por usar os membros da classe de maneira apropriada, respeitando as convenções de encapsulamento.

Essas convenções ajudam a manter o código mais organizado, seguro e fácil de manter, permitindo que os desenvolvedores saibam quais propriedades e métodos devem ou não ser acessados diretamente.

Seguir link para leitura PEP8:

    https://peps.python.org/pep-0008/#descriptive-naming-styles

## Aula 19 - Relações entre classes: associação, agregação e composição:
Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Associacao.

### Associação
A associação é uma relação entre duas classes onde os objetos de uma classe se relacionam com os objetos de outra, mas ambos podem existir independentemente. É a forma mais básica de relação que simplesmente indica que uma classe conhece a outra.

#### Definição Matemática:
Associação pode ser vista como uma relação binária $\R$ entre dois conjuntos $\A$ e $\B$, onde $\A$ e $\B$ representam diferentes tipos de objetos (classes). Matematicamente, isso é expresso como:

$\R\subseteq\A\times\B$

Cada par ordenado $\left(a,b\right)\in\R$ indica o objeto $\a$ da classe $\A$ está associado ao objeto $\b$ da classe $\B$.

#### Exemplos de Associação Simples
Vamos considerar um exemplo simples de uma biblioteca e seus livros:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Bibliotecario:
        def __init__(self, nome):
            self.nome = nome

        def empresta_livro(self, livro):
            print(f"{self.nome} emprestou o livro {livro.titulo}")

    # Instâncias
    livro1 = Livro("1984")
    bibliotecario = Bibliotecario("João")

    # Associação sendo utilizada
    bibliotecario.empresta_livro(livro1)

Neste exemplo, a classe Bibliotecario está associada à classe Livro através do método empresta_livro. O bibliotecário conhece o livro, mas ambos podem existir independentemente.

#### Exemplos de Associação com Múltiplas Formas
Vamos expandir o exemplo para incluir alunos que podem alugar livros da biblioteca:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Bibliotecario:
        def __init__(self, nome):
            self.nome = nome

        def empresta_livro(self, livro):
            print(f"{self.nome} emprestou o livro {livro.titulo}")

    class Aluno:
        def __init__(self, nome):
            self.nome = nome
            self.livros_alugados = []

        def aluga_livro(self, livro):
            self.livros_alugados.append(livro)
            print(f"{self.nome} alugou o livro {livro.titulo}")

    # Instâncias
    livro1 = Livro("1984")
    bibliotecario = Bibliotecario("João")

    # Associação sendo utilizada
    bibliotecario.empresta_livro(livro1)

    # Instâncias
    aluno1 = Aluno("Maria")

    # Associação sendo utilizada
    aluno1.aluga_livro(livro1)

Aqui, a classe Aluno também está associada à classe Livro. A associação permite que o aluno alugue livros, adicionando-os à sua lista de livros alugados. Cada aluno mantém uma lista de livros que alugou, demonstrando uma associação onde o aluno "conhece" os livros.

#### Exemplo de Associação Bidirecional
Em alguns casos, pode ser útil que ambos os objetos associados conheçam um ao outro. Por exemplo, um livro pode saber quem o alugou:

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo
            self.alugado_por = None

        def alugar(self, pessoa):
            self.alugado_por = pessoa
            pessoa.livros_alugados.append(self)
            print(f"{self.titulo} foi alugado por {pessoa.nome}")

    # Atualizando a classe Aluno para suportar a associação bidirecional
    class Aluno:
        def __init__(self, nome):
            self.nome = nome
            self.livros_alugados = []

        def aluga_livro(self, livro):
            livro.alugar(self)

    # Associação bidirecional sendo utilizada
    aluno1.aluga_livro(livro1)
    print(f"O livro {livro1.titulo} está alugado por {livro1.alugado_por.nome}")

### Conclusao
Essas relações ajudam a modelar a realidade no design de software, permitindo que os desenvolvedores criem sistemas mais organizados e compreensíveis, onde as dependências e interações entre objetos são claramente definidas.

Composicao $\subseteq$ Agregacao $\subseteq$ Associacao

Seguir link para leitura - Unified Modeling Language

    https://en.wikipedia.org/wiki/Unified_Modeling_Language

## Aula 20 - Agregação - Python Orientado a Objetos:
A agregação é um tipo de associação que representa uma relação "tem-um" ou "parte-de" entre duas classes, onde as partes podem existir separadamente do todo. Isso significa que se o objeto contêiner (o todo) for destruído, os objetos contidos (as partes) podem continuar a existir.

Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Agregacao.

#### Caracteristicas da Agregacao
- Independência: As partes (objetos contidos) podem existir independentemente do todo (objeto contêiner).

- Relação não exclusiva: Uma parte pode pertencer a mais de um todo sem que isso implique exclusividade.

- Transitividade: Se um objeto contêiner contém outro objeto, e este por sua vez contém um terceiro objeto, a relação de agregação pode ser transitiva.

#### Exemplo de Agregação
Consideremos um exemplo de uma biblioteca que contém livros. A biblioteca pode fechar, mas os livros ainda existirão.

    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

    class Biblioteca:
        def __init__(self, nome):
            self.nome = nome
            self.livros = []

        def adicionar_livro(self, livro):
            self.livros.append(livro)

    # Criando objetos
    biblioteca = Biblioteca("Biblioteca Central")
    livro1 = Livro("1984")
    livro2 = Livro("Brave New World")

    # Agregando livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Listando livros na biblioteca
    for livro in biblioteca.livros:
        print(f"{livro.titulo} está na {biblioteca.nome}")

#### Diversos Usos da Agregação
1. Sistemas de Gerenciamento de Recursos: Em um sistema de gerenciamento de recursos humanos, uma empresa pode ter diversos departamentos. Cada departamento pode existir sem a empresa, e a empresa pode existir sem um departamento específico.

        class Departamento:
            def __init__(self, nome):
                self.nome = nome
                self.funcionarios = []

            def adicionar_funcionario(self, funcionario):
                self.funcionarios.append(funcionario)

        class Empresa:
            def __init__(self, nome):
                self.nome = nome
                self.departamentos = []

            def adicionar_departamento(self, departamento):
                self.departamentos.append(departamento)

        # Uso
        empresa = Empresa("TechCorp")
        departamento = Departamento("Desenvolvimento")
        empresa.adicionar_departamento(departamento)

2. Sistemas de Gerenciamento de Conteúdo: Em um sistema de gerenciamento de conteúdo, uma página pode conter vários elementos, como textos, imagens e vídeos. A página pode ser deletada, mas os elementos podem ser reutilizados em outras páginas.

        class Elemento:
            def __init__(self, tipo):
                self.tipo = tipo

        class Pagina:
            def __init__(self, titulo):
                self.titulo = titulo
                self.elementos = []

            def adicionar_elemento(self, elemento):
                self.elementos.append(elemento)

        # Uso
        pagina = Pagina("Página Inicial")
        texto = Elemento("Texto")
        imagem = Elemento("Imagem")
        pagina.adicionar_elemento(texto)
        pagina.adicionar_elemento(imagem)

#### Conclusão
A agregação é uma forma de associação que permite uma flexibilidade maior na modelagem de sistemas, representando relações onde as partes podem existir sem o todo. Isso é útil em muitos contextos de desenvolvimento de software, especialmente em sistemas complexos onde a independência entre os componentes é crucial para a manutenção e escalabilidade do sistema.

## Aula 21 - Composição - Python Orientado a Objetos:
Na programação orientada a objetos (POO), as relações entre classes descrevem como objetos de diferentes classes interagem e dependem uns dos outros. Existem três tipos principais de relações: associação, agregação e composição. Cada tipo define um nível diferente de dependência entre as classes.

Neste topico iremos abordar sobre a relacao de Composicao.

### Composição
A composição é uma forma mais restritiva de agregação onde as partes não podem existir sem o todo. Se o objeto contêiner for destruído, então os objetos contidos também serão destruídos.

#### Exemplo
Um carro e um motor. Um motor é uma parte essencial de um carro, e não existe sem o carro.

    class Motor:
        def __init__(self, potencia):
            self.potencia = potencia

    class Carro:
        def __init__(self, modelo):
            self.modelo = modelo
            self.motor = Motor(potencia=120)  # Motor é criado junto com o Carro

        def __del__(self):
            print("O carro e o motor foram destruídos.")

## Aula 22 - Exercício (+solução) com classes e relações:

## Aula 23 - TEORIA: Herança, generalização e especialização:

## Aula 24 - Herança Simples - Python Orientado a Objetos:

## Aula 15 - (Parte 1) super e a sobreposição de membros em Python Orientado a Objetos:

## Aula 16 - (Parte 1) super e a sobreposição de membros em Python Orientado a Objetos:

## Aula 17 - Teoria - Herança múltipla - Python Orientado a Objetos:

## Aula 18 - Herança múltipla - Python Orientado a Objetos:

## Aula 19 - (Parte 1) Mixins, Abstração e a união de tudo até aqui:

## Aula 20 - (Parte 2) Log, LogFileMixin, LogPrintMixin e a união de tudo até aqui:

## Aula 21 - (Parte 3) LogFileMixin e a união de tudo até aqui:

## Aula 22 - (Parte 4) Eletrônico, Smartphone com Mixin e a união de tudo até aqui:

## Aula 23 - Classes abstratas - Abstract Base Class (abc) - Python Orientado a Objetos:

## Aula 24 - abstractmethod para qualquer método já decorado (property e setter):

## Aula 25 - Teoria: polimorfismo, assinatura de métodos e Liskov Substitution Principle:

## Aula 26 - Na prática: polimorfismo, assinatura de métodos e Liskov Substitution Principle:

## Aula 27 - Criando Exceptions em Python Orientado a Objetos (Exceções):

## Aula 28 - Levantando e tratando suas Exceptions (Exceções):

## Aula 29 - Notas das exceptions em Python 3.11+ (add_notes, __notes__):

## Aula 30 - Teoria: python Special Methods, Magic Methods ou Dunder Methods:

## Aula 31 - Python Dunder Methods __repr__ e __str__:

## Aula 32 - Exemplo de uso de dunder methods (métodos mágicos):

## Aula 33 - __new__ e __init__ em classes Python:

## Aula 34 - Context Manager com classes - Criando e Usando gerenciadores de contexto:

## Aula 35 - Exceptions em context manager com classes:

## Aula 36 - Context Manager com contextlib.contextmanager:

## Aula 37 - Funções decoradoras e decoradores com classes:

## Aula 38 - Funções decoradoras e decoradores com métodos:

## Aula 39 - Método especial __call__:

## Aula 40 - Classes decoradoras (Decorator classes):

## Aula 41 - Teoria: metaclasses são o tipo das classes:

## Aula 42 - __new__ de uma metaclass cria e retorna a classe em si:

## Aula 43 - __call__ de uma metaclass cria e retorna a instância da classe:

## Aula 44 - dir e help + DocStrings de uma linha (Documentação):

## Aula 45 - DocStrings de várias linhas (Documentação):

## Aula 46 - DocStrings em funções (Documentação):

## Aula 47 - DocStrings em class (Documentação):

## Aula 48 - Teoria: enum.Enum (Enumerações):

## Aula 49 - Código: enum.Enum (Enumerações):

## Aula 50 - Exercício com Abstração, Herança, Encapsulamento e Polimorfismo:

## Aula 51 - Solução - Criando a classe abstrata Conta:

## Aula 52 - Solução - Criando a classe ContaPoupanca:

## Aula 53 - Solução - Criando a classe ContaCorrente:

## Aula 54 - DICA Extra: tipagem, linters e settings.json do VS Code:

## Aula 55 - Solução - Criando a classe Pessoa:

## Aula 56 - Solução - Criando a classe Cliente:

## Aula 57 - Solução - Criando a classe Banco (Parte 1):

## Aula 58 - Solução - Criando a classe Banco (Parte 2):

## Aula 59 - dataclasses - O que são dataclasses?:

## Aula 60 - dataclasses com métodos, property e setter:

## Aula 61 - __init__ e __post_init__ em dataclasses:

## Aula 62 - Configurações do decorator dataclass:

## Aula 63 - asdict e astuple em dataclasses:

## Aula 64 - Valores padrão, field e fields em dataclasses:

## Aula 65 - namedtuple - tuplas imutáveis com nomes para valores:

## Aula 66 - Criando sua própria lista com Iterable, Iterator e Sequence (collections.abc):
