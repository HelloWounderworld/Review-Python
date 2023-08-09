def fatia_max(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    Tem que ser O(n²)
    '''
    soma_parcial = [0]
    for i in range(p,r):
        soma_parcial.append(soma_parcial[i-p]+v[i])
    soma_max = soma_parcial[-1]-soma_parcial[0]
    nlin, ncol = p, r
    for i in range(p,r+1):
        for j in range(p,i+1):
            soma = soma_parcial[i-p] - soma_parcial[j-p]
            if soma_max < soma:
                soma_max = soma
                nlin, ncol = j, i
    return soma_max, nlin, ncol
            

#--------------------------------------------------------
def fatia_max_meio(p, q, r, v):
    '''(int, int, int, list) -> int, int, int

    RECEBE números inteiros p < q < r e uma lista v[p:r] de 
    números inteiros e RETORNA valores inteiros 
    soma_max, e, d tais que 

        soma_max==sum(v[e:d]) é a maior soma de uma fatia 
        v[i:j] com p <= i < q < j <= r.
    tem que ser O(n)
    '''
    soma_parcial = {0:0}
    for i in range(len(v)):
        soma_parcial[i+1] = soma_parcial[i] + v[i]
    soma_max1 = soma_parcial[q] - soma_parcial[p]
    soma_max2 = soma_parcial[r] - soma_parcial[q]
    nlin1 = p
    ncol2 = r
    for j in range(p,q):
        soma = soma_parcial[q] - soma_parcial[j]
        if soma_max1 < soma:
            soma_max1 = soma
            nlin1 = j
    for l in range(q+1,r+1):
        soma = soma_parcial[l] - soma_parcial[q]
        if soma_max2 < soma:
            soma_max2 = soma
            ncol2 = l
    soma_max = soma_max1 + soma_max2
    return soma_max, nlin1, ncol2

#--------------------------------------------------------
def fatia_max_div_conq(p, r, v):
    '''(int, int, list) -> int, int, int

    RECEBE uma lista lista v[p:r] de números inteiros e RETORNA
    valores inteiros soma_max, e, d tais que

        soma_max == sum(v[e,d]) é a maior soma de uma fatia 
        v[i:j] com p <= i <= j <= r.
    tem que ser O(nlog(n))
    '''
    soma_parcial = {0:0}
    for i in range(len(v)):
        soma_parcial[i+1] = soma_parcial[i] + v[i]
    soma_max = soma_parcial[r]-soma_parcial[p]
    nlin, ncol = p, r
    for i in range(p+1,r):
        valor, lin, col = fatia_max_meio(p,i,r,v)
        if soma_max < valor:
            soma_max = valor
            nlin, ncol = lin, col
    soma = soma_parcial[r] - soma_parcial[r-1]
    if soma_max < soma:
        soma_max = soma
        nlin, ncol= r-1, r
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
    print()
    print('Teste fatia_max_meio')
    print(fatia_max_meio(0,1,2,v))
    print()
    print(fatia_max_meio(0,2,3,v))
    print()
    print(fatia_max_meio(0,2,4,v))
    print()
    print(fatia_max_meio(0,2,5,v))
    print()
    print(fatia_max_meio(0,2,6,v))
    print()
    print(fatia_max_meio(0,3,6,v))
    print()
    print(fatia_max_meio(0,3,5,v))
    print()
    print(fatia_max_meio(3,5,6,v))
    print()
    print(fatia_max_meio(3,5,7,v))
    print()
    print('Teste fatia_max_div_conq')
    print(fatia_max_div_conq(0,10,v))
    print()
    print(fatia_max_div_conq(2,9,v))
    print()
    print(fatia_max_div_conq(3,9,v))
    print()
    print(fatia_max_div_conq(7,10,v))

if __name__== "__main__":
    main()

'''
   In [2]: v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [3]: fatia_max(0,10,v)
    Out[3]: (187, 2, 7)

    In [4]: fatia_max(2,9,v)
    Out[4]: (187, 2, 7)

    In [5]: fatia_max(3,9,v)
    Out[5]: (155, 5, 7)

    In [6]: fatia_max(7,10,v)
    Out[6]: (84, 9, 10)
    
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
    
    In [22]: v = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

    In [23]: fatia_max_div_conq(0,10,v)
    Out[23]: (187, 2, 7)

    In [24]: fatia_max_div_conq(2,9,v)
    Out[24]: (187, 2, 7)

    In [25]: fatia_max_div_conq(3,9,v)
    Out[25]: (155, 5, 7)

    In [26]: fatia_max_div_conq(7,10,v)
    Out[26]: (84, 9, 10)


         n     div_conq    fatia_max 
       256       0.00s        0.00s
       512       0.00s        0.01s
      1024       0.00s        0.04s
      2048       0.00s        0.16s
      4096       0.01s        0.62s
      8192       0.02s        2.45s
     16384       0.04s        9.82s
     32768       0.08s       39.37s
     65536       0.16s      161.20s
    131072       0.33s      663.06s
    262144       0.68s     2581.96s
    524288       1.40s    10163.39s
'''


