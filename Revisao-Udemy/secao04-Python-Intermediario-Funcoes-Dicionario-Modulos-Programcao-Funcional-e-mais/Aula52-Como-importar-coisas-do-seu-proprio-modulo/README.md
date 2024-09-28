# Aula 52 - Como importar coisas do seu próprio módulo (ponto de vista do __main__):
Lembrando, novamente, os níveis dos arquivos tem que estarem iguais ou abaixo do "__main__"!!! Se não, ficaria mais complicado conseguirmos montar toda a arquitetura do sistema!!

Vamos aprender a importar coisas do seu próprio módulo. Algo análogo de como foi feito nos módulos que foram importados ou métodos que importamos diretamente a partir dos módulos nativos que já vem com a linguagem Python.

Bom, já vimos na última aula, se importarmos o módulo inteiro, tudo que tiver dentro desse módulo será importado. Agora se vai ser ou não executado já é outra história. Vamos criar uma pasta "code-class-52" e dentro dela criamos o arquivo "aula52.py" que será o nosso arquivo principal, __main__, e no mesmo nível de arquivo dele criamos módulo "aula52_m.py".

No arquivo, aula52.py, colocamos o seguinte

    import aula52_m

    print('Este módulo, aula52.py, se chama: ', __name__)

E no arquivo, aula52_m.py, colocamos o seguinte

    print('Este módulo, aula52_m, se chama: ', __name__)

Bom, ao rodarmos o arquivo, aula52.py, vimos que até aqui nada de novidade. Vimos que o print que está dentro do módulo, aula52_m.py, já é executado no momento em que executamos o arquivo, aula52.py.

Agora, no arquivo, aula52_m.py, vamos criar uma variável

    print('Este módulo, aula52_m, se chama: ', __name__)

    variavel_modulo = 'Leonardo'

Se rodarmos o arquivo, aula52.py, vamos ver só o print que está no arquivo, aula52_m.py. Como vamos acessar essa variável? 

A resposta é da mesma forma como acessamos os métodos dos módulos nativos do Python. Ou seja, acessamos da seguinte forma, no arquivo, aula52.py

    import aula52_m

    print('Este módulo, aula52.py, se chama: ', __name__)
    print(aula52_m) # Uma forma de saber de qual path esse módulo está vindo
    print(aula52_m.variavel_modulo)

Agora, da mesma forma que vimos nos módulos nativos do Python, temos uma forma de importamos somente os métodos ou variáveis definidas dentro daquele módulo da seguinte forma, no arquivo, aula52.py

    import aula52_m
    from aula52_m import variavel_modulo

    print('Este módulo, aula52.py, se chama: ', __name__)
    print(aula52_m) # Uma forma de saber de qual path esse módulo está vindo
    print(aula52_m.variavel_modulo)
    print(variavel_modulo)

Da mesma forma que se definimos os métodos, funções que ficam dentro de um objeto/módulo, a forma como vamos usa-las é o mesmo que vimos nos módulos nativos que Python. No caso, no arquivo, aula52_m.py, colocamos 

    print('Este módulo, aula52_m, se chama: ', __name__)

    variavel_modulo = 'Leonardo'

    def soma(x, y):
        return x + y

E assim no arquivo, aula52.py, temos

    import aula52_m
    from aula52_m import soma, variavel_modulo

    print('Este módulo, aula52.py, se chama: ', __name__)
    #print(aula52_m)
    print(aula52_m.variavel_modulo)
    print(variavel_modulo)
    print(aula52_m.soma(2, 3))
    print(soma(3, 4))

Claro que, assim como vimos para os módulos nativos, conseguimos apelidar os módulos personalizados que importamos, no arquivo, aula52.py
