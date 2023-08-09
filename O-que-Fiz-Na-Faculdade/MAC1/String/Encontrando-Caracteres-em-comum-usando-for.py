def find(string,Ch):
    indice = 0
    x = []
    while indice < len(string):
        if string[indice] == Ch:
            x.append(string[indice])
            indice = indice + 1
        else:
            indice = indice + 1
    return print("Essa frase possui {} caractere '{}'". format(len(x),Ch))
'''Bom, essa funcao ainda esta simples, pois ela so analisa um caractere por vez de uma string
caso a pessoa queira fazer uma procura mais avancada, mas nao queira tr que criar uma funcao que
atenda a essa solicitacao, pode-se usar um pacote chamado "import string" pois neste pacote havera
inumeras ferramentas para poder fazer a manipulacao das strings que a pessoa deseja. A vantagem seria
que esse pacote esta apto tbm para uso das strings de paises que tenham caracteres especificos'''
