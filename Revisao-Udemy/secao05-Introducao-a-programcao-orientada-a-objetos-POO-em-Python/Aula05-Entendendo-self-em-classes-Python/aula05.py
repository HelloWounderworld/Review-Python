class Carro:
    def __init__(blablabla, nome):
        blablabla.nome = nome

    def acelerar(blablabla):
        print(f'{blablabla.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
# print(fusca.acelerar()) # Se fizermos isso, vai aparecer um None, pois esse metodo nao retorna nada e, em seguida, processar o print dentro do metodo que foi definido
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 30)
print(pessoa1.saudacao())
