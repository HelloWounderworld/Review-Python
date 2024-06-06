def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9))

def identifica(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

identifica(nome="Alice", idade=30)

def funcao(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

funcao(1, 2, nome="Alice", idade=30)
