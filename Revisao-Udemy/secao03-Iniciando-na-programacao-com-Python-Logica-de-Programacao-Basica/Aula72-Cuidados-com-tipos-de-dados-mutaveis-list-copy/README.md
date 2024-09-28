# Aula 72 - Cuidados com tipos de dados mutáveis - list e copy:
Vamos ver alguns cuidados que precisamos tomar ao trabalharmos com os tipos de dados mutáveis.

A princípio a lógica é a mesma do que eu estudei em JavaScript, sobre a forma de copiar uma lista

    lista_a = [1, 2, 3]
    lista_b = lista_a

No caso, o formato acima não estará gerando uma cópia da lista. Ou seja, as duas variáveis estará apontando para a mesma memória.

Agora, a forma certa de realizar a tal cópia seria o seguinte

    """
    Cuidados com dados mutáveis
    = - copiado o valor (imutáveis)
    = - aponta para o mesmo valor na memória (mutável)
    """
    lista_a = ['Luiz', 'Maria', 1, True, 1.2]
    lista_b = lista_a.copy()
    print(lista_a)
    print(lista_b)
    print('--------------------')

    lista_a[0] = 'Qualquer coisa'
    print(lista_a)
    print(lista_b)
    print('--------------------')
