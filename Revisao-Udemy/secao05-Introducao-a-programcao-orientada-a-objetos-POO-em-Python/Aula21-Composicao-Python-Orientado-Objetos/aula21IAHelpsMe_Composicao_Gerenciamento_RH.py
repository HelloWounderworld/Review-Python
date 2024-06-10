class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

desenvolvimento = Departamento("Desenvolvimento")
empregado = Funcionario("João")
desenvolvimento.adicionar_funcionario(empregado)