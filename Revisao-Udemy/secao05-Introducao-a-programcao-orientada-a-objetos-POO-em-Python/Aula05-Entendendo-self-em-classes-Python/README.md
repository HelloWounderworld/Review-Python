# Aula 05 - Entendendo self em classes Python:
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