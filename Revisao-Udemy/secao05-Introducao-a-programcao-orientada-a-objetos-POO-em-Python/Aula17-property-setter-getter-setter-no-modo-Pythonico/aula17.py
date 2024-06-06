# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos ou metodos que começar com um ou dois underlines
# não devem ser usados fora da classe.
# Usar o underline, _, para definir um atributo em Python, e uma convencao de dizer que nao se deve usa-la fora da classe.

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        # self.cor = cor # Consigo acionar o metodo setter, cor, no init tbm. No caso, eu posso usar o setter logo de inicio
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no getter')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no Setter', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

    
def mostrar(classeInstanciada):
    return classeInstanciada.cor
    
caneta = Caneta('Azul')
# getter -> obter valor
print(caneta.cor)
print()
mostrar(caneta)
print(mostrar(caneta))
print()
caneta.cor = 'Rosa' # Lembre-se que, cor, e um metodo, e nao um atributo. Isso dara erro se nao habilitarmos o setter.
print(caneta.cor)
print()
print(caneta.cor_tampa)
caneta.cor_tampa = 'Pokari'
print(caneta.cor_tampa)
