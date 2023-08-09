def fatia_max(p, r, v):
    soma_parcial = [v[p]]*len(v[p:r])
    for i in range(p+1,r):
        soma_parcial[i] = soma_parcial[i-1]+v[i]
    soma_max = 0
    for i in range(p+1,r):
        for j in range(p,i):
            soma = soma_parcial[i]-soma_parcial[j]
            if i == p:
                soma_max = soma
                nlin, ncol = j, i
            else:
                if soma_max < soma:
                    soma_max = soma
                    nlin, ncol = j, i
    return soma_max, nlin, ncol

def main():
    v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    print('Teste fatia_max')
    print(fatia_max(0,10,v))
    print()
    print(fatia_max(2,9,v))
    print()
    print(fatia_max(3,9,v))
    print()
    print(fatia_max(7,10,v))
main()
'''
    In [12]:v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [13]: fatia_max_meio(0,1,2,v)
    Out[13]: (-10, 0, 2)

    In [14]: fatia_max_meio(0,2,3,v)
    Out[14]: (49, 0, 3)

    In [15]: fatia_max_meio(0,2,4,v)
    Out[15]: (75, 0, 4)

    In [16]: fatia_max_meio(0,2,5,v)
    Out[16]: (75, 0, 4)

    In [17]: fatia_max_meio(0,2,6,v)
    Out[17]: (80, 0, 6)

    In [18]: fatia_max_meio(0,3,6,v)
    Out[18]: (90, 2, 6)

    In [19]: fatia_max_meio(0,3,5,v)
    Out[19]: (85, 2, 4)

    In [20]: fatia_max_meio(3,5,6,v)
    Out[20]: (31, 3, 6)

    In [21]: fatia_max_meio(3,5,7,v)
    Out[21]: (128, 3, 7)
'''



