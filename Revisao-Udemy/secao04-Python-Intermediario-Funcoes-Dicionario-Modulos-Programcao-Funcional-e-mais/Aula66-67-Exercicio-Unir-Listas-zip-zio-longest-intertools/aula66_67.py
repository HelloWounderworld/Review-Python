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

# Claro, que a forma acima não estou verificando qual é a menor lista para iterar sobre ele
# Poderia, eu realizar o seguinte para melhorar a função

def uniao(cidade, estado):
    return [(cidade[i], estado[i]) for i in range(min(len(cidade), len(estado)))]

result = uniao(cidade, estado)
print(result)

# Usando o método zip
print(zip(cidade, estado))
print(list(zip(cidade, estado)))

# Usando o método zip_longest do módulo itertools
from itertools import zip_longest

print(zip_longest(cidade, estado))
print(list(zip_longest(cidade, estado)))
print(list(zip_longest(cidade, estado, fillvalue='SEM CIDADE!')))
