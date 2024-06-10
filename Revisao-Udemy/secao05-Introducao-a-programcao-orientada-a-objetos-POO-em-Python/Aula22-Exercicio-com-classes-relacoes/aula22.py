# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def nomeCarro(self):
        return self.nome
    
    @property
    def motorTipo(self):
        return self._motor
    
    @motorTipo.setter
    def motorTipo(self, motor):
        self._motor = motor

    @property
    def nomeFabricante(self):
        return self._fabricante
    
    @nomeFabricante.setter
    def nomeFabricante(self, fabricante):
        self._fabricante = fabricante

    def mostrar_qual_motor_quem_montou(self):
        if self._motor is not None and self._fabricante is not None:
            print(f'O carro, {self.nome}, foi montado pelo fabricante, {self._fabricante.nome}, e inserido o motor, {self._motor.nome}.')
        else:
            print('Carro ainda nao montado.')

class Motor:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nomeMotor(self):
        return self.nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nomeFabricante(self):
        return self.nome

print('O que foi solicitado acima, a relacao, parece ser Associacao, somente.')
print()

print('Bom, isso era o que o exercicio pedia. Eu, pelo contrario, a maneira como enxergo isso seria o seguinte:')
print('A relacao entre motor e carro poderia ser de Associacao. Ja a relacao de Fabricante e o carro, poderia ser de Agregacao.')
print('Motivo disso, seria que, enquanto que o motor e o carro podem existir de forma independente')
print('A instalacao do motor dentro do carro, alguem precisa realizar e, sem esse intermedio,')
print('nao tem como o motor sozinho se instalar dentro do capo do carro.')
print()

carro1 = Carro('Lancer Evolution')
motor1 = Motor('2.0 turbo de 37.7kgfm de torque')
fabricante1 = Fabricante('Leonardo')

carro1.motorTipo = motor1
carro1.nomeFabricante = fabricante1
carro1.mostrar_qual_motor_quem_montou()
