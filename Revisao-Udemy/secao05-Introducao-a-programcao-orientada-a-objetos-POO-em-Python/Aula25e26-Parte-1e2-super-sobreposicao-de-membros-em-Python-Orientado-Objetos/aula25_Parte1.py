# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# Tudo o que aparecer na cor azul claro e uma classe em Python.
# Sobreposicao de metodos
class MinhaString(str):
    def upper(self):
        print('Chamou UPPER')
        retorno = super(MinhaString, self).upper() # super(), sem colocar nada dentro do parenteses, e o mesmo que super(MinhaString, self). Ou seja, super() e a forma implicita de super(MinhaString, self)
        print('Depois do UPPER')
        return retorno

# A classe MinhaString herdou a classe str.
string = MinhaString('Leonardo')
print(string)
print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('Ei, burlei o sistema!!')
        super().__init__(*args, **kwargs)

    # Sobreposicao - Overriding
    def metodo(self):
        # super(A, self).metodo() # Quem e a superclasse de A??? O object... Nela tem o metodo, metodo()?
        A.metodo(self) # = super(B, self).metodo()
        super(B, self).metodo() # Estou pedindo para que herde o metodo da superclasse de B, que e o A
        super().metodo()
        print('C')

c = C('atributo', 'outra_coisa') # Se eu definir o metodo __init__, nao irei mais conseguir instanciar a classe dessa forma. Basicamente, o init ele e o construtor de uma classe, como e visto em Java, quando vc define o construtor que tem o mesmo nome da classe.
# c = C() # Mesmo tendo o init da classe A, na classe B, o init herdado nao esta exibindo nada. Ou seja, a prioridade e o que foi herdado o mais proximo em relacao a subclasse
print(c.atributo) # Por conta do metodo init da classe B, que nao coloquei nada, perdi esse atributo.
print(c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()

print(C.mro()) # Method Resolution Order - Metodo de resolucao de ordem - Mostra a hierarquia de baixo para cima, que se le de esquerda para direta, da classe indicada.
print(B.mro())
print(A.mro())
