# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        # So de vc trocar a ordem de atribuicao, faz muita diferenca. (self._name e self.name) com (self.name e self._name)
        self._name = None
        self.name = name

    # cuidado, se vc inverter a ordem, entre @property e @abstractmethod, tera problema.
    # vc quer abstrair um metodo que aplica uma propriedade, e nao aplicar a abstracao na propriedade.
    # @property
    # @abstractmethod
    # def name(self): ...

    # @name.setter
    # def name(self, name):
    #     self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...

class Foo(AbstractFoo):
    # Ironicamente, name = '' e o mesmo que foi feito tudo abaixo com o @property... So pelo fato de ter @abstractmethod para o getter na superclasse...
    # name = ''

    def __init__(self, name):
        super().__init__(name)
        # print('Sou inutil: ', name)

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     self._name = name

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)
