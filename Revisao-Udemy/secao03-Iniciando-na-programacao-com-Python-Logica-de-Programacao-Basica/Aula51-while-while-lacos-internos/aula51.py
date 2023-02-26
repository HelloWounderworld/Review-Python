"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    
    # print(linha)
    coluna = 1
    matriz = ''
    while coluna <= qtd_colunas:
        matriz = matriz + f'a{linha}{coluna} '
        # print(f'{linha=} {coluna=}')
        coluna += 1
    print(matriz)
    linha += 1


print('Acabou')