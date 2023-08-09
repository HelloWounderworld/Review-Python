import math
def tabela_Log(n):
    m = n**2
    n = int(math.sqrt(m))
    for i in range(1,n+1):
        print(float(i),"\t",math.log(float(i)))
'''Essa tabela de Log sera ineficiente, pois considera os indices somente da funçao for, entao caso a pessoa entre com algum float
a funçao nao rodara'''
