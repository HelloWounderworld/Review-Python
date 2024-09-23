# Aula 04 - Métodos em instâncias de classes Python:
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