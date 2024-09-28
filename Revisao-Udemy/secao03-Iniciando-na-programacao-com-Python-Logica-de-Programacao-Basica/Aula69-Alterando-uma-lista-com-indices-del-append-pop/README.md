# Aula 69 - Alterando uma lista com índices, del, append e pop (Tipo list):
Vamos ver os métodos que temos para as listas, as mais usadas.

Bom, eu já vi isso na minha faculdade, então essa aula será mais como uma revisão

    """
    Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append, insert, pop, del, clear, extend, +
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
    """
    #        0   1   2   3   4   5
    lista = [10, 20, 30, 40]
    # lista[2] = 300
    # del lista[2]
    # print(lista)
    # print(lista[2])
    lista.append(50)
    lista.pop()
    lista.append(60)
    lista.append(70)
    ultimo_valor = lista.pop(3)
    print(lista, 'Removido,', ultimo_valor)

Obs: Muito cuidado ao usar a função delete, del. Pois, dependendo do uso dele vc poderá deixar o processamento do seu código muito, mas muito, lento. Por exemplo, quando usamos o del para apagar qualquer elemento que não esteja no último, a lista que será exibida seria uma espécie de lista nova. Ou seja, quando uso esse del, praticamente é criado uma nova lista. Agora, suponhamos que usamos esse del para apagar o segundo elemento de uma lista que tenha 10 mil elementos? No caso, o processo estaria realizando uma criação de uma nova lista só para deslocar os outros 9998 elementos à um índice antecessor. Isso vai requer um consumo muito enorme do processamento da sua máquina e tornaria o código seu muito, mas muito, lento.

Na medida do possível, uma boa prática que podemos realizar com as listas é add e remover apenas os últimos elementos. Ou seja, usamos as funções del e insert somente quando a lista que estamos manipulando seja uma lista bem menor.
