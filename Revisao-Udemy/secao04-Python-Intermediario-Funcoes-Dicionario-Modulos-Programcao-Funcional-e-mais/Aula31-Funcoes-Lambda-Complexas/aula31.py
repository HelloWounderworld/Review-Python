def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(executa(cria_multiplicador(soma(1,3)), 10))

print(
    executa(
        lambda x,y: x+y,
        9, 3
    ),
    executa(soma, 9,3),
    soma(9,3)
)

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7
    )
)

duplica = executa(
        lambda x: lambda y: x*y,
        19
    )

print(duplica(3))
