'''
Para busca binária usaremos o modulo 
Lib/bisect.py: https://docs.python.org/3/library/bisect.html
'''
from bisec import bisect_left
def index(a,x,lo,hi):
    i = bisect_left(a,x,lo,hi)
    if i != len(a) and a[i] == x:
        return i
    return None

def conta_bb(a):
    conta = 0
    n = len(a)
    a.sort()
    for i in range(n):
        for j in range(i+1,n):
            soma = a[i]+a[j]
            k = index(a,-soma,j+1,n)
            if  k != None:
                conta+= 1
    return conta




