# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco_composicao(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_semComposicao(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        # print(*self.enderecos, sep='\n')
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('Apagando, ', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    # Esse __del__ depois que todo o codigo for compilado, sera apagado tudo o que foi criado
    # E como se vc nao deixasse vestigios do que foi feito.
    def __del__(self):
        print('Apagando, ', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco_composicao('Av Brasil', 54)
cliente1.inserir_endereco_composicao('Rua B', 6745)
# print(cliente1.enderecos[0].rua)
# print(cliente1.enderecos[1].rua)
cliente1.listar_enderecos()
endereco_externo = Endereco('Av Vital Brasil', 12345)
cliente1.inserir_endereco_semComposicao(endereco_externo)
cliente1.listar_enderecos()

# Note que, ao apagarmos o cliente1, em conjunto, e apagado tbm as outras informas da classe Endereco
# Indicando assim que o Endereco tem uma forte relacao de dependencia com a classe Cliente
# Sem ela, a classe Endereco nao tem como existir.
# Isso mostra a relacao de composicao.
# Basicamente, se vc viu que uma classe foi instanciado numa outra classe, ja suspeita que ha uma composicao
# Para deixar de ser uma composicao, seria necessario que a instanciacao ocorra fora da classe.
del cliente1

# Note que, os enderecos que tem uma relacao de composicao, ao ser deletado a classe cliente1, foi deletado junto
# Entretanto, aos enderecos que foram criado de forma externa, nao foi deletado
print(endereco_externo.rua, endereco_externo.numero)

print('############################ AQUI TERMINA O MEU CODIGO')
print('GARBAGE COLLECTOR! COLETANDO LIXO E APAGANDO O LIXO')
