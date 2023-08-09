import math
def tabela_Log(n):
    m = n**2
    n = math.sqrt(m)
    x = n - int(n)
    i = 0
    if x == 0:
        for i in range(1,int(n)+1):
            print(float(i),"\t",math.log(float(i)))
    else:
        while i <(int(n)+1):
            print(x,"\t",math.log(x))
            x = x + 1
            i = i + 1
