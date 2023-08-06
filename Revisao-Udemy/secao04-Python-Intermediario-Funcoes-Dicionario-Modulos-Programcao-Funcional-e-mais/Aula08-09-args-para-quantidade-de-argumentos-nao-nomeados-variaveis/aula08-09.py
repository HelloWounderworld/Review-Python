"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
print(1)
print(1,2,3)
print(1,2,3,4,5,6,7)

x, y, *resto = 1, 2, 3, 4, 5, 6, 7
print(x,y,resto)

# def soma(x,y):
#     return x + y

# def soma(*args):
#     args = list(args)
#     print(args, type(args))

def soma(*args):
    sum = 0
    for i in args:
        print(i)
        sum+=i
    return sum

variavel = soma(1,2,3,4,5,6,7)
print(variavel)

random = (1,2,3,4,5,6,7)
# print(soma(random))
print(soma(*random))
