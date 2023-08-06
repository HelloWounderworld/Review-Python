# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def duplica(x):
    return 2 * x

def triplica(x):
    return 3 * x

def quadruplica(x):
    return 4 * x

y = 3

print(duplica(y))
print(triplica(y))
print(quadruplica(y))

def multiplica(x):
    def calcula(y):
        return x*y
    return calcula

z = 3
conta = multiplica(z)
print(conta(2))
print(conta(3))
print(conta(4))
