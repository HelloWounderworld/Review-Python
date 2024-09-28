# Aula 51 - while + while (laços internos):
Vamos continuar com o assunto do while, desta vez vendo while dentro de um while.

Bom, um bom exemplo que faz o uso de while dentro de um while seria para construir uma matriz, visto que ela precisa de linha e coluna. Isso em forma de lista é definitivamente uma lista dentro de uma lista.

Obs: Podemos criar matriz 3d nessa brincadeira tbm colocando mais listas dentro de listas.

Assim, para entendermos o uso do while dentro de while vamos usar a matriz como um exemplo disso. Primeiramente, indo passo a passo, vamos fazer o seguinte

    """
    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    Loop infinito -> Quando um código não tem fim
    """
    qtd_linhas = 5

    linha = 1
    while linha <= qtd_linhas:

        print(linha)

        linha += 1


    print('Acabou')

Para certificarmos de que está funcionando.

Visto que ele está funcionando corretamente, vamos agora trabalhar na sua coluna

    qtd_linhas = 5
    qtd_colunas = 5

    linha = 1
    while linha <= qtd_linhas:
        
        # print(linha)
        coluna = 1
        matriz = ''
        while coluna <= qtd_colunas:
            matriz = matriz + f'{linha}{coluna} '
            # print(f'{linha=} {coluna=}')
            coluna += 1
        print(matriz)
        linha += 1


    print('Acabou')

Bom, basicamente, nessa brincadeira, já daría para brincarmos com as teorias de álgebra linear e realizar algumas simulações com elas.
