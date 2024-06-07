# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado. Nem na subclasse ela nao pode ser usado

from functools import partial # clica com o botao direito do mouse e clica em "Go to Definition". Sera possivel ver como foi construida a classe

class Foo:
    def __init__(self):
        self.public = 'isso e publico'
        self._protected = 'isso e protegido'
        self.__private = 'isso e privado'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return 'metodo protegido'
    
    def __metodo_private(self):
        print('__metodo_private')
        return 'metodo private'

f = Foo()
print(f.public)
print(f.metodo_publico())
# print(f._protected) # Se o Python tivesse modificadores de acesso, isso nao seria possivel. Em Java, por exemplo, nao e possivel fazer esse print
# print(f._metodo_protected())
# print(f.__metodo_private()) # Isso ira gerar um erro, e por conta disso que utilizamos-a como um metodo privado dentro da classe
# print(f._Foo__metodo_private()) # So assim para conseguir acessar o metodo privado fora da classe e, sim, isso e proposital, seguindo a definicao de algo privado, mas o certo e que vc nao use isso fora da classe
