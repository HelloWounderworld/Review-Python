"""
Retorno de valores das funções (return)
"""

variavel = print("Leonardo")
print(variavel)
print(variavel is None)

def soma(x,y):
    print(x+y)

random = soma(1,2)
# random = int('1')
print(random)

def sum(x,y):
    return x + y

x = sum(1,2)
print(x)
