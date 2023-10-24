# Decoradores com parametros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Fabrica de Funcoes 1')

        def aninhada(*args, **kwargs):
            print('Parametros do decorador: ', a, b, c)
            print('Aninhado')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

#def fabrica_de_decoradores(a, b, c):
#    return fabrica_de_funcoes

#def arcaico(a, b, c):
#    print(a, b, c)
#    return fabrica_de_funcoes

#@arcaico(1, 2, 3)
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x*y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
