# Exercício - Adiando execução de 
# Bom, temos as funções abaixo, mas se executarmos terá um problema
# O que eu quero é que vc corrija esse problema de modo que
# para a soma, sempre ocorrerá uma soma de 5
# para a multiplicação, sempre ocorrerá a multiplicação de 10
# Basicamente, o que está acontecendo aqui é que a função soma e mutiplica está se precipitando
# antes mesmo de definir um valor para y.
# Ou seja, o que eu quero que vc faça seria em aditar a executação, para ter tempo em definir o y
# e, finalmente, conseguirmos executar.
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def argumento_y(y):
        return funcao(*args, y)
    return argumento_y


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
print(soma_com_cinco(7))
print(multiplica_por_dez(3))
