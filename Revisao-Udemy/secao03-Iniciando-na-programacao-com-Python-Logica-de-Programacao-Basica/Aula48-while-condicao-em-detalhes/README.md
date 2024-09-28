# Aula 48 - while - Condição em detalhes:
Vamos ver com mais detalhe a condição que colocamos dentro do while.

Vimos que além de usarmos diretamente os booleanos, podemos, por meio de várias formas de comparações, criarmos um boolenanos de forma implícitas e considerar esses booleanos na condição do while

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    contador = 0

    while contador <= 10:
        contador = contador + 1
        print(contador)

    print('Acabou')

Ou seja, assim como usamos inúmeras formas de booleanos de forma implícita em condicionais if's, podemos realizar o mesmo para o while.
