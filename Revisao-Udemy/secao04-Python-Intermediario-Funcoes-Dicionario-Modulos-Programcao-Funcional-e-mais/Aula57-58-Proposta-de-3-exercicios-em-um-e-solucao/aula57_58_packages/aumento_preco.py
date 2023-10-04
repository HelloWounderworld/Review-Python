def aumento_preco_dez(lista):
    for i in lista:
        i['preco'] = round(1.1 * i['preco'], 2)

    return lista