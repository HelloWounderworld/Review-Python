'''
Essa e uma forma quadratica de encontrar os trio de somas que dê 0. No caso, o
consumo de tempo seria em notacao assintotica O(n²)
'''

def conta_n2(a):
    conta = 0 
    n = len(a)
    a.sort()
    for i in range(n-2):
        x = a[i]
        e = i+1
        d = n-1
        while e<d:
            y = a[e]
            z = a[d]
            soma = x+y+z
            if soma == 0:
                conta += 1
                e += 1
                d -= 1
            elif soma>0: 
                d -= 1
            else:
                e += 1
    return conta




