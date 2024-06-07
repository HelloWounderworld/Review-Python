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