# Aula 70 - Inserindo itens em qualquer índice da lista com insert (Tipo list):
Vamos entender agora uma função que chamado insert que serve para inserir os elementos dentro de uma lista.

No caso, vamos revisar o seguinte

    """
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
    """
    #        0   1   2   3
    lista = [10, 20, 30, 40]
    lista.append('Luiz')
    nome = lista.pop()
    lista.append(1233)
    del lista[-1]
    # lista.clear()
    lista.insert(100, 5)
    print(lista[4])
