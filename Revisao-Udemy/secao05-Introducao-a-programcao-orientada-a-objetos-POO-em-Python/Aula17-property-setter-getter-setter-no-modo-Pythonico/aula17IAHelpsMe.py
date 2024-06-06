class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
            raise ValueError("O nome deve ser uma string")
        self._nome = valor

persol = Pessoa('Alan')

print(persol.nome)
persol.nome = 'Leonardo'
print(persol.nome)
persol.nome = 'Pedro'
print(persol.nome)
persol.nome = 'Thayna'
print(persol.nome)
persol.nome = 'Paula'
print(persol.nome)
persol.nome = 1234
print(persol.nome)
