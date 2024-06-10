# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
# Basicamente, a relacao de associacao usa-se getter e setter, para suspeitarmos se esta sendo ou nao associado
# junto com uma outra classe.
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} esta escrevendo.'
    
escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina')
# escritor.ferramenta.escrever() # O ponto e que nao esta sendo carregado uma classe, ela esta None, entao isso dara um erro
# escritor.ferramenta = caneta # Um atributo de uma classe esta recebendo uma classe... Uhummmm, cheirinho de Heranca...
escritor.ferramenta = maquina_de_escrever # Um atributo de uma classe esta recebendo uma classe... Uhummmm, cheirinho de Heranca...
print(escritor.ferramenta)
print(caneta.escrever())
print(escritor.ferramenta.escrever())
