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

## Aula 10 - Exercício - Salve sua classe em JSON:

## Aula 11 - Solução - Exercício + if __name__ == '__main__':

## Aula 12 - Curiosidades sobre convenções de nomes:
Como você viu na aula anterior, usamos certas convenções para nomes de variáveis, funções, classes e assim por diante. Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa: PascalCase, camelCase e snake_case.

PascalCase - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: MinhaClasse, Classe, MeuObjeto, MeuProgramaMuitoLegal. Essa á a convenção utilizada para classes em Python;

camelCase - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: minhaFuncao, funcaoDeSoma, etc... Essa conversão não é usada em Python (apesar de eu confundir as duas e às vezes acabar chamando camelCase de PascalCase ou vice-versa, mas agora você sabe a diferença);

snake_case - este é o padrão usado em Python para definir qualquer coisa que não for uma classe. Todas as letras serão minúsculas e separadas por um underline, como em: minha_variavel, funcao_legal, soma.

Os padrões usados em Python são: snake_case para qualquer coisa e PascalCase para classes.

## Aula 13 - Métodos de classe (@classmethod) + factories methods (métodos fábrica):

## Aula 14 - @staticmethod (métodos estáticos) são inúteis em Python =):

## Aula 15 - method vs @classmethod vs @staticmethod:

## Aula 16 - @property - um getter no modo Pythônico:

## Aula 17 - @property + @setter - getter e setter no modo Pythônico:

## Aula 18 - Encapsulamento (modificadores de acesso: public, _protected, __private):

## Aula 19 - Relações entre classes: associação, agregação e composição:

## Aula 20 - Agregação - Python Orientado a Objetos:

## Aula 21 - Composição - Python Orientado a Objetos:

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
