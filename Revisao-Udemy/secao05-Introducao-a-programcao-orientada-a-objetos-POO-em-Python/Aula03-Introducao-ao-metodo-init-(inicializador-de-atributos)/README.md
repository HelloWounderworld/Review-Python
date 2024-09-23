# Aula 03 -  Introdução ao método __init__ (inicializador de atributos):
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

## Link para leitura:

    https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python
    https://www.analyticsvidhya.com/blog/2024/02/all-about-init-in-python/#:~:text=The%20__init__%20method,necessary%20setup%20or%20initialization%20tasks.
    https://www.geeksforgeeks.org/__init__-in-python/
    https://www.shiksha.com/online-courses/articles/understanding-self-in-python/#:~:text=The%20use%20of%20%E2%80%9Cself%E2%80%9D%20in,and%20class%20variables%20or%20methods.