class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
# print(fusca.acelerar()) # Se fizermos isso, vai aparecer um None, pois esse metodo nao retorna nada e, em seguida, processar o print dentro do metodo que foi definido
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()