# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, ABCMeta, abstractmethod

# ABC <=> ABCMeta
# class Log(metaclass=ABCMeta):
#     ...

# Todo o metodo abstrado devem ser implementado dentro da sua respectiva subclasse! Isso e obrigatorio!
# Se eu esquecer o Python vai te lembrar.
class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l.log_error('Oi')
