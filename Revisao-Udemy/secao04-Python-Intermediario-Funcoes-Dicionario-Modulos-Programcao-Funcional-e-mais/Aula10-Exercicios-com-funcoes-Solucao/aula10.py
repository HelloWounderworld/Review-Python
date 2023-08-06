# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def product(*arg):
    prod = 1
    for i in arg:
        prod*=i
    return prod

argumentos = 5,62,73,14,95
variavel = product(*argumentos)
print(variavel)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def mod2(x):
    if x%2 ==0:
        return f'{x} é par!'
    return f'{x} é ímpar!'

integer1 = 4
random1 = mod2(integer1)

integer2 = 5
random2 = mod2(integer2)

print(random1)
print(random2)
