# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

def fabrica_de_funcoes(func):
    print('Decorador')
    def nova_funcao(*args, **kwargs):
        print('Aninhado')
        print(*args)
        print(**kwargs)
        res = func(*args, **kwargs)
        return res
    return nova_funcao

@fabrica_de_funcoes
def unir_list(cidade, estado):
    unido = []
    for i in range(0,len(cidade)):
        unido.append((cidade[i], estado[i]))
    return unido


resultado = unir_list(cidade, estado)
print(resultado)

# Bom, o exercicio em si nao precisa de decoradores.
# Seguir a resolucao mais enxuta que eu faria

def uniao(cidade, estado):
    return [(cidade[i], estado[i]) for i in range(len(cidade))]

result = uniao(cidade, estado)
print(result)
