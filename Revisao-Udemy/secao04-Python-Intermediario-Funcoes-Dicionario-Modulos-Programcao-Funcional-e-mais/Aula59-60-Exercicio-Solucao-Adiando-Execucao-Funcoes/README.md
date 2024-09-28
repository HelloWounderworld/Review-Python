# Aula 59 e 60 - Exercício e Solução - Adiando execução de funções:
Seguir com o enunciado

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
        return funcao(*args)


    soma_com_cinco = criar_funcao(soma, 5)
    multiplica_por_dez = criar_funcao(multiplica, 10)

Foi usado clousure para resolver esse problema.
