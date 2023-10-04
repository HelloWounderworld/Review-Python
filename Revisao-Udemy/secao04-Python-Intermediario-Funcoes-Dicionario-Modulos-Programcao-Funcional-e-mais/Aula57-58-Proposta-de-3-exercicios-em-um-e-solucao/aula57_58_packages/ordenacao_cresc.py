def ordena(item):
    return item['preco']

def ordenacao_cresc_preco(lista):
    lista.sort(key=ordena)
    return lista