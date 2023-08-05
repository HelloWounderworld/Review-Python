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

'''
Quantidade de números inteiros ímpares com três algarismos distintos entre 100 e 999.
'''

count = 0
for i in range(100, 1000):
    if i%2==1:
        j = str(i)
        if (int(j[0]) != int(j[1])) and (int(j[0]) != int(j[2])) and (int(j[1]) != int(j[2])):
            count+=1
print(count)